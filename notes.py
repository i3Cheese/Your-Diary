import sqlite3
from PyQt5.QtWidgets import QTableWidgetItem, QTableWidget, QMenu, QAction, QDialog, \
    QDialogButtonBox
from PyQt5.Qt import QColor, QBrush
from datetime import datetime
from ui_noteEditor import Ui_noteEditor


class NoteTableWidgetItem(QTableWidgetItem):
    """Создан для сортировки"""
    id_: int

    def __init__(self, value, brush=None, id_=-1):
        self.value = value
        self.id_ = id_
        if isinstance(value, datetime):
            value.replace(microsecond=0)
            super().__init__(value.isoformat(' '))
        else:
            super().__init__(str(value))
        if brush is not None:
            self.setBackground(brush)

    def __lt__(self, other):
        return self.value < other.value


class CategoryTableWidget(QTableWidget):
    """Предназначен для отображения и взаимодействия пользователя
     с записями внутри default category"""
    category_id: int
    data_base: str

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.data_base = ''
        self.category_id = -1

        self.acDelete = QAction(self)
        self.acDelete.setText("Delete")
        self.acDelete.triggered.connect(self.deleteNotes)

    def reload(self) -> None:
        """Полностью перезагружаем таблицу из базы данных"""
        # Задают максимальную длину отображаемых данных
        max_text_len = 100
        max_title_len = 20

        self.setColumnCount(4)
        self.setHorizontalHeaderLabels(("Начало", "Конец", "Текст", "Флаг"))
        notes = self.loadNotes()
        con = sqlite3.connect(self.data_base)
        cur = con.cursor()
        self.setRowCount(len(notes))
        for i, note in enumerate(notes):
            id_ = note[0]

            # начало
            self.setItem(i, 0, NoteTableWidgetItem(datetime.fromisoformat(note[1]), id_=id_))
            # конец
            self.setItem(i, 1, NoteTableWidgetItem(datetime.fromisoformat(note[2]), id_=id_))
            # текст
            self.setItem(i, 2, NoteTableWidgetItem(note[3] if
                                                   len(note[3]) <= max_text_len else
                                                   note[3][:max_text_len - 3] + '...',
                                                   id_=id_))
            # флаг
            if note[4]:
                title, r, g, b = cur.execute(
                    f'SELECT title, red, blue, green FROM flags WHERE title = "{note[4]}"'
                ).fetchone()
                self.setItem(i, 4, NoteTableWidgetItem(title if
                                                       len(title) < max_title_len else
                                                       title[:max_title_len - 3] + '...',
                                                       brush=QBrush(QColor(r, g, b)), id_=id_))
        self.resizeColumnsToContents()
        con.close()

    def loadNotes(self) -> list:
        con = sqlite3.connect(self.data_base)
        cur = con.cursor()
        notes = cur.execute(
            f'SELECT id, start, end, text, flag '
            f'FROM defaultNotes WHERE category = {self.category_id}'
        ).fetchall()
        con.close()
        return notes

    def itemDoubleClicked(self, item: QTableWidgetItem) -> None:
        """Открытие редактора"""
        print("A")
        self.editor = NoteEditor(self.data_base, self.category_id, self.currentItem().id_)
        self.editor.exec()
        self.reload()

    def contextMenuEvent(self, event):
        """Создаём контекстное меню"""
        menu = QMenu(self)
        menu.addAction(self.acDelete)
        menu.exec(self.mapToGlobal(event.pos()))

    def deleteNotes(self):
        ids = set()
        for item in self.selectedItems():
            ids.add(item.id_)
        ids.discard(-1)
        con = sqlite3.connect(self.data_base)
        cur = con.cursor()
        cur.execute(f'DELETE FROM defaultNotes WHERE id IN {tuple(ids)}')
        con.commit()
        con.close()


class NoteEditor(QDialog, Ui_noteEditor):
    def __init__(self, data_base, category_id, id_=-1, **kwargs):
        super().__init__(**kwargs)
        self.setupUi(self)
        self.data_base = data_base
        self.category_id = category_id
        self.id_ = id_

        # Задаём кнопкам действия
        self.buttonBox.button(QDialogButtonBox.Save).clicked.connect(self.save)
        self.buttonBox.button(QDialogButtonBox.Save).setShortcut("Ctrl+S")
        self.buttonBox.button(QDialogButtonBox.Ok).clicked.connect(self.accept)
        self.buttonBox.button(QDialogButtonBox.Cancel).clicked.connect(self.reject)

    def save(self):
        text = self.textEdit.toPlainText()
        flag = self.cbFlags.currentText()
        start = self.dteStart.dateTime().toPyDateTime().isoformat(' ')
        end = self.dteEnd.dateTime().toPyDateTime().isoformat(' ')

        con = sqlite3.connect(self.data_base)
        cur = con.cursor()

        if self.id_ == -1:
            # наибольший существующий id + 1
            self.id_ = cur.execute('SELECT id FROM defaultNotes ORDER BY id DESC').fetchone()[0] + 1

        # Создаёт или заменяет запись
        cur.execute(f'INSERT INTO defaultNotes(id, category, text, flag, start, end) '
                    f'VALUES(?, ?, ?, ?, ?, ?)',
                    (self.id_, self.category_id, text, flag, start, end))
        con.commit()
        con.close()

    def accept(self):
        self.save()
        super().accept()

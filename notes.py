import sqlite3
from PyQt5.QtWidgets import QTableWidgetItem, QTableWidget, QMenu, QAction, QDialog, \
    QDialogButtonBox
from PyQt5.Qt import QColor, QBrush
from PyQt5 import QtCore
from datetime import datetime
from ui_noteEditor import Ui_noteEditor
from ui_DateTimeDialog import Ui_DateTimeDialog
from flags import FlagIcon


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

        self.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)

    def __lt__(self, other):
        return self.value < other.value


class NotesTableWidget(QTableWidget):
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

        self.cellDoubleClicked.connect(self.openEditor)

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
            self.setItem(i, 2, NoteTableWidgetItem(note[3].ljust(max_text_len, ' ') if
                                                   len(note[3]) <= max_text_len else
                                                   note[3][:max_text_len - 3] + '...',
                                                   id_=id_))
            # флаг
            if note[4]:
                title, r, g, b = cur.execute(
                    f'SELECT title, red, green, blue FROM flags WHERE id = "{note[4]}"'
                ).fetchone()
                self.setItem(i, 3, NoteTableWidgetItem(title.ljust(max_title_len, ' ') if
                                                       len(title) < max_title_len else
                                                       title[:max_title_len - 3] + '...',
                                                       brush=QBrush(QColor(r, g, b)), id_=id_))
            else:
                self.setItem(i, 3, NoteTableWidgetItem(' ' * max_title_len, id_=id_))

        self.resizeColumnsToContents()
        self.resize(sum([self.columnWidth(i) for i in range(self.columnCount())]), self.height())
        self.setMinimumSize(self.size())
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

    def openEditor(self) -> None:
        """Открытие редактора"""
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
        cur.execute(f'DELETE FROM defaultNotes WHERE id IN ({"? " * len(ids)})', tuple(ids))
        con.commit()
        con.close()

        self.reload()


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
        self.pbStart.clicked.connect(self.getDT)
        self.pbEnd.clicked.connect(self.getDT)

        self.loadData()

    def loadData(self):
        """Заполняет виджеты данными из базы или стандартными"""
        if self.id_ == -1:
            # Стандартные
            start = datetime.now().replace(microsecond=0).isoformat(' ')
            end = start
            text = ''
            flag = -1
        else:
            # Загружаем данные из базы
            con = sqlite3.connect(self.data_base)
            cur = con.cursor()
            start, end, text, flag = cur.execute(
                f'SELECT start, end, text, flag FROM defaultNotes WHERE id = ?',
                (self.id_,)
            ).fetchone()
            con.commit()
            con.close()

        # Загружаем их в виджет
        self.dteStart.setDateTime(datetime.fromisoformat(start))
        self.dteEnd.setDateTime(datetime.fromisoformat(end))
        self.textEdit.setText(text)
        self.fillFlagCB(flag)
        # TODO: Обработать флаг

    def save(self):
        text = self.textEdit.toPlainText()
        flag = self.cbFlags.currentData()
        start = self.dteStart.dateTime().toPyDateTime().isoformat(' ')
        end = self.dteEnd.dateTime().toPyDateTime().isoformat(' ')

        con = sqlite3.connect(self.data_base)
        cur = con.cursor()

        if self.id_ == -1:
            # наибольший существующий id + 1
            old_id = cur.execute('SELECT id FROM defaultNotes ORDER BY id DESC').fetchone()
            if old_id:
                self.id_ = old_id[0] + 1
            else:
                self.id_ = 0

        # Создаёт или заменяет запись
        cur.execute(f'INSERT INTO defaultNotes(id, category, text, flag, start, end) '
                    f'VALUES(?, ?, ?, ?, ?, ?)',
                    (self.id_, self.category_id, text, flag, start, end))
        con.commit()
        con.close()

    def accept(self):
        self.save()
        super().accept()

    def getDT(self):
        place = self.dteStart if self.sender() is self.pbStart else self.dteEnd
        self.dialog = DateTimeDialog(place.dateTime().toPyDateTime())
        if self.dialog.exec():
            place.setDateTime(self.dialog.answer())

    def fillFlagCB(self, cur_flag_id=-1):
        """Заполняем combobox данными о флагах"""
        con = sqlite3.connect(self.data_base)
        cur = con.cursor()
        flags = cur.execute(
            f'SELECT id, title, red, green, blue FROM flags WHERE category = {self.category_id}')
        index = 0
        for id_, title, r, g, b in flags:
            self.cbFlags.addItem(FlagIcon(QColor(r, g, b)), title, userData=id_)
            if cur_flag_id != -1 and id_ == cur_flag_id:
                self.cbFlags.setCurrentIndex(index)
            index += 1


class DateTimeDialog(QDialog, Ui_DateTimeDialog):
    def __init__(self, dt: datetime):
        super().__init__()
        super().setupUi(self)

        self.calendarWidget.setSelectedDate(dt.date())
        self.timeEdit.setTime(dt.time())

    def answer(self):
        dt = self.timeEdit.dateTime().toPyDateTime()
        date = self.calendarWidget.selectedDate().toPyDate()
        dt = dt.replace(year=date.year, month=date.month, day=date.day)
        return dt

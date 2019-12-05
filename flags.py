import sqlite3

from PyQt5.QtGui import QColor, QBrush, QIcon, QPixmap, QImage, QPalette
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QListWidget, QListWidgetItem, QAction, QMenu, QDialog, QColorDialog
from ui_FlagEditor import Ui_FlagEditor
from typing import Tuple


class FlagListWidgetItem(QListWidgetItem):
    def __init__(self, id_, data_base):
        self.id_ = id_
        self.data_base = data_base

        # Загрузка информации о флаге из бд
        con = sqlite3.connect(self.data_base)
        cur = con.cursor()
        self.title, r, g, b = cur.execute(
            f'SELECT title, red, green, blue FROM flags WHERE id = {self.id_}').fetchone()
        con.close()

        super().__init__(str(self))
        self.setBackground(QBrush(QColor(r, g, b)))

    def __str__(self):
        return self.title

    def deleteFromDB(self):
        """Удаляет себя из базы данных"""
        con = sqlite3.connect(self.data_base)
        cur = con.cursor()
        cur.execute(f'PRAGMA foreign_keys = 1;')
        cur.execute(f'DELETE FROM flags WHERE id = {self.id_}')
        con.commit()
        con.close()
        del self

    def open(self):
        print(self.id_, "flag was opened")


class FlagListWidget(QListWidget):
    """Предназначен для отображения существующих категорий в MainWindow"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.itemDoubleClicked.connect(self.openFlagEditor)

        self.data_base = ''  # Необходимо объявить вне класса
        self.category_id = 0

        # Инициализация действий
        self.acDelete = QAction(self)
        self.acDelete.setText("Delete")
        self.acDelete.triggered.connect(self.deleteFlags)

    def contextMenuEvent(self, event):
        """Создаём контекстное меню"""
        menu = QMenu(self)
        menu.addAction(self.acDelete)
        menu.exec(self.mapToGlobal(event.pos()))

    def deleteFlags(self):
        """Удаляет выбранные элементы из базы данных"""
        items = self.selectedItems()
        for item in items:
            item.deleteFromDB()
        self.reload()

    def loadFlagsId(self) -> list:
        con = sqlite3.connect(self.data_base)
        cur = con.cursor()
        ids = [tup[0] for tup in cur.execute(
            f'SELECT id FROM flags WHERE category = {self.category_id}').fetchall()]
        con.close()
        return ids

    def reload(self):
        self.clear()
        print("FlagsReload")
        ids = self.loadFlagsId()
        items = [FlagListWidgetItem(id_, self.data_base) for id_ in ids]
        for item in items:
            self.addItem(item)

    @staticmethod
    def openFlagEditor(item: FlagListWidgetItem):
        item.open()


class FlagIcon(QIcon):
    def __init__(self, c: QColor):
        self.color = c
        im = QImage(10, 10, QImage.Format_RGB444)
        im.fill(c)
        super().__init__(QPixmap.fromImage(im))


class FlagEditor(QDialog, Ui_FlagEditor):
    def __init__(self, data_base, category_id, flag_id=-1):
        super().__init__()
        self.category_id = category_id
        self.color = QColor(100, 100, 100)
        self.flag_id = flag_id
        self.data_base = data_base

        super().setupUi(self)
        self.pbColor.clicked.connect(self.changeColor)

    def changeColor(self):
        color = QColorDialog.getColor(initial=self.color, title="Выберите цвет")
        if color.isValid():
            self.color = color
            # настраиваем цвет leTitle
            self.leTitle.hide()
            palette = QPalette()
            brush = QBrush(color)
            brush.setStyle(Qt.SolidPattern)
            palette.setBrush(QPalette.Active, QPalette.Window, brush)
            self.leTitle.setPalette(palette)
            self.leTitle.setAutoFillBackground(True)
            self.leTitle.show()

            print("Color  SETUP")

    def accept(self) -> None:
        self.save()
        super().accept()

    def save(self):
        title = self.leTitle.text()
        r, g, b, a = self.color.getRgb()

        con = sqlite3.connect(self.data_base)
        cur = con.cursor()

        if self.flag_id == -1:
            # наибольший существующий id + 1
            old_id = cur.execute('SELECT id FROM flags ORDER BY id DESC').fetchone()
            if old_id:
                self.flag_id = old_id[0] + 1
            else:
                self.flag_id = 1

        # Создаёт или заменяет запись
        cur.execute(f'INSERT INTO flags(id, title, category, red, green, blue)'
                    f'VALUES(?, ?, ?, ?, ?, ?)',
                    (self.flag_id, title, self.category_id, r, g, b))
        con.commit()
        con.close()

    def answer(self) -> Tuple[str, QColor, int]:
        return self.leTitle.text(), self.color, self.flag_id
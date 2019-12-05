import sqlite3

from PyQt5.QtGui import QColor, QBrush, QIcon, QPixmap, QImage
from PyQt5.QtWidgets import QListWidget, QListWidgetItem, QAction, QMenu
from qtpy import QtCore


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
        ids = self.loadFlagsId()
        items = [FlagListWidgetItem(id_, self.data_base) for id_ in ids]
        for item in items:
            self.addItem(item)

    def openFlagEditor(self, item: FlagListWidgetItem):
        item.open()


class FlagIcon(QIcon):
    def __init__(self, c: QColor):
        self.color = c
        im = QImage(10, 10, QImage.Format_RGB444)
        im.fill(c)
        super().__init__(QPixmap.fromImage(im))
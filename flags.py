import sqlite3

from PyQt5.QtGui import QColor, QBrush, QIcon, QPixmap, QImage
from PyQt5.QtWidgets import QListWidget, QListWidgetItem, QAction, QMenu, QDialog, QColorDialog
from ui_FlagEditor import Ui_FlagEditor
from typing import Tuple


class FlagListWidgetItem(QListWidgetItem):
    def __init__(self, flag_id, data_base):
        self.flag_id = flag_id
        self.data_base = data_base

        # Загрузка информации о флаге из бд
        con = sqlite3.connect(self.data_base)
        cur = con.cursor()
        self.title, r, g, b = cur.execute(
            f'SELECT title, red, green, blue FROM flags WHERE id = {self.flag_id}').fetchone()
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
        cur.execute(f'DELETE FROM flags WHERE id = {self.flag_id}')
        con.commit()
        con.close()
        del self


class FlagListWidget(QListWidget):
    """Предназначен для отображения существующих категорий в MainWindow"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.data_base = self.parent().data_base
        self.category_id = self.parent().category_id

        # Инициализация действий
        self.acDelete = QAction(self)
        self.acDelete.setText("Delete")
        self.acDelete.triggered.connect(self.deleteFlags)
        self.acOpenEditor = QAction(self)
        self.acOpenEditor.setText("Edit")
        self.acOpenEditor.triggered.connect(self.openFlagEditor)

        # Настройка кликов
        self.editable = True
        self.itemClicked.connect(self.setFilter)

        self.reload()

    def contextMenuEvent(self, event):
        """Создаём контекстное меню"""
        if not self.editable:
            return None
        menu = QMenu(self)
        menu.addAction(self.acOpenEditor)
        menu.addAction(self.acDelete)
        menu.exec(self.mapToGlobal(event.pos()))

    def deleteFlags(self):
        """Удаляет выбранные элементы из базы данных"""
        items = self.selectedItems()
        for item in items:
            if isinstance(item, FlagListWidgetItem):
                item.deleteFromDB()
        self.parent().reload()

    def reload(self):
        self.clear()
        ids = self.parent().loadFlagsId()
        items = [FlagListWidgetItem(flag_id, self.data_base) for flag_id in ids]
        for item in items:
            self.addItem(item)

        if self.editable:
            self.addItem(QListWidgetItem("Показать все"))

    def openFlagEditor(self):
        if not self.editable:
            return None

        item = self.selectedItems()[0]
        if not isinstance(item, FlagListWidgetItem):
            return None
        self.dl = FlagEditor(self.data_base, self.category_id, item.flag_id)
        self.dl.exec()
        self.parent().reload()

    def setFilter(self, item):
        if not self.editable:
            return None

        if isinstance(item, FlagListWidgetItem):
            self.parent().setFlagFilter(item.flag_id)
        else:
            self.parent().setFlagFilter(-1)


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
        self.flag_id = flag_id
        self.data_base = data_base

        super().setupUi(self)
        self.loadData()
        self.pbColor.clicked.connect(self.changeColor)

    def loadData(self):
        """Заполняет виджеты данными из базы или стандартными"""
        if self.flag_id == -1:
            # Стандартные
            self.color = QColor(100, 100, 100)
            # Title оставляем пустым
        else:
            # Загружаем данные из базы
            con = sqlite3.connect(self.data_base)
            cur = con.cursor()
            title, r, g, b = cur.execute(
                f'SELECT title, red, green, blue FROM flags WHERE id = ?',
                (self.flag_id,)
            ).fetchone()
            con.commit()
            con.close()

            self.color = QColor(r, g, b)
            self.leTitle.setStyleSheet(
                f"background-color: rgb({r}, {g}, {b});")
            self.leTitle.setText(title)

    def changeColor(self):
        color = QColorDialog.getColor(initial=self.color)
        if color.isValid():
            self.color = color
            # настраиваем цвет leTitle
            self.leTitle.setStyleSheet(
                f"background-color: rgb({color.red()}, {color.green()}, {color.blue()});")

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

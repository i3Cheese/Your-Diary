from PyQt5.QtWidgets import QListWidget
from PyQt5.QtWidgets import QMenu
from PyQt5.QtWidgets import QAction
import sqlite3
from Categories import CategoryListWidgetItem


class DiaryListWidget(QListWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.itemDoubleClicked.connect(self.openCategory)

    def contextMenuEvent(self, event):
        menu = QMenu(self)
        action = QAction("Delete")
        action.triggered.connect(self.deleteCategory)
        menu.addAction(action)
        menu.exec(self.mapToGlobal(event.pos()))

    def deleteCategory(self):
        item = self.selectedItems()[0]
        item.deleteFromDB()
        self.showCategories()

    def setDB(self, date_base):
        self.data_base = date_base

    def loadCategoriesId(self):
        con = sqlite3.connect(self.data_base)
        cur = con.cursor()
        ids = [tup[0] for tup in cur.execute(
            f'SELECT id FROM categories ORDER BY NOT creation').fetchall()]
        con.close()
        return ids

    def showCategories(self):
        ids = self.loadCategoriesId()
        items = [CategoryListWidgetItem(id_, self.data_base) for id_ in ids]
        self.clear()
        for item in items:
            self.addItem(item)

    def openCategory(self, item):
        item.open()


import sqlite3
from PyQt5.QtWidgets import QListWidgetItem, QWidget
from ui_category import Ui_Category
from datetime import datetime


DEFAULT_CATEGORY = 1
BUDGET_CATEGORY = 2


class CategoryListWidgetItem(QListWidgetItem):
    def __init__(self, id_, data_base):
        self.id_ = id_
        self.data_base = data_base

        # Загрузка информации о категории из бд
        con = sqlite3.connect(self.data_base)
        cur = con.cursor()
        self.title, creation, self.categoryType = cur.execute(
                f'SELECT title, creation, type FROM categories WHERE id = {self.id_}').fetchone()
        con.close()
        self.creation = datetime.fromisoformat(creation)

        super().__init__(str(self))

    def open(self):
        if self.categoryType == DEFAULT_CATEGORY:
            self.widget = CategoryWidget(self.id_, self.data_base)
            self.widget.show()
        else:
            # TODO: add budgetCategoryWidget
            pass

    def __str__(self):
        return f'"{self.title}". {"БЮДЖЕТ. " if self.categoryType == BUDGET_CATEGORY else ""}' \
               f'Создан {self.creation}.'

    def __lt__(self, other):
        return self.creation < other.creation


class CategoryWidget(QWidget, Ui_Category):
    def __init__(self, id_, data_base):
        super().__init__()

        self.id_ = id_
        self.data_base = data_base

        # Загрузка информации о категории из бд
        con = sqlite3.connect(self.data_base)
        cur = con.cursor()
        self.title, self.creation = \
            cur.execute(f'SELECT title, creation FROM categories WHERE id = {self.id_}').fetchone()
        con.close()

        self.setupUi(self)

    def setupUi(self, Category):
        super().setupUi(Category)
        self.setWindowTitle(self.title)

    def loadNotes(self):
        con = sqlite3.connect(self.data_base)
        cur = con.cursor()
        notes = cur.execute(f'SELECT * FROM defaultNotes WHERE category = {self.id_}').fetchall()
        con.close()
        return notes

    def loadFlags(self):
        con = sqlite3.connect(self.data_base)
        cur = con.cursor()
        flags = cur.execute(f'SELECT * FROM defaultNotes WHERE category = {self.id_}').fetchall()
        con.close()
        return flags


class BudgetCategory():
    pass
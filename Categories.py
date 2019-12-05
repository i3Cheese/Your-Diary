import sqlite3
from PyQt5.QtWidgets import QListWidgetItem, QWidget, QDialog, QListWidget, QAction, QMenu

from ui_CategoryCreateDialog import Ui_CategoryCreateDialog
from ui_category import Ui_Category
from datetime import datetime
from notes import NoteEditor

DEFAULT_CATEGORY = 1
BUDGET_CATEGORY = 2


class CategoryCreateDialog(QDialog, Ui_CategoryCreateDialog):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)

    def answer(self) -> tuple:
        title = self.leTitle.text()
        categoryType = DEFAULT_CATEGORY if self.rbDefault.isChecked() \
            else BUDGET_CATEGORY if self.rbBudget.isChecked() else None
        return title, categoryType


class CategoryListWidgetItem(QListWidgetItem):
    """Общия для Budget и Default"""
    data_base: str
    id_: int

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

    def deleteFromDB(self):
        """Удаляет себя из базы данных"""
        con = sqlite3.connect(self.data_base)
        cur = con.cursor()
        cur.execute(f'PRAGMA foreign_keys = 1;')
        cur.execute(f'DELETE FROM categories WHERE id = {self.id_}')
        con.commit()
        con.close()
        del self


class DiaryListWidget(QListWidget):
    """Предназначен для отображения существующих категорий в MainWindow"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.itemDoubleClicked.connect(self.openCategory)

        self.data_base = ''  # Необходимо объявить вне класса

        # Инициализация действий
        self.acDelete = QAction(self)
        self.acDelete.setText("Delete")
        self.acDelete.triggered.connect(self.deleteCategories)

    def contextMenuEvent(self, event):
        """Создаём контекстное меню"""
        menu = QMenu(self)
        menu.addAction(self.acDelete)
        menu.exec(self.mapToGlobal(event.pos()))

    def deleteCategories(self):
        """Удаляет выбранные элементы из базы данных"""
        items = self.selectedItems()
        for item in items:
            item.deleteFromDB()
        self.reload()

    def loadCategoriesId(self) -> list:
        con = sqlite3.connect(self.data_base)
        cur = con.cursor()
        ids = [tup[0] for tup in cur.execute(
            f'SELECT id FROM categories ORDER BY NOT creation').fetchall()]
        con.close()
        return ids

    def reload(self):
        ids = self.loadCategoriesId()
        items = [CategoryListWidgetItem(id_, self.data_base) for id_ in ids]
        self.clear()
        for item in items:
            self.addItem(item)

    def openCategory(self, item: CategoryListWidgetItem):
        item.open()


class CategoryWidget(QWidget, Ui_Category):
    data_base: str
    id_: int

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

        # инициализируем TableWidget и ListWidget
        self.tableWidget.data_base = self.listWidget.data_base = self.data_base
        self.tableWidget.category_id = self.listWidget.category_id = self.id_
        self.tableWidget.reload()
        self.listWidget.reload()
        # инициализируем ListWidget=
        # TODO: resize CategoryWidget
        self.resize(
            self.verticalLayout.maximumSize().width() + self.tableWidget.size().width() + 49,
            self.height())
        self.setMinimumWidth(self.size().width())

        self.pbNew.clicked.connect(self.createNote)
        self.pbNew.setShortcut("Ctrl+N")

    def createNote(self):
        """Открытие редактора"""
        self.editor = NoteEditor(self.data_base, self.id_, -1)
        self.editor.exec()
        self.tableWidget.reload()

    def setupUi(self, Category):
        super().setupUi(Category)
        self.setWindowTitle(self.title)

    def loadNotes(self) -> list:
        con = sqlite3.connect(self.data_base)
        cur = con.cursor()
        notes = cur.execute(f'SELECT * FROM defaultNotes WHERE category = {self.id_}').fetchall()
        con.close()
        return notes

    def loadFlags(self) -> list:
        con = sqlite3.connect(self.data_base)
        cur = con.cursor()
        flags = cur.execute(f'SELECT * FROM defaultNotes WHERE category = {self.id_}').fetchall()
        con.close()
        return flags


class BudgetCategory():
    pass

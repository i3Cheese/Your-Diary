import sqlite3

from PyQt5.QtWidgets import QListWidgetItem, QWidget, QDialog, QListWidget, QAction, QMenu

from ui_CategoryCreateDialog import Ui_CategoryCreateDialog
from ui_category import Ui_Category
from datetime import datetime
from notes import NoteEditor
from flags import FlagEditor
from diagram import DiagramWidget

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
    category_id: int

    def __init__(self, category_id, data_base):
        super().__init__()

        self.category_id = category_id
        self.data_base = data_base

        # Загрузка информации о категории из бд
        con = sqlite3.connect(self.data_base)
        cur = con.cursor()
        self.title, self.creation = \
            cur.execute(
                f'SELECT title, creation FROM categories WHERE id = {self.category_id}').fetchone()
        con.close()

        self.setupUi(self)

        # Отображаем записи(Если делать это в __init__ NotesTableWidget то их не будет видно)
        self.tableWidget.reload()

        # Настройки размера окна
        self.resize(
            self.verticalLayout.maximumSize().width() + self.tableWidget.size().width() + 35,
            self.height())  # +35 компенсирует пространство между виджетами
        # 35 я подобрал, на других устройствах может быть подругому.
        self.setMinimumWidth(self.size().width())

        # Настройки кнопок
        self.pbNew.clicked.connect(self.createNote)
        self.pbNew.setShortcut("Ctrl+N")
        self.pbAddFlag.clicked.connect(self.createFlag)
        self.pbChart.clicked.connect(self.openDiagram)

    def createNote(self):
        """Открытие редактора"""
        self.editor = NoteEditor(self.data_base, self.category_id, -1)
        self.editor.exec()
        self.tableWidget.reload()
        self.listWidget.reload()

    def setupUi(self, Category):
        super().setupUi(Category)
        self.setWindowTitle(self.title)

    def loadNotes(self, flag_id=-1) -> list:
        con = sqlite3.connect(self.data_base)
        cur = con.cursor()
        if flag_id == -1:
            notes = cur.execute(
                f'SELECT id, start, end, text, flag '
                f'FROM defaultNotes WHERE category = {self.category_id}'
            ).fetchall()
        else:  # фильтрация по флагу
            notes = cur.execute(
                f'SELECT id, start, end, text, flag '
                f'FROM defaultNotes WHERE category = {self.category_id} '
                f'AND flag = {flag_id}'
            ).fetchall()
        con.close()
        return notes

    def loadFlagsId(self) -> list:
        con = sqlite3.connect(self.data_base)
        cur = con.cursor()
        ids = [tup[0] for tup in cur.execute(
            f'SELECT id FROM flags WHERE category = {self.category_id}').fetchall()]
        con.close()
        return ids

    def createFlag(self):
        self.dl = FlagEditor(self.data_base, self.category_id)
        self.dl.exec()
        self.listWidget.reload()

    def setFlagFilter(self, flag_id: int = -1):
        self.tableWidget.setFlagFilter(flag_id)

    def reload(self):
        self.tableWidget.reload()
        self.listWidget.reload()

    def openDiagram(self):
        self.dia = DiagramWidget(self)
        self.dia.show()


class BudgetCategory():
    pass

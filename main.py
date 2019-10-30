import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow
from ui_mainWindow import Ui_MainWindow
from dialogs import CategoryCreateDialog
from Categories import CategoryListWidgetItem
from datetime import datetime
import sqlite3

DATA_BASE = '_Your_Diary.db'


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setupDB()

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.acCreate.triggered.connect(self.create_category)
        self.lwCategories.setDB(DATA_BASE)
        self.lwCategories.showCategories()

    def create_category(self) -> None:
        """Запрашивает название и тип категории через CategoryCreateDialog и затем создает её
        вызвав addCategory. Вызывается пользователем"""
        self.dialog = CategoryCreateDialog()
        if not self.dialog.exec():
            return None
        title, categoryType = self.dialog.answer()
        self.addCategory(title, categoryType)
        self.lwCategories.showCategories()

    def addCategory(self, title, categoryType) -> None:
        """Добавляет категорию в базу. В качестве creation использует системное время"""
        creation = datetime.today().replace(microsecond=0)
        con = sqlite3.connect(DATA_BASE)
        cur = con.cursor()
        cur.execute(f'''INSERT INTO categories(type, title, creation) '''
                    f'''VALUES({categoryType}, "{title}", "{creation.isoformat(" ")}");''')
        con.commit()
        con.close()

    def setupDB(self):
        """Подключается к существующей или создаёт свою базу данных.
        Если в папке с программой существовала база с таким же названием, но другой архитектурой
        программа будет работать некорректно."""
        if os.path.exists(DATA_BASE):
            return None
        else:
            con = sqlite3.connect(DATA_BASE)
            cur = con.cursor()

            # Создаём таблицу категорий
            cur.execute('''CREATE TABLE categories (
    id       INTEGER  PRIMARY KEY ON CONFLICT REPLACE AUTOINCREMENT
                      NOT NULL,
    type     INTEGER,
    title    STRING,
    creation DATETIME);''')

            # Создаём таблицу флагов
            cur.execute('''CREATE TABLE flags (
    id       INTEGER PRIMARY KEY ON CONFLICT REPLACE AUTOINCREMENT
                     NOT NULL,
    category INTEGER REFERENCES categories (id) ON DELETE CASCADE
                     NOT NULL,
    title    STRING,
    red      INTEGER,
    green    INTEGER,
    blue     INTEGER);''')  # red, green, blue - значение каналов RGB

            # Создаём таблицу записей стандартного типа
            cur.execute('''CREATE TABLE defaultNotes (
    id       INTEGER  PRIMARY KEY ON CONFLICT REPLACE AUTOINCREMENT,
    category INTEGER  REFERENCES categories (id) ON DELETE CASCADE,
    text     TEXT,
    flag     INTEGER  REFERENCES flags (id) ON DELETE SET NULL,
    start    DATETIME,
    [end]    DATETIME);''')

            # TODO: Создаём таблицу записей типа budget

            con.commit()
            con.close()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    mw = MainWindow()
    mw.show()
    sys.exit(app.exec())

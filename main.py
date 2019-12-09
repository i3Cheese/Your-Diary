import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QStyleFactory
from PyQt5.QtGui import QIcon

from ui_mainWindow import Ui_MainWindow
from Categories import CategoryCreateDialog
from datetime import datetime
import sqlite3


class MainWindow(QMainWindow, Ui_MainWindow):
    date_base = "_Your_Diary.db"

    def __init__(self):
        super().__init__()
        self.setupDB()
        self.setupUi(self)
        self.update()

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.acCreate.triggered.connect(self.createCategory)

        self.lwCategories.data_base = self.date_base
        self.lwCategories.reload()

    def createCategory(self) -> None:
        """Запрашивает название через CategoryCreateDialog и затем создает её
        вызвав addCategory. Вызывается пользователем"""
        self.dialog = CategoryCreateDialog()
        if not self.dialog.exec():
            return None
        title = self.dialog.answer()
        self.addCategory(title)
        self.lwCategories.reload()

    def addCategory(self, title:  str) -> None:
        """Добавляет категорию в базу. В качестве creation использует системное время"""
        creation = datetime.today().replace(microsecond=0)
        con = sqlite3.connect(self.date_base)
        cur = con.cursor()
        cur.execute(f'''INSERT INTO categories(type, title, creation) '''
                    f'''VALUES(1, "{title}", "{creation.isoformat(" ")}");''')
        con.commit()
        con.close()

    def setupDB(self) -> None:
        """Подключается к существующей или создаёт свою базу данных.
        Если в папке с программой существовала база с таким же названием, но другой архитектурой
        программа будет работать некорректно."""
        if os.path.exists(self.date_base):
            return None
        else:
            con = sqlite3.connect(self.date_base)
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
    id       INTEGER PRIMARY KEY ASC ON CONFLICT REPLACE AUTOINCREMENT,
    title    STRING  NOT NULL,
    category INTEGER REFERENCES categories (id) ON DELETE CASCADE
                     NOT NULL,
    red      INTEGER,
    green    INTEGER,
    blue     INTEGER
);''')  # red, green, blue - значение каналов RGB

            # Создаём таблицу записей
            cur.execute('''CREATE TABLE defaultNotes (
    id       INTEGER  PRIMARY KEY ON CONFLICT REPLACE AUTOINCREMENT,
    category INTEGER  REFERENCES categories (id) ON DELETE CASCADE,
    text     TEXT,
    flag     INTEGER  REFERENCES flags (id) ON DELETE SET NULL
                                            ON UPDATE CASCADE,
    start    DATETIME,
    [end]    DATETIME
);''')

            con.commit()
            con.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    icon = QIcon('icon.png')
    app.setWindowIcon(icon)
    app.setStyle(QStyleFactory.create('Fusion'))
    mw = MainWindow()
    mw.show()
    sys.exit(app.exec())

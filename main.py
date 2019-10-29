import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from ui_mainWindow import Ui_MainWindow
from dialogs import CategoryCreateDialog


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.acCreate.triggered.connect(self.create_category)

    def create_category(self) -> None:
        """Запрашивает название и тип категории через CategoryCreateDialog и затем создает её
        вызвав addCategory. Вызывается пользователем"""
        self.dialog = CategoryCreateDialog()
        if not self.dialog.exec():
            return None
        title, categoryType = self.dialog.reject()

    def addCategory(self, title, category) -> None:
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mw = MainWindow()
    mw.show()
    sys.exit(app.exec())

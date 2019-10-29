from PyQt5.QtWidgets import QDialog
from ui_CategoryCreateDialog import Ui_CategoryCreateDialog
from Categories import *


class CategoryCreateDialog(QDialog, Ui_CategoryCreateDialog):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)

    def reject(self) -> tuple:
        title = self.leTitle.text()
        categoryType = Category if self.rbDefault.isChecked() \
                        else BudgetCategory if self.rbBudget.isChecked() else None
        return title, categoryType

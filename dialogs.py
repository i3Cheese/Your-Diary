from PyQt5.QtWidgets import QDialog
from ui_CategoryCreateDialog import Ui_CategoryCreateDialog
from Categories import DEFAULT_CATEGORY, BUDGET_CATEGORY


class CategoryCreateDialog(QDialog, Ui_CategoryCreateDialog):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)

    def answer(self) -> tuple:
        title = self.leTitle.text()
        categoryType = DEFAULT_CATEGORY if self.rbDefault.isChecked() \
                        else BUDGET_CATEGORY if self.rbBudget.isChecked() else None
        return title, categoryType

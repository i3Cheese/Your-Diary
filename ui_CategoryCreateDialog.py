# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_CategoryCreateDialog.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_CategoryCreateDialog(object):
    def setupUi(self, CategoryCreateDialog):
        CategoryCreateDialog.setObjectName("CategoryCreateDialog")
        CategoryCreateDialog.resize(365, 200)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(CategoryCreateDialog.sizePolicy().hasHeightForWidth())
        CategoryCreateDialog.setSizePolicy(sizePolicy)
        CategoryCreateDialog.setMinimumSize(QtCore.QSize(0, 200))
        CategoryCreateDialog.setMaximumSize(QtCore.QSize(16777215, 200))
        CategoryCreateDialog.setStyleSheet("background-color: rgb(0, 44, 44);\n"
"selection-background-color: rgb(7, 52, 80);\n"
"alternate-background-color: rgb(0, 25, 25);\n"
"\n"
"color: rgb(217, 212, 199);\n"
"\n"
"font: 11.5pt \"MS Shell Dlg 2\";")
        self.verticalLayout = QtWidgets.QVBoxLayout(CategoryCreateDialog)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(CategoryCreateDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.leTitle = QtWidgets.QLineEdit(CategoryCreateDialog)
        self.leTitle.setInputMask("")
        self.leTitle.setText("")
        self.leTitle.setObjectName("leTitle")
        self.verticalLayout.addWidget(self.leTitle)
        spacerItem = QtWidgets.QSpacerItem(20, 16, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.label_2 = QtWidgets.QLabel(CategoryCreateDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.rbDefault = QtWidgets.QRadioButton(CategoryCreateDialog)
        self.rbDefault.setChecked(True)
        self.rbDefault.setObjectName("rbDefault")
        self.verticalLayout.addWidget(self.rbDefault)
        self.rbBudget = QtWidgets.QRadioButton(CategoryCreateDialog)
        self.rbBudget.setObjectName("rbBudget")
        self.verticalLayout.addWidget(self.rbBudget)
        self.buttonBox = QtWidgets.QDialogButtonBox(CategoryCreateDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)
        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 1)
        self.verticalLayout.setStretch(2, 1)
        self.verticalLayout.setStretch(3, 1)
        self.verticalLayout.setStretch(4, 3)
        self.verticalLayout.setStretch(5, 3)
        self.verticalLayout.setStretch(6, 3)

        self.retranslateUi(CategoryCreateDialog)
        self.buttonBox.accepted.connect(CategoryCreateDialog.accept)
        self.buttonBox.rejected.connect(CategoryCreateDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(CategoryCreateDialog)

    def retranslateUi(self, CategoryCreateDialog):
        _translate = QtCore.QCoreApplication.translate
        CategoryCreateDialog.setWindowTitle(_translate("CategoryCreateDialog", "Новая категория"))
        self.label.setText(_translate("CategoryCreateDialog", "Название:"))
        self.leTitle.setPlaceholderText(_translate("CategoryCreateDialog", "Мои сновидения"))
        self.label_2.setText(_translate("CategoryCreateDialog", "Тип:"))
        self.rbDefault.setText(_translate("CategoryCreateDialog", "Обычный"))
        self.rbBudget.setText(_translate("CategoryCreateDialog", "Бюджет"))


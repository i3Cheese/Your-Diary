# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/ui_CategoryCreateDialog.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_CategoryCreateDialog(object):
    def setupUi(self, CategoryCreateDialog):
        CategoryCreateDialog.setObjectName("CategoryCreateDialog")
        CategoryCreateDialog.setWindowModality(QtCore.Qt.WindowModal)
        CategoryCreateDialog.resize(365, 144)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(CategoryCreateDialog.sizePolicy().hasHeightForWidth())
        CategoryCreateDialog.setSizePolicy(sizePolicy)
        CategoryCreateDialog.setMinimumSize(QtCore.QSize(365, 144))
        CategoryCreateDialog.setMaximumSize(QtCore.QSize(123456, 144))
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
        self.lblTitle = QtWidgets.QLabel(CategoryCreateDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblTitle.sizePolicy().hasHeightForWidth())
        self.lblTitle.setSizePolicy(sizePolicy)
        self.lblTitle.setObjectName("lblTitle")
        self.verticalLayout.addWidget(self.lblTitle)
        self.leTitle = QtWidgets.QLineEdit(CategoryCreateDialog)
        self.leTitle.setInputMask("")
        self.leTitle.setText("")
        self.leTitle.setObjectName("leTitle")
        self.verticalLayout.addWidget(self.leTitle)
        self.buttonBox = QtWidgets.QDialogButtonBox(CategoryCreateDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)
        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 1)
        self.verticalLayout.setStretch(2, 3)

        self.retranslateUi(CategoryCreateDialog)
        self.buttonBox.accepted.connect(CategoryCreateDialog.accept)
        self.buttonBox.rejected.connect(CategoryCreateDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(CategoryCreateDialog)

    def retranslateUi(self, CategoryCreateDialog):
        _translate = QtCore.QCoreApplication.translate
        CategoryCreateDialog.setWindowTitle(_translate("CategoryCreateDialog", "Новая категория"))
        self.lblTitle.setText(_translate("CategoryCreateDialog", "Название:"))
        self.leTitle.setPlaceholderText(_translate("CategoryCreateDialog", "Мои сновидения"))

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/ui_FlagEditor.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_FlagEditor(object):
    def setupUi(self, FlagEditor):
        FlagEditor.setObjectName("FlagEditor")
        FlagEditor.resize(325, 117)
        FlagEditor.setMinimumSize(QtCore.QSize(0, 117))
        FlagEditor.setMaximumSize(QtCore.QSize(16777215, 117))
        FlagEditor.setStyleSheet("background-color: rgb(0, 44, 44);\n"
"selection-background-color: rgb(7, 52, 80);\n"
"alternate-background-color: rgb(0, 85, 0);\n"
"\n"
"color: rgb(217, 212, 199);\n"
"\n"
"font: 11.5pt \"MS Shell Dlg 2\";")
        self.gridLayout = QtWidgets.QGridLayout(FlagEditor)
        self.gridLayout.setObjectName("gridLayout")
        self.leTitle = QtWidgets.QLineEdit(FlagEditor)
        self.leTitle.setObjectName("leTitle")
        self.gridLayout.addWidget(self.leTitle, 0, 0, 1, 1)
        self.lbTitle = QtWidgets.QLabel(FlagEditor)
        self.lbTitle.setTextFormat(QtCore.Qt.AutoText)
        self.lbTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.lbTitle.setObjectName("lbTitle")
        self.gridLayout.addWidget(self.lbTitle, 0, 1, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(FlagEditor)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 2, 0, 1, 2)
        self.pbColor = QtWidgets.QPushButton(FlagEditor)
        self.pbColor.setDefault(False)
        self.pbColor.setObjectName("pbColor")
        self.gridLayout.addWidget(self.pbColor, 1, 1, 1, 1)

        self.retranslateUi(FlagEditor)
        self.buttonBox.accepted.connect(FlagEditor.accept)
        self.buttonBox.rejected.connect(FlagEditor.reject)
        QtCore.QMetaObject.connectSlotsByName(FlagEditor)

    def retranslateUi(self, FlagEditor):
        _translate = QtCore.QCoreApplication.translate
        FlagEditor.setWindowTitle(_translate("FlagEditor", "Флаг"))
        self.lbTitle.setText(_translate("FlagEditor", "Название"))
        self.pbColor.setText(_translate("FlagEditor", "Выбор цвета"))


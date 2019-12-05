# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI/ui_DateTimeDialog.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_DateTimeDialog(object):
    def setupUi(self, DateTimeDialog):
        DateTimeDialog.setObjectName("DateTimeDialog")
        DateTimeDialog.resize(400, 300)
        DateTimeDialog.setStyleSheet("background-color: rgb(0, 44, 44);\n"
"selection-background-color: rgb(7, 52, 80);\n"
"alternate-background-color: rgb(0, 85, 0);\n"
"\n"
"color: rgb(217, 212, 199);\n"
"\n"
"font: 11.5pt \"MS Shell Dlg 2\";")
        self.gridLayout = QtWidgets.QGridLayout(DateTimeDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.calendarWidget = QtWidgets.QCalendarWidget(DateTimeDialog)
        self.calendarWidget.setObjectName("calendarWidget")
        self.gridLayout.addWidget(self.calendarWidget, 0, 0, 1, 2)
        self.timeEdit = QtWidgets.QTimeEdit(DateTimeDialog)
        self.timeEdit.setAutoFillBackground(True)
        self.timeEdit.setButtonSymbols(QtWidgets.QAbstractSpinBox.UpDownArrows)
        self.timeEdit.setObjectName("timeEdit")
        self.gridLayout.addWidget(self.timeEdit, 1, 0, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(DateTimeDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 1, 1, 1, 1)

        self.retranslateUi(DateTimeDialog)
        self.buttonBox.accepted.connect(DateTimeDialog.accept)
        self.buttonBox.rejected.connect(DateTimeDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(DateTimeDialog)

    def retranslateUi(self, DateTimeDialog):
        _translate = QtCore.QCoreApplication.translate
        DateTimeDialog.setWindowTitle(_translate("DateTimeDialog", "Dialog"))


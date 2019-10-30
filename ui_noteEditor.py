# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_noteEditor.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_noteEditor(object):
    def setupUi(self, noteEditor):
        noteEditor.setObjectName("noteEditor")
        noteEditor.resize(578, 379)
        noteEditor.setStyleSheet("background-color: rgb(0, 44, 44);\n"
"selection-background-color: rgb(7, 52, 80);\n"
"alternate-background-color: rgb(0, 85, 0);\n"
"\n"
"color: rgb(217, 212, 199);\n"
"\n"
"font: 11.5pt \"MS Shell Dlg 2\";")
        self.gridLayout_2 = QtWidgets.QGridLayout(noteEditor)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.textEdit = QtWidgets.QTextEdit(noteEditor)
        self.textEdit.setStyleSheet("background-color: rgb(0, 25, 25);")
        self.textEdit.setObjectName("textEdit")
        self.gridLayout_2.addWidget(self.textEdit, 1, 0, 1, 4)
        self.label = QtWidgets.QLabel(noteEditor)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.dateTimeEdit = QtWidgets.QDateTimeEdit(noteEditor)
        self.dateTimeEdit.setObjectName("dateTimeEdit")
        self.gridLayout.addWidget(self.dateTimeEdit, 2, 1, 1, 1)
        self.dteStart = QtWidgets.QDateTimeEdit(noteEditor)
        self.dteStart.setObjectName("dteStart")
        self.gridLayout.addWidget(self.dteStart, 2, 0, 1, 1)
        self.cbFlags = QtWidgets.QComboBox(noteEditor)
        self.cbFlags.setFrame(False)
        self.cbFlags.setObjectName("cbFlags")
        self.gridLayout.addWidget(self.cbFlags, 2, 2, 1, 1)
        self.pbStart = QtWidgets.QPushButton(noteEditor)
        self.pbStart.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.pbStart.setAcceptDrops(False)
        self.pbStart.setAutoFillBackground(False)
        self.pbStart.setFlat(True)
        self.pbStart.setObjectName("pbStart")
        self.gridLayout.addWidget(self.pbStart, 1, 0, 1, 1)
        self.pbFlag = QtWidgets.QPushButton(noteEditor)
        self.pbFlag.setFlat(True)
        self.pbFlag.setObjectName("pbFlag")
        self.gridLayout.addWidget(self.pbFlag, 1, 2, 1, 1)
        self.pbEnd = QtWidgets.QPushButton(noteEditor)
        self.pbEnd.setFlat(True)
        self.pbEnd.setObjectName("pbEnd")
        self.gridLayout.addWidget(self.pbEnd, 1, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 2, 0, 1, 4)
        self.pushButton_2 = QtWidgets.QPushButton(noteEditor)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout_2.addWidget(self.pushButton_2, 3, 3, 1, 1)
        self.pushButton = QtWidgets.QPushButton(noteEditor)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_2.addWidget(self.pushButton, 3, 2, 1, 1)

        self.retranslateUi(noteEditor)
        QtCore.QMetaObject.connectSlotsByName(noteEditor)

    def retranslateUi(self, noteEditor):
        _translate = QtCore.QCoreApplication.translate
        noteEditor.setWindowTitle(_translate("noteEditor", "Запись"))
        self.label.setText(_translate("noteEditor", "Текст"))
        self.pbStart.setText(_translate("noteEditor", "Начало"))
        self.pbFlag.setText(_translate("noteEditor", "Флаг"))
        self.pbEnd.setText(_translate("noteEditor", "Конец"))
        self.pushButton_2.setText(_translate("noteEditor", "Отмена"))
        self.pushButton_2.setShortcut(_translate("noteEditor", "Esc"))
        self.pushButton.setText(_translate("noteEditor", "Ок"))


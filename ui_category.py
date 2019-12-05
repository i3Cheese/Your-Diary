# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/ui_category.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from notes import NotesTableWidget
from flags import FlagListWidget

class Ui_Category(object):
    def setupUi(self, Category):
        Category.setObjectName("Category")
        Category.resize(912, 517)
        Category.setStyleSheet("background-color: rgb(0, 44, 44);\n"
"selection-background-color: rgb(7, 52, 80);\n"
"alternate-background-color: rgb(0, 85, 0);\n"
"\n"
"color: rgb(217, 212, 199);\n"
"\n"
"font: 11.5pt \"MS Shell Dlg 2\";")
        self.horizontalLayout = QtWidgets.QHBoxLayout(Category)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.pbNew = QtWidgets.QPushButton(Category)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pbNew.sizePolicy().hasHeightForWidth())
        self.pbNew.setSizePolicy(sizePolicy)
        self.pbNew.setMinimumSize(QtCore.QSize(183, 87))
        self.pbNew.setMaximumSize(QtCore.QSize(183, 87))
        self.pbNew.setStyleSheet("background-color: rgb(0, 25, 25);")
        self.pbNew.setObjectName("pbNew")
        self.verticalLayout.addWidget(self.pbNew)
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem)
        self.pbLoadShedule = QtWidgets.QPushButton(Category)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pbLoadShedule.sizePolicy().hasHeightForWidth())
        self.pbLoadShedule.setSizePolicy(sizePolicy)
        self.pbLoadShedule.setMinimumSize(QtCore.QSize(183, 52))
        self.pbLoadShedule.setMaximumSize(QtCore.QSize(183, 52))
        self.pbLoadShedule.setStyleSheet("background-color: rgb(0, 25, 25);")
        self.pbLoadShedule.setObjectName("pbLoadShedule")
        self.verticalLayout.addWidget(self.pbLoadShedule)
        self.pbChart = QtWidgets.QPushButton(Category)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pbChart.sizePolicy().hasHeightForWidth())
        self.pbChart.setSizePolicy(sizePolicy)
        self.pbChart.setMinimumSize(QtCore.QSize(183, 53))
        self.pbChart.setMaximumSize(QtCore.QSize(183, 53))
        self.pbChart.setStyleSheet("background-color: rgb(0, 25, 25);")
        self.pbChart.setObjectName("pbChart")
        self.verticalLayout.addWidget(self.pbChart)
        self.pbAddFlag = QtWidgets.QPushButton(Category)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pbAddFlag.sizePolicy().hasHeightForWidth())
        self.pbAddFlag.setSizePolicy(sizePolicy)
        self.pbAddFlag.setMinimumSize(QtCore.QSize(183, 35))
        self.pbAddFlag.setMaximumSize(QtCore.QSize(183, 35))
        self.pbAddFlag.setStyleSheet("background-color: rgb(0, 25, 25);")
        self.pbAddFlag.setObjectName("pbAddFlag")
        self.verticalLayout.addWidget(self.pbAddFlag)
        spacerItem1 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem1)
        self.label = QtWidgets.QLabel(Category)
        self.label.setMinimumSize(QtCore.QSize(183, 18))
        self.label.setMaximumSize(QtCore.QSize(183, 18))
        self.label.setStyleSheet("")
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.listWidget = FlagListWidget(Category)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listWidget.sizePolicy().hasHeightForWidth())
        self.listWidget.setSizePolicy(sizePolicy)
        self.listWidget.setMaximumSize(QtCore.QSize(183, 16777215))
        self.listWidget.setStyleSheet("background-color: rgb(0, 25, 25);")
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout.addWidget(self.listWidget)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.tableWidget = NotesTableWidget(Category)
        self.tableWidget.setStyleSheet("background-color: rgb(0, 25, 25);")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.horizontalLayout.addWidget(self.tableWidget)

        self.retranslateUi(Category)
        QtCore.QMetaObject.connectSlotsByName(Category)

    def retranslateUi(self, Category):
        _translate = QtCore.QCoreApplication.translate
        Category.setWindowTitle(_translate("Category", "Какая-то категория"))
        self.pbNew.setText(_translate("Category", "Новая запись"))
        self.pbNew.setShortcut(_translate("Category", "Ctrl+N"))
        self.pbLoadShedule.setText(_translate("Category", "График загружености"))
        self.pbChart.setText(_translate("Category", "Диаграмма"))
        self.pbAddFlag.setText(_translate("Category", "Добавить флаг"))
        self.label.setText(_translate("Category", "Флаги:"))


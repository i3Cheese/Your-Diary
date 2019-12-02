# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI/ui_category.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from notes import CategoryTableWidget

class Ui_Category(object):
    def setupUi(self, Category):
        Category.setObjectName("Category")
        Category.resize(690, 514)
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
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pbNew.sizePolicy().hasHeightForWidth())
        self.pbNew.setSizePolicy(sizePolicy)
        self.pbNew.setStyleSheet("background-color: rgb(0, 25, 25);")
        self.pbNew.setObjectName("pbNew")
        self.verticalLayout.addWidget(self.pbNew)
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.pbLoadShedule = QtWidgets.QPushButton(Category)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pbLoadShedule.sizePolicy().hasHeightForWidth())
        self.pbLoadShedule.setSizePolicy(sizePolicy)
        self.pbLoadShedule.setStyleSheet("background-color: rgb(0, 25, 25);")
        self.pbLoadShedule.setObjectName("pbLoadShedule")
        self.verticalLayout.addWidget(self.pbLoadShedule)
        self.pbChart = QtWidgets.QPushButton(Category)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pbChart.sizePolicy().hasHeightForWidth())
        self.pbChart.setSizePolicy(sizePolicy)
        self.pbChart.setStyleSheet("background-color: rgb(0, 25, 25);")
        self.pbChart.setObjectName("pbChart")
        self.verticalLayout.addWidget(self.pbChart)
        self.pbAddFlag = QtWidgets.QPushButton(Category)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pbAddFlag.sizePolicy().hasHeightForWidth())
        self.pbAddFlag.setSizePolicy(sizePolicy)
        self.pbAddFlag.setStyleSheet("background-color: rgb(0, 25, 25);")
        self.pbAddFlag.setObjectName("pbAddFlag")
        self.verticalLayout.addWidget(self.pbAddFlag)
        spacerItem1 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.label = QtWidgets.QLabel(Category)
        self.label.setStyleSheet("")
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.listView = QtWidgets.QListView(Category)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(10)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listView.sizePolicy().hasHeightForWidth())
        self.listView.setSizePolicy(sizePolicy)
        self.listView.setSizeIncrement(QtCore.QSize(0, 0))
        self.listView.setStyleSheet("background-color: rgb(0, 25, 25);")
        self.listView.setObjectName("listView")
        self.verticalLayout.addWidget(self.listView)
        self.verticalLayout.setStretch(0, 10)
        self.verticalLayout.setStretch(1, 3)
        self.verticalLayout.setStretch(2, 6)
        self.verticalLayout.setStretch(3, 6)
        self.verticalLayout.setStretch(4, 4)
        self.verticalLayout.setStretch(5, 1)
        self.verticalLayout.setStretch(6, 2)
        self.verticalLayout.setStretch(7, 20)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.tableWidget = CategoryTableWidget(Category)
        self.tableWidget.setStyleSheet("background-color: rgb(0, 25, 25);")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.horizontalLayout.addWidget(self.tableWidget)
        self.horizontalLayout.setStretch(0, 5)
        self.horizontalLayout.setStretch(1, 13)

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


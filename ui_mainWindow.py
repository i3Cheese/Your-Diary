# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_mainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

from DiaryListWidget import DiaryListWidget  # Заменяем QListWidget на свой


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(598, 456)
        MainWindow.setStyleSheet("background-color: rgb(0, 44, 44);\n"
                                 "selection-background-color: rgb(7, 52, 80);\n"
                                 "alternate-background-color: rgb(0, 85, 0);\n"
                                 "\n"
                                 "color: rgb(217, 212, 199);\n"
                                 "\n"
                                 "font: 11.5pt \"MS Shell Dlg 2\";")
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.lwCategories = DiaryListWidget(self.centralwidget)
        self.lwCategories.setStyleSheet("background-color: rgb(0, 25, 25);")
        self.lwCategories.setObjectName("lwCategories")
        self.gridLayout.addWidget(self.lwCategories, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 598, 24))
        self.menubar.setStyleSheet("background-color: rgb(0, 44, 44);\n"
                                   "")
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setStyleSheet("border-color: rgb(0, 0, 0);")
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.acCreate = QtWidgets.QAction(MainWindow)
        self.acCreate.setObjectName("acCreate")
        self.menu.addAction(self.acCreate)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Твой Дневник"))
        self.menu.setTitle(_translate("MainWindow", "Меню"))
        self.acCreate.setText(_translate("MainWindow", "Создать категорию"))
        self.acCreate.setShortcut(_translate("MainWindow", "Ctrl+N"))

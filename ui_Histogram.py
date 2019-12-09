# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/ui_histogram.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Histogram(object):
    def setupUi(self, Histogram):
        Histogram.setObjectName("Histogram")
        Histogram.resize(723, 474)
        Histogram.setStyleSheet("background-color: rgb(0, 44, 44);\n"
"selection-background-color: rgb(7, 52, 80);\n"
"alternate-background-color: rgb(0, 85, 0);\n"
"\n"
"color: rgb(217, 212, 199);\n"
"\n"
"font: 11.5pt \"MS Shell Dlg 2\";")
        self.gridLayout = QtWidgets.QGridLayout(Histogram)
        self.gridLayout.setObjectName("gridLayout")
        self.deStart = QtWidgets.QDateEdit(Histogram)
        self.deStart.setObjectName("deStart")
        self.gridLayout.addWidget(self.deStart, 0, 1, 1, 1)
        self.lblFrom = QtWidgets.QLabel(Histogram)
        self.lblFrom.setObjectName("lblFrom")
        self.gridLayout.addWidget(self.lblFrom, 0, 0, 1, 1)
        self.deEnd = QtWidgets.QDateEdit(Histogram)
        self.deEnd.setObjectName("deEnd")
        self.gridLayout.addWidget(self.deEnd, 0, 3, 1, 1)
        self.lbllTo = QtWidgets.QLabel(Histogram)
        self.lbllTo.setObjectName("lbllTo")
        self.gridLayout.addWidget(self.lbllTo, 0, 2, 1, 1)
        self.pbCreate = QtWidgets.QPushButton(Histogram)
        self.pbCreate.setObjectName("pbCreate")
        self.gridLayout.addWidget(self.pbCreate, 0, 4, 1, 1)
        self.graphicsView = PlotWidget(Histogram)
        self.graphicsView.setObjectName("graphicsView")
        self.gridLayout.addWidget(self.graphicsView, 1, 0, 1, 5)

        self.retranslateUi(Histogram)
        QtCore.QMetaObject.connectSlotsByName(Histogram)

    def retranslateUi(self, Histogram):
        _translate = QtCore.QCoreApplication.translate
        Histogram.setWindowTitle(_translate("Histogram", "Гистограмма"))
        self.lblFrom.setText(_translate("Histogram", "C"))
        self.lbllTo.setText(_translate("Histogram", "По"))
        self.pbCreate.setText(_translate("Histogram", "Сформировать"))
from pyqtgraph import PlotWidget

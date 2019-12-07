# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/ui_diagram.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from flags import FlagListWidget

class Ui_Diagramm(object):
    def setupUi(self, Diagramm):
        Diagramm.setObjectName("Diagramm")
        Diagramm.resize(723, 474)
        Diagramm.setStyleSheet("background-color: rgb(0, 44, 44);\n"
"selection-background-color: rgb(7, 52, 80);\n"
"alternate-background-color: rgb(0, 85, 0);\n"
"\n"
"color: rgb(217, 212, 199);\n"
"\n"
"font: 11.5pt \"MS Shell Dlg 2\";")
        self.gridLayout = QtWidgets.QGridLayout(Diagramm)
        self.gridLayout.setObjectName("gridLayout")
        self.listWidget = FlagListWidget(Diagramm)
        self.listWidget.setStyleSheet("background-color: rgb(0, 25, 25);")
        self.listWidget.setObjectName("listWidget")
        self.gridLayout.addWidget(self.listWidget, 1, 5, 1, 1)
        self.dteStart = QtWidgets.QDateTimeEdit(Diagramm)
        self.dteStart.setObjectName("dteStart")
        self.gridLayout.addWidget(self.dteStart, 0, 1, 1, 1)
        self.dteEnd = QtWidgets.QDateTimeEdit(Diagramm)
        self.dteEnd.setObjectName("dteEnd")
        self.gridLayout.addWidget(self.dteEnd, 0, 3, 1, 1)
        self.lbllTo = QtWidgets.QLabel(Diagramm)
        self.lbllTo.setObjectName("lbllTo")
        self.gridLayout.addWidget(self.lbllTo, 0, 2, 1, 1)
        self.label = QtWidgets.QLabel(Diagramm)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 5, 1, 1)
        self.lblFrom = QtWidgets.QLabel(Diagramm)
        self.lblFrom.setObjectName("lblFrom")
        self.gridLayout.addWidget(self.lblFrom, 0, 0, 1, 1)
        self.frame = QtWidgets.QWidget(Diagramm)
        self.frame.setObjectName("frame")
        self.gridLayout.addWidget(self.frame, 1, 0, 1, 5)

        self.retranslateUi(Diagramm)
        QtCore.QMetaObject.connectSlotsByName(Diagramm)

    def retranslateUi(self, Diagramm):
        _translate = QtCore.QCoreApplication.translate
        Diagramm.setWindowTitle(_translate("Diagramm", "Диаграмма"))
        self.lbllTo.setText(_translate("Diagramm", "По"))
        self.label.setText(_translate("Diagramm", "Флаги"))
        self.lblFrom.setText(_translate("Diagramm", "C"))

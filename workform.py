# -*- coding: utf-8 -*-
import sys
from PyQt4 import QtGui,QtCore
from form import Ui_Form
from calculate import Engine

class WorkForm():

    def __init__(self):
        self.engine=Engine()
        self.ui=Ui_Form()
        self.MainWindow = QtGui.QMainWindow()

        self.ui.setupUi(self.MainWindow)
        self.ui.stackedWidget.setCurrentIndex(3)
        self.setSignals()
        pass

    def chooseWay(self):

        wayIndex=self.ui.comboBox.currentIndex()
        self.ui.stackedWidget.setCurrentIndex(wayIndex)
        pass

    def calculate1(self):
        square=self.ui.spinBox_2.value()
        sizeOne=self.ui.spinBox_3.value()
        print self.engine.bySquare(square,sizeOne)
        self.ui.stackedWidget.setCurrentIndex(2)
        self.ui.textBrowser.setText(u"Понадобится "+str(self.engine.number)+u" огнетушителей")
        pass

    def calculate2(self):
        square = self.ui.spinBox.value()
        category=self.ui.comboBox_2.currentIndex()
        print  self.engine.byDistance(category,square)
        self.ui.stackedWidget.setCurrentIndex(2)
        self.ui.textBrowser.setText(u"Понадобится " + str(self.engine.number) + u" огнетушителей")
        pass

    def setSignals(self):
        self.ui.spinBox.setMaximum(9999999999)
        self.ui.spinBox_2.setMaximum(9999999999)
        self.ui.spinBox_3.setMaximum(9999999999)
        self.ui.pushButton.clicked.connect(self.chooseWay)
        self.ui.pushButton_2.clicked.connect(self.calculate2)
        self.ui.pushButton_3.clicked.connect(self.calculate1)
        pass



    pass


WorkForm
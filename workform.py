# -*- coding: utf-8 -*-
import sys
from PyQt4 import QtGui,QtCore

from PyQt4.QtGui import QPalette, QPixmap,QBrush

from form import Ui_Form
from calculate import Engine

class WorkForm():

    def __init__(self):
        self.engine=Engine()
        self.ui=Ui_Form()
        self.MainWindow = QtGui.QMainWindow()

        self.ui.setupUi(self.MainWindow)
        self.ui.stackedWidget.setCurrentIndex(4)
        self.setSignals()

        palette = QPalette()
        palette.setBrush(QPalette.Background, QBrush (QPixmap("background.jpg")))

        #self.MainWindow.setPalette(palette)
        #self.ui.page_2.setStyleSheet("background-image: url("+"background.jpg"+"); background-repeat: no-repeat; background-position: center;")

        pass

    def chooseWay(self):

        wayIndex=self.ui.comboBox.currentIndex()
        if(wayIndex==2): wayIndex=3
        elif(wayIndex==3): wayIndex=6


        self.ui.stackedWidget.setCurrentIndex(wayIndex)
        pass

    def calculate1(self):
        square=self.ui.spinBox_2.value()
        sizeOne=self.ui.spinBox_3.value()
        print self.engine.bySquare(square,sizeOne)
        self.ui.stackedWidget.setCurrentIndex(2)
        self.ui.textBrowser.setText(u"Понадобится "+str(self.engine.bySquare(square,sizeOne))+u" огнетушителей")
        pass

    def calculate2(self):
        square = self.ui.spinBox.value()
        category=self.ui.comboBox_2.currentIndex()
        min=self.engine.byDistance(category,square).x
        max=self.engine.byDistance(category,square).y
        self.ui.stackedWidget.setCurrentIndex(2)
        self.ui.textBrowser.setText(u"Понадобится " + str(min)+ u" огнетушителей")
        pass

    def escape(self):
        outputs=self.ui.spinBox_7.value()
        people=self.ui.spinBox_6.value()
        for_one_output=55 # 55 mans per minute
        needs_min=people/(outputs*for_one_output)
        if(needs_min<0.5):
            needs_min=1
        self.ui.textBrowser_4.setText(u"Эвакуация будет длиться около "+ str(needs_min)+u" минут")

        pass

    def gidranty(self):
         low=(30,51,101,301,1001,1501)
         up=(50,100,300,1000,1500,2000)
         litres=(15,20,25,40,60,80,100)

         grounds=self.ui.spinBox_4.value()
         one_gidrant=self.ui.spinBox_5.value()

         need_speed=0
         for i in range(len(low)):
             if (grounds>=low[i] and grounds<=up[i]): need_speed=litres[i]

         need_gidrants=need_speed/one_gidrant
         if need_gidrants<0.5 :need_gidrants=1

         self.ui.textBrowser_5.setText(u"Понадобится "+str(need_gidrants)+u" гидрантов")

         pass

    def go_to_info(self):
        self.ui.stackedWidget.setCurrentIndex(5)
        pass

    def go_to_main(self):
        self.ui.stackedWidget.setCurrentIndex(4)
        pass

    def setSignals(self):
        self.ui.spinBox.setMaximum(99999999)
        self.ui.spinBox_2.setMaximum(99999999)
        self.ui.spinBox_3.setMaximum(99999999)
        self.ui.pushButton.clicked.connect(self.chooseWay)
        self.ui.pushButton_2.clicked.connect(self.calculate2)
        self.ui.pushButton_3.clicked.connect(self.calculate1)
        self.ui.pushButton_4.clicked.connect(self.go_to_info)
        self.ui.pushButton_5.clicked.connect(self.go_to_main)
        self.ui.pushButton_6.clicked.connect(self.go_to_main)
        self.ui.pushButton_7.clicked.connect(self.go_to_main)
        self.ui.pushButton_8.clicked.connect(self.go_to_main)
        self.ui.pushButton_9.clicked.connect(self.gidranty)
        self.ui.pushButton_10.clicked.connect(self.escape)
        pass



    pass


WorkForm
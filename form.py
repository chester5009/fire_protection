# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(599, 652)
        self.stackedWidget = QtGui.QStackedWidget(Form)
        self.stackedWidget.setGeometry(QtCore.QRect(10, 10, 571, 621))
        self.stackedWidget.setObjectName(_fromUtf8("stackedWidget"))
        self.page = QtGui.QWidget()
        self.page.setObjectName(_fromUtf8("page"))
        self.label_2 = QtGui.QLabel(self.page)
        self.label_2.setGeometry(QtCore.QRect(10, 40, 561, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setTextFormat(QtCore.Qt.AutoText)
        self.label_2.setScaledContents(False)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self.page)
        self.label_3.setGeometry(QtCore.QRect(200, 190, 171, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.comboBox_2 = QtGui.QComboBox(self.page)
        self.comboBox_2.setGeometry(QtCore.QRect(180, 240, 201, 27))
        self.comboBox_2.setObjectName(_fromUtf8("comboBox_2"))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.label_4 = QtGui.QLabel(self.page)
        self.label_4.setGeometry(QtCore.QRect(180, 310, 211, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.spinBox = QtGui.QSpinBox(self.page)
        self.spinBox.setGeometry(QtCore.QRect(180, 340, 191, 27))
        self.spinBox.setObjectName(_fromUtf8("spinBox"))
        self.pushButton_2 = QtGui.QPushButton(self.page)
        self.pushButton_2.setGeometry(QtCore.QRect(230, 510, 99, 27))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.stackedWidget.addWidget(self.page)
        self.page_3 = QtGui.QWidget()
        self.page_3.setObjectName(_fromUtf8("page_3"))
        self.label_6 = QtGui.QLabel(self.page_3)
        self.label_6.setGeometry(QtCore.QRect(10, 60, 561, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setTextFormat(QtCore.Qt.AutoText)
        self.label_6.setScaledContents(False)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setWordWrap(True)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.pushButton_3 = QtGui.QPushButton(self.page_3)
        self.pushButton_3.setGeometry(QtCore.QRect(250, 480, 99, 27))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.spinBox_2 = QtGui.QSpinBox(self.page_3)
        self.spinBox_2.setGeometry(QtCore.QRect(210, 220, 161, 27))
        self.spinBox_2.setObjectName(_fromUtf8("spinBox_2"))
        self.label_7 = QtGui.QLabel(self.page_3)
        self.label_7.setGeometry(QtCore.QRect(190, 190, 211, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.label_8 = QtGui.QLabel(self.page_3)
        self.label_8.setGeometry(QtCore.QRect(160, 290, 301, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.spinBox_3 = QtGui.QSpinBox(self.page_3)
        self.spinBox_3.setGeometry(QtCore.QRect(210, 320, 161, 27))
        self.spinBox_3.setObjectName(_fromUtf8("spinBox_3"))
        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QtGui.QWidget()
        self.page_4.setObjectName(_fromUtf8("page_4"))
        self.label_5 = QtGui.QLabel(self.page_4)
        self.label_5.setGeometry(QtCore.QRect(200, 100, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.textBrowser = QtGui.QTextBrowser(self.page_4)
        self.textBrowser.setGeometry(QtCore.QRect(120, 210, 311, 221))
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        self.pushButton_4 = QtGui.QPushButton(self.page_4)
        self.pushButton_4.setGeometry(QtCore.QRect(330, 460, 99, 27))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.pushButton_6 = QtGui.QPushButton(self.page_4)
        self.pushButton_6.setGeometry(QtCore.QRect(210, 530, 99, 27))
        self.pushButton_6.setObjectName(_fromUtf8("pushButton_6"))
        self.stackedWidget.addWidget(self.page_4)
        self.page_6 = QtGui.QWidget()
        self.page_6.setObjectName(_fromUtf8("page_6"))
        self.pushButton_5 = QtGui.QPushButton(self.page_6)
        self.pushButton_5.setGeometry(QtCore.QRect(420, 40, 99, 27))
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.pushButton_10 = QtGui.QPushButton(self.page_6)
        self.pushButton_10.setGeometry(QtCore.QRect(220, 290, 99, 27))
        self.pushButton_10.setObjectName(_fromUtf8("pushButton_10"))
        self.spinBox_6 = QtGui.QSpinBox(self.page_6)
        self.spinBox_6.setGeometry(QtCore.QRect(70, 190, 101, 27))
        self.spinBox_6.setMaximum(100000)
        self.spinBox_6.setObjectName(_fromUtf8("spinBox_6"))
        self.label_13 = QtGui.QLabel(self.page_6)
        self.label_13.setGeometry(QtCore.QRect(200, 130, 161, 17))
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.textBrowser_4 = QtGui.QTextBrowser(self.page_6)
        self.textBrowser_4.setGeometry(QtCore.QRect(80, 430, 381, 151))
        self.textBrowser_4.setObjectName(_fromUtf8("textBrowser_4"))
        self.spinBox_7 = QtGui.QSpinBox(self.page_6)
        self.spinBox_7.setGeometry(QtCore.QRect(110, 130, 61, 27))
        self.spinBox_7.setMaximum(1000)
        self.spinBox_7.setObjectName(_fromUtf8("spinBox_7"))
        self.label_14 = QtGui.QLabel(self.page_6)
        self.label_14.setGeometry(QtCore.QRect(200, 190, 161, 17))
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.label_15 = QtGui.QLabel(self.page_6)
        self.label_15.setGeometry(QtCore.QRect(200, 60, 131, 17))
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.stackedWidget.addWidget(self.page_6)
        self.page_2 = QtGui.QWidget()
        self.page_2.setStyleSheet(_fromUtf8("background-image: url(\"background.jpg\")"))
        self.page_2.setObjectName(_fromUtf8("page_2"))
        self.label = QtGui.QLabel(self.page_2)
        self.label.setGeometry(QtCore.QRect(50, 60, 471, 91))
        font = QtGui.QFont()
        font.setPointSize(26)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet(_fromUtf8("background-color:rgb(85, 170, 0)"))
        self.label.setObjectName(_fromUtf8("label"))
        self.comboBox = QtGui.QComboBox(self.page_2)
        self.comboBox.setGeometry(QtCore.QRect(50, 200, 461, 27))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 255, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 255, 63))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(42, 127, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(56, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 255, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 255, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 255, 63))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(42, 127, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(56, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 255, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(42, 127, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 255, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 255, 63))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(42, 127, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(56, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(42, 127, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(42, 127, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        self.comboBox.setPalette(palette)
        self.comboBox.setStyleSheet(_fromUtf8("background-color:rgb(170, 255, 0)"))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.pushButton = QtGui.QPushButton(self.page_2)
        self.pushButton.setGeometry(QtCore.QRect(230, 400, 99, 27))
        self.pushButton.setStyleSheet(_fromUtf8("background-color:rgb(0, 85, 255);\n"
"color:rgb(156, 255, 241)\n"
""))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.stackedWidget.addWidget(self.page_2)
        self.page_5 = QtGui.QWidget()
        self.page_5.setObjectName(_fromUtf8("page_5"))
        self.label_10 = QtGui.QLabel(self.page_5)
        self.label_10.setGeometry(QtCore.QRect(210, 50, 191, 17))
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.pushButton_7 = QtGui.QPushButton(self.page_5)
        self.pushButton_7.setGeometry(QtCore.QRect(440, 30, 99, 27))
        self.pushButton_7.setObjectName(_fromUtf8("pushButton_7"))
        self.textBrowser_3 = QtGui.QTextBrowser(self.page_5)
        self.textBrowser_3.setGeometry(QtCore.QRect(100, 100, 381, 501))
        self.textBrowser_3.setObjectName(_fromUtf8("textBrowser_3"))
        self.stackedWidget.addWidget(self.page_5)
        self.page_7 = QtGui.QWidget()
        self.page_7.setObjectName(_fromUtf8("page_7"))
        self.label_9 = QtGui.QLabel(self.page_7)
        self.label_9.setGeometry(QtCore.QRect(170, 80, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.pushButton_8 = QtGui.QPushButton(self.page_7)
        self.pushButton_8.setGeometry(QtCore.QRect(440, 30, 99, 27))
        self.pushButton_8.setObjectName(_fromUtf8("pushButton_8"))
        self.spinBox_4 = QtGui.QSpinBox(self.page_7)
        self.spinBox_4.setGeometry(QtCore.QRect(130, 210, 131, 27))
        self.spinBox_4.setMaximum(900000)
        self.spinBox_4.setObjectName(_fromUtf8("spinBox_4"))
        self.label_11 = QtGui.QLabel(self.page_7)
        self.label_11.setGeometry(QtCore.QRect(300, 210, 231, 17))
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.spinBox_5 = QtGui.QSpinBox(self.page_7)
        self.spinBox_5.setGeometry(QtCore.QRect(130, 280, 131, 27))
        self.spinBox_5.setObjectName(_fromUtf8("spinBox_5"))
        self.label_12 = QtGui.QLabel(self.page_7)
        self.label_12.setGeometry(QtCore.QRect(300, 280, 251, 17))
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.pushButton_9 = QtGui.QPushButton(self.page_7)
        self.pushButton_9.setGeometry(QtCore.QRect(230, 360, 99, 27))
        self.pushButton_9.setObjectName(_fromUtf8("pushButton_9"))
        self.textBrowser_5 = QtGui.QTextBrowser(self.page_7)
        self.textBrowser_5.setGeometry(QtCore.QRect(100, 420, 381, 151))
        self.textBrowser_5.setObjectName(_fromUtf8("textBrowser_5"))
        self.stackedWidget.addWidget(self.page_7)

        self.retranslateUi(Form)
        self.stackedWidget.setCurrentIndex(4)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Противопожарная защита", None))
        self.label_2.setText(_translate("Form", "Расстояние от возможного очага возгорания до огнетушителя", None))
        self.label_3.setText(_translate("Form", "Выбрать категорию", None))
        self.comboBox_2.setItemText(0, _translate("Form", "Общественные здания", None))
        self.comboBox_2.setItemText(1, _translate("Form", "Категории А, Б, В", None))
        self.comboBox_2.setItemText(2, _translate("Form", "Категория Г", None))
        self.comboBox_2.setItemText(3, _translate("Form", "Категория Д", None))
        self.label_4.setText(_translate("Form", "Введите площать в м кв", None))
        self.pushButton_2.setText(_translate("Form", "Рассчитать", None))
        self.label_6.setText(_translate("Form", "Количество огнетушащего состава на площадь помещения", None))
        self.pushButton_3.setText(_translate("Form", "Рассчитать", None))
        self.label_7.setText(_translate("Form", "Введите площать в м кв", None))
        self.label_8.setText(_translate("Form", "Введите объем огнетушителей (кг)", None))
        self.label_5.setText(_translate("Form", "Результат", None))
        self.pushButton_4.setText(_translate("Form", "Справка", None))
        self.pushButton_6.setText(_translate("Form", "На главную", None))
        self.pushButton_5.setText(_translate("Form", "На главную", None))
        self.pushButton_10.setText(_translate("Form", " Расчет", None))
        self.label_13.setText(_translate("Form", "Количество выходов", None))
        self.textBrowser_4.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:24px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><br /></p></body></html>", None))
        self.label_14.setText(_translate("Form", "Количество человек", None))
        self.label_15.setText(_translate("Form", "Время эвакуации", None))
        self.label.setWhatsThis(_translate("Form", "<html><head/><body><p><span style=\" color:#ffff00;\">hththth</span></p></body></html>", None))
        self.label.setText(_translate("Form", "<html><head/><body><p><span style=\" color:#ffff00;\">Выберите способ расчёта</span></p></body></html>", None))
        self.comboBox.setItemText(0, _translate("Form", "Расстояние от возможного очага возгорания до огнетушителя", None))
        self.comboBox.setItemText(1, _translate("Form", "Количество огнетушащего состава на площадь помещения", None))
        self.comboBox.setItemText(2, _translate("Form", "Время эвакуации", None))
        self.comboBox.setItemText(3, _translate("Form", "Количество гидрантов", None))
        self.pushButton.setText(_translate("Form", "далее", None))
        self.label_10.setText(_translate("Form", "Информация при пожаре", None))
        self.pushButton_7.setText(_translate("Form", "На главную", None))
        self.textBrowser_3.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" background-color:#ffffff;\">Пропускная способность выходов. Под удельной пропускной способностью выходов подразумевают количество людей, проходящих через выход шириной в 1 м за 1 мин.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" background-color:#ffffff;\">Наименьшее значение удельной пропускной способности, полученное опытным путем, при данной плотности именуется расчетной удельной пропускной способностью. Удельная пропускная способность выходов зависит от ширины выходов, плотностей людских потоков и отношения ширины людских потоков к ширине выхода.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" background-color:#ffffff;\">Нормами установлена пропускная способность дверей шириной до 1,5 м, равная 50 чел./м-мин, а шириной более 1,5 м 60 чел./м-мин (для предельных плотностей).</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" background-color:#ffffff;\">Размеры эвакуационных выходов. Кроме размеров эвакуационных путей и выходов, нормы регламентируют их конструктивно-планировочные решения, обеспечивающие организованное и безопасное движение людей.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" background-color:#ffffff;\">Пожарная опасность производственных процессов в промышленных зданиях характеризуется физико-химическими свойствами веществ, образующихся в производстве. Производства категорий А и Б, в которых обращаются жидкости и газы, представляют особую опасность при пожарах в силу возможности быстрого распространения горения и задымления зданий, поэтому протяженность путей для них является наименьшей. В производствах категории В, где обращаются твердые горючие вещества, скорость распространения горения меньше, срок эвакуации может быть несколько увеличен, а следовательно, и протяженность путей эвакуации будет больше, чем для производства категорий А и В. В производствах категорий Г и Д, размещаемых в зданиях I и II степеней огнестойкости, протяженность путей эвакуации не ограничивается (для определения категории здания см. приложение А).</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" background-color:#ffffff;\">Продолжение по ссылке  http://www.bestreferat.ru/referat-284124.html</span></p></body></html>", None))
        self.label_9.setText(_translate("Form", "Количество гидрантов", None))
        self.pushButton_8.setText(_translate("Form", "На главную", None))
        self.label_11.setText(_translate("Form", "Количество площадок с грузом", None))
        self.label_12.setText(_translate("Form", "Литров в секунду одного гидранта", None))
        self.pushButton_9.setText(_translate("Form", "Расчёт", None))
        self.textBrowser_5.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:24px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><br /></p></body></html>", None))


# -*- coding: utf-8 -*-

# Pysal implementation generated from reading ui file 'Ui_Pysal.ui'
#
# Created: Sat Nov 17 17:14:37 2012
#      by: PyQt4 UI code generator 4.9.5
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Pysal(object):
    def setupUi(self, Pysal):
        Pysal.setObjectName(_fromUtf8("Pysal"))
        Pysal.resize(748, 598)
        self.radioButton = QtGui.QRadioButton(Pysal)
        self.radioButton.setGeometry(QtCore.QRect(190, 190, 111, 21))
        self.radioButton.setObjectName(_fromUtf8("radioButton"))
        self.pushButton = QtGui.QPushButton(Pysal)
        self.pushButton.setGeometry(QtCore.QRect(560, 390, 75, 23))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.radioButton_2 = QtGui.QRadioButton(Pysal)
        self.radioButton_2.setGeometry(QtCore.QRect(190, 220, 151, 16))
        self.radioButton_2.setObjectName(_fromUtf8("radioButton_2"))
        self.radioButton_3 = QtGui.QRadioButton(Pysal)
        self.radioButton_3.setGeometry(QtCore.QRect(190, 250, 141, 16))
        self.radioButton_3.setObjectName(_fromUtf8("radioButton_3"))
        self.radioButton_4 = QtGui.QRadioButton(Pysal)
        self.radioButton_4.setGeometry(QtCore.QRect(190, 280, 111, 16))
        self.radioButton_4.setObjectName(_fromUtf8("radioButton_4"))
        self.lineEdit = QtGui.QLineEdit(Pysal)
        self.lineEdit.setGeometry(QtCore.QRect(360, 190, 113, 20))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.textEdit = QtGui.QTextEdit(Pysal)
        self.textEdit.setGeometry(QtCore.QRect(10, 430, 641, 141))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.lineEdit_2 = QtGui.QLineEdit(Pysal)
        self.lineEdit_2.setGeometry(QtCore.QRect(360, 220, 113, 20))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.lineEdit_3 = QtGui.QLineEdit(Pysal)
        self.lineEdit_3.setGeometry(QtCore.QRect(360, 250, 113, 20))
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.lineEdit_4 = QtGui.QLineEdit(Pysal)
        self.lineEdit_4.setGeometry(QtCore.QRect(360, 280, 113, 20))
        self.lineEdit_4.setObjectName(_fromUtf8("lineEdit_4"))
        self.label = QtGui.QLabel(Pysal)
        self.label.setGeometry(QtCore.QRect(20, 350, 131, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.checkBox = QtGui.QCheckBox(Pysal)
        self.checkBox.setGeometry(QtCore.QRect(190, 350, 70, 17))
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.checkBox_2 = QtGui.QCheckBox(Pysal)
        self.checkBox_2.setGeometry(QtCore.QRect(290, 350, 70, 17))
        self.checkBox_2.setObjectName(_fromUtf8("checkBox_2"))
        self.checkBox_3 = QtGui.QCheckBox(Pysal)
        self.checkBox_3.setGeometry(QtCore.QRect(380, 350, 70, 17))
        self.checkBox_3.setObjectName(_fromUtf8("checkBox_3"))
        self.checkBox_4 = QtGui.QCheckBox(Pysal)
        self.checkBox_4.setGeometry(QtCore.QRect(500, 350, 70, 17))
        self.checkBox_4.setObjectName(_fromUtf8("checkBox_4"))
        self.label_2 = QtGui.QLabel(Pysal)
        self.label_2.setGeometry(QtCore.QRect(30, 30, 121, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.radioButton_5 = QtGui.QRadioButton(Pysal)
        self.radioButton_5.setGeometry(QtCore.QRect(190, 30, 251, 16))
        self.radioButton_5.setObjectName(_fromUtf8("radioButton_5"))
        self.radioButton_6 = QtGui.QRadioButton(Pysal)
        self.radioButton_6.setGeometry(QtCore.QRect(190, 60, 141, 16))
        self.radioButton_6.setObjectName(_fromUtf8("radioButton_6"))
        self.lineEdit_5 = QtGui.QLineEdit(Pysal)
        self.lineEdit_5.setGeometry(QtCore.QRect(430, 60, 191, 21))
        self.lineEdit_5.setObjectName(_fromUtf8("lineEdit_5"))
        self.label_3 = QtGui.QLabel(Pysal)
        self.label_3.setGeometry(QtCore.QRect(30, 190, 121, 16))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(Pysal)
        self.label_4.setGeometry(QtCore.QRect(520, 190, 131, 16))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(Pysal)
        self.label_5.setGeometry(QtCore.QRect(520, 220, 131, 16))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_6 = QtGui.QLabel(Pysal)
        self.label_6.setGeometry(QtCore.QRect(520, 250, 131, 16))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.label_7 = QtGui.QLabel(Pysal)
        self.label_7.setGeometry(QtCore.QRect(520, 280, 131, 16))
        self.label_7.setObjectName(_fromUtf8("label_7"))

        self.retranslateUi(Pysal)
        QtCore.QMetaObject.connectSlotsByName(Pysal)

    def retranslateUi(self, Pysal):
        Pysal.setWindowTitle(QtGui.QApplication.translate("Pysal", "Pysal", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButton.setText(QtGui.QApplication.translate("Pysal", "Nearest Neighbors", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setToolTip(QtGui.QApplication.translate("Pysal", "<html><head/><body><p>Run</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("Pysal", "OK", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButton_2.setText(QtGui.QApplication.translate("Pysal", "Adjacent Polygons(Queen)", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButton_3.setText(QtGui.QApplication.translate("Pysal", "Shared Boundaries(Rook)", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButton_4.setText(QtGui.QApplication.translate("Pysal", "Threshold Distance", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit.setToolTip(QtGui.QApplication.translate("Pysal", "<html><head/><body><p>Enter Number of Neighbors</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit_2.setToolTip(QtGui.QApplication.translate("Pysal", "<html><head/><body><p>Enter Order</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit_3.setToolTip(QtGui.QApplication.translate("Pysal", "<html><head/><body><p>Enter Order</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit_4.setToolTip(QtGui.QApplication.translate("Pysal", "<html><head/><body><p>Enter Distance</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Pysal", "Choose Significance Level", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox.setText(QtGui.QApplication.translate("Pysal", "0.01", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_2.setText(QtGui.QApplication.translate("Pysal", "0.05", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_3.setText(QtGui.QApplication.translate("Pysal", "Other1", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_4.setText(QtGui.QApplication.translate("Pysal", "Other2", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Pysal", "Choose Shape file", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButton_5.setText(QtGui.QApplication.translate("Pysal", "Use shapefile that is currently open", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButton_6.setText(QtGui.QApplication.translate("Pysal", "Choose a new shapefile", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Pysal", "Choose Weights Matrix", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("Pysal", "Enter Number of Neighbors", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("Pysal", "Enter Order", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("Pysal", "Enter Order", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("Pysal", "Enter Distance", None, QtGui.QApplication.UnicodeUTF8))


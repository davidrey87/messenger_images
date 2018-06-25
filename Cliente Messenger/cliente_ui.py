# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cliente.ui'
#
# Created by: PyQt4 UI code generator 4.12.1
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(480, 640)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.pantalla = QtGui.QGraphicsView(self.centralwidget)
        self.pantalla.setGeometry(QtCore.QRect(10, 300, 461, 281))
        self.pantalla.setObjectName(_fromUtf8("pantalla"))
        self.chat = QtGui.QPlainTextEdit(self.centralwidget)
        self.chat.setGeometry(QtCore.QRect(10, 60, 381, 231))
        self.chat.setObjectName(_fromUtf8("chat"))
        self.mensaje = QtGui.QTextEdit(self.centralwidget)
        self.mensaje.setGeometry(QtCore.QRect(10, 10, 381, 31))
        self.mensaje.setObjectName(_fromUtf8("mensaje"))
        self.enviar = QtGui.QPushButton(self.centralwidget)
        self.enviar.setGeometry(QtCore.QRect(400, 10, 71, 31))
        self.enviar.setObjectName(_fromUtf8("enviar"))
        self.transmitir = QtGui.QPushButton(self.centralwidget)
        self.transmitir.setGeometry(QtCore.QRect(400, 60, 71, 31))
        self.transmitir.setObjectName(_fromUtf8("transmitir"))
        self.detener = QtGui.QPushButton(self.centralwidget)
        self.detener.setGeometry(QtCore.QRect(400, 100, 71, 31))
        self.detener.setObjectName(_fromUtf8("detener"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 480, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.enviar.setText(_translate("MainWindow", "Enviar", None))
        self.transmitir.setText(_translate("MainWindow", "Transmitir", None))
        self.detener.setText(_translate("MainWindow", "Detener", None))


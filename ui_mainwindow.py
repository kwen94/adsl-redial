# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(509, 305)
        self.tabWidget = QtWidgets.QTabWidget(Dialog)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 491, 291))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.label_4 = QtWidgets.QLabel(self.tab)
        self.label_4.setGeometry(QtCore.QRect(200, 60, 31, 20))
        self.label_4.setObjectName("label_4")
        self.label_7 = QtWidgets.QLabel(self.tab)
        self.label_7.setGeometry(QtCore.QRect(40, 190, 71, 20))
        self.label_7.setObjectName("label_7")
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setGeometry(QtCore.QRect(120, 150, 211, 20))
        self.label_3.setObjectName("label_3")
        self.label_5 = QtWidgets.QLabel(self.tab)
        self.label_5.setGeometry(QtCore.QRect(290, 60, 61, 20))
        self.label_5.setObjectName("label_5")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.tab)
        self.plainTextEdit.setGeometry(QtCore.QRect(120, 10, 61, 121))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.pushButton = QtWidgets.QPushButton(self.tab)
        self.pushButton.setGeometry(QtCore.QRect(200, 220, 111, 31))
        self.pushButton.setObjectName("pushButton")
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(40, 60, 71, 20))
        self.label_2.setObjectName("label_2")
        self.label_6 = QtWidgets.QLabel(self.tab)
        self.label_6.setGeometry(QtCore.QRect(120, 190, 171, 20))
        self.label_6.setObjectName("label_6")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(40, 150, 61, 20))
        self.label.setObjectName("label")
        self.spinBox = QtWidgets.QSpinBox(self.tab)
        self.spinBox.setGeometry(QtCore.QRect(240, 60, 42, 22))
        self.spinBox.setMinimum(3)
        self.spinBox.setMaximum(20)
        self.spinBox.setObjectName("spinBox")
        self.tabWidget.addTab(self.tab, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.lineEdit = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit.setGeometry(QtCore.QRect(90, 40, 113, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_2.setGeometry(QtCore.QRect(90, 90, 113, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_3.setGeometry(QtCore.QRect(90, 140, 113, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_8 = QtWidgets.QLabel(self.tab_3)
        self.label_8.setGeometry(QtCore.QRect(30, 40, 41, 16))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.tab_3)
        self.label_9.setGeometry(QtCore.QRect(30, 90, 41, 16))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.tab_3)
        self.label_10.setGeometry(QtCore.QRect(30, 140, 41, 16))
        self.label_10.setObjectName("label_10")
        self.tabWidget.addTab(self.tab_3, "")

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "ADSL重拨助手"))
        self.label_4.setText(_translate("Dialog", "提前"))
        self.label_7.setText(_translate("Dialog", "上次换IP时间"))
        self.label_3.setText(_translate("Dialog", "0.0.0.0"))
        self.label_5.setText(_translate("Dialog", "分钟切换IP"))
        self.plainTextEdit.setPlainText(_translate("Dialog", "11:00\n"
"11:30\n"
"13:00\n"
"13:30\n"
"14:00\n"
"14:30\n"
"15:00"))
        self.pushButton.setText(_translate("Dialog", "开始运行"))
        self.label_2.setText(_translate("Dialog", "时间点"))
        self.label_6.setText(_translate("Dialog", "1970-01-01 00:00:00"))
        self.label.setText(_translate("Dialog", "本机外网IP"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Dialog", "模式1"))
        self.label_8.setText(_translate("Dialog", "连接名"))
        self.label_9.setText(_translate("Dialog", "用户名"))
        self.label_10.setText(_translate("Dialog", "密码"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Dialog", "Settings"))


# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GuiDialogBoxError.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 192)
        Dialog.setStyleSheet("background-color: rgb(95, 92, 90);")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(0, 30, 141, 141))
        self.label.setStyleSheet("image: url(:/cct/error-png-8.png);\n"
"background-image: url(:/cct/transparente.png);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.lblText = QtWidgets.QLabel(Dialog)
        self.lblText.setGeometry(QtCore.QRect(150, 60, 251, 51))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(11)
        font.setItalic(True)
        self.lblText.setFont(font)
        self.lblText.setStyleSheet("color: rgb(255, 255, 255);")
        self.lblText.setObjectName("lblText")
        self.btnConfirm = QtWidgets.QPushButton(Dialog)
        self.btnConfirm.setGeometry(QtCore.QRect(260, 140, 101, 23))
        self.btnConfirm.setStyleSheet("QPushButton{\n"
"    \n"
"    \n"
"    background-color: rgb(85, 255, 0);\n"
"    background-image: url(:/cct/transparente.png);\n"
"    border-radius:10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    \n"
"    background-color: rgb(0, 255, 255);\n"
"}\n"
"QPushButton:pressed{\n"
"    \n"
"    background-color: rgb(255, 0, 127);\n"
"}")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/cct/confirm.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnConfirm.setIcon(icon)
        self.btnConfirm.setIconSize(QtCore.QSize(30, 20))
        self.btnConfirm.setObjectName("btnConfirm")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Error"))
        self.lblText.setText(_translate("Dialog", "Error, no se pudo completar \n"
"la operación."))
        self.btnConfirm.setText(_translate("Dialog", "Confirmar"))
#import Resource_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

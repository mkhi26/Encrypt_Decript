# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GuiDialogBox.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(452, 191)
        Dialog.setStyleSheet("background-image: url(:/cct/mainWindow.jpg);")
        self.lblText = QtWidgets.QLabel(Dialog)
        self.lblText.setGeometry(QtCore.QRect(120, 40, 301, 31))
        font = QtGui.QFont()
        font.setFamily("Sarai")
        font.setPointSize(16)
        self.lblText.setFont(font)
        self.lblText.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-image: url(:/cct/transparente.png);")
        self.lblText.setObjectName("lblText")
        self.lblCuestion = QtWidgets.QLabel(Dialog)
        self.lblCuestion.setGeometry(QtCore.QRect(190, 100, 111, 16))
        font = QtGui.QFont()
        font.setFamily("Waree")
        font.setPointSize(11)
        font.setItalic(True)
        self.lblCuestion.setFont(font)
        self.lblCuestion.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-image: url(:/cct/transparente.png);")
        self.lblCuestion.setObjectName("lblCuestion")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(0, 80, 131, 111))
        self.label_3.setStyleSheet("image: url(:/cct/man.png);\n"
"background-image: url(:/cct/transparente.png);")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.btnReject = QtWidgets.QPushButton(Dialog)
        self.btnReject.setGeometry(QtCore.QRect(140, 140, 91, 23))
        self.btnReject.setStyleSheet("QPushButton{\n"
"    \n"
"    background-color: rgb(190, 0, 0);\n"
"    background-image: url(:/cct/transparente.png);\n"
"    border-radius:10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    \n"
"    background-color: rgb(0, 85, 255);\n"
"}\n"
"QPushButton:pressed{\n"
"    \n"
"    ;\n"
"    background-color: rgb(85, 255, 0);\n"
"}")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/cct/close.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnReject.setIcon(icon)
        self.btnReject.setObjectName("btnReject")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(0, 0, 451, 191))
        self.label.setStyleSheet("background-image: url(:/cct/lblBackground.png);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.btnConfirm = QtWidgets.QPushButton(Dialog)
        self.btnConfirm.setGeometry(QtCore.QRect(270, 140, 101, 23))
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
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/cct/confirm.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnConfirm.setIcon(icon1)
        self.btnConfirm.setIconSize(QtCore.QSize(30, 20))
        self.btnConfirm.setObjectName("btnConfirm")
        self.label.raise_()
        self.lblText.raise_()
        self.lblCuestion.raise_()
        self.label_3.raise_()
        self.btnReject.raise_()
        self.btnConfirm.raise_()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialogo de confirmación"))
        self.lblText.setText(_translate("Dialog", "Se encriptaran los archivos seleccionados."))
        self.lblCuestion.setText(_translate("Dialog", "¿Esta seguro?"))
        self.label_3.setWhatsThis(_translate("Dialog", "<html><head/><body><p><img src=\":/cct/man.png\"/></p></body></html>"))
        self.btnReject.setText(_translate("Dialog", "Cancelar"))
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

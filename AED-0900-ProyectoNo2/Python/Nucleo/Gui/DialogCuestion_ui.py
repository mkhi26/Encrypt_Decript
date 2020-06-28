# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GuiCuestion.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(367, 220)
        Dialog.setStyleSheet("background-color: rgb(75, 75, 75);")
        self.lblTitle = QtWidgets.QLabel(Dialog)
        self.lblTitle.setGeometry(QtCore.QRect(100, 20, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Pothana2000")
        font.setPointSize(14)
        self.lblTitle.setFont(font)
        self.lblTitle.setStyleSheet("background-image: url(:/cct/transparente.png);\n"
"color: rgb(255, 255, 255);")
        self.lblTitle.setObjectName("lblTitle")
        self.btnConfirm = QtWidgets.QPushButton(Dialog)
        self.btnConfirm.setGeometry(QtCore.QRect(260, 170, 80, 23))
        self.btnConfirm.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.btnConfirm.setObjectName("btnConfirm")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(40, 70, 41, 31))
        self.label_3.setStyleSheet("background-image: url(:/cct/transparente.png);\n"
"image: url(:/cct/carpeta.png);")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(40, 120, 41, 21))
        self.label_4.setStyleSheet("background-image: url(:/cct/transparente.png);\n"
"image: url(:/cct/files-and-folders.png);")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(90, 70, 161, 81))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.rbtnFile = QtWidgets.QRadioButton(self.widget)
        self.rbtnFile.setStyleSheet("color: rgb(255, 255, 255);")
        self.rbtnFile.setObjectName("rbtnFile")
        self.gridLayout.addWidget(self.rbtnFile, 1, 1, 1, 1)
        self.rbtnFolder = QtWidgets.QRadioButton(self.widget)
        self.rbtnFolder.setStyleSheet("color: rgb(255, 255, 255);")
        self.rbtnFolder.setObjectName("rbtnFolder")
        self.gridLayout.addWidget(self.rbtnFolder, 0, 1, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Examinar"))
        self.lblTitle.setText(_translate("Dialog", "Elija una opción"))
        self.btnConfirm.setText(_translate("Dialog", "Examinar"))
        self.rbtnFile.setText(_translate("Dialog", "Se&leccionar Archivos"))
        self.rbtnFolder.setText(_translate("Dialog", "Seleccionar Carpe&ta"))
#import Resource_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

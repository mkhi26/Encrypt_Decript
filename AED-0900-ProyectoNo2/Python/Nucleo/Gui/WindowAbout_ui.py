# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GuiAbout.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 500)
        MainWindow.setStyleSheet("background-image: url(:/cct/mainSkin1.png);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lblAED = QtWidgets.QLabel(self.centralwidget)
        self.lblAED.setGeometry(QtCore.QRect(180, 60, 281, 20))
        font = QtGui.QFont()
        font.setFamily("Sarai")
        font.setPointSize(18)
        self.lblAED.setFont(font)
        self.lblAED.setStyleSheet("background-image: url(:/cct/transparente.png);\n"
"color: rgb(255, 255, 255);")
        self.lblAED.setObjectName("lblAED")
        self.lblRight = QtWidgets.QLabel(self.centralwidget)
        self.lblRight.setGeometry(QtCore.QRect(530, 10, 31, 451))
        self.lblRight.setStyleSheet("background-image: url(:/cct/lblBackground.png);\n"
"border-radius:50px;\n"
"")
        self.lblRight.setText("")
        self.lblRight.setObjectName("lblRight")
        self.lblNameProyect = QtWidgets.QLabel(self.centralwidget)
        self.lblNameProyect.setGeometry(QtCore.QRect(160, 130, 271, 20))
        font = QtGui.QFont()
        font.setFamily("Sarai")
        font.setPointSize(14)
        self.lblNameProyect.setFont(font)
        self.lblNameProyect.setStyleSheet("background-image: url(:/cct/transparente.png);\n"
"color: rgb(255, 255, 255);")
        self.lblNameProyect.setObjectName("lblNameProyect")
        self.lblFor = QtWidgets.QLabel(self.centralwidget)
        self.lblFor.setGeometry(QtCore.QRect(240, 280, 401, 51))
        font = QtGui.QFont()
        font.setFamily("Sarai")
        font.setPointSize(14)
        self.lblFor.setFont(font)
        self.lblFor.setStyleSheet("background-image: url(:/cct/transparente.png);\n"
"color: rgb(255, 255, 127);")
        self.lblFor.setObjectName("lblFor")
        self.lblDate = QtWidgets.QLabel(self.centralwidget)
        self.lblDate.setGeometry(QtCore.QRect(240, 370, 121, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lblDate.setFont(font)
        self.lblDate.setStyleSheet("background-image: url(:/cct/transparente.png);\n"
"color: rgb(255, 255, 255);")
        self.lblDate.setObjectName("lblDate")
        self.lblProyect = QtWidgets.QLabel(self.centralwidget)
        self.lblProyect.setGeometry(QtCore.QRect(240, 90, 81, 20))
        font = QtGui.QFont()
        font.setFamily("Sarai")
        font.setPointSize(14)
        self.lblProyect.setFont(font)
        self.lblProyect.setStyleSheet("background-image: url(:/cct/transparente.png);\n"
"color: rgb(255, 255, 255);")
        self.lblProyect.setObjectName("lblProyect")
        self.lblDevelopment = QtWidgets.QLabel(self.centralwidget)
        self.lblDevelopment.setGeometry(QtCore.QRect(180, 260, 121, 20))
        font = QtGui.QFont()
        font.setFamily("Sarai")
        font.setPointSize(14)
        self.lblDevelopment.setFont(font)
        self.lblDevelopment.setStyleSheet("background-image: url(:/cct/transparente.png);\n"
"color: rgb(0, 170, 255);")
        self.lblDevelopment.setObjectName("lblDevelopment")
        self.lblProfessor = QtWidgets.QLabel(self.centralwidget)
        self.lblProfessor.setGeometry(QtCore.QRect(180, 190, 121, 20))
        font = QtGui.QFont()
        font.setFamily("Sarai")
        font.setPointSize(14)
        self.lblProfessor.setFont(font)
        self.lblProfessor.setStyleSheet("background-image: url(:/cct/transparente.png);\n"
"color: rgb(0, 170, 255);")
        self.lblProfessor.setObjectName("lblProfessor")
        self.lblNameProfessor = QtWidgets.QLabel(self.centralwidget)
        self.lblNameProfessor.setGeometry(QtCore.QRect(240, 220, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Sarai")
        font.setPointSize(14)
        self.lblNameProfessor.setFont(font)
        self.lblNameProfessor.setStyleSheet("background-image: url(:/cct/transparente.png);\n"
"color: rgb(255, 255, 127);")
        self.lblNameProfessor.setObjectName("lblNameProfessor")
        self.lblLeft = QtWidgets.QLabel(self.centralwidget)
        self.lblLeft.setGeometry(QtCore.QRect(50, 10, 31, 451))
        self.lblLeft.setStyleSheet("background-image: url(:/cct/lblBackground.png);\n"
"border-radius:50px;")
        self.lblLeft.setText("")
        self.lblLeft.setObjectName("lblLeft")
        self.lblLogoIs = QtWidgets.QLabel(self.centralwidget)
        self.lblLogoIs.setGeometry(QtCore.QRect(10, -60, 561, 81))
        self.lblLogoIs.setStyleSheet("background-image: url(:/cct/logos-UNAH-11.png);")
        self.lblLogoIs.setText("")
        self.lblLogoIs.setObjectName("lblLogoIs")
        self.lblBlack = QtWidgets.QLabel(self.centralwidget)
        self.lblBlack.setGeometry(QtCore.QRect(50, 430, 511, 31))
        self.lblBlack.setStyleSheet("background-image: url(:/cct/lblOpacidad50.png);\n"
"border-radius:50px;")
        self.lblBlack.setText("")
        self.lblBlack.setObjectName("lblBlack")
        self.lblLogoIs.raise_()
        self.lblRight.raise_()
        self.lblLeft.raise_()
        self.lblBlack.raise_()
        self.lblAED.raise_()
        self.lblNameProyect.raise_()
        self.lblFor.raise_()
        self.lblDate.raise_()
        self.lblProyect.raise_()
        self.lblDevelopment.raise_()
        self.lblProfessor.raise_()
        self.lblNameProfessor.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Acerca de"))
        self.lblAED.setText(_translate("MainWindow", "Algoritmos y Estructura De Datos"))
        self.lblNameProyect.setText(_translate("MainWindow", "Encriptador y desencriptador de Archivos."))
        self.lblFor.setText(_translate("MainWindow", "Keren Barrante        20171005145\n"
"Amilcar Rodriguez    20172500133"))
        self.lblDate.setText(_translate("MainWindow", "I PAC 2020"))
        self.lblProyect.setText(_translate("MainWindow", "Proyecto #2"))
        self.lblDevelopment.setText(_translate("MainWindow", "Desarrollado por:"))
        self.lblProfessor.setText(_translate("MainWindow", "Catedratico:"))
        self.lblNameProfessor.setText(_translate("MainWindow", "Jose Inestroza"))
#import Resource_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

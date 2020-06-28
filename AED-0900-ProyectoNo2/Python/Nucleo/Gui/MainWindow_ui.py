# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GuiWindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(700, 500)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/cct/Encriptar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("background-image: url(:/cct/transparente.png);\n"
"background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btnEncrypt = QtWidgets.QPushButton(self.centralwidget)
        self.btnEncrypt.setGeometry(QtCore.QRect(130, 290, 191, 51))
        self.btnEncrypt.setStyleSheet("\n"
"QPushButton{\n"
"    \n"
"    \n"
"    background-image: url(:/cct/transparente.png);\n"
"    font: \"Samyak Gujarati\";\n"
"    background-color: rgb(255, 0, 0);\n"
"    text-decoration:none;\n"
"    font-weight:100;\n"
"    font-size:14px;\n"
"    color: rgb(255, 255, 255);\n"
"    padding-top:5px;\n"
"    padding-bottom:10px;\n"
"    padding-left:150px;\n"
"    padding-right:150px;\n"
"    border-radius:10px;\n"
"    }\n"
"\n"
"QPushButton:hover{\n"
"    \n"
"    \n"
"    \n"
"    background-color: rgb(85, 170, 255);\n"
"    }\n"
"QPushButton:pressed{\n"
"    \n"
"    \n"
"    background-color: rgb(0, 170, 0);\n"
"    }")
        self.btnEncrypt.setAutoDefault(False)
        self.btnEncrypt.setObjectName("btnEncrypt")
        self.btnDecrypt = QtWidgets.QPushButton(self.centralwidget)
        self.btnDecrypt.setGeometry(QtCore.QRect(430, 290, 191, 51))
        self.btnDecrypt.setStyleSheet("QPushButton{\n"
"    \n"
"    background-image: url(:/cct/transparente.png);\n"
"    font: \"Samyak Gujarati\";\n"
"    \n"
"    background-color: rgb(170, 0, 127);\n"
"    text-decoration:none;\n"
"    font-weight:100;\n"
"    font-size:14px;\n"
"    color: rgb(255, 255, 255);\n"
"    padding-top:5px;\n"
"    padding-bottom:10px;\n"
"    padding-left:150px;\n"
"    padding-right:150px;\n"
"    border-radius:10px;\n"
"    }\n"
"\n"
"QPushButton:hover{\n"
"    \n"
"    \n"
"    \n"
"    background-color: rgb(85, 170, 255);\n"
"    }\n"
"QPushButton:pressed{\n"
"    \n"
"    \n"
"    background-color: rgb(0, 170, 0);\n"
"    }")
        self.btnDecrypt.setObjectName("btnDecrypt")
        self.txtSelectOrigin = QtWidgets.QLineEdit(self.centralwidget)
        self.txtSelectOrigin.setGeometry(QtCore.QRect(150, 40, 281, 41))
        self.txtSelectOrigin.setStyleSheet("QLineEdit{\n"
"    \n"
"    background-color: rgb(255, 255, 255);\n"
"    background-image: url(:/cct/transparente.png);\n"
"    font: \"Samyak Gujarati\";\n"
"    border-radius:8px;\n"
"    border: 1px solid black\n"
"    \n"
"}")
        self.txtSelectOrigin.setObjectName("txtSelectOrigin")
        self.btnSelectOrigin = QtWidgets.QPushButton(self.centralwidget)
        self.btnSelectOrigin.setGeometry(QtCore.QRect(450, 40, 101, 41))
        self.btnSelectOrigin.setStyleSheet("QPushButton{\n"
"    \n"
"    font: \"Samyak Gujarati\";\n"
"    \n"
"    background-image: url(:/cct/transparente.png);\n"
"    background-color: rgb(0, 0, 127);\n"
"    \n"
"    text-decoration:none;\n"
"    font-weight:100;\n"
"    font-size:14px;\n"
"    color: rgb(255, 255, 255);\n"
"    padding-top:5px;\n"
"    padding-bottom:10px;\n"
"    padding-left:150px;\n"
"    padding-right:150px;\n"
"    border-radius:10px;\n"
"    }\n"
"\n"
"QPushButton:hover{\n"
"    \n"
"    \n"
"    \n"
"    background-color: rgb(85, 170, 255);\n"
"    }\n"
"QPushButton:pressed{\n"
"    \n"
"    \n"
"    background-color: rgb(0, 170, 0);\n"
"    }")
        self.btnSelectOrigin.setObjectName("btnSelectOrigin")
        self.txtSelectDestination = QtWidgets.QLineEdit(self.centralwidget)
        self.txtSelectDestination.setGeometry(QtCore.QRect(150, 120, 281, 41))
        self.txtSelectDestination.setStyleSheet("QLineEdit{\n"
"    \n"
"    background-color: rgb(255, 255, 255);\n"
"    \n"
"    background-image: url(:/cct/transparente.png);\n"
"    font: \"Samyak Gujarati\";\n"
"    border-radius:8px;\n"
"    border: 1px solid black\n"
"    \n"
"}")
        self.txtSelectDestination.setClearButtonEnabled(False)
        self.txtSelectDestination.setObjectName("txtSelectDestination")
        self.btnSelectDestination = QtWidgets.QPushButton(self.centralwidget)
        self.btnSelectDestination.setGeometry(QtCore.QRect(450, 120, 101, 41))
        self.btnSelectDestination.setStyleSheet("QPushButton{\n"
"    \n"
"    background-image: url(:/cct/transparente.png);\n"
"    font: \"Samyak Gujarati\";\n"
"    \n"
"    background-color: rgb(0, 0, 127);\n"
"    text-decoration:none;\n"
"    font-weight:100;\n"
"    font-size:14px;\n"
"    color: rgb(255, 255, 255);\n"
"    padding-top:5px;\n"
"    padding-bottom:10px;\n"
"    padding-left:150px;\n"
"    padding-right:150px;\n"
"    border-radius:10px;\n"
"    }\n"
"\n"
"QPushButton:hover{\n"
"    \n"
"    \n"
"    \n"
"    background-color: rgb(85, 170, 255);\n"
"    }\n"
"QPushButton:pressed{\n"
"    \n"
"    \n"
"    background-color: rgb(0, 170, 0);\n"
"    }")
        self.btnSelectDestination.setObjectName("btnSelectDestination")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(90, 40, 51, 41))
        self.label.setStyleSheet("border-radius:5px;\n"
"image: url(:/cct/openFile.png);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(70, 280, 51, 51))
        self.label_3.setStyleSheet("border-radius:5px;\n"
"image: url(:/cct/Encriptar.png);")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(380, 290, 41, 41))
        self.label_4.setStyleSheet("border-radius:5px;\n"
"\n"
"image: url(:/cct/descodificar.png);")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.btnAbout = QtWidgets.QPushButton(self.centralwidget)
        self.btnAbout.setGeometry(QtCore.QRect(590, 430, 101, 41))
        self.btnAbout.setStyleSheet("\n"
"QPushButton{\n"
"    \n"
"    background-image: url(:/cct/transparente.png);\n"
"    \n"
"    font: \"Samyak Gujarati\";\n"
"    \n"
"    background-color: rgb(170, 0, 255);\n"
"    text-decoration:none;\n"
"    font-weight:100;\n"
"    font-size:14px;\n"
"    \n"
"    color: rgb(0, 0, 0);\n"
"    padding-top:5px;\n"
"    padding-bottom:10px;\n"
"    padding-left:150px;\n"
"    padding-right:150px;\n"
"    border-radius:10px;\n"
"    }\n"
"\n"
"QPushButton:hover{\n"
"    \n"
"    \n"
"    \n"
"    background-color: rgb(85, 170, 255);\n"
"    }\n"
"QPushButton:pressed{\n"
"    \n"
"    \n"
"    background-color: rgb(0, 170, 0);\n"
"    }")
        self.btnAbout.setObjectName("btnAbout")
        self.txtPassword = QtWidgets.QLineEdit(self.centralwidget)
        self.txtPassword.setGeometry(QtCore.QRect(260, 200, 281, 41))
        self.txtPassword.setStyleSheet("QLineEdit{\n"
"    \n"
"    background-color: rgb(255, 255, 255);\n"
"    \n"
"    background-image: url(:/cct/transparente.png);\n"
"    font: \"Samyak Gujarati\";\n"
"    border-radius:8px;\n"
"    border: 1px solid black\n"
"    \n"
"}")
        self.txtPassword.setFrame(True)
        self.txtPassword.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.txtPassword.setDragEnabled(False)
        self.txtPassword.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.txtPassword.setClearButtonEnabled(False)
        self.txtPassword.setObjectName("txtPassword")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(200, 200, 51, 41))
        self.label_5.setStyleSheet("border-radius:5px;\n"
"image: url(:/cct/contrasena.png);\n"
"")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(90, 120, 51, 41))
        self.label_2.setStyleSheet("border-radius:5px;\n"
"image: url(:/cct/saveFile.png);\n"
"\n"
"")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.btnShowGraph = QtWidgets.QPushButton(self.centralwidget)
        self.btnShowGraph.setGeometry(QtCore.QRect(250, 370, 211, 51))
        self.btnShowGraph.setStyleSheet("\n"
"QPushButton{\n"
"    \n"
"    \n"
"    background-image: url(:/cct/transparente.png);\n"
"    font: \"Samyak Gujarati\";\n"
"    \n"
"    background-color: rgb(32, 32, 45);\n"
"    text-decoration:none;\n"
"    font-weight:100;\n"
"    font-size:14px;\n"
"    color: rgb(255, 255, 255);\n"
"    padding-top:5px;\n"
"    padding-bottom:10px;\n"
"    padding-left:200px;\n"
"    padding-right:200px;\n"
"    border-radius:10px;\n"
"    }\n"
"\n"
"QPushButton:hover{\n"
"    \n"
"    \n"
"    \n"
"    background-color: rgb(85, 170, 255);\n"
"    }\n"
"QPushButton:pressed{\n"
"    \n"
"    \n"
"    background-color: rgb(0, 170, 0);\n"
"    }")
        self.btnShowGraph.setObjectName("btnShowGraph")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(200, 370, 41, 41))
        self.label_6.setStyleSheet("border-radius:5px;\n"
"\n"
"\n"
"image: url(:/cct/grafo.png);\n"
"")
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(540, 430, 41, 41))
        self.label_7.setStyleSheet("border-radius:5px;\n"
"\n"
"\n"
"image: url(:/cct/about.png);")
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Encriptador/Desencriptador"))
        self.btnEncrypt.setText(_translate("MainWindow", "Ejecutar \n"
"encriptado"))
        self.btnDecrypt.setText(_translate("MainWindow", "Ejecutar \n"
"Desencriptado"))
        self.txtSelectOrigin.setText(_translate("MainWindow", "Ruta, Archivo o Archivos origen"))
        self.btnSelectOrigin.setText(_translate("MainWindow", "Seleccionar"))
        self.txtSelectDestination.setText(_translate("MainWindow", "Ruta Destino"))
        self.btnSelectDestination.setText(_translate("MainWindow", "Seleccionar"))
        self.btnAbout.setText(_translate("MainWindow", "Acerca de"))
        self.txtPassword.setText(_translate("MainWindow", "Contraseña"))
        self.btnShowGraph.setText(_translate("MainWindow", "Mostrar Grafo \n"
"Desde Archivo JSON"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

# -*- coding: utf-8 -*-
import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import QPropertyAnimation, QRect, QAbstractAnimation
from PyQt5.QtWidgets import QApplication, QMainWindow
from Nucleo.Gui.WindowAbout_ui import Ui_MainWindow
from time import clock
class WindowAbout(QMainWindow):
    def __init__(self, parent = None):
        """
        Nombre: WindowAbout
        Parametros: No recibe parametros.
        Descripción: Hereda de QMainWindow, se encarga de administrar la ventana Acerca DE.
        """
        super(WindowAbout, self).__init__(parent)
        self.uiAbout = Ui_MainWindow()
        self.uiAbout.setupUi(self)
        self.centerWindow()

    def startAnimationLblLeft(self):
        """
        Inicia la animación del label izquierdo.
        """
        self.animationLblLeft = QPropertyAnimation(self.uiAbout.lblLeft,b"geometry")
        self.animationLblLeft.setDuration(700)
        self.animationLblLeft.setStartValue(QRect(50, 10, 31, 451))
        self.animationLblLeft.setEndValue(QRect(50, 10, 511, 451))
        self.animationLblLeft.start()

    def startAnimationLblRight(self):
        """
        Inicia la animación del label derecho.
        """
        self.animationLblRight = QPropertyAnimation(self.uiAbout.lblRight,b"geometry")
        self.animationLblRight.setDuration(700)
        self.animationLblRight.setStartValue(QRect(530, 10, 31, 451))
        self.animationLblRight.setEndValue(QRect(50, 10, 511, 451))
        self.animationLblRight.start()

    def startAnimationLogoIs(self):
        """
        Inicia la animación del logo IS.
        """
        self.animationLogoIs = QPropertyAnimation(self.uiAbout.lblLogoIs,b"geometry")
        self.animationLogoIs.setDuration(500)
        self.animationLogoIs.setStartValue(QRect(10,-60,561,81))
        self.animationLogoIs.setEndValue(QRect(10,-60,561,521))
        self.animationLogoIs.start()

    def startAnimationLblBlack(self):
        """
        Inicia la animacion del label oscuro.
        """
        self.animationLblBlack =   QPropertyAnimation(self.uiAbout.lblBlack, b"geometry")
        self.animationLblBlack.setDuration(500)
        self.animationLblBlack.setStartValue(QRect(50,441,511,20))
        self.animationLblBlack.setEndValue(QRect(50,10,511,451))
        self.animationLblBlack.start()



    def startAnimation(self):
        """
        Inicia todas las animaciones.
        """
        self.startAnimationLblRight()
        self.startAnimationLblBlack()
        self.startAnimationLblLeft()
        self.startAnimationLogoIs()

            

    def disableLbl(self):
        """
        Desactiva u oculta los labels graficos.
        """
        self.uiAbout.lblLogoIs.setVisible(False)
        self.uiAbout.lblAED.setVisible(False)
        self.uiAbout.lblProyect.setVisible(False)
        self.uiAbout.lblNameProyect.setVisible(False)
        self.uiAbout.lblProfessor.setVisible(False)
        self.uiAbout.lblNameProfessor.setVisible(False)
        self.uiAbout.lblDevelopment.setVisible(False)
        self.uiAbout.lblFor.setVisible(False)
        self.uiAbout.lblDate.setVisible(False)
    
    def enableLbl(self):
        """
        Activa o muestra los labels graficos.
        """
        
        self.uiAbout.lblLogoIs.setVisible(True)
        self.uiAbout.lblAED.setVisible(True)
        self.uiAbout.lblProyect.setVisible(True)
        self.uiAbout.lblNameProyect.setVisible(True)
        self.uiAbout.lblProfessor.setVisible(True)
        self.uiAbout.lblNameProfessor.setVisible(True)
        self.uiAbout.lblDevelopment.setVisible(True)
        self.uiAbout.lblFor.setVisible(True)
        self.uiAbout.lblDate.setVisible(True)
    """
    Nombre: centerWindow
    Parametros: No recibe parametros
    Descripcion: Inicializa la ventana al centro de la pantalla.
    Retorno: Retorna True
    """
    def centerWindow(self):
        screen = self.frameGeometry()
        ubication = QtWidgets.QDesktopWidget().availableGeometry().center()
        screen.moveCenter(ubication)
        self.move(screen.topLeft())


        


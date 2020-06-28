# -*- coding: utf-8 -*-
import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from Nucleo.Gui.LoadingWindow_ui import Ui_MainWindow

class WindowLoading(QMainWindow):
    """
    Administra la ventana de la barra de proceso.
    """
    def __init__(self, parent = None):
        super(WindowLoading, self).__init__(parent)
        self.uiLoading = Ui_MainWindow()
        self.uiLoading.setupUi(self)
        self.uiLoading.progressBar.setValue(0)      
        self.centerWindow()
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




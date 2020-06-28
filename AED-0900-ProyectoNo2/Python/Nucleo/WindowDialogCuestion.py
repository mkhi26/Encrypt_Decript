# -*- coding: utf-8 -*-
"""
    Esta es la clase que gestiona la GUI del QDialog
"""
import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog
from Nucleo.Gui.DialogCuestion_ui import Ui_Dialog
class DialogCuestion(QDialog):

    def __init__(self, parent = None):

        
        super(DialogCuestion, self).__init__(parent)
        self.uiDialogCuestion = Ui_Dialog()
        self.uiDialogCuestion.setupUi(self)
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

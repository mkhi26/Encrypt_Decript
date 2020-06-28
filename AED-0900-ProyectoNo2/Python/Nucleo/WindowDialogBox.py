# -*- coding: utf-8 -*-
"""
    Esta es la clase que gestiona la GUI del QDialog
"""
import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog
from Nucleo.Gui.DialogBox_ui import Ui_Dialog
class DialogConfirm(QDialog):

    def __init__(self, parent = None):

        
        super(DialogConfirm, self).__init__(parent)
        self.uiDialog = Ui_Dialog()
        self.uiDialog.setupUi(self)
        self.centerWindow()

    """
    Nombre: openDialogConfirm
    Parametros: No recibe parametros.
    Descripción: Abre una ventana que muestra el dialogo de confirmación.
    Retorno: No retorna.
    """
    def openDialogConfirm(self):
        self.show()

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
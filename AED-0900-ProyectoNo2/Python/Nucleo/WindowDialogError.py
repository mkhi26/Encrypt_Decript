
import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog
from Nucleo.Gui.DialogBoxError_ui import Ui_Dialog
class DialogBoxError(QDialog):
    """
    Esta clase Administra la ventana de un dialogo que muestra un error.
    """
    def __init__(self, parent = None):

        
        super(DialogBoxError, self).__init__(parent)
        self.uiDialogError = Ui_Dialog()
        self.uiDialogError.setupUi(self)
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

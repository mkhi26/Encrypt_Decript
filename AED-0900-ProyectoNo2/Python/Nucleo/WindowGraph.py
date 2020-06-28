import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import QPropertyAnimation, QRect, QAbstractAnimation
from PyQt5.QtWidgets import QApplication, QMainWindow
from Nucleo.Gui.GraphWindow_ui import Ui_Form
from time import clock
class WindowGraph(QMainWindow):
    """
    Administra la ventana que mostrara la imagen del grafo.
    """
    def __init__(self, parent = None):
        super(WindowGraph, self).__init__(parent)
        self.uiGraph = Ui_Form()
        self.uiGraph.setupUi(self)
        self.position()

    def position(self):
        self.move(598, 0)
        
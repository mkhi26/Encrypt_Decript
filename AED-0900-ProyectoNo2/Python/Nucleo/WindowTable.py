# -*- coding: utf-8 -*-
import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from Nucleo.Gui.TableWindow_ui import Ui_MainWindow
from PyQt5.QtWidgets import QTableWidgetItem
class WindowTable(QMainWindow):
    """
    Nombre: WindowTable
    Descripción: Administra la tabla de resumen.

    """
    def __init__(self, parent = None):
        super(WindowTable, self).__init__(parent)
        self.uiTable = Ui_MainWindow()
        self.uiTable.setupUi(self)
        self.position()

    def position(self):
        self.move(0,0)

    def addTable(self):
        item = QtWidgets.QTableWidgetItem()
        self.uiTable.tblFileProcess.setVerticalHeader(item)

    def generateTableProcess(self, filesProcessed, timeProcess, sizeFilesProcessed):

        self.uiTable.tblProcess.setItem(0,1, QTableWidgetItem("%s"% filesProcessed))
        self.uiTable.tblProcess.setItem(1,1, QTableWidgetItem("%s"% timeProcess))
        self.uiTable.tblProcess.setItem(2,1, QTableWidgetItem("%s KB"% sizeFilesProcessed))
        return True

    def generateTableFilesProcess(self, name, time, size, index):

        self.uiTable.tblFileProcess.setItem(index,0, QTableWidgetItem("%s"% name))
        self.uiTable.tblFileProcess.setItem(index,1, QTableWidgetItem("%s"% time))
        self.uiTable.tblFileProcess.setItem(index,2, QTableWidgetItem("%s"% size))
        return True
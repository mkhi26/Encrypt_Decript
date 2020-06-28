#-*-coding:utf-8 -*-
import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit
from Nucleo import Resource_rc
from Nucleo.Gui.MainWindow_ui import Ui_MainWindow
from Nucleo.GuiFileDialog import UiDialogFile
from Nucleo.WindowDialogError import DialogBoxError
from PyQt5.QtGui import QMouseEvent
from Nucleo.WindowTable import WindowTable
from Nucleo.WindowAbout import WindowAbout
from Nucleo.Validations import *
from Nucleo.EncryptManager import *
from Nucleo.WindowDialogCuestion import DialogCuestion
from Nucleo.WindowLoading import WindowLoading

import datetime
import os

from Nucleo.WindowDialogBox import DialogConfirm

class mainWindow(QMainWindow):
    """
    Clase que gestona todas las ventanas.
    """
    def __init__(self):
        super(mainWindow, self).__init__()

        # Se inicializa la ventana principal
        self.mainWindow = Ui_MainWindow()
        self.mainWindow.setupUi(self) 
        self.centerWindow()

        # Instancias de ventanas secundarias.
        self.uiDialog = DialogConfirm()
        self.uiAbout =  WindowAbout()
        self.uiDialogError = DialogBoxError()
        self.uiTable= WindowTable()
        self.uiFileDialog = UiDialogFile()
        self.uiDialogCuestion = DialogCuestion()




        # Otras instancias
        self.validations = Validations()
        self.encryptMannager = EncryptManager()
        self.encript = True
        self.table = False
        self.selectOrigin = True
        if(self.table):
            self.uiTable.show()


        # Eventos de los botones de la pantalla principal.

        self.mainWindow.btnSelectOrigin.clicked.connect(self.openDialogCuestion)
        self.mainWindow.btnSelectDestination.clicked.connect(self.openDialogFileDestination)
        self.mainWindow.btnEncrypt.clicked.connect(self.eventBtnEncript)
        self.mainWindow.btnDecrypt.clicked.connect(self.eventBtnDecrypt)
        self.mainWindow.btnAbout.clicked.connect(self.openWindowAbout)

        self.uiDialogCuestion.uiDialogCuestion.btnConfirm.clicked.connect(self.openDialogFileOrigin)
        self.uiDialogCuestion.uiDialogCuestion.rbtnFile.toggled.connect(self.activateOrigin)
        self.uiDialogCuestion.uiDialogCuestion.rbtnFolder.toggled.connect(self.disableOrigin)
        self.mainWindow.btnShowGraph.clicked.connect(self.openDialogFileJSON)

        # Eventos de los botones de dialogos de confirmación.
        self.uiDialog.uiDialog.btnConfirm.clicked.connect(self.executeAction)
        self.uiDialog.uiDialog.btnReject.clicked.connect(self.closeDialog)

        # Eventos del dialogo de error.
        self.uiDialogError.uiDialogError.btnConfirm.clicked.connect(self.closeDialogError)
        self.encryptMannager.dialog.uiDialogError.btnConfirm.clicked.connect(self.encryptMannager.closeDialog)


        self.initializeTextBox()

    # Funciones para los eventos de los botones de la pantalla priincipal.


    def openDialogFileJSON(self):
        """
        Nombre: openDialogFileJSON
        Parametros: No recibe parametros.
        Descripción: Abre un fileDialog para cargar grafo desde archivo JSON.
        Retorno: No retorna.
        """
        fileName =self.uiFileDialog.openFileNameDialog()
        if(fileName):
            self.encryptMannager.logGenerator.getDataFromJSON(fileName)
            self.encryptMannager.logGenerator.logJson.createImgGraph()
            self.openGraph()
        
    def showResume(self):
        """
        Nombre: showResume
        Parametros: No recibe parametros.
        Descripción: Abre la ventana con el grafo y otra ventana para mostrar el resumen.
        Retorno: No retorna.
        """
        self.enableorDisableBtns(False)
        self.OpenTable()
        self.openGraph()


    def OpenTable(self):
        """
        Nombre: OpenTable
        Parametros: No recibe parametros.
        Descripción: Abre una ventana con la tabla de resumen de los archivos procesados.
        Retorno: No retorna.
        """
        self.encryptMannager.processBarr.close()
        self.encryptMannager.logGenerator.table.show()


    def openGraph(self):
        """
        Nombre: openGraph
        Parametros: No recibe parametros.
        Descripción: Abre una ventana que mostrara el grafo.
        Retorno: No retorna.
        """

        self.encryptMannager.logGenerator.setImageToGraph()
        self.encryptMannager.logGenerator.uiGraph.show()




    def openDialogFileOrigin(self):
        """
        Nombre: openDialogFileOrigin
        Parametros: No recibe parametros.
        Descripción: Se llama esta función desde un evento de botón que abrirá un dialogo
                    para seleccionar un archivo, varios archivos o un directorio, luego que se seleccione
                    los archivos se visualizara en pantalla principal la ruta de los archivos seleccionados.
        Retorno: No retorna nada.
        """
        self.uiDialogCuestion.close()
        if(self.selectOrigin):
            files = self.uiFileDialog.openFileNamesDialog()
            if(files):
                self.mainWindow.txtSelectOrigin.setText(files)
        else:
            files = self.uiFileDialog.openFolderDialog()
            if(files):
                self.mainWindow.txtSelectOrigin.setText(files)

    def activateOrigin(self):
        """
        Nombre: activateOrigin
        Parametros: No recibe parametros.
        Descripción: Vuelve una variable booleana de instancia (self.selectOrigin) True.
        Retorno: No retorna
        """

        self.uiDialogCuestion.uiDialogCuestion.btnConfirm.setDisabled(False)
        self.selectOrigin = True
    
    def disableOrigin(self):
        """
        Nombre: disableOrigin
        Parametros: No recibe parametros.
        Descripción: Vuelve una variable booleana de instancia (self.selectOrigin) False.
        Retorno: No retorna
        """
        self.uiDialogCuestion.uiDialogCuestion.btnConfirm.setDisabled(False)
        self.selectOrigin = False
    
    def openDialogCuestion(self):
        """
        Nombre: openDialogCuestion
        Parametros: No recibe parametros.
        Descripción: Abre un dialogo para seleccionar si se desea abrir una carpeta o archivos.
        Retorno: No retorna.
        """
        self.uiDialogCuestion.uiDialogCuestion.btnConfirm.setDisabled(True)
        self.uiDialogCuestion.show()


    def openDialogFileDestination(self):
        """
        Nombre: openDialogFileDestination
        Parametros: No recibe parametros.
        Descripción: Se llama esta función desde un evento de botón que abrirá un dialogo
                    para seleccionar una ruta donde se guardara el archivo, luego visualiza 
                    la dirección de la ruta en una caja de texto de la pantalla principal.
        Retorno: No retorna nada.
        """
        ruteSave = self.uiFileDialog.openFolderDialog()
        if(ruteSave):
            self.mainWindow.txtSelectDestination.setText(ruteSave)


    def initializeTextBox(self):
        """
        Nombre: initializeTextBox
        Parametros: No recibe parametros.
        Descripción: Reinicia los textBox a su estado por defecto.
        Retorno: No retorna.
        """
        self.mainWindow.txtSelectOrigin.setText("")
        self.mainWindow.txtSelectOrigin.setPlaceholderText("Ruta, Archivo o Archivos Origen")
        self.mainWindow.txtSelectDestination.setText("")
        self.mainWindow.txtSelectDestination.setPlaceholderText("Ruta destino")
        self.mainWindow.txtPassword.setText("")
        self.mainWindow.txtPassword.setPlaceholderText("Contraseña")
        self.mainWindow.txtPassword.setEchoMode(QLineEdit.Password)

    def eventBtnEncript(self):
        """
        Nombre: eventBtnEncript
        Parametros: no recibe parametros.
        Descripción: Se llama esta función desde el evento del boton 'Encriptar'
                    luego se valida que los campos esten llenos, si estan llenos
                    abre un dialogo de confirmación, de lo contrario mostrara
                    un dialogo de error.
        Retorno: Retorna True

        """
        self.encript = True
        validateFields = self.validateFields()
        validateOrigin = self.validations.validateOrigin(self.mainWindow.txtSelectOrigin.text())
        validateDestination = self.validations.validateDir(self.mainWindow.txtSelectDestination.text())
        validatePass = self.validations.validatePassWord(self.mainWindow.txtPassword.text())
        if(validateFields and validateOrigin and validateDestination and validatePass):
            self.openDialogConfirmation()
            return True
        else:
            return self.errorMsj(validateFields, validateOrigin, validateDestination,validatePass)
    def eventBtnDecrypt(self):
        """
        Nombre: eventBtnDecrypt
        Parametros: no recibe parametros.
        Descripción: Se llama esta función desde el evento del boton 'Desencriptar'
                    luego abre un dialogo de confirmación si las validaciones retornan True,
                    en caso contrario abrirá un dialogo que mostrara un error.
        Retorno: Retorna True

        """
        self.encript = False
        validateFields = self.validateFields()
        validateOrigin = self.validations.validateOrigin(self.mainWindow.txtSelectOrigin.text())
        validateDestination = self.validations.validateDir(self.mainWindow.txtSelectDestination.text())
        validatePass = self.validations.validatePassWord(self.mainWindow.txtPassword.text())

        if(validateFields and validateOrigin and validateDestination and validatePass):
            self.openDialogConfirmation()
            return True
        else:
            return self.errorMsj(validateFields, validateOrigin, validateDestination, validatePass)


    def errorMsj(self, validateFields, validateOrigin, validateDestination, validatePass):
        """
        Nombre: errorMsj
        Parametros: 
                    ValidateFields, ValidateOrigin, ValidateDestination:
                    son las validaciones correspondientes (Bool)
        Descripción: Abre un dialogo de error con los mensajes correspondientes, segun el tipo de error.
        Retorno: Retorna False.

        """
        if(isinstance((validateFields and validateDestination and validateOrigin and validatePass),bool)):
            if(not validateFields):
                self.openDialogError("Error, es necesario completar\ntodos los campos.")
                return False
            if(not validateDestination and not validateOrigin):
                self.openDialogError("Error, ruta origen y ruta destino\nNo son validas.")
                return False
            if(not validateOrigin):
                self.openDialogError("Error, uno o mas elementos\nde la ruta origen no existen.")
                return False
            if(not validateDestination):
                self.openDialogError("Error, la ruta destino no existe.")
                return False
            if(not validatePass):
                self.openDialogError("Error, la contraseña ingreasada\nes muy larga.")
        return False




    def openDialogConfirmation(self):
        """
        Nombre: openDialogConfirmation
        Parametros: No recibe parametros.
        Descripción: Abre un dialogo de confirmación con un mensaje según la acción que
                    el usuario eligió.
        Retorno: No retorna
        """
        if(self.encript):
            self.uiDialog.uiDialog.lblText.setText("Se encriptaran los archivos seleccionados.")
        else:
            self.uiDialog.uiDialog.lblText.setText("Se desencriptaran los archivos seleccionados.")
        self.uiDialog.show()
    
    def closeDialog(self):
        """
        Nombre: closeDialog
        Parametros: No recibe parametros.
        Descripción: Cierra el dialogo de confirmación.
        Retorno: No retorna.
        """
        self.uiDialog.close()
    

    def openDialogError(self, text = "Error"):
        """
        Nombre: openDialogError
        Parametros: No recibe parametros.
        Descripción: Muestra un dialogo de error.
        Retorno: No retorna.
        """
        self.uiDialogError.uiDialogError.lblText.setText(text)
        self.uiDialogError.show()
    def closeDialogError(self):
        """
        Nombre: closeDeialogError
        Parametros: No recibe parametros.
        Descripción: Cierra un dialogo de error.
        Retorno: No retorna.
        """
        self.uiDialogError.close()


    def executeAction(self):
        """
        Nombre: executeAction
        Parametros: No recibe parametros.
        Descripción: Cierra el dialogo de confirmación y según la elección del usuario (Encriptar/ Desencriptar)
                    mostrara una barra de progreso en la pantalla.
        Retorno: No retorna
        """
        self.uiDialog.close()
        self.encryptMannager.processBarr.uiLoading.progressBar.setValue(0)
        password = self.mainWindow.txtPassword.text()
        origin = self.mainWindow.txtSelectOrigin.text()
        destination = self.mainWindow.txtSelectDestination.text()

        self.encryptMannager.password = password
        self.encryptMannager.origin = origin
        self.encryptMannager.destination = destination
        self.enableorDisableBtns(True)
        self.encryptMannager.processBarr.show()


        
        if(self.encript):  
            self.encryptMannager.typeWork = 'encrypt'
            if(self.validations.validateFolder(origin)):
                self.encryptMannager.type = 'folder'

            else:  
                self.encryptMannager.type = 'file'
            self.encryptMannager.start()



        else:
            self.encryptMannager.typeWork = 'decrypt'
            if(self.validations.validateFolder(origin)):
                self.encryptMannager.type = 'folder'
          
            else:
                self.encryptMannager.type = 'file'
            self.encryptMannager.start()
        self.encryptMannager.signal.connect(self.showResume)
        



        
    def setValues(self):
        """
        Nombre:setValues
        Parametros: No recibe parametros.
        Descripción:  Las rutas de carpetas o archivos de los textbox se asignan a las variables de instancia
                    del objeto EncryptManager.
        Retorno: No retorna.
        """
        password = self.mainWindow.txtPassword.text()
        origin = self.mainWindow.txtSelectOrigin.text()
        destination = self.mainWindow.txtSelectDestination.text()
        self.encryptMannager.password = password
        self.encryptMannager.origin = origin
        self.encryptMannager.destination = destination

    def validateFields(self):
        """
        Nombre: validateFields
        Parametros: No recibe parametros.
        Descripción: Valida que los campos de textos estén llenos,
        Retorno: True si se valida, False si hay campos vacíos.
        """
        origin = self.mainWindow.txtSelectOrigin.text()
        destination = self.mainWindow.txtSelectDestination.text()
        password = self.mainWindow.txtPassword.text()
        if((origin and destination and password) != ""):
            return True
        return False
    def openWindowAbout(self):
        """
        Nombre: openWindowAbout
        Parametros: No recibe parametros.
        Descripción: Abre una ventana con la información de este proyecto.
        Retorno: No retorna.

        """
        self.uiAbout.show()
        self.uiAbout.startAnimation()

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


    def enableorDisableBtns(self,value = True):
        """
        Nombre: enableorDisableBtns
        Parametros: 
                    value: Booleano Tru o False, True para desactivar los botones, False para activar.
        Descripcion: Desactiva o activa los botones.
        Retorno: No retorna
        """
        if isinstance(value,bool):
            self.mainWindow.btnDecrypt.setDisabled(value)
            self.mainWindow.btnEncrypt.setDisabled(value)
            self.mainWindow.btnSelectDestination.setDisabled(value)
            self.mainWindow.btnSelectOrigin.setDisabled(value)
            self.mainWindow.btnShowGraph.setDisabled(value)


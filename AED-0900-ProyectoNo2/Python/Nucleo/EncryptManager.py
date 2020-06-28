from Nucleo.EncryptAES_256 import *
from Nucleo.Encryptor import *
from Nucleo.Validations import *
from Nucleo.WindowLoading import WindowLoading
from PyQt5.QtCore import QThread, pyqtSignal, QBasicTimer
from Nucleo.WindowDialogError import DialogBoxError
from Nucleo.LogGenerator import LogGenerator
from Nucleo.WindowTable import WindowTable
import math
import datetime
import os
from Nucleo.TimeManager import *

class EncryptManager(QThread):
    """
    Nombre: EncryptManager
    Notas: 
           1. Esta clase hereda de QTread para poder ejecutarse en un nuevo hilo.
           2. signal (linea 39) es una instancia de pyqtSignal, sirve para enviar una señal al main para saber si el proceso de encriptado/ desencriptao ya termino.
    Atributos:
                self.password = Contraseña necesaria para encriptar o desencriptar.
                self.origin = Ruta origen de la carpeta o archivo origen.
                self.destination = Ruta destino donde se guardaran los archivos encriptados o desencriptados.
                self.typeWork = Tipo de tarea a realizar, los unicos valores que puede recibir son: 
                                'encrypt': Para encriptar.
                                'decrypt'Para desencriptar.

                self.type = Tipo de encriptado, los unicos valores que puede recibir son:
                            'file': si se estan encriptando archivos.
                            'Folder': Si se esta encriptando una carpeta.
                self.processBarr = Instancia de la GUI de barra de proceso.
                self.logGenerator = Instancia de la clase LogGenerator.
                self.dialog = GUI que muestra un dialogo de error.

    Descripción: Gestiona en un hilo secundario el proceso de encriptado o desencriptado.
    """
    signal = pyqtSignal(bool)
    def __init__(self, password = "", origin= "", destination= "", tipeWork= "encrypt", f = "file"):
        super().__init__()
        self.password = password
        self.origin = origin
        self.destination = destination
        self.typeWork = tipeWork
        self.type = f
        self.processBarr = WindowLoading()
        self.logGenerator = LogGenerator()
        self.dialog = DialogBoxError()

    def run(self):
        """
        Nombre: run -> Sobreescribe el metodo run de la clase padre 'QTread'
        Parametros: No recibe parametros.
        Descripción: Esta es la funcion que sobreescribe al metodo run de la clase padre 'QThread'
                    ejecuta en un hilo o proceso nuevo las operaciones de encriptado o descencriptado.
                    envia la señal al main cuando este ya termino la tarea.
        Retorno: Retorna True
        """
        
        if(self.type == 'file'):
            if(self.typeWork == 'encrypt'):
                self.encryptFileInner()
            elif(self.typeWork == 'decrypt'):
                self.decryptFileInner()
        elif(self.type == 'folder'):
            
            if(self.typeWork == 'encrypt'):
                self.encryptFolderInner()


            elif(self.typeWork == 'decrypt'):
                self.decryptFolderInner()

        self.signal.emit(True)
        

    def encryptFolderInner(self):
        """
        Nombre: encryptFolderInner
        Parametros:No recibe parametros.
        Descripción: Llama a la función encryptFolder y le pasa los atributos de instancia correspondientes.
        Retorno: Retorna True
        """
        startTime = time.time()

        password, origin, destination = self.getAttributes()
        self.encryptFolder(password,origin,destination)

        endTime = time.time()
        totalTime = endTime - startTime
        self.logGenerator.typeWork = "Encripdado"
        self.logGenerator.totaltime = totalTime
        self.logGenerator.resume()
        self.restoreDefaultAttributes()
        return True

    def encryptFileInner(self):
        """
        Nombre: encryptFileInner
        Parametros: No recibe parametros.
        Descripción: Llama a la función encryptFile y le pasa los atributos de instancia correspondientes.
        Retorno: Retorna True
        """
        startTime = time.time()

        password, origin, destination = self.getAttributes()
        self.encryptFile(password, origin, destination)

        endTime = time.time()
        totalTime = endTime - startTime
        self.logGenerator.typeWork = "Encripdado"
        self.logGenerator.totaltime = totalTime
        self.logGenerator.resume()
        self.restoreDefaultAttributes()
        return True
    def decryptFolderInner(self):
        """
        Nombre: decryptFolderInner
        Parametros: No recibe parametros.
        Descripción: Llama a la función decryptFolder y le pasa los atributos de instancia correspondiente.
        Retorno: Retorna True
        """
        startTime = time.time()

        password, origin, destination = self.getAttributes()
        self.decryptFolder(password,origin,destination)

        endTime = time.time()
        totalTime = endTime - startTime
        self.logGenerator.typeWork = "Desencriptado"
        self.logGenerator.totaltime = totalTime
        self.logGenerator.resume()
        self.restoreDefaultAttributes()
        return True

    def decryptFileInner(self):
        """
        Nombre: decryptFileInner
        Parametros: No recibe parametros.
        Descripción: Llama a la función decryptFile y le pasa los atributos de instancia corrspondientes.
        Retorno: Retorna True.
        """
        startTime = time.time()
        password, origin, destination = self.getAttributes()
        self.decryptFile(password, origin, destination)
        endTime = time.time()
        totalTime = endTime - startTime
        self.logGenerator.typeWork = "Desencriptado"
        self.logGenerator.totaltime = totalTime
        self.logGenerator.resume()
        self.restoreDefaultAttributes()
        return True

    def setValueProcessBarr(self, size = 1, current = 1):
        """
        Nombre: setValueProcessBarr
        Parametros: 
                    size: Total de archivos a procesar.
                    current: numero de archivos procesados.
        Descripción: Se hace el calculo del porcentaje de archivos procesados al momento, luego se muestra en la 
                    barra de proceso dicho valor.
        Retorno: Retorna True

        """    
        value = int(((current)/size)*100)
        self.processBarr.uiLoading.progressBar.setValue(value)
        return True

    def encryptFolder(self, password="", origin = "", destination = ""):
        """
        Nombre: encriptFolderAES_256
        Paramtros:
                    password: Clave necesaria para encriptar la carpeta.
                    origin: Ruta del directorio a encriptar.
                    destination: Ruta destino donde se guardara el directorio encriptado.
        Descripción: Encripta una carpeta con todo su contenido.
        Retorno: Retorna True

        """
        if(os.path.isdir(origin) and os.path.isdir(destination)):
            files, folders = self.getAllFiles(origin)
            if(len(files)>=1):
                nameRoot = origin.split("/")[-1]
                currentDestinationAES = "%s/%s/%s"%(destination,"AES_256",nameRoot)
                currentDestinationOWN = "%s/%s/%s"%(destination,"OWNAlgorithm",nameRoot)

                if(not os.path.isdir("%s/%s"%(destination, "AES_256"))):
                    try:
                        os.mkdir("%s/%s"%(destination, "AES_256")) # Se crea la carpeta raiz de encriptado
                        os.mkdir(currentDestinationAES)
                    except:
                        pass
                if (not os.path.isdir("%s/%s"%(destination, "OWNAlgorithm"))):
                    try:
                        os.mkdir("%s/%s"%(destination, "OWNAlgorithm")) # Se crea la carpeta raiz de encriptado
                        os.mkdir(currentDestinationOWN)
                    except:
                        pass

                self.generateRoutesDestination(folders,currentDestinationAES,currentDestinationOWN, nameRoot)
                self.logGenerator.logJson.addRoutesToTheGraph(folders,nameRoot)
                rootFiles = files[0].split("/")
                index = rootFiles.index(nameRoot)
                AES = EncryptorAES_256(password)
                OWN = Encryptor(password)

                for i in range(len(files)):
                        firstTimeFile = time.time()
                        currentOrigin = files[i]
                        listRoot= files[i].split("/")
                        routeDestineAES = "%s/%s"%(currentDestinationAES,"/".join(listRoot[index+1:]))
                        routeDestineOWN = "%s/%s"%(currentDestinationOWN,"/".join(listRoot[index+1:]))
                        AES.encryptFile(currentOrigin,routeDestineAES)
                        OWN.encryptFile(currentOrigin,routeDestineOWN)
                        self.logGenerator.logJson.addFileToTheGraph(currentOrigin)
                        
                        value = int(((i+1)/len(files))*100)
                        self.processBarr.uiLoading.progressBar.setValue(value)
                        endTimeFile = time.time()
                        totalTime = endTimeFile - firstTimeFile
                        self.logGenerator.addToFileList(currentOrigin,totalTime)
                                
                return True
            # Si la carpeta esta vacia:
            self.processBarr.close()
            self.dialog.uiDialogError.lblText.setText("La carpeta origen esta vacía,\n no hay nada que encriptar.")
            self.dialog.show()
            return False

        

    def encryptFile(self, password, origin = "", destination = ""):
        """
        Nombre: encryptAES_256
        Parametros: 
                    password: Contraseña proporcionada por el usuario.
                    origin: Ruta original del archivo.
                    destination: Ruta destino donde se guardara el archivo encriptado.

        Descripción: Genera un archivo  encriptado.
        Retorno: Retorna True
        """
        files = origin.split(",")
        AES = EncryptorAES_256(password)
        OWN = Encryptor(password)
        for i in range(len(files)):
            firstTimeFile = time.time()
            nameFile = self.getNameFile(files[i])
            try:
                os.mkdir("%s/AES_256/"%destination)
                os.mkdir("%s/OWNAlgorithm/"%destination)
            except:
                pass
            
            destinationFileAES = "%s/AES_256/%s" %(destination,nameFile)
            destinationFileOWN = "%s/OWNAlgorithm/%s"%(destination,nameFile)
            AES.encryptFile(files[i], destinationFileAES)
            OWN.encryptFile(files[i], destinationFileOWN)
            self.setValueProcessBarr(len(files), i+1)
            endTimeFile = time.time()
            totalTimeFile = endTimeFile - firstTimeFile
            self.logGenerator.addToFileList(files[i], totalTimeFile)
            folderRoot = files[i].split("/")[-2]
            self.logGenerator.logJson.graph.addVertex(folderRoot)
            self.logGenerator.logJson.addFileToTheGraph(files[i])
             

        
        return True
        
    def decryptFile(self, password, origin="", destination= ""):
        """
        Nombre: DESC_AES_256
        Parametros: 
                    password: Contraseña proporcionada por el usuario.
                    origin: Ruta original del archivo.
                    typeDecrypt: 'file' si se descifra un archivo
                                'folder' si se descifra un directorio.
        Descripción: Genera un archivo descifrado..
        Retorno: Retorna True
        """
        files = origin.split(",")
        AES = EncryptorAES_256(password)
        OWN = Encryptor(password)
        for i in range(len(files)):
            firstTimeFile = time.time()
            nameFile = self.getNameFile(files[i])
            if not os.path.isdir("%s/DESC_AES_256"%(destination)):
                os.mkdir(("%s/DESC_AES_256"%(destination)))  
            if(not os.path.isdir("%s/DESC_OWNAlgorithm"%(destination))):
                os.mkdir("%s/DESC_OWNAlgorithm"%(destination)) # Se crea la ruta raiz
            
            destinationFileAES = "%s/DESC_AES_256/%s"%(destination, nameFile)
            destinationFileOWN= "%s/DESC_OWNAlgorithm/%s"%(destination, nameFile)
            AES.decryptFile(files[i], destinationFileAES)
            OWN.decryptFile(files[i], destinationFileOWN)
            self.setValueProcessBarr(len(files), i+1)
            endTimeFile = time.time()
            totalTime = endTimeFile - firstTimeFile
            self.logGenerator.addToFileList(files[i], totalTime)
            folderRoot = files[i].split("/")[-2]
            self.logGenerator.logJson.graph.addVertex(folderRoot)
            self.logGenerator.logJson.addFileToTheGraph(files[i],encrypt= False)

        return True
    
    def decryptFolder(self, password, origin, destination):
        """
        Nombre: decryptFolderAES_256
        Paramtros:
                    password: Clave necesaria para descifrar la carpeta.
                    origin: Ruta del directorio a descifrar.
                    destination: Ruta destino donde se guardara el directorio descifrado.
        Descripción: Descifra una carpeta con todo su contenido.
        Retorno: Retorna True

        """
        
        if (os.path.isdir(origin) and os.path.isdir(destination)):

            files, folders = self.getAllFiles(origin)
            if(len(files)>=1):
                nameRoot = origin.split("/")[-1]
                rootDestination = "%s/%s"%(destination, "DESC_AES_256")
                currentDestinationAES = "%s/%s/%s"%(destination,"DESC_AES_256", nameRoot)
                currentDestinationOWN = "%s/%s/%s"%(destination,"DESC_OWNAlgorithm", nameRoot)

                if(not os.path.isdir("%s/%s"%(destination, "DESC_AES_256" ))):
                    os.mkdir("%s/%s"%(destination, "DESC_AES_256" ))
                    os.mkdir(currentDestinationAES)
                
                if(not os.path.isdir("%s/%s"%(destination, "DESC_OWNAlgorithm"))):
                    os.mkdir("%s/%s"%(destination, "DESC_OWNAlgorithm")) # Se crea la ruta raiz
                    os.mkdir(currentDestinationOWN)

                self.generateRoutesDestination(folders,currentDestinationAES,currentDestinationOWN,nameRoot) # Se crean los directorios
                self.logGenerator.logJson.addRoutesToTheGraph(folders,nameRoot)
                rootFiles = files[0].split("/")
                index = rootFiles.index(nameRoot)
                AES = EncryptorAES_256(password)
                OWN = Encryptor(password)
                for i in range(len(files)):
                    firstTimeFile = time.time()
                    currentOrigin = files[i]
                    listRoot = files[i].split("/")
                    routeDestineAES = "%s/%s"%(currentDestinationAES, "/".join(listRoot[index+1:]))
                    routeDestineOWN = "%s/%s"%(currentDestinationOWN,"/".join(listRoot[index+1:]))
                    OWN.decryptFile(currentOrigin, routeDestineOWN)
                    AES.decryptFile(currentOrigin,routeDestineAES)
                    
                    self.logGenerator.logJson.addFileToTheGraph(currentOrigin,encrypt= False)
                    endTimeFile = time.time()
                    totalTime = endTimeFile - firstTimeFile
                    self.setValueProcessBarr(len(files), i+1)
                    self.logGenerator.addToFileList(currentOrigin, totalTime)

            else:
                # Si la carpeta esta vacia:
                self.processBarr.close()
                self.dialog.uiDialogError.lblText.setText("La carpeta origen esta vacía,\n no hay nada que desencriptar.")
                self.dialog.show()
        return True


    def getAttributes(self):
        """
        Nombre: getAttributes
        Parametros: No recibe parametros.
        Descripción: Asigna los valores de instancias dentro de una función
        Retorno: retorna las variables de instancia.
        """
        return self.password, self.origin, self.destination



    def generateRoutesDestination(self, folders = [], destinationAES= "", DestinationOWN="", nameRoot=""):
        """
        Nombre: generateRoutesDestination
        Parametros:
                    folders: Lista con las rutas de origen de todos los archivos que contiene la carpeta raiz.
                    currentDestination: La ruta raiz de destino,
                    nameRoot: Nombre de la carpeta raiz de Origen.
        Descripción: Crea rutas en el disco duro segun las rutas destino.
        Retorno: True

        """

        if(len(folders)>=1):
            rootFiles = folders[0].split("/")
            index = rootFiles.index(nameRoot)
            for i in range(len(folders)):
                listRoot= folders[i].split("/")

                routeDestineAES = "%s/%s"%(destinationAES,"/".join(listRoot[index+1:]))
                routeDestineOWN = "%s/%s"%(DestinationOWN,"/".join(listRoot[index+1:]))
                try:
                    os.mkdir(routeDestineAES)
                    os.mkdir(routeDestineOWN)
                except:
                    pass
            return True
        return False
    """
    def addRoutesToTheGraph(self, folders = [], destinationAES= "", DestinationOWN="", nameRoot=""):

        if(len(folders)>=1):
            rootFiles = folders[0].split("/")
            index = rootFiles.index(nameRoot)
            for i in range(len(folders)):
                listRoot= folders[i].split("/")

                routeDestineAES = "%s/%s"%(destinationAES,"/".join(listRoot[index+1:]))
                routeDestineOWN = "%s/%s"%(DestinationOWN,"/".join(listRoot[index+1:]))

            return True
        return False
    """


    def getAllFiles(self, dirFolder):
        """
        Nombre: getAllFiles
        Parametros: 
                    dirFolder: Directorio raiz de donde se quieren obtener todos los archivos y subcarpetas 
                    que contiene la carpeta raiz.
        Descripción: Obtiene todas las rutas de archivos y directorios que contiene dicha carpeta.
        Retorno: Retorna la lista de archivos y subCarpetas que contiene la carpeta raiz.
        """
        dirs =[]
        subDirs = []
        for dirName, subDirList, fileList in os.walk(dirFolder):
            for fname  in fileList:
                dirs.append(dirName + "/" + fname)
            for subDirName in subDirList:
                subDirs.append(dirName+ "/"+ subDirName)
        return dirs, subDirs

    def getFiles(self, dirFolder):
        """
        Nombre: getFiles
        Parametros: 
                    dirFolder: Direccion o ruta de la carpeta de donde se quiere obtener
                    la ruta de archivos.
        Descripción: Obtiene en una lista los archivos que se encuentran en una carpeta.
        Retorno: -> list : retorna una lista con la ruta de los archivos que contiene dicha carpeta
        """
        filesList = []
        for nameFiles in dirFolder:
            if(os.path.isfile(nameFiles)):
                filesList.append(nameFiles)
        return filesList

    def getsubFolders(self, dirFolder):
        """
        Nombre: getSubFolders
        Parametros: 
                    dirFolder: Dirección o ruta de la carpeta de donde se quiere obtener
                    la ruta de subCarpetas.
        Descripción: Obtiene en una lista los archivos que se encuentran en una carpeta.
        Retorno: -> list : retorna una lista con la ruta de los archivos que contiene dicha carpeta

        """
        foldersList = []
        for nameFolders in dirFolder:
            if(os.path.isdir(nameFolders)):
                foldersList.append(nameFolders)
        return foldersList
                
    def getNameFile(self, ruteFile):
        """
        Nombre: getNameFile
        Parametros: ruteFile: Ruta del archivo.
        Descripción: Obtiene el nombre de un archivo segun su ruta.
        Retorno: Retorna un String con el nombre del archivo.
        """
        return  os.path.split(ruteFile)[1]
    def openLoading(self):
        """
        Nombre: openLoading
        Parametros: No recibe parametros.
        Descripción: Muestra una ventana con una barra de progreso.
        Retorno: No retorna
        """
        self.processBarr.setVisible(False)
        self.processBarr.show()
    def restoreDefaultAttributes(self):
        """
        Nombre:  restoreDefaultAttributes
        Parametros: No recibe parametros.
        Descripción: Restaura las variables de instancia a su valor por defecto,
        Retorno: No retorna.
        """
        self.password = ""
        self.origin = ""
        self.destination = ""
        self.type = ""
        self.typeWork = ""
    def closeDialog(self):
        """
        Nombre: closeDialog
        Parametros: No recibe parametros.
        Descripción: Cierra un dialogBox
        Retorno: No retorna.
        """
        self.dialog.close()


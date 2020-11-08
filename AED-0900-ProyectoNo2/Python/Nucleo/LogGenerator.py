import os
from Nucleo.WindowTable import WindowTable
from Nucleo.TimeManager import *
from PyQt5.QtCore import QThread
import datetime
import networkx as nx
import matplotlib.pyplot as plt
from Nucleo.Graph import *
from Nucleo.LogJSON import *
import json
from Nucleo.WindowGraph import WindowGraph
class LogGenerator:
    """
    Nombre: LogGenerator
    Atributos: 
                self.files= Lista que contiene el registro de los archivos procesados.
                self.timeManager =  Instancia de la clase TimeManager para gestionar el tiempo.
                self.totaltime = 0 Tiempo total de ejecución.
                self.table = GUI que muestra la tabla de los archivos procesados.
                self.uiGraph = GUI que muestra la imagen del grafo.
                self.typeWork = Tipo de tarea realizada ("Encrypt/Decript)
                self.logJson = Instancia de la clase logJson la cual maneja el registro en un JSON.
    Descripción: Genera registros en tablas HTML, Tablas de QT5, Diccionarios/ JSON.
    """
    def __init__(self):
        self.files= []
        self.timeManager = TimeManager()
        self.totaltime = 0
        self.table = WindowTable()
        self.uiGraph = WindowGraph()
        self.typeWork = ""
        self.logJson = LogJSON()




    def getDataFromJSON(self, route=""):
        """
        Nombre: getDataFromJSON
        Parametros: route: Ruta del archivo JSON.
        Descripción: Obtiene la data de un archivo JSON con el contenido del grafo.
        Retorno: True o False.
        """
        
        try:
            with open(route) as file:
                self.logJson.graph.graph= json.load(file)
                file.close()

        except:
            return False
        return True

    def addToFileList(self, ubicationFile, processingTime = 0):
        """
        Nombre: addToFileList

        Parametros:
                    ubicationFile: Ubicación del archivo a agregar.
                    processingTime: Tiempo que tarda el archivo en procesarce.

        Descripción: Agrega en una lista un registro con los datos de procesamiento del archivo.
                    nombre, tamaño y tiempo que tardo en encriptar.

        Retorno: No retorna.
        """
        nameFile = self.getNameFile(ubicationFile)
        sizeFile = os.path.getsize(ubicationFile)/1000
        dataFile = [nameFile, processingTime, sizeFile]
        self.files.append(dataFile)

    def resume(self):
        """
        Nombre: resume

        Parametro:
                    typeWork: Tipo de trabajo reaalizado, Encriptado/ Desencriptado.

        Descripción:    Genera una tabla html con el registro de todos los archivos procesados en la lista.
                        Genera una tabla QT5 con el registro de todos los archivos procesados.

        Retorno: No retorna.

        """

        self.generateTableProcess()
        self.generateTableFilesProcess()
        self.generateLogHtml(self.typeWork)
        self.generateLogJSON()

        self.files.clear()
        self.logJson.graph.graph.clear()



    
    def generateTableProcess(self):
        """
        Nombre: generateTableProcess

        Parametros: No recibe parametros.

        Descripción: Genera una tabla QT con la información general de todos los archivos procesasodos.

        Retorno: Retorna True.

        """
        filesProcessed = "%s Archivos"%len(self.files)
        timeProcess =self.timeManager.timeToString(0, self.totaltime)
        sizeFilesProcessed = round(self.getFileSizeProcess(),2)
        strSize = self.getStringFileSize(str(sizeFilesProcessed))
        self.table.uiTable.lblProcess.setText("Proceso ejecutado: %s"%self.typeWork)
        self.table.generateTableProcess(filesProcessed,timeProcess,strSize)
        return True

    def generateTableFilesProcess(self):
        """
        Nombre:  generateTableFilesProcess

        Parametros: No recibe parametros.

        Descripción: Genera una tabla QT5 con todos los elementos de la lista.

        Retorno: No retorna.

        """
        self.table.uiTable.lblFileProcess.setText("Archivos: %ss"% self.typeWork)
        self.table.uiTable.tblFileProcess.setRowCount(len(self.files) + 1)
        self.table.uiTable.tblFileProcess.setColumnCount(3)
        index = 1
        for element in self.files:

            name = "%s"% element[0]
            time = "%s"% self.timeManager.getTimeProcessFile(0, element[1])
            strSize = self.getStringFileSize(str(element[2]))
            size = "%s KB"% strSize
            self.table.generateTableFilesProcess(name, time, size, index)
            index+=1

    def generateLogJSON(self):
        """
        Nombre: generateLogJSON

        Parametros: No recibe parametros.

        Descripción: Genera un regisro de los archivos procesados en un archivo JSON.

        Retorno: Retoena True.
        """
        nameFile = "%s.json"% self.getCurrentLogName()
        content = self.logJson.graph.graph
        f = open("Nucleo/LOGS/%s"%nameFile, 'w', encoding= 'utf8')
        json.dump(content, f, indent=4)
        f.close()
        self.logJson.createImgGraph()
        self.logJson.graphNx.g = nx.DiGraph()

        return True

    def generateLogHtml(self, TypeWork = ""):
        """
        Nombre: generateLogHtml

        Parametros: TypeWork: Tipo de trabajo a realizar ('Encriptado/Desencriptado')

        Descripción: Genera una tabla HTMl con todos los archivos procesados en la lista.

        Retorno: No retorna.

        """
        nameFile = "%s.html"%self.getCurrentLogName()
        f = "Nucleo/LOGS/%s"%nameFile
        f = open(f,'w')
        tableProcess = self.getTableProcessHtml()
        tableFilesProcess = self.getContentTableHtml()
        title1 = "<h2>Proceso ejecutado: %s</h2>"% TypeWork
        title2 = "<h2>Archivos %s</h>"%TypeWork
        content = "%s<br>%s<br>%s<br>%s"%(title1,tableProcess, title2,tableFilesProcess)
        f.write(content)
        f.close()

    def getContentProcessHtml(self):
        """
        Nombre: getContentProcessHtml

        Parametros: No recibe parametros.

        Descripción: Obtiene el contenido de la lista para darle un formato de tabla HTML.

        Retorno: Retorna un String con el contenido de la tabla HTML.

        """

        FilesProcess = "<td>%s  </td>"% "Archivos procesados." 
        numFiles = "<td>%s Archivos </td>"% len(self.files)
        time = "<td>%s  </td>"% "Tiempo"
        timeProcess = "<td>%s  </td>"% self.timeManager.timeToString(0,self.totaltime)
        size = "<td>%s  </td>"% "Tamaño total"
        strSize = self.getStringFileSize(str(self.getFileSizeProcess()))
        sizeProcess = "<td>%s KB </td>"% strSize
    
        header_1 = "<tr>%s%s</tr>"% (FilesProcess,numFiles)
        header_2 = "<tr>%s%s</tr>"% (time,timeProcess)
        header_3 = "<tr>%s%s</tr>"% (size,sizeProcess)
        txt = "%s%s%s"%(header_1,header_2, header_3)
        return txt
    def getTableProcessHtml(self):
        """
        Nombre: getTableProcessHtml

        Parametros: No recibe parametros.

        Descripción: Se obtiene la tabla HTML en su formato final.

        Retorno: Retorna un String con la forma total de la tabla HTML.

        """
        conten = self.getContentProcessHtml()
        txt = "<table border = '1'> %s </table>"%(conten)
        return txt


    def getContentTableHtml(self):
        """
        Nombre:  getContentTableHtml

        Parametros: No recibe parametros.

        Descripción: Obtiene el contenido de la tabla HTML

        Retorno: Retorna una tabla HTML con su forma final.
        """
        header = self.getHeaderTableHtml()
        array = []
        array.append(header)
        count = 1
        for element in self.files:
            num = "<td>%s  </td>"%  count
            name = "<td>%s  </td>"% element[0]
            time = "<td>%s  </td>"% self.timeManager.getTimeProcessFile(0,element[1])
            size = "<td>%s KB</td>"% self.getStringFileSize(str(round(element[2],2)))
            row = "<tr>%s%s%s%s</tr>"% (num,name, time, size)
            array.append(row)
            count += 1
        txt = "<table border = '1'> %s </table>" %("".join(array))
        return txt

    def getHeaderTableHtml(self):
        """
        Nombre: getHeaderTableHtml

        Parametros: No recibe parametros.

        Descripción: Obtiene el encabezado de la tabla HTML.

        Retorno: Retorna un String con el encabezado de la tabla.

        """

        num = "<td>%s  </td>"% "Num." 
        name = "<td>%s  </td>"% "Nombre"
        time = "<td>%s  </td>"% "Tiempo de procesamiento"
        size = "<td>%s  </td>"% "Tamaño"
    
        header = "<tr>%s%s%s%s</tr>"% (num,name, time, size)
        return header

    def getCurrentLogName(self):
        """
        Nombre: getCurrentLogName

        Parametros: No recibe parametros.

        Descripción: Obtiene el nombre del archivo LOG.

        Retorno: Retorna un String con el nombre del archivo log.

        """
        date = datetime.datetime.now()
        year = date.year
        month = date.month
        day = date.day
        hour = date.hour
        minutes = date.minute
        second = date.second
        nameFile = "LOG_%s_%s_%s_%s_%s_%s"%(year,month,day,hour,minutes,second)
        return nameFile



    def getFileSizeProcess(self):
        """
        Nombre: getFileSizeProcess

        Parametros: No recibe parametros.

        Descripción: Obtiene el tamaño total de todos los archivos procesados.

        Retorno: Retorna un flotante del tamaño de los archivos procesados.

        """    
        sume = 0
        for i in range(len(self.files)):
            sume += self.files[i][2]
        return round(sume,3)

    def getTimeProcess(self):
        """
        Nombre: getTimeProcess

        Parametros: No recibe parametros.

        Descripción: Obtiene el tiempo total que tardaron los archivos en procesar.

        Retorno: No retorna.

        """
        sume = 0
        for i in range(len(self.files)):
            sume += self.files[i][1]
        return sume



    def getNameFile(self, ruteFile):
        """
        Nombre: getNameFile

        Parametros: ruteFile: Ruta del archivo.

        Descripción: Obtiene el nombre de un archivo segun su ruta.

        Retorno: Retorna un String con el nombre del archivo.
        """
        return  os.path.split(ruteFile)[1]


    def getStringFileSize(self, size = ""):
        """
        Nombre: getStringFileSize

        Parametros: 
                    size: Es una cadena de texto que contiene el tamaño del archivo.

        Descripción: Genera ina cadena de texto con la coma que se para la unidad de millar.

        Retorno: Retorna una cadena de texto.
        """
        integerSize = size.split(".")
        strSize = ""

        if len(integerSize) == 2:
            a, b = integerSize
            if len(a) > 3:
                strSize = "%s,%s.%s"%(a[:-3], a[-3:],b)
            else:
                strSize = "%s.%s"%(a,b)
        if len(integerSize) == 1:
            a = integerSize[0]
            if(len(a)> 3):
                strSize = "%s,%s.%s"%(a[:-3], a[-3:],00)
            else:
                strSize = "%s.%s"%(a,00)
        return strSize

        return strSize

    def setImageToGraph(self):
        """
        Nombre: setImageToGraph

        Parametros: No recibe parametros.

        Descripción: Agrega la imagen del grafo al textbox de la ventana 'Grafo'
        
        Retorno: Retorna True
        """
        self.uiGraph.uiGraph.txtImage.setHtml("<img src=\"Nucleo/LOGS/img.png\">")
        self.uiGraph.uiGraph.txtImage.setReadOnly(True)
        return True




from Nucleo.Graph import *
from Nucleo.GraphToNetworkx import *
from Nucleo.TimeManager import *
import networkx as nx
import matplotlib.pyplot as plt
import json
import os

class LogJSON:
    """
    Nombre:  LogJSON
    Atributos:
                self.graph: Instancia del TDA Graph
                self.graphNx: Instancia del TDA GraphToNetworkx
    Descripción: Gestiona un LOG JSON.

    """
    def __init__(self):
        self.graph= Graph()
        self.graphNx = GraphToNetworkx()


    def addRoutesToTheGraph(self, folders = [], nameRoot=""):
        """
        Nombre: addRoutesToTheGraph
        Parametros:
                    folders: lista con las rutas de las carpetas.
                    nameRoot: Nombre de la carpeta Raiz
        Descripción: Agrega las carpetas al grafo.
        Retorno: True si se agregan, False en caso contrario.

        """

        if(len(folders)>=1):
            rootFiles = folders[0].split("/")
            index = rootFiles.index(nameRoot)
            for i in range(len(folders)):
                listRoot= folders[i].split("/")
                sizeFolder = self.getSizeFolder(folders[i])
                currentFolders = listRoot[index:]
                self.graph.addEdges(currentFolders[-2],currentFolders[-1], 0)

            return True
        return False

    def addFileToTheGraph(self, ruteOrigin = "", encrypt = True):

        """
        Nombre: addFileToTheGraph
        Parametros:
                    ruteOrigin: Ruta de origen del archivo.
                    encrypt: --> True si se esta agregando desde encrypt.
                            --> False Si se esta agregando un archivo encriptado.
        Descripción: Agrega nombres de archivos como aristas de las carpetas.
        Retorno: Retorna True.
        """
        vertexA = ruteOrigin.split("/")[-2]
        vertexB =  ruteOrigin.split("/")[-1]
        if(not encrypt):
            extension = ".%s"%vertexB.split(".")[-2]
        else:
            extension = ".%s"%vertexB.split(".")[-1]
        sizeFile = round(os.path.getsize(ruteOrigin)/1000,2)

        if(not self.graph.relatedTo(extension)):
    
            self.graph.addEdges(vertexA,extension,sizeFile,1)
        else:
            self.graph.addEdges(vertexA, extension)
            
            totalList = self.graph.graph[vertexA][extension]["totalFiles"] + 1
            sumeSizeList = self.graph.graph[vertexA][extension]["weight"] + sizeFile
            self.graph.graph[vertexA][extension] = {"weight": sumeSizeList, "totalFiles":totalList}
        return True



    def createImgGraph(self):
        """
        Nombre: createImgGraph
        Parametros: No recibe parametros.
        Descripción: Genera un grafo de networkx a partir de un TDA Graph, se genera la imagen con el grafo.
        Retorno: Retorna True.
        """
        contentJson = self.graph.graph
        self.graphNx.generateNxGraph(contentJson)
        g = self.graphNx.g
        colorMap = self.graphNx.getMapColours()
        edgeLabels = self.graphNx.getEdgeLabels(g)
        
        pos=nx.spring_layout(g)
        

        nx.draw_networkx_edge_labels(g,pos,edge_labels=edgeLabels,font_size=8)
        nx.draw(g,pos,node_color = "black",with_labels = False,node_size = 2000)
        nx.draw(g ,pos, node_color = colorMap, font_color = "black",with_labels = True, node_size = 1500, linewidths = 0.9, width = 2, edge_color = "black",edge_cmap=plt.cm.Reds, font_size = 8,font_weight= "bold", arrowsize = 24)
        
        plt.savefig("Nucleo/LOGS/img.png")
        self.graph = Graph()
        self.graphNx = GraphToNetworkx()
        plt.clf()

        return True
 
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

    def getSizeFolder(self, rootFolder = '.'):
        """
        Nombre: getSizeFolder
        Parametros: rootFolder: Folder raiz.
        Descripción: Obtiene el peso en KB de una carpeta.
        Retorno: Retorna un Float con el peso de la carpeta.

        """
        totalSize = 0
        for dirpath, dirnames, filenames in os.walk(rootFolder):
            for f in filenames:
                currentFile = os.path.join(dirpath, f)
                totalSize += os.path.getsize(currentFile)
        return round(totalSize/1000,2)
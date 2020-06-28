import networkx as nx
import matplotlib.pyplot as plt
from Nucleo.Graph import *
class GraphToNetworkx:
    def __init__(self):
        """
        Nombre: GraphToNetworkx
        Atributos:
                    self.g: instancia del Grafo dirigido de networkx
        Descripción:
        """
        self.g = nx.DiGraph()

    def generateNxGraph(self, json = {}):
        """
        Nombre: generateNxGraph
        Parametros: 
                    json: Json con el contenido del TDA Grapho.
        Descripción: Genera el grafo de networkx a partir de un TDA Graph.
        Retorno: No retorna.
        """
        listItems = list(json.items())
        for i in listItems:
            currentFolder = i[0]
            contenCurrentFolder = i[1]
            self.addEdges(currentFolder, contenCurrentFolder)

    def getMapColours(self):
        """
        Nombre: getMapColours
        Parametros: No recibe parametros.
        Descripción: genera en una lista los colores de los nodos del grafo.
        Retorno: retorna la lista con los colores de los nodos.
        """
        g = self.g
        colorMap = []
        for node in g:
            if not "." in node:
                colorMap.append("khaki")
            else:
                color = self.getColor(node)
                colorMap.append(color)
        return colorMap

    def getListFiles(self):
        """
        Nombre: getListFiles
        Parametros: No recibe parametros.
        Descripción: Obtiene los nodos que tienen extensiones (Excluyendo las carpetas)
        Retorno: Retorna una lista con las extensiones agregadas (Las extensiones no se repiten)
        """
        g = self.g
        listFiles = []
        for node in g:
            if "." in node:
                extension = "".join(node.split("\n")[:-1])
                if(not extension in listFiles):
                    listFiles.append(extension)
        return listFiles

    def getColor(self, nodeName = ""):
        """
        Nombre: getColor
        Parametros: 
                        nodeName: Nombre del nodo al que se le asignara un color.
        Descripción: Obtiene el color del nodo.
        Retorno: Retorna un string con el nombre del color para el nodo.
        """
        nodeName = "".join(nodeName.split("\n")[:-1])
        listFiles = self.getListFiles()
        couplesList=[]
        colors = ["red","chartreuse","navy","turquoise","yellow","blue", "green", "purple", "brown", "teal", "lime", "pink",  "coral"]
        sizeListFiles =len(listFiles)
        count = 0
        for i in listFiles:
            if(count < len(colors)):

                if i == nodeName:
                    return colors[count]
                else:
                    count +=1
            else:
                count =0
        return "olive"


            
            
        

    def addEdges(self, vertexA = "", contenVertex = {}):
        """
        Nombre: addEdges
        Parametros: 
                    vertexA: Nombre del vertexA (Carpeta)
                    contenVertex: Diccionario con el contenido de la carpeta (Extensiones de los archivos).
        Descripción: Agrega los archivos (extensiones ) como los aristas de la carpeta al grafo de networkx.
        Retorno: No retorna.
        """
        listItems = contenVertex.items()
        for j in listItems:
            currentName = j[0]
            currentKey = j[1]
            weight = currentKey["weight"]
            totalFiles = currentKey["totalFiles"]
            nameVertexA = self.generateName(vertexA,0,0)
            nameVertexB = self.generateName(currentName,weight,totalFiles)
            self.g.add_edge(nameVertexA, nameVertexB, weight = weight)


    def generateName(self, name, weight, totalFiles):
        """
        Nombre:  generateName
        Parametros:
                        name: Nombre del nodo(Archivo)
                        weight: Peso de la arista del archivo.
                        totalFiles: Total de archivos con la misma extension.

        Descripción: Genera el nombre para que se visualice en el label del draw de networkx
        Retorno: retorna el nombre del nodo de networkx.
        """
        if(len(name)> 4 and len(name) <= 6):
            name = "\n%s"%(name)


        if(len(name)> 6 and len(name) <= 12):
            name = "%s\n%s\n%s"%(name[:3], name[3:9], name[9:])
        if(len(name)> 12):
            name = "%s\n%s\n%s"%(name[:3], name[3:9],name[9:13])
        if(weight >0):
            name = "%s\n%s"%(name,totalFiles)
        return name

    def getEdgeLabels(self, graphNx = nx.DiGraph()):
        """
        Nombre:  getEdgeLabels
        Parametros: 
                    graphNx: Grafo de network x. (puede ser self.g)
        Descripción: Obtiene las aristas del grafo de networkx con su respectivo peso.
        Retorno: retorna un diccionario con las aristas del grafo.
        """

        listEdges = []
        for u,v,d in graphNx.edges(data = True):
            if(d['weight']==0):
                listEdges.append([(u,v),"%s"%""])
            else:
                listEdges.append([(u,v),"%s kb"%round(d['weight'],2)])
        return dict(listEdges)







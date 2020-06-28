class Graph:
    """
    Nombre: Graph

    Atributos:
                self.graph: Diccionario que contendra los elementos agregados al grafo.

    Descripción: 
                    TDA que gestiona un diccionario para la construcción de un grafo.

    """
    def __init__(self):
        self.graph = {}
    
    def addVertex(self, vertexName = None):
        """
        Nombre: addVertex
        Parametros:
                    vertexName: Nombre del vertice a agregar.

        Descripción: Agrega un vertice al grafo, siendo grafo un diccionario.
                     Este método verifica que el nombre del vértice
        
        Retorno: No retorna.
        
        """
        if not ("%s".strip() % vertexName) in list(self.graph.keys()):
            self.graph["%s".strip()% vertexName] = {}
            return True
        return False

    def addEdges(self, vertexNameOrigin = None, vertexNameDestination = None, weight = 1, totalFiles = 0):
        """
        Nombre: addEdges

        Parametros: 
                    vertexNameOrigin: Nombre del vertice origen.
                    vertexNameDestination: Nombre del vertice destino.
                    weight: Peso de la arsta.
                    totalFiles: Total de archivos en la arista.

        Descripción: Este metodo crea una arista entre los vertices. Si los vertices no existen, los crea.
                     Si ya existe una arista entre los vertices, no se puede modificar el dato existente.
                     Se mantiene la integridad de los datos.

         Retorno: No retorna.   
        """
        
        if not vertexNameOrigin or not vertexNameDestination:
            return False
        self.addVertex(vertexNameOrigin)
        self.addVertex(vertexNameDestination)
        """
         Si no existe dentro de vertexNameOrigen  un elemento llamado vertexNameDestination,
        entonces se crea un elemento vertexNameDestination adentro de vertexNameOrigen
        """
        if not ("%s".strip() % vertexNameDestination) in list(self.graph["%s".strip()% vertexNameOrigin].keys()):
            self.graph["%s".strip() % vertexNameOrigin]["%s".strip()% vertexNameDestination] = {"weight": weight, "totalFiles":totalFiles}

    def __str__(self):
        """
        Nombre: __Str__
        Parametros: No recibe parametros.
        Descripción: Sobreescribe el metodo __str__ del string.
        Retorna: Retorna una version texto del grafo.

        """
        g = self.graph
        result = []
        for k, v in g.items():
            for edge, weight in v.items():
                result.append(" El vértice %s tiene una arista con el vertice %s y con peso %s"%(k, edge, weight["weight"]))
        return "\n".join(result)

    def relatedTo(self, vertexName = None):
        """
        Nombre: relatedTo
        Parametros: 
                    vertexName: Nombre del vertice al que se quiere comprobar su existencia dentro del grafo.

        Descripción: Comprueba la existencia de un vertice dentro del grafo.

        Retorno: si existe retorana la lista de llaves, de lo contrario retorna None.

        """
        if not vertexName: return None

        g = self.graph
        g, result = self.graph, {}
        for k, v in g.items():
            if(k == vertexName):
                for edge, weight in v.items():
                    result["%s".strip()% edge] = None
            elif( vertexName in list(v.keys())):
                result["%s".strip() % k]= None
        return list(result.keys())

    def relatedToTextInner(self, vertexName, element):
        """
        Nombre: 
        Parametros: 
                    vertexName: Nombre del vertice.
                    
                    element: elemento que hace arista con el verticeA.

        Descripción: Genera un texto de conexión de dos vertices.

        Retorno: Retorna un texto.
        """
        return "El vértice %s se conecta con el vértice %s" % (vertexName, element)

    def relatedToText(self, vertexName = None):
        if not vertexName: return None
        result = self.relatedTo(vertexName)
        result = list(
            map(
            
                self.relatedToTextInner,
                result,
                [
                vertexName for i in range(len(result))
                ]
            )
        )

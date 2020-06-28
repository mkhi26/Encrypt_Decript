import math
class EncryptAlgh:

    """
    Nombre: EncryptAlgh

    Atributos: 
                self.key: llave necesaria para encriptar o desencriptar.

    Descripción: Se encriptan arcivos.

    """
    def __init__(self, key):
        self.key = bytearray(self.complementKey(key), "utf-8")

    def complementKey(self, key):
        """
        Nombre: complementKey
        
        Parametros:
                    key: contraseña o llave necesaria para encriptar o desencriptar.

        Descripción: Rellena la cadena de contraseña a un len(16) o len(32)

        Retorno: Retorna un String con la contraseña rellenada.

        """
        if(len(key)==16  or len(key)==32):
            return key
        elif len( key)<16:
            password= []
            for i in range(16):
                password+= [key[i % len(key)]]
            return "".join(password)
        elif len(key)>16 and len(key)<32:
            for i in range(32):
                password+= [key[i % len(key)]]
            return "".join(password)
        else:
            return False


    def generateMatrix(self, conten):
        """
        Nombre: generateMatrix
        Parametros:
                    bytes(contenido: contenido de bytes.)
        Descripción: Agrega a una matriz de 16 x n elementos todo el contenido del archivo.

        Retorno: list-> Retorna una lista.
        """
        vector = self.getBlockNull()
        matrix = []
        count = 0

        for i in range(len(conten)):
            if(count == 16):
                count =0
                matrix.append(vector)
                vector = self.getBlockNull()
                vector[0] = chr(conten[i])

            if(i == len(conten)-1):
                
                vector[count]= chr(conten[i])

                matrix.append(vector)
                return matrix
            if(count < 16): 
                vector[count]= chr(conten[i])
                count +=1

    def rotateMatrix(self, matrix = []):
        """
        Nombre: rotateMatrix
        parametros: 
                    matrix: lista de lista.
        Descripción: Desplaza los elementos de la matriz una determinada posición en la lista.
        
        Retorno: Retorna una lista con una matriz de elementos desplazados
        """

        matrixRotate = []
        for i in matrix:
            vector= self.rotateElement(i)
            matrixRotate.append(vector)
        return matrixRotate


    def recoverMatrixElement(self, matrixIndex):
        """
        Nombre: recoverMatrixElement

        Parametros: matrixIndex

        Descripción: recupera los elementos de una matriz.

        Retorno: Retorna la matriz de los elementos.
        """
        for i in range(len(matrixIndex)):
            matrixIndex[i] = self.recoverPositions(matrixIndex[i])
        return matrixIndex

    def recoverPositions(self, listElement):

        """
        Nombre: recoverPositions
        Parametros: 
                    listElement: Lista de elementos para recobrar su posición original.
        Descripción: Recobra la posición de los elementos de una lista que han sido modificados con el metodo
        rotateElement.

        Retorno: Retorna una lista.

        """
        listRecover = self.getBlockNull()
        if(len(listElement)==16):
            listPartner = []
            for i in range(0,16,2):
                listPartner.append((listElement[i],listElement[i+1]))
                fistFragment = []
                endFragment = []

            for j in listPartner:
                fistFragment.append(j[0])
                endFragment.append(j[1])
            
            return fistFragment + endFragment
    

            
    def rotateElement(self, listElement):
        """
        Nombre: rotateElement

        Parametros: 
                    listElement: Lista con los elementos a rotar.
        Descripción: Cambia de posicion los elementos de la lista.

        Retorno: Retorna una lista con los elementos traspuestos.
        """
        listRotate = self.getBlockNull()
        if(len(listElement)==16):
            fistFragment = listElement[:8]
            endFragment = listElement[8:]
            count = 0
            for i in range(0,16,2):
            
                listRotate[i]= fistFragment[count]
                listRotate[i+1] = endFragment[count]
                count +=1
            return listRotate
        return False


    def getBlockNull(self):
        """
        Nombre:  getBlock
        Parametros: No recibe parametros.
        Descripción: Genera una vector de 16 elementos rellenado de ceros
        Retorno: retorna un vector de ceros.
        """
        block = []
        for j in range(16):
            block.append(" ")
        return block

    def matrixToString(self, matrix):
        """
        Nomnre: matrixToString
        Parametros: 
                    matrix: Lista de lista de chr.
        Descripción: Convierte los elementos de una ,matriz(lista de listas) a una cadena de texto(String)

        Retorno: Retorna una cadena (String)

        """
        conten =""

        for i in matrix:
            conten+= self.listToString(i)
        return conten

    def listToString(self,vector):
        """
        Nombre: listToString
        Parametros: 
                    vector: Lista con caracteres (chr)
        Descripción: Convierte los elementos de una lista a String.

        Retorno: Retorna unca cadena (String)
        """
        conten = ""
        for i in vector:
            conten += "%s"%i
        return conten



    def decryptMatrix(self, matrix):
        """
        Nombre: decryptMatrix
        Parametros: 
                    matrix: Matriz a desencriptar.

        Descripción: Desencripta una matriz.

        Retorno: Retorna una matriz desencriptada.
        """
        matrixDecrypt = []
        for i in matrix:
            matrixDecrypt.append(self.listDecrypt(i))
        return matrixDecrypt

    def listDecrypt(self, vector = []):
        """
        Nombre: listDecrypt
        Parametros: 
                    vector: Lista a desencriptar.

        Descripción: Desencripta una lista.

        Retorno: Retorna una lista desencriptada.
        """
        d = []
        count = 0
        for i in vector:
            de = chr(ord(i) ^ self.key[count])
            d.append(de)
            count +=1
        return d
            

    def encryptMatrix(self, matrix):
        """
        Nombre: encryptMatrix
        Parametros: 
                    matrix: Matriz a encriptar.

        Descripción: encripta una matriz.

        Retorno: Retorna una matriz encriptada.
        """

        matrixEncrypt = []
        for i in matrix:
            matrixEncrypt.append(self.listEncrypt(i))
        
        return matrixEncrypt
        
    def listEncrypt(self, vector = []):
        """
        Nombre: encryptMatrix
        Parametros: 
                    matrix: Matriz a encriptar.

        Descripción: encripta una matriz.

        Retorno: Retorna una matriz encriptada.
        """
        e = self.getBlockNull()
        count = 0
        for i in vector:
            en = chr(ord(i) ^ self.key[count])
            e[count]= en
            count+=1

        return e


        
    def matrixToString(self, matrix):
        """
        Nombre: matrixToString
        Parametros: 
                    matrix: Matriz con contenido.

        Descripción: convierte una matriz a cadena de texto (string)

        Retorno: Retorna una matriz encriptada.
        """
        conten = ""
        for i in range(len(matrix)):
            conten+= self.getString(matrix[i])
        
        return conten.strip()
       

    def getString(self, listElement= []):
        """
        Nombre: getString
        Parametros: 
                    listElement: Lista con elementos.
        Descripción: obtiene el contenido de una lista en una cadena de texto.
        Retorno: retorna un string.
        """
        conten = ""
        for i in listElement:
            conten+= "%s"%i

        return "%s".strip()%conten
        
    def encrypt(self,conten):
        """
        Nombre: encrypt

        Parametros: conten: bytes a encriptar.

        Descripción:  Encripta una cadena de bytes.

        Retorno: Retorna un bytearray
        """
        # Se genera una matriz de 16 columnas.
        matrixConten = self.generateMatrix(conten)
        # Se encripta esa matriz.
        matrixDisplace = self.rotateMatrix(matrixConten)
        # Se recobra la posición de los elementos de la matriz original.
        matrixEncrypt = self.encryptMatrix(matrixDisplace)
        # Se obtiene el texto de la matrix recuperada.
        strEncrypt = self.matrixToString(matrixEncrypt)
        # Se retorna un bytearray.
        return bytearray(strEncrypt, "utf-8")

    def decrypt(self, conten):
        """
        Nombre: encrypt

        Parametros: conten: bytes a desencriptar.

        Descripción:  Desencripta una cadena de bytes.

        Retorno: Retorna un bytearray
        """

        # Se genera una matriz de 16 columnas.
        matrixConten = self.generateMatrix(conten)
        # Se desencripta esa matriz.
        matrixDecrypt = self.decryptMatrix(matrixConten)
        # Se recobra la posición de los elementos de la matriz original.
        matrixRecover = self.recoverMatrixElement(matrixDecrypt)
        # Se obtiene el texto de la matrix recuperada.
        strDecrypt = self.matrixToString(matrixRecover)
        
        # Se retorna un bytearray.
        return bytearray(strDecrypt, "utf-8")
            
            
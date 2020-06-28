import os
class Validations:
    def __init__(self):
        """
        Nombre: Validations
        Atributos: No tiene atributos.
        Descripción: Realiza las validaciones de carpetas o archivos.
        """
        pass
    
    

    def validateOrigin(self, f= ""):
        """
        Nombre: validateOrigin
        Parametros:   f: ruta de archivo o archivos que se desea validar.
        Descripción: Valida la existencia de una ruta de archivos orígenes.
        Retorno: True o False.

        """
        rutes = f.split(",")
        for i in range(len(rutes)):
            if not self.validateDir(rutes[i]) and not self.validateFile(rutes[i]):
                return False
        return True
    def validateDir(self, ruteDir= ""):
        """
        Nombre: validateDir
        Parametros: 
                    ruteDir: Es la ruta que se desea comprobar su existencia.
        Descripción: Comprueba que una ruta ingresada sea valida.
        Retorno: 
                    True: Si la ruta es valida.
                    False: Si la ruta no es valida.
        """
        if(os.path.isdir(ruteDir)):
            return True
        else:
            return False

    def validateFile(self, ruteFile= ""):
        """
        Nombre: validateFile
        Parametros: 
                    ruteFile: Es la ruta de archivo que se desea comprobar su existencia.
        Descripción: Comprueba que una ruta, Archivo ingresada sea valida.
        Retorno: 
                    True: Si la ruta es valida.
                    False: Si la ruta no es valida.
        """
        if(os.path.isfile(ruteFile)):
            return True
        else:
            return False

    def validateFolder(self, ruteFolder):
        """
        Nombre: validateFolder
        Parametros: 
                    ruteFolder: Ruta del archivo que se desea validar su existencia.
        Descripción: 
                    Valida la existencia de una carpeta.
        Retorno: True o False, segun su existencia.
        """
        if(os.path.isdir(ruteFolder)):
            return True
        else:
            return False


    """
    Nombre: validatePassWord
    Parametros: Recibe una cadena de texto que contiene la contraseña.
    Descripción: Valida que la contraseña ingresada sea valida:
                 Es valida si el tamaño en el len es menor a 16
    Retorno:    Retorna True o False.
    """
    def validatePassWord(self, passWord=""):
        if(len(passWord)>32):
            return False
        return True
        
        


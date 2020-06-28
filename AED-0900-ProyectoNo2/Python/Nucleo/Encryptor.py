from Nucleo.EncryptAlgh import *
class Encryptor:
    """
    Nombre: Encryptor
    Atributos: self.key: Llave requerida para encriptar o desencriptar.

    Descripción: Este TDA administra un TDA 'EncryptAlght' para encriptar o desencriptar archivos.
    """
    def __init__(self, key):

        self.key = key

    
    def encrypt(self, text, key):
        """
        Nombre: encrypt

        Parametros:
                    text: Texto plano a encriptar.

        Descripción: Encripta un texto plano.

        Retorno: Retorna un texto plano cifrado.
        """
        en = EncryptAlgh(self.key)

        encrypt = en.encrypt(text)
        return encrypt

    def encryptFile(self, origin, destination ):
        """
        Nombre: encryptFile

        Parametros:
                    origin: Ruta origen del archivo a cifrar.

                    destination: Ruta destino donde se desea guardar el archivo cifrado.

        Descripción: Encripta un archivo y lo guarda en una ruta destino.
                    

        Retorno: No retorna.
        """
        

        conten = self.getContent(origin)
        enc = self.encrypt(conten,self.key) 
        destination = "%s.crp"% destination
        
        try:
            f = open(destination,"wb")
            f.write(enc)
            f.close()
        except:
            pass

        return True
    def getContent(self, route):
        """
        Nombre: getContent

        Parametros:
                    route: Ruta del archivo a obtener.

        Descripción: Obtiene el contenodo del archivo
 
        Retorno: Retorna un texto plano.
        """
    
        f = open(route, 'rb')
        text = f.read()
        if not text:
            text = bytes(" ", "utf-8")


        f.close()
        
        return text

    def decrypt(self, text, key):
        """
        Nombre: decrypt

        Parametros:
                    text: Texto plano a descifrar.

                    key: Contraseña o llave necesaria para descifrar.

        Descripción: Descifra un texto plano.

        Retorno: Retorna un texto plano con el contenido descifrado.
        """
        dec = EncryptAlgh(self.key)
        decrypt = dec.decrypt(text)

        return decrypt

    def decryptFile(self, origin, destination):
        """
        Nombre: decryptFile

        Parametros: origin: Ruta origen del archivo encriptado.

                    destination: Ruta destino del archivo descifrado.

        Descripción: Descifra un archivo, lo guarda en el disco segun su ruta destino.

        Retorno: No retorna.
        """
        if destination[-4:] != ".crp":
            return False
        conten = self.getContent(origin)

        dec = self.decrypt(conten,self.key)

        destination = destination[:-4]
        
        f = open(destination,"wb")
        f.write(dec)
        f.close()
        return True
        
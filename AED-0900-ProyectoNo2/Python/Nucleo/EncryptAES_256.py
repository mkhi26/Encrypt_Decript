
from Crypto import Random
from Crypto.Cipher import AES
import os
import os.path
from os import listdir
from os.path import isfile, join
import time

class EncryptorAES_256:
    """
    Nombre: EncryptorAES_256
    Atributos:
                self.key: clave para cifrar/descifrar.
    Descripción: Se encarga de gestionar el encriptado y decriptado de archivos.

    """
    def __init__(self, key):
        self.key = self.complementKey(key)


    """
    Nombre: textPad
    Parametros: s: Cadena con el contenido de el archivo.
    Descripción: Rellena el contenido con el bloque de bytes necesario.
    Retorno: Retorna una cadena con relleno.
    """
    def textPad(self, s):
        return s + b"\0" * (AES.block_size - len(s) % AES.block_size)



    def complementKey(self, key):
        """
        Nombre: complementKey
        Parametros: 
                    key: contraseña proporcionada por el usuario.
        Descripción: Rellena una contraseña de tal manera que contenga una cadena
                    con el tamaño de bytes de 16  o 32.
        Retorno: Retorna una contraseña con la cadena de bytes de relleno.

        """
        if(len(key)==16 or len(key)==24 or len(key)==32):
            return key
        elif len( key)<16:
            password= []
            for i in range(16):
                password+= [key[i % len(key)]]
            return "".join(password)
        elif len(key)>16 and len(key)<24:
            for i in range(24):
                password+= [key[i % len(key)]]
            return "".join(password)
        elif len(key)>24 and len(key)<32:
            for i in range(32):
                password+= [key[i % len(key)]]
            return "".join(password)


    """
    Nombre: encrypt
    Parametros:
                message: Contenido en string o byte que se desea encriptar.
                key: Llave con la que se desea encriptar.

    Descripción: Encripta el mensaje con su respectiva llave.
    Retorrno: Retorna el mensaje encriptado.
    """  
    def encrypt(self, message, key, key_size=256):
        message = self.textPad(message)
        iv = Random.new().read(AES.block_size)
        cipher = AES.new(key, AES.MODE_CBC, iv)
        return iv + cipher.encrypt(message)

    """
    Nombre: encryptFile
    Parametros:
                file_name: Ruta completa del archivo a encriptar
                destination: Ruta completa donde y como se desea guardar el archivo a encriptar.
    Descripción: Se encriptan archivos y se guardan en una ruta proporcionada por el usuario.

    Retorno: No retorna.

    """
    def encryptFile(self, file_name, destination):

        with open(file_name, 'rb') as fo:
            plaintext = fo.read()
        enc = self.encrypt(plaintext, self.key)
        destination = "%s.enc"%destination
        try:
            with open(destination, 'wb') as fo:
                fo.write(enc)
        except:
            
            return False

    """
    Nombre: decrypt
    Parametros: 
                ciphertext: Texto cifrado que se desea descifrar.
                key: Contraseña con la que se descifrara.
    Descripción: Descifra un texto o Bytes.
    Retorno: Retorna un texto plano con el contenido descifrado.
    """
    def decrypt(self, ciphertext, key):
        iv = ciphertext[:AES.block_size]
        cipher = AES.new(key, AES.MODE_CBC, iv)
        plaintext = cipher.decrypt(ciphertext[AES.block_size:])
        return plaintext.rstrip(b"\0")

    """
    Nombre: decrypt_file
    Parametros:
                file_name: Ruta del archivo que se desea encriptar incluyendo en la extensión el nombre del mismo.
                destination: Ruta destino con la que de desea guardar el archivo.
    Descripción: Descifra un archivo encriptado.
    Retorno: No retorna.
    """
    def decryptFile(self, file_name, destination):

        if(destination[-4:] != '.enc' and destination[-4:] != ".cry"):
            return False
        else:
            try:
                with open(file_name, 'rb') as fo:
                    ciphertext = fo.read()
                dec = self.decrypt(ciphertext, self.key)
                with open(destination[:-4], 'wb') as fo:
                    fo.write(dec)
            except:
                return False
import time
import datetime
import math
class TimeManager:
    def __init__(self):
        """
        Nombre: TimeManager
        Atributos: No tiene atributos.
        Descripción: Gestiona el tiempo de ejecución del programa.
        """
        pass

    def timeToString(self, firstTime, lastTime):
        """
        Nombre: timeToString
        Parametros: 
                    firstTime = Primer tiempo registrado en segundos.
                    lastTime = Tiempo final registrado en segundos.
        Descripción: Convierte los segundos a una cadena de texto representada en Horas minutos y segundos.
        Retorno: Retorna cadena de texto con la descripción del tiempo.

        """
        totalTime = lastTime - firstTime
        h, m, s, ms = self.getFormateTime(totalTime)
        strHour = ""
        strMinutes = ""
        strSeconds = ""
        stringFormate = ""
        strMilliseconds = ""
        if(h>0):
            if(h == 1):
                strHour = "hora"
            else:
                strHour = "horas"
        if(m>=0):
            if(m== 1):
                strMinutes = "minuto"
            else:
                strMinutes = "minutos"
        if(s>=0):
            if(s == 1):
                strSeconds = "segundo"
            else:
                strSeconds = "Segundos"
        if(ms >= 0):
            if(ms == 1):
                strMilliseconds = "milisegundo"
            else:
                strMilliseconds = "milisegundos"
        if(h > 0):
            return "%s %s %s %s %s %s %s %s"%(h, strHour, m, strMinutes, s, strSeconds, ms, strMilliseconds)
        else:
            return "%s %s %s %s %s %s"%(m, strMinutes, s, strSeconds, ms, strMilliseconds)
            

    def getFormateTime(self, totalTime):
        """
        Nombre: getFormateTime
        Parametros: 
                    totalTime: Tiempo total en segundos.
        Descripción: Recibe el tiempo total en segundos para generar un arreglo con el tiempo en [HH,MM,SS].
        Retorno: Retoena un arreglo conla forma [HH, MM, SS, MS]
        """
        arrayTime = []
        if(totalTime >= 3600):
            h = math.floor(totalTime / 3600)
            arrayTime.append(h)
            totalTime = totalTime - h*3600
        else:
            arrayTime.append(0)

        if(totalTime >=60):
            m = math.floor(totalTime / 60)
            arrayTime.append(m)
            totalTime = totalTime - m*60
        else:
            arrayTime.append(0)
        if(totalTime >= 1):
            s = math.floor(totalTime)
            arrayTime.append(s)
            totalTime = totalTime - s
        else:
            arrayTime.append(0)
        if(totalTime <=1):

            ms = math.floor(totalTime * 1000)
            arrayTime.append(ms)
        else:
            arrayTime.append(0)
        return arrayTime


    def getTimeProcessFile(self, firstTime, endTime):
        """
        Nombre: getTimeProcessFile
        Parametros: 
                    firstTime: primer tiempo registrado en segundos.
                    endTime: segundo tiempo registrado en segundos.
        Descripción: Genera una cadena de texto con la forma 'hh:mm:ss'
        Retorno: Retorna una cadena de texto.

        """
        totalTime= endTime - firstTime
        h, m, s, ms = self.getFormateTime(totalTime)

        if(h >0):
            return "%s:%s:%s:%s"%(h,m,s,ms)
        else:

            return "%s:%s:%s"%(m,s,ms)




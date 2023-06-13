import pickle

class Horario:
    dias = ['lunes', 'martes', 'miercoles', 'jueves', 'viernes', 'sabado', 'domingo']
    
    def __init__(self, dia, hora_inicio, hora_Fin):
        self.dia = dia
        self.hora_inicio = hora_inicio
        self.hora_Fin = hora_Fin
    
    def getDia(self):
        return self.dia
    
    def setDia(self, dia):
        self.dia = dia
    
    def getHora_inicio(self):
        return self.hora_inicio
    
    def setHora_inicio(self, hora_inicio):
        self.hora_inicio = hora_inicio
    
    def getHora_Fin(self):
        return self.hora_Fin
    
    def setHoraFinal(self, hora_Fin):
        self.hora_Fin = hora_Fin
    
    def __str__(self):
        return "Los dias " + str(self.dia) + " de " + self.hora_inicio + " a " + self.hora_Fin

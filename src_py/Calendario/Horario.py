from typing import List
from enum import Enum

class Horario:
    class Dias(Enum):
        LUNES = 'lunes'
        MARTES = 'martes'
        MIERCOLES = 'miercoles'
        JUEVES = 'jueves'
        VIERNES = 'viernes'
        SABADO = 'sabado'
        DOMINGO = 'domingo'

    def __init__(self, dia: List[Dias], hora_inicio: str, hora_fin: str):
        self.__dia = dia
        self.__hora_inicio = hora_inicio
        self.__hora_fin = hora_fin

    def getDia(self):
        return self.__dia

    def setDia(self, dia):
        self.__dia = dia

    def getHora_inicio(self) :
        return self.__hora_inicio

    def setHora_inicio(self, hora_inicio):
        self.__hora_inicio = hora_inicio

    def getHora_fin(self):
        return self.__hora_fin

    def setHora_fin(self, hora_fin):
        self.__hora_fin = hora_fin

    def __str__(self):
        dias_str = ', '.join(day.name for day in self.__dia)
        return f'Los días [{dias_str}] de {self.__hora_inicio} a {self.__hora_fin}'


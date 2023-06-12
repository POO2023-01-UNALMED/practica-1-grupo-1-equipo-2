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
        self.dia = dia
        self.hora_inicio = hora_inicio
        self.hora_fin = hora_fin

    @property
    def dia(self) -> List[Dias]:
        return self.__dia

    @dia.setter
    def dia(self, dia: List[Dias]):
        self.__dia = dia

    @property
    def hora_inicio(self) -> str:
        return self.__hora_inicio

    @hora_inicio.setter
    def hora_inicio(self, hora_inicio: str):
        self.__hora_inicio = hora_inicio

    @property
    def hora_fin(self) -> str:
        return self.__hora_fin

    @hora_fin.setter
    def hora_fin(self, hora_fin: str):
        self.__hora_fin = hora_fin

    def __str__(self) -> str:
        return f'Los dias {self.dia} de {self.hora_inicio} a {self.hora_fin}'


from personas.Estudiante import Estudiante
from typing import List
from enum import Enum

class Beca:
    class Tipos(Enum):
        BECA_INICIAL = 'becaInicial'
        BECA_NORMAL = 'becaNormal'
        BECA_AVANZADA = 'becaAvanzada'

    estudiantes = []

    def __init__(self, nombre: str):
        self.nombre = nombre
        self.estudiantes_aptos_inicial = []
        self.estudiantes_aptos_normal = []
        self.estudiantes_aptos_avanzada = []

    @property
    def estudiantes(self):
        return Beca.__estudiantes

    @estudiantes.setter
    def estudiantes(self, estudiantes):
        Beca.__estudiantes = estudiantes

    def asignar_estudiantes_beca(self):
        estudiantes_aptos_inicial2 = []
        estudiantes_aptos_normal2 = []
        estudiantes_aptos_avanzada2 = []

        for estudiante in Beca.estudiantes:
            if estudiante.porcentaje_de_avance >= 20 and estudiante.porcentaje_de_avance < 40 and estudiante.calcular_promedio() >= 4.5 and not estudiante.fue_becado:
                estudiantes_aptos_inicial2.append(estudiante)
            elif estudiante.porcentaje_de_avance >= 40 and estudiante.porcentaje_de_avance < 60 and estudiante.calcular_promedio() >= 4.0 and not estudiante.fue_becado:
                estudiantes_aptos_normal2.append(estudiante)
            elif estudiante.porcentaje_de_avance >= 60 and estudiante.porcentaje_de_avance < 100 and estudiante.calcular_promedio() >= 3.5 and not estudiante.fue_becado:
                estudiantes_aptos_avanzada2.append(estudiante)

        estudiantes_aptos_inicial2.sort(key=lambda x: x.calcular_promedio(), reverse=True)
        estudiantes_aptos_normal2.sort(key=lambda x: x.calcular_promedio(), reverse=True)
        estudiantes_aptos_avanzada2.sort(key=lambda x: x.calcular_promedio(), reverse=True)

        if len(estudiantes_aptos_inicial2) >= 2:
            for i in range(2):
                self.estudiantes_aptos_inicial.append(estudiantes_aptos_inicial2[i])
        elif len(estudiantes_aptos_inicial2) == 1:
            self.estudiantes_aptos_inicial.append(estudiantes_aptos_inicial2[0])

        if len(estudiantes_aptos_normal2) >= 2:
            for i in range(2):
                self.estudiantes_aptos_normal.append(estudiantes_aptos_normal2[i])
        elif len(estudiantes_aptos_normal2) == 1:
            self.estudiantes_aptos_normal.append(estudiantes_aptos_normal2[0])

        if len(estudiantes_aptos_avanzada2) >= 2:
            for i in range(2):
                self.estudiantes_aptos_avanzada.append(estudiantes_aptos_avanzada2[i])
        elif len(estudiantes_aptos_avanzada2) == 1:
            self.estudiantes_aptos_avanzada.append(estudiantes_aptos_avanzada2[0])
    @property
    def estudiantes_aptos_inicial(self):
        return self.__estudiantes_aptos_inicial

    @property
    def estudiantes_aptos_normal(self):
        return self.__estudiantes_aptos_normal

    @property
    def estudiantes_aptos_avanzada(self):
        return self.__estudiantes_aptos_avanzada

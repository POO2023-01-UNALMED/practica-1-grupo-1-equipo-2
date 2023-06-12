from Calendario.Tarea import Tarea
from Calendario.Horario import Horario
from personas.Profesor import Profesor
from typing import List
from enum import Enum


class Materia:
    class Tipo(Enum):
        FUNDAMENTACION = 'fundamentacion'
        DISCIPLINAR = 'disciplinar'
        LIBRE_ELECCION = 'libreEleccion'

    def __init__(self, codigo: int, nombre: str, profesor: 'Profesor', horario: 'Horario', creditos: int, prerrequisito: 'Materia' = None, tipo: Tipo = None):
        self.codigo = codigo
        self.nombre = nombre
        self.profesor = profesor
        self.horario = horario
        self.creditos = creditos
        self.aprobado = False
        self.tareas_de_materia = []
        self.estudiantes_inscritos = []
        self.prerrequisito = prerrequisito
        self.tipo = tipo

    @property
    def codigo(self) -> int:
        return self.__codigo

    @codigo.setter
    def codigo(self, codigo: int):
        self.__codigo = codigo

    @property
    def nombre(self) -> str:
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre: str):
        self.__nombre = nombre

    @property
    def profesor(self) -> 'Profesor':
        return self.__profesor

    @profesor.setter
    def profesor(self, profesor: 'Profesor'):
        self.__profesor = profesor

    @property
    def horario(self) -> 'Horario':
        return self.__horario

    @horario.setter
    def horario(self, horario: 'Horario'):
        self.__horario = horario

    @property
    def creditos(self) -> int:
        return self.__creditos

    @creditos.setter
    def creditos(self, creditos: int):
        self.__creditos = creditos

    @property
    def promedios(self):
        return self.__promedios

    @promedios.setter
    def promedios(self, promedios):
        self.__promedios = promedios

    @property
    def estudiantes_inscritos(self):
        return self.__estudiantes_inscritos

    @estudiantes_inscritos.setter
    def estudiantes_inscritos(self, estudiantes_inscritos):
        self.__estudiantes_inscritos = estudiantes_inscritos

    @property
    def tareas_de_materia(self):
        return self.__tareas_de_materia

    @tareas_de_materia.setter
    def tareas_de_materia(self, tareas_de_materia):
        self.__tareas_de_materia = tareas_de_materia

    @property
    def prerrequisito(self) -> 'Materia':
        return self.__prerrequisito
    
    @prerrequisito.setter
    def prerrequisito(self, prerrequisito: 'Materia'):
        self.__prerrequisito = prerrequisito

    def inscribir_estudiante(self, nuevo_estudiante: 'Estudiante'):
        self.estudiantes_inscritos.append(nuevo_estudiante)

    def retirar_estudiante(self, estudiante: 'Estudiante'):
        self.estudiantes_inscritos.remove(estudiante)

    def inscribir_tarea(self,tarea: 'Tarea'):
        self.tareas_de_materia.append(tarea)

    def retirar_tarea(self,tarea: 'Tarea'):
        self.tareas_de_materia.remove(tarea)

    def calcular_promedio(self, estudiante: 'Estudiante') -> float:
        total_score = 0
        contador = 0
        for tarea in self.tareas_de_materia:
            contador += 1
            total_score +=tarea.get_grade(estudiante)
        return round((total_score/contador) * 100.0) / 100.0

    def __str__(self) -> str:
        return f'{self.nombre} {self.horario}'

    def calcular_necesario_para_pasar(self, estudiante: 'Estudiante') -> float:
        total_score = 0
        contador = 0
        for tarea in self.tareas_de_materia:
            contador += 1
            total_score +=tarea.get_grade(estudiante)
        nota = round((total_score/contador) * 100.0) / 100.0

        nota_necesaria = 0.0

        if nota < 3:
            nota_necesaria = 3*(contador+1)-total_score

        return nota_necesaria

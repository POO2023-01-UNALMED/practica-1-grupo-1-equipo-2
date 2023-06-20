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
        self.__codigo = codigo
        self.__nombre = nombre
        self.__profesor = profesor
        self.__horario = horario
        self.__creditos = creditos
        self.aprobado = False
        self.__tareas_de_materia = []
        self.__estudiantes_inscritos = []
        self.__prerrequisito = prerrequisito
        self.tipo = tipo

    def getTipo(self):
        return self.tipo

    def setTipo(self, tipo):
        self.tipo = tipo

    def getCodigo(self):
        return self.__codigo

    def setCodigo(self, codigo):
        self.__codigo = codigo

    def getNombre(self):
        return self.__nombre

    def setNombre(self, nombre):
        self.__nombre = nombre

    def getProfesor(self):
        return self.__profesor

    def setProfesor(self, profesor):
        self.__profesor = profesor

    def getHorario(self):
        return self.__horario

    def setHorario(self, horario):
        self.__horario = horario

    def getCreditos(self):
        return self.__creditos
    
    def setCreditos(self, creditos):
        self.__creditos = creditos

    def getPromedios(self):
        return self.__promedios

    def setPromedios(self, promedios):
        self.__promedios = promedios

    def getEstudiantes_inscritos(self):
        return self.__estudiantes_inscritos

    def setEstudiantes_inscritos(self, estudiantes_inscritos):
        self.__estudiantes_inscritos = estudiantes_inscritos

    def getTareas_de_materia(self):
        return self.__tareas_de_materia
    
    def setTareas_de_materia(self, tareas_de_materia):
        self.__tareas_de_materia = tareas_de_materia

    def getPrerrequisito(self) :
        return self.__prerrequisito
    
    def setPrerrequisito(self, prerrequisito):
        self.__prerrequisito = prerrequisito

    def inscribir_estudiante(self, nuevo_estudiante):
        self.__estudiantes_inscritos.append(nuevo_estudiante)

    def retirar_estudiante(self, estudiante):
        self.__estudiantes_inscritos.remove(estudiante)

    def inscribir_tarea(self,tarea):
        self.__tareas_de_materia.append(tarea)

    def retirar_tarea(self,tarea):
        self.__tareas_de_materia.remove(tarea)

    def calcular_promedio(self, estudiante):
        total_score = 0
        contador = 0
        for tarea in self.__tareas_de_materia:
            contador += 1
            total_score +=tarea.get_grade(estudiante)
        return round((total_score/contador) * 100.0) / 100.0

    def calcular_necesario_para_pasar(self, estudiante):
        total_score = 0
        contador = 0
        for tarea in self.__tareas_de_materia:
            contador += 1
            total_score +=tarea.get_grade(estudiante)
        nota = round((total_score/contador) * 100.0) / 100.0

        nota_necesaria = 0.0

        if nota < 3:
            nota_necesaria = 3*(contador+1)-total_score

        return nota_necesaria
    
    def __str__(self):
        return f'{self.__nombre} {self.__horario}'

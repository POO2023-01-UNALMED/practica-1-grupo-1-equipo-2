from Calendario.TareaEstudiante import TareaEstudiante
from typing import List

class Tarea:
    def __init__(self, descripcion: str, fecha_entrega: str, fecha_inicio: str):
        self.__descripcion = descripcion
        self.__fecha_entrega = fecha_entrega
        self.__fecha_inicio = fecha_inicio
        self.__tarea_estudiantes = []

    def __init__(self, descripcion):
        self.descripcion = descripcion
        self.tarea_estudiantes = []

    def getTarea_estudiantes(self):
        return self.__tarea_estudiantes

    def setTarea_estudiantes(self, tarea_estudiantes):
        self.__tarea_estudiantes = tarea_estudiantes

    def getDescripcion(self):
        return self.__descripcion

    def setDescripcion(self, descripcion):
        self.__descripcion = descripcion

    def getFecha_entrega(self):
        return self.__fecha_entrega

    def setFecha_entrega(self, fecha_entrega):
        self.__fecha_entrega = fecha_entrega

    def getFecha_inicio(self):
        return self.__fecha_inicio

    def setFecha_inicio(self, fecha_inicio):
        self.__fecha_inicio = fecha_inicio

    def set_grade(self, estudiante, grade):
        found = False
        for tarea_estudiante in self.tarea_estudiantes:
            if TareaEstudiante(tarea_estudiante).getEstudiante == estudiante:
                TareaEstudiante(tarea_estudiante).getGrade = grade
                found = True
                break
        if not found:
            self.tarea_estudiantes.append(TareaEstudiante(self, estudiante, grade))

    def get_grade(self, estudiante):
        for tarea_estudiante in self.tarea_estudiantes:
            if TareaEstudiante(tarea_estudiante).getEstudiante == estudiante:
                return TareaEstudiante(tarea_estudiante).getGrade
        return 0.0

    def __str__(self):
        return f'Tarea sobre {self.descripcion}'

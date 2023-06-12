from Materia import Materia
from TareaEstudiante import TareaEstudiante
from personas.Estudiante import Estudiante

from typing import List

class Tarea:
    def __init__(self, descripcion: str, materia: 'Materia', fecha_entrega: str, fecha_inicio: str):
        self.descripcion = descripcion
        self.fecha_entrega = fecha_entrega
        self.fecha_inicio = fecha_inicio
        self.tarea_estudiantes = []

    def __init__(self, materia: 'Materia', descripcion: str):
        self.descripcion = descripcion
        self.tarea_estudiantes = []

    @property
    def tarea_estudiantes(self):
        return self.__tarea_estudiantes

    @tarea_estudiantes.setter
    def tarea_estudiantes(self, tarea_estudiantes):
        self.__tarea_estudiantes = tarea_estudiantes

    @property
    def descripcion(self) -> str:
        return self.__descripcion

    @descripcion.setter
    def descripcion(self, descripcion: str):
        self.__descripcion = descripcion

    @property
    def fecha_entrega(self) -> str:
        return self.__fecha_entrega

    @fecha_entrega.setter
    def fecha_entrega(self, fecha_entrega: str):
        self.__fecha_entrega = fecha_entrega

    @property
    def fecha_inicio(self) -> str:
        return self.__fecha_inicio

    @fecha_inicio.setter
    def fecha_inicio(self, fecha_inicio: str):
        self.__fecha_inicio = fecha_inicio

    def set_grade(self, estudiante: 'Estudiante', grade: float):
        found = False
        for tarea_estudiante in self.tarea_estudiantes:
            if tarea_estudiante.estudiante == estudiante:
                tarea_estudiante.grade = grade
                found = True
                break
        if not found:
            self.tarea_estudiantes.append(TareaEstudiante(self, estudiante, grade))

    def get_grade(self, estudiante: 'Estudiante') -> float:
        for tarea_estudiante in self.tarea_estudiantes:
            if tarea_estudiante.estudiante == estudiante:
                return tarea_estudiante.grade
        return 0.0

    def __str__(self) -> str:
        return f'Tarea sobre {self.descripcion}'

from personas.Persona import Persona
from typing import List

class Profesor(Persona):
    def __init__(self, nombre: str, ID: int, Email: str):
        super().__init__(nombre, ID, Email)
        self.calificaciones_docente = []
        self.__materias_asignadas = []
        self.calificacion_docente = 0

    def setCalificacion_docente(self, calificacion):
        self.calificacion_docente = calificacion

    def getCalificacion_docente(self):
        return self.calificacion_docente

    def setMaterias_asignadas(self):
        return self.__materias_asignadas

    def getMaterias_asignadas(self, materias_asignadas):
        self.__materias_asignadas = materias_asignadas

    #Metodos de clase
    def asignar_materia(self, nueva_materia):
        self.__materias_asignadas.append(nueva_materia)

    def retirar_materia(self, materia):
        self.__materias_asignadas.remove(materia)

    def ingresar_calificacion(self, calificacion):
        self.calificaciones_docente.append(calificacion)

    def retirar_calificacion(self, calificacion):
        self.calificaciones_docente.remove(calificacion)

    def evaluacion_docente(self):
        total_calificaciones = 0
        for calificacion in self.calificaciones_docente:
            total_calificaciones += calificacion
        self.calificacion_docente = round((total_calificaciones/len(self.calificaciones_docente))*10)/10.0

    def __str__(self):
        return f'Docente {self.getNombre()}'

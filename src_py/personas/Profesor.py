from personas.Persona import Persona
from Calendario.Materia import Materia
from typing import List

class Profesor(Persona):
    def __init__(self, nombre: str, ID: int, Email: str):
        super().__init__(nombre, ID, Email)
        self.calificaciones_docente = []
        self.materias_asignadas = []
        self.calificacion_docente = 0

    @property
    def calificacion_docente(self) -> float:
        return self.__calificacion_docente

    @calificacion_docente.setter
    def calificacion_docente(self, calificacion_docente: float):
        self.__calificacion_docente = calificacion_docente

    @property
    def calificaciones_docente(self) -> List[float]:
        return self.__calificaciones_docente

    @calificaciones_docente.setter
    def calificaciones_docente(self, calificaciones_docente: List[float]):
        self.__calificaciones_docente = calificaciones_docente

    @property
    def materias_asignadas(self):
        return self.__materias_asignadas

    @materias_asignadas.setter
    def materias_asignadas(self, materias_asignadas):
        self.__materias_asignadas = materias_asignadas

    #Metodos de clase
    def asignar_materia(self, nueva_materia: 'Materia'):
        self.materias_asignadas.append(nueva_materia)

    def retirar_materia(self, materia: 'Materia'):
        self.materias_asignadas.remove(materia)

    def ingresar_calificacion(self, calificacion: float):
        self.calificaciones_docente.append(calificacion)

    def retirar_calificacion(self, calificacion: float):
        self.calificaciones_docente.remove(calificacion)

    def evaluacion_docente(self):
        total_calificaciones = 0
        for calificacion in self.calificaciones_docente:
            total_calificaciones += calificacion
        self.calificacion_docente = round((total_calificaciones/len(self.calificaciones_docente))*10)/10.0

    def __str__(self) -> str:
        return f'Docente {self.nombre}'

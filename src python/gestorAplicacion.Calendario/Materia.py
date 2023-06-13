from typing import List
from gestorAplicacion.personas import Estudiante, Profesor
from Horario import Horario
from enum import Enum
from TareaEstudiante import TareaEstudiante
from gestorAplicacion.Calendario import Materia, Tarea

class tipo(Enum):
    fundamentacion = 1
    disciplinar = 2
    libreEleccion = 3

class Materia:
    def __init__(self, codigo: int, nombre: str, profesor: Profesor, horario: Horario, creditos: int, prerrequisito: Materia = None, tipo: tipo = None):
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

    def getCodigo(self) -> int:
        return self.codigo

    def setCodigo(self, codigo: int) -> None:
        self.codigo = codigo

    def getNombre(self) -> str:
        return self.nombre

    def setNombre(self, nombre: str) -> None:
        self.nombre = nombre

    def getProfesor(self) -> Profesor:
        return self.profesor

    def setProfesor(self, profesor: Profesor) -> None:
        self.profesor = profesor

    def getHorario(self) -> Horario:
        return self.horario

    def setHorario(self, horario: Horario) -> None:
        self.horario = horario

    def getCreditos(self) -> int:
        return self.creditos

    def setCreditos(self, creditos: int) -> None:
        self.creditos = creditos

    def getPromedio(self) -> List[TareaEstudiante]:
        return self.promedios

    def setPromedio(self, promedios: List[TareaEstudiante]) -> None:
        self.promedios = promedios

    def getEstudiantesInscritos(self) -> List[Estudiante]:
        return self.estudiantes_inscritos

    def setEstudiantesInscritos(self, estudiantesInscritos: List[Estudiante]) -> None:
        self.estudiantes_inscritos = estudiantesInscritos

    def getTareasDeMateria(self) -> List[Tarea]:
        return self.tareas_de_materia

    def setTareasDeMateria(self, nuevasTareas: List[Tarea]) -> None:
        self.tareas_de_materia = nuevasTareas

    def getPrerrequisito(self) -> Materia:
        return self.prerrequisito

    def setPrerrequisito(self, prerrequisito: Materia) -> None:
        self.prerrequisito = prerrequisito

    def getTipo(self) -> tipo:
        return self.tipo

    def setTipo(self, tipo: tipo) -> None:
        self.tipo = tipo

    def inscribirEstudiante(self, nuevoEstudiante: Estudiante) -> None:
        self.estudiantes_inscritos.append(nuevoEstudiante)

    def retirarEstudiante(self, Estudiante: Estudiante) -> None:
        self.estudiantes_inscritos.remove(Estudiante)

    def inscribirTarea(self, tarea: Tarea) -> None:
        self.tareas_de_materia.append(tarea)

    def retirarTarea(self, tarea: Tarea) -> None:
        self.tareas_de_materia.remove(tarea)

    def calcularPromedio(estudiante):
        totalScore = 0
        contador = 0
        for tarea in tareas_de_materia:
            contador += 1
            totalScore += tarea.getGrade(estudiante)
        return round((totalScore/contador) * 100.0) / 100.0

    def __str__():
        return nombre + " " + horario

    def Calcular_necesario_para_pasar(estudiante):
        totalScore = 0
        contador = 0
        for tarea in tareas_de_materia:
            contador += 1
            totalScore += tarea.getGrade(estudiante)
        nota = round((totalScore/contador) * 100.0) / 100.0
        Nota_necesaria = 0.0
        if nota < 3:
            Nota_necesaria = 3*(contador+1)-totalScore
        return Nota_necesaria


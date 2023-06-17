from enum import Enum
from src_py.Calendario.TareaEstudiante import TareaEstudiante
from typing import List
class Materia:
    class Tipo(Enum):
        FUNDAMENTACION = 'fundamentacion'
        DISCIPLINAR = 'disciplinar'
        LIBRE_ELECCION = 'libreEleccion'

    def __init__(self, codigo: int, nombre: str, profesor: 'Profesor', horario: 'Horario', creditos: int,
                 prerrequisito: 'Materia' = None, tipo: Tipo = None):
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

    def inscribir_tarea(self, tarea: 'Tarea'):
        self.tareas_de_materia.append(tarea)

    def retirar_tarea(self, tarea: 'Tarea'):
        self.tareas_de_materia.remove(tarea)

    def calcular_promedio(self, estudiante: 'Estudiante') -> float:
        total_score = 0
        contador = 0
        for tarea in self.tareas_de_materia:
            contador += 1
            total_score += tarea.get_grade(estudiante)
        return round((total_score / contador) * 100.0) / 100.0

    def __str__(self) -> str:
        return f'{self.nombre} {self.horario}'

    def calcular_necesario_para_pasar(self, estudiante: 'Estudiante') -> float:
        total_score = 0
        contador = 0
        for tarea in self.tareas_de_materia:
            contador += 1
            total_score += tarea.get_grade(estudiante)
        nota = round((total_score / contador) * 100.0) / 100.0

        nota_necesaria = 0.0

        if nota < 3:
            nota_necesaria = 3 * (contador + 1) - total_score

        return nota_necesaria

class Tarea1:
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

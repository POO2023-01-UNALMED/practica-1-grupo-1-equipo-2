

class TareaEstudiante:
    def __init__(self, tarea: 'Tarea', estudiante: 'Estudiante', grade: float):
        self.tarea = tarea
        self.estudiante = estudiante
        self.grade = grade

    @property
    def estudiante(self) -> 'Estudiante':
        return self.__estudiante

    @estudiante.setter
    def estudiante(self, estudiante: 'Estudiante'):
        self.__estudiante = estudiante

    @property
    def grade(self) -> float:
        return self.__grade

    @grade.setter
    def grade(self, grade: float):
        self.__grade = grade

    @property
    def tarea(self) -> 'Tarea':
        return self.__tarea

    @tarea.setter
    def tarea(self, tarea: 'Tarea'):
        self.__tarea = tarea

    def __str__(self) -> str:
        return f'TareaEstudiante{{tarea={self.tarea}, estudiante={self.estudiante}, grade={self.grade}}}'

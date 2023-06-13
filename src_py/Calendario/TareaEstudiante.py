

class TareaEstudiante:
    def __init__(self, tarea, estudiante, grade: float):
        self.__tarea = tarea
        self.__estudiante = estudiante
        self.__grade = grade

    def getEstudiante(self):
        return self.__estudiante

    def setEstudiante(self, estudiante):
        self.__estudiante = estudiante

    def getGrade(self) -> float:
        return self.__grade

    def setGrade(self, grade: float):
        self.__grade = grade

    def getTarea(self):
        return self.__tarea

    def setTarea(self, tarea):
        self.__tarea = tarea

    def __str__(self) -> str:
        return f'TareaEstudiante{{tarea={self.__tarea}, estudiante={self.__estudiante}, grade={self.__grade}}}'

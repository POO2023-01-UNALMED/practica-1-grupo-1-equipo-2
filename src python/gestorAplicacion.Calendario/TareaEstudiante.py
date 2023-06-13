from gestorAplicacion.personas import Estudiante
import pickle

class TareaEstudiante:
    def __init__(self, tarea, estudiante, grade):
        self.tarea = tarea
        self.estudiante = estudiante
        self.grade = grade

    def getEstudiante(self):
        return self.estudiante

    def setEstudiante(self, estudiante):
        self.estudiante = estudiante

    def getGrade(self):
        return self.grade

    def setGrade(self, grade):
        self.grade = grade

    def getTarea(self):
        return self.tarea

    def setTarea(self, tarea):
        self.tarea = tarea

    def __str__(self):
        return "TareaEstudiante{" + "tarea=" + str(self.tarea) + ", estudiante=" + str(self.estudiante) + ", grade=" + str(self.grade) + "}"

    def __getstate__(self):
        state = self.__dict__.copy()
        del state['estudiante']
        return state

    def __setstate__(self, state):
        self.__dict__.update(state)
        self.estudiante = None

from baseDatos import Deserializador
from gestorAplicacion.personas import Estudiante, Profesor
from gestorAplicacion.Calendario import Facultad, Materia, Beca

class gestionDatos:
    def __init__(self):
        self.facultadMinas = Facultad()
        self.estudiantes = []
        self.materias = self.facultadMinas.getMaterias()
        self.profesores = self.facultadMinas.getProfesores()
        self.sistemaBecas = Beca("")
        Deserializador.deserializar(self)

    def getMaterias(self):
        return self.materias

    def setMaterias(self, materias):
        self.materias = materias

    def getEstudiantes(self):
        return self.estudiantes

    def setEstudiantes(self, estudiantes):
        self.estudiantes = estudiantes

    def getProfesores(self):
        return self.profesores

    def setProfesores(self, profesores):
        self.profesores = profesores

    def getSistemaBecas(self):
        return self.sistemaBecas

    def setSistemaBecas(self, sistemaBecas):
        self.sistemaBecas = sistemaBecas

    def nuevoEstudiante(self, nombre, ID, Email, fueBecado, materias_cursadas=[]):
        nuevoEstudiante = Estudiante(nombre, ID, Email, fueBecado, materias_cursadas)
        self.estudiantes.append(nuevoEstudiante)
        return nuevoEstudiante

    def nuevoEstudiante(self, nombre, ID, Email, fueBecado):
        nuevoEstudiante = Estudiante(nombre, ID, Email, fueBecado)
        self.estudiantes.append(nuevoEstudiante)
        return nuevoEstudiante

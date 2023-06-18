import pickle
import os
from src_py.Calendario.Facultad import Facultad
from src_py.Calendario.Beca import Beca
from src_py.personas.Estudiante import Estudiante

class gestionDatos:
    def __init__(self):

        from src_py.baseDatos import Deserializador
        self.facultadMinas = Facultad()
        self.estudiantes = []
        self.materias = self.facultadMinas.getMaterias()
        self.profesores = self.facultadMinas.getProfesores()
        self.sistemaBecas = Beca("")
        Deserializador.Deserializador()
    
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
    
    def nuevoEstudiante(self, nombre, ID, Email, fueBecado, materias_cursadas=None):
        nuevoEstudiante = Estudiante(nombre, ID, Email, fueBecado, materias_cursadas)
        self.estudiantes.append(nuevoEstudiante)
        return nuevoEstudiante
    


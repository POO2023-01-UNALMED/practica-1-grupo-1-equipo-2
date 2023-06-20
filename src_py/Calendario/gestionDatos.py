import pickle
import os
from Calendario.Facultad import Facultad
from Calendario.Beca import Beca
from personas.Estudiante import Estudiante
from baseDatos.Deserializador import Deserializador


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

    def getDocumentos(self):
        Documentos = []
        for estudiante in self.getEstudiantes():
            Documentos.append(estudiante.getID())
        return Documentos

    def getDocumentosProfesores(self):
        Documentos = []
        for profesor in self.getProfesores():
            Documentos.append(profesor.getID())
        return Documentos

    def nuevoEstudiante(self, nombre, ID, Email, fueBecado, materias_cursadas=None):
        nuevoEstudiante = Estudiante(nombre, ID, Email, fueBecado, materias_cursadas)
        self.estudiantes.append(nuevoEstudiante)
        return nuevoEstudiante


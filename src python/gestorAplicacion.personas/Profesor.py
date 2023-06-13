from gestorAplicacion.Calendario import *
from Persona import Persona
import numpy as np

class Profesor(Persona):
    def __init__(self, nombre, ID, Email):
        super().__init__(nombre, ID, Email)
        self.materias_Asignadas = []
        self.calificacionesDocente = []
        self.calificacionDocente = 0
        
    def setCalificacionDocente(self, calificacion):
        self.calificacionDocente = calificacion
        
    def getCalificacionDocente(self):
        return self.calificacionDocente
    
    def setCalificacionesDocente(self, calificacionDocente):
        self.calificacionesDocente = calificacionDocente
        
    def getCalificacionesDocente(self):
        return self.calificacionesDocente
    
    def getMaterias_Asignadas(self):
        return self.materias_Asignadas
    
    def setMaterias_Asignadas(self, materiasAsignadas):
        self.materias_Asignadas = materiasAsignadas
        
    def asignarMateria(self, nuevaMateria):
        self.materias_Asignadas.append(nuevaMateria)
        
    def retirarMateria(self, Materia):
        self.materias_Asignadas.remove(Materia)
        
    def ingresarCalificacion(self, calificacion):
        self.calificacionesDocente.append(calificacion)
        self.calificacionDocente = np.mean(self.calificacionesDocente)
    
    def ingresarCalificacion(self, calificacion):
        self.calificacionesDocente.append(calificacion)

    def retirarCalificacion(self, calificacion):    
        self.calificacionesDocente.remove(calificacion)

    def evaluacionDocente(self):
        totalCalificaciones = 0
        for calificacion in self.calificacionesDocente:
            totalCalificaciones += calificacion
        self.calificacionDocente = round((totalCalificaciones/len(self.calificacionesDocente))*10)/10.0

    def __str__(self):
        return "Docente " + self.getNombre()

from typing import List
from gestorAplicacion.personas import Estudiante
from Materia import Materia
import pickle
from TareaEstudiante import TareaEstudiante

class Tarea:
    def __init__(self, descripcion: str, materia: Materia, fecha_Entrega: str, fecha_Inicio: str):
        self.descripcion = descripcion
        self.fecha_Entrega = fecha_Entrega
        self.fecha_Inicio = fecha_Inicio
        self.tareaEstudiantes = []
        
    def getTareaEstudiantes(self) -> List[TareaEstudiante]:
        return self.tareaEstudiantes
    
    def setTareaEstudiantes(self, tareaEstudiantes: List[TareaEstudiante]):
        self.tareaEstudiantes = tareaEstudiantes
        
    def setDescripcion(self, descripcion: str):
        self.descripcion = descripcion
        
    def getDescripcion(self) -> str:
        return self.descripcion
    
    def setFecha_Entrega(self, fecha_Entrega: str):
        self.fecha_Entrega = fecha_Entrega
        
    def getFecha_Entrega(self) -> str:
        return self.fecha_Entrega
    
    def setFecha_Intrega(self, fecha_Inicio: str):
        self.fecha_Inicio = fecha_Inicio
        
    def getFecha_Inicio(self) -> str:
        return self.fecha_Inicio
    
    def setGrade(self, estudiante: Estudiante, grade: float):
        found = False
        for tareaEstudiante in self.tareaEstudiantes:
            if tareaEstudiante.getEstudiante() == estudiante:
                tareaEstudiante.setGrade(grade)
                found = True
                break
        if not found:
            self.tareaEstudiantes.append(TareaEstudiante(self, estudiante, grade))
    
    def getGrade(self, estudiante: Estudiante) -> float:
        for tareaEstudiante in self.tareaEstudiantes:
            if tareaEstudiante.getEstudiante() == estudiante:
                return tareaEstudiante.getGrade()
        return 0.0
    
    def __str__(self) -> str:
        return "Tarea sobre " + self.descripcion

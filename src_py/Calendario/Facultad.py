
from personas.Estudiante import Profesor
from Calendario.Horario import Horario
from Calendario.Materia import Materia
from typing import List

class Facultad:
    def __init__(self):
        self.__nombre = 'Minas'
        self.__carrera = 'Ingenieria de Sistemas'
        self.materias = []
        self.__profesores = []

        horario1 = Horario([Horario.Dias.LUNES, Horario.Dias.MIERCOLES, Horario.Dias.VIERNES], '8', '10')
        guillermo = Profesor('Juan Guillermo', 10, 'guille@unal.edu.co')
        calculo_diferencial = Materia(10012, 'Calculo Diferencial', guillermo, horario1, 4, None, Materia.Tipo.FUNDAMENTACION)

        horario2 = Horario([Horario.Dias.LUNES, Horario.Dias.MARTES, Horario.Dias.JUEVES], '8', '10')
        diego = Profesor('Diego', 11, 'diego@unal.edu.co')
        calculo_integral = Materia(10013, 'Calculo Integral', diego, horario2, 4, calculo_diferencial, Materia.Tipo.FUNDAMENTACION)

        horario3 = Horario([Horario.Dias.LUNES, Horario.Dias.MARTES, Horario.Dias.JUEVES], '14', '16')
        marcos = Profesor('Marcos', 12, 'marcos@unal.edu.co')
        calculo_varias_variables = Materia(10014, 'Calculo Varias Variables', marcos, horario3, 4, calculo_integral, Materia.Tipo.FUNDAMENTACION)

        horario4 = Horario([Horario.Dias.MARTES, Horario.Dias.JUEVES], '18', '20')
        nelson = Profesor('Nelson', 13, 'nelson@unal.edu.co')
        fundamentos_programacion = Materia(10015, 'Fundamentos Programacion', nelson, horario4, 3,None,Materia.Tipo.DISCIPLINAR)

        horario5 = Horario([Horario.Dias.MARTES ,Horario.Dias.JUEVES],'14','16')
        jaime = Profesor('Jaime' ,14 ,'jaime@unal.edu.co')
        programacion_orientada_objetos = Materia(10016 ,'Programacion Orientada Objetos' ,jaime ,horario5 ,3 ,fundamentos_programacion ,Materia.Tipo.DISCIPLINAR)

        horario6 = Horario([Horario.Dias.MIERCOLES ,Horario.Dias.VIERNES],'8','10')
        julian = Profesor('Julian' ,15 ,'julian@unal.edu.co')
        estructura_datos = Materia(10017 ,'Estructura Datos' ,julian ,horario6 ,3 ,programacion_orientada_objetos ,Materia.Tipo.DISCIPLINAR)

        horario7 = Horario([Horario.Dias.LUNES],'14','16')
        sierra = Profesor('Sierra' ,16 ,'sierra@unal.edu.co')
        catedra_antioquia = Materia(10018 ,'Catedra Antioquia' ,sierra ,horario7 ,3 ,None ,Materia.Tipo.LIBRE_ELECCION)

        horario8 = Horario([Horario.Dias.SABADO],'8','10')
        catedra_apun = Materia(10019 ,'Catedra Apun' ,sierra ,horario8 ,3 ,None ,Materia.Tipo.LIBRE_ELECCION)

        horario9 = Horario([Horario.Dias.MARTES],'8','10')
        marisol = Profesor('Marisol' ,17 ,'marisol@unal.edu.co')
        catedra_felicidad = Materia(10019 ,'Catedra Felicidad' ,marisol ,horario9 ,3 ,None ,Materia.Tipo.LIBRE_ELECCION)

        self.materias.append(calculo_diferencial)
        self.materias.append(calculo_integral)
        self.materias.append(calculo_varias_variables)
        self.materias.append(fundamentos_programacion)
        self.materias.append(programacion_orientada_objetos)
        self.materias.append(estructura_datos)
        self.materias.append(catedra_antioquia)
        self.materias.append(catedra_apun)
        self.materias.append(catedra_felicidad)

        for i in range(len(self.materias)):
            profesor = self.materias[i].getProfesor()
            if profesor not in self.__profesores:
                self.__profesores.append(profesor)
            profesor.asignar_materia(self.materias[i])

    def getNombre(self) -> str:
        return self.__nombre

    def setNombre(self, nombre: str):
        self.__nombre = nombre

    def getCarrera(self) -> str:
        return self.__carrera

    def setCarrera(self, carrera: str):
        self.__carrera = carrera

    def getMaterias(self):
        return self.materias
    
    def setMaterias(self, materias):
        self.materias = materias

    def getProfesores(self):
        return self.__profesores
    
    def setProfesores(self, profesores):
        self.__profesores = profesores


from typing import List
from enum import Enum

class dias(Enum):
    lunes = 1
    martes = 2
    miercoles = 3
    jueves = 4
    viernes = 5
    sabado = 6
    domingo = 7

class tipo(Enum):
    fundamentacion = 1
    disciplinar = 2
    libreEleccion = 3

class Horario:
    def __init__(self, dias: List[dias], horaInicio: str, horaFin: str):
        self.dias = dias
        self.horaInicio = horaInicio
        self.horaFin = horaFin

class Profesor:
    def __init__(self, nombre: str, id: int, correo: str):
        self.nombre = nombre
        self.id = id
        self.correo = correo
        self.materias = []

    def asignarMateria(self, materia):
        self.materias.append(materia)

class Materia:
    def __init__(self, codigo: int, nombre: str, profesor: Profesor, horario: Horario, creditos: int, tipo: tipo, prerequisito=None):
        self.codigo = codigo
        self.nombre = nombre
        self.profesor = profesor
        self.horario = horario
        self.creditos = creditos
        self.tipo = tipo
        self.prerequisito = prerequisito

class Facultad:
    def __init__(self):
        self.nombre = "Minas"
        self.carrera = "Ingenieria de Sistemas"
        self.materias = []
        self.profesores = []
        horario1 = Horario([dias.lunes, dias.miercoles, dias.viernes], "8", "10")
        Guillermo = Profesor("Juan Guillermo", 10, "guille@unal.edu.co")
        Calculo_Diferencial = Materia(10012,"Calculo Diferencial",Guillermo,horario1,4, tipo.fundamentacion)
        horario2 = Horario([dias.lunes, dias.martes, dias.jueves], "8", "10")
        Diego = Profesor("Diego", 11, "diego@unal.edu.co")
        Calculo_Integral = Materia(10013, "Calculo Integral", Diego, horario2, 4, Calculo_Diferencial, tipo.fundamentacion)
        horario3 = Horario([dias.lunes, dias.martes, dias.jueves], "14", "16")
        Marcos = Profesor("Marcos", 12, "marcos@unal.edu.co")
        Calculo_VariasVariables = Materia(10014, "Calculo Varias Variables", Marcos, horario3, 4, Calculo_Integral, tipo.fundamentacion)
        horario4 = Horario([dias.martes, dias.jueves], "18", "20")
        Nelson = Profesor("Nelson", 13, "nelson@unal.edu.co")
        Fundamentos_Programacion = Materia(10015, "Fundamentos Programacion", Nelson, horario4, 3, tipo.disciplinar)
        horario5 = Horario([dias.martes, dias.jueves], "14", "16")
        Jaime = Profesor("Jaime", 14, "jaime@unal.edu.co")
        Programacion_Orientada_Objetos = Materia(10016, "Programacion Orientada Objetos", Jaime, horario5, 3, Fundamentos_Programacion, tipo.disciplinar)
        horario6 = Horario([dias.miercoles, dias.viernes], "8", "10")
        Julian = Profesor("Julian", 15, "julian@unal.edu.co")
        Estructura_Datos = Materia(10017, "Estructura Datos", Julian, horario6, 3, Programacion_Orientada_Objetos, tipo.disciplinar)
        horario7 = Horario([dias.lunes], "14", "16")
        Sierra = Profesor("Sierra", 16, "sierra@unal.edu.co")
        Catedra_Antioquia = Materia(10018, "Catedra Antioquia", Sierra, horario7, 3, tipo.libreEleccion)
        horario8 = Horario([dias.sabado], "8", "10")
        Catedra_Apun = Materia(10019, "Catedra Apun", Sierra, horario8, 3, tipo.libreEleccion)
        horario9 = Horario([dias.martes], "8", "10")
        Marisol = Profesor("Marisol", 17, "marisol@unal.edu.co")
        Catedra_Felicidad = Materia(10019, "Catedra Felicidad", Marisol, horario9, 3, tipo.libreEleccion)
        self.materias.append(Calculo_Diferencial)
        self.materias.append(Calculo_Integral)
        self.materias.append(Calculo_VariasVariables)
        self.materias.append(Fundamentos_Programacion)
        self.materias.append(Programacion_Orientada_Objetos)
        self.materias.append(Estructura_Datos)
        self.materias.append(Catedra_Antioquia)
        self.materias.append(Catedra_Apun)
        self.materias.append(Catedra_Felicidad)
        for i in range(len(self.materias)):
            profesor = self.materias[i].profesor
            if profesor not in self.profesores:
                self.profesores.append(profesor)
            profesor.asignarMateria(self.materias[i])
    
import pickle

class Beca:
    estudiantes = []
    estudiantesAptosInicial = []
    estudiantesAptosNormal = []
    estudiantesAptosAvanzada = []
    
    def __init__(self, nombre):
        self.nombre = nombre
    
    def getEstudiantes(self):
        return self.estudiantes
    
    def setEstudiantes(self, estudiantes):
        Beca.estudiantes = estudiantes
    
    def asignarEstudiantesBeca(self):
        estudiantesAptosInicial2 = []
        estudiantesAptosNormal2 = []
        estudiantesAptosAvanzada2 = []
        for estudiante in self.estudiantes:
            if estudiante.getPorcentajeDeAvance() >= 20 and estudiante.getPorcentajeDeAvance() < 40 and estudiante.calcularPromedio() >= 4.5 and estudiante.getFueBecado() == False:
                estudiantesAptosInicial2.append(estudiante)
            elif estudiante.getPorcentajeDeAvance() >= 40 and estudiante.getPorcentajeDeAvance() < 60 and estudiante.calcularPromedio() >= 4.0 and estudiante.getFueBecado() == False:
                estudiantesAptosNormal2.append(estudiante)
            elif estudiante.getPorcentajeDeAvance() >= 60 and estudiante.getPorcentajeDeAvance() < 100 and estudiante.calcularPromedio() >= 3.5 and estudiante.getFueBecado() == False:
                estudiantesAptosAvanzada2.append(estudiante)
        estudiantesAptosInicial2.sort(key=lambda x: x.calcularPromedio(), reverse=True)
        estudiantesAptosNormal2.sort(key=lambda x: x.calcularPromedio(), reverse=True)
        estudiantesAptosAvanzada2.sort(key=lambda x: x.calcularPromedio(), reverse=True)
        if len(estudiantesAptosInicial2) >= 2:
            for i in range(2):
                self.estudiantesAptosInicial.append(estudiantesAptosInicial2[i])
        elif len(estudiantesAptosInicial2) == 1:
            self.estudiantesAptosInicial.append(estudiantesAptosInicial2[0])
        if len(estudiantesAptosNormal2) >= 2:
            for i in range(2):
                self.estudiantesAptosNormal.append(estudiantesAptosNormal2[i])
        elif len(estudiantesAptosNormal2) == 1:
            self.estudiantesAptosNormal.append(estudiantesAptosNormal2[0])
        if len(estudiantesAptosAvanzada2) >= 2:
            for i in range(2):
                self.estudiantesAptosAvanzada.append(estudiantesAptosAvanzada2[i])
        elif len(estudiantesAptosAvanzada2) == 1:
            self.estudiantesAptosAvanzada.append(estudiantesAptosAvanzada2[0])
    
    def getEstudiantesAptosInicial(self):
        return self.estudiantesAptosInicial
    
    def getEstudiantesAptosNormal(self):
        return self.estudiantesAptosNormal
    
    def getEstudiantesAptosAvanzada(self):
        return self.estudiantesAptosAvanzada

from typing import List

from personas.Persona import Persona
from personas.Profesor import Profesor
from Calendario.Materia import Materia
from Calendario.Tarea import Tarea
from Calendario.Horario import Horario

class Estudiante(Persona):
    def __init__(self, nombre: str, ID: int, email: str, fue_becado: bool, materias_cursadas: List['Materia'] = None):
        super().__init__(nombre, ID, email)
        self.__falla_horario = False
        self.__calificacion_asignada = False
        self.__fue_becado = fue_becado
        self.promedio = 0.0
        self.__materias_inscritas = []
        self.materias_cursadas = materias_cursadas
        self.porcentaje_avance = 0.0
        self.creditos_inscritos = 0
        self.intento_materias = []
        self.__profesores_inscritos = []
        self.materias_seleccionadas = []
        self.__profesores_calificados = []

    def getProfesores_calificados(self):
        return self.__profesores_calificados

    def addProfesor_calificado(self, profesor):
        self.__profesores_calificados.append(profesor)

    def getProfesores_inscritos(self):
        return self.__profesores_inscritos

    def setProfesores_inscritos(self, profesor):
        self.__profesores_inscritos = profesor

    def getMaterias_inscritas(self):
        return self.__materias_inscritas

    def setMaterias_inscritas(self, materias_inscritas):
        self.__materias_inscritas = materias_inscritas

    def getFalla_horario(self):
        return self.__falla_horario

    def setFalla_horario(self, falla_horario):
        self.__falla_horario = falla_horario

    def getFue_becado(self):
        return self.__fue_becado

    def setFue_becado(self, fue_becado):
        self.__fue_becado = fue_becado

    def getPorcentaje_de_avance(self):
        return self.porcentaje_de_avance

    def setPorcentaje_de_avance(self, porcentaje_de_avance):
        self.porcentaje_de_avance = porcentaje_de_avance

    def getMaterias_cursadas(self):
        return self.materias_cursadas

    def setMaterias_cursadas(self, materias_cursadas):
        self.materias_cursadas = materias_cursadas

    def getCalificacion_asignada(self):
        return self.__calificacion_asignada

    def setCalificacion_asignada(self, calificacion_asignada):
        self.__calificacion_asignada = calificacion_asignada

    def getCreditos_inscritos(self):
        return self.creditos_inscritos

    def setCreditos_inscritos(self, creditos_inscritos):
        self.creditos_inscritos = creditos_inscritos



    def inscribir_materia(self, nombre_materia: str, materias_disponibles: List['Materia']):
        from Calendario.Materia import Materia

        tiene_fundamentacion = False
        fallo_prerrequisito = False
        intento_creditos = 0

        for materia in materias_disponibles:
            if materia.getNombre() == nombre_materia:
                if materia in self.__materias_inscritas:
                    return False
                prerrequisito = materia.getPrerrequisito()
                tiene_prerrequisito = False
                if prerrequisito is not None:
                    for materia_cursada in self.materias_cursadas:
                        if materia_cursada.getNombre() == prerrequisito.getNombre():
                            tiene_prerrequisito = True
                            break
                if prerrequisito is None or tiene_prerrequisito:
                    self.__materias_inscritas.append(materia)
                    break
                else:
                    fallo_prerrequisito = True

        for m in self.__materias_inscritas:
            intento_creditos += m.getCreditos()
            if m.tipo == Materia.Tipo.FUNDAMENTACION:
                tiene_fundamentacion = True

        if intento_creditos >= 10 and tiene_fundamentacion:
            for ma in self.__materias_inscritas:
                self.__profesores_inscritos.append(ma.getProfesor())
                ma.inscribir_estudiante(self)
            return True

        return not fallo_prerrequisito

    def agregar_promedio(self, calificacion: float):
        if self.getCalificacion_asignada():
            self.promedio = self.promedio * len(self.materias_cursadas)
            self.promedio += calificacion
            self.promedio = self.promedio / (len(self.materias_cursadas) + 1)
        else:
            self.setCalificacion_asignada(True)
            self.promedio = calificacion

    def mostrar_inscribir_asignaturas(self, materias_disponibles: List['Materia']):
        print("Materias disponibles:")
        for materia in materias_disponibles:
            print(materia.getNombre())

    def seleccionar_materia(self, materia):
        self.materias_seleccionadas.append(materia)

    def mostrar_materias_inscritas(self):
        print("Materias inscritas:")
        for materia in self.materias_seleccionadas:
            print(materia.getNombre())

    def retirar_materia(self, materia):
        self.materias_inscritas.remove(materia)

    def aplicar_beca(self):
        from Calendario.Beca import Beca
        Beca.estudiantes.append(self)

    def calcular_promedio(self):
        final_score = 0.0
        num_materias = len(self.__materias_inscritas)
        for materia in self.__materias_inscritas:
            materia_score = 0.0
            num_tareas = len(materia.getTareas_de_materia())
            for tarea in materia.getTareas_de_materia():
                materia_score += tarea.get_grade(self)
            if num_tareas > 0:
                materia_score /= num_tareas
            final_score += materia_score
        if num_materias > 0:
            final_score /= num_materias
        return round(final_score * 100.0) / 100.0


    def comparar_horario(self, materias_inscritas):
        materias_error = []
        self.falla_horario = False

        for i in range(len(materias_inscritas)):
            horario = materias_inscritas[i].getHorario()
            hora1 = horario.getHora_inicio()
            hora2 = horario.getHora_fin()
            dia1 = horario.getDia()

            for j in range(i + 1, len(materias_inscritas)):
                horario2 = materias_inscritas[j].getHorario()
                hora3 = horario2.getHora_inicio()
                hora4 = horario2.getHora_fin()
                dia2 = horario2.getDia()

                for k in range(len(dia1)):
                    dia11 = dia1[k]
                    for h in range(len(dia2)):
                        dia22 = dia2[h]
                        if dia11 == dia22 and materias_inscritas[i] not in materias_error:
                            if hora1 == hora3 or hora2 == hora4:
                                self.falla_horario = True
                                materias_error.append(materias_inscritas[i])
                                materias_error.append(materias_inscritas[j])
        
        return self.falla_horario

    def sugerir_materias(self, materias_disponibles: List['Materia']):
        materias_recomendadas = []

        # Get the names of the completed subjects
        materias_cursadas_nombres = [materia.getNombre() for materia in self.materias_cursadas]

        # Prioritize fundamentacion and disciplinar subjects
        for materia in materias_disponibles:
            if materia.tipo == Materia.Tipo.FUNDAMENTACION or materia.tipo == Materia.Tipo.DISCIPLINAR:
                # Check if the student has not completed the subject yet
                if materia.getNombre() not in materias_cursadas_nombres:
                    # Check if the student has completed the prerequisite subject
                    if materia.getPrerrequisito() is None or materia.getPrerrequisito().getNombre() in materias_cursadas_nombres:
                        # Check for schedule collision
                        if not self.comparar_horario(materias_recomendadas + [materia]):
                            materias_recomendadas.append(materia)
                            self.__profesores_inscritos.append(materia.getProfesor())
                            materia.inscribir_estudiante(self)

        # If no fundamentacion or disciplinar subjects are available or can be taken, consider libreEleccion subjects
        for materia in materias_disponibles:
            if materia.tipo == Materia.Tipo.LIBRE_ELECCION:
                # Check if the student has not completed the subject yet
                if materia.getNombre() not in materias_cursadas_nombres:
                    # Check for schedule collision
                    if not self.comparar_horario(materias_recomendadas + [materia]):
                        materias_recomendadas.append(materia)
                        self.__profesores_inscritos.append(materia.getProfesor())
                        materia.inscribir_estudiante(self)

        self.__materias_inscritas = materias_recomendadas

    def sugerir_materias(self, materias_disponibles: List['Materia']):
        materias_recomendadas = []

        # Get the names of the completed subjects
        materias_cursadas_nombres = [materia.getNombre() for materia in self.materias_cursadas]

        # Prioritize fundamentacion and disciplinar subjects
        for materia in materias_disponibles:
            if materia.tipo == Materia.Tipo.FUNDAMENTACION or materia.tipo == Materia.Tipo.DISCIPLINAR:
                # Check if the student has not completed the subject yet
                if materia.getNombre() not in materias_cursadas_nombres:
                    # Check if the student has completed the prerequisite subject
                    if materia.getPrerrequisito() is None or materia.getPrerrequisito().getNombre() in materias_cursadas_nombres:
                        # Check for schedule collision
                        if not self.comparar_horario(materias_recomendadas + [materia]):
                            materias_recomendadas.append(materia)
                            self.__profesores_inscritos.append(materia.getProfesor())
                            materia.inscribir_estudiante(self)

        # If no fundamentacion or disciplinar subjects are available or can be taken, consider libreEleccion subjects
        for materia in materias_disponibles:
            if materia.tipo == Materia.Tipo.LIBRE_ELECCION:
                # Check if the student has not completed the subject yet
                if materia.getNombre() not in materias_cursadas_nombres:
                    # Check for schedule collision
                    if not self.comparar_horario(materias_recomendadas + [materia]):
                        materias_recomendadas.append(materia)
                        self.__profesores_inscritos.append(materia.getProfesor())
                        materia.inscribir_estudiante(self)

        self.__materias_inscritas = materias_recomendadas

    def calcular_porcentaje_avance(self):
        self.porcentaje_avance = (1.0/9) * len(self.materias_cursadas)
        self.porcentaje_de_avance = round(self.porcentaje_avance * 100.0)

    
    def __str__(self):
        return f'Estudiante: {self.getNombre()}'  
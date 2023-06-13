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
        self.intento_materias = []
        self.__profesores_inscritos = []

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
        return self.__porcentaje_de_avance

    def setPorcentaje_de_avance(self, porcentaje_de_avance):
        self.__porcentaje_de_avance = porcentaje_de_avance

    def getMaterias_cursadas(self):
        return self.__materias_cursadas

    def setMaterias_cursadas(self, materias_cursadas):
        self.__materias_cursadas = materias_cursadas

    def getCalificacion_asignada(self):
        return self.__calificacion_asignada

    def setCalificacion_asignada(self, calificacion_asignada):
        self.__calificacion_asignada = calificacion_asignada

    def getCreditos_inscritos(self):
        return self.__creditos_inscritos

    def setCreditos_inscritos(self, creditos_inscritos):
        self.__creditos_inscritos = creditos_inscritos


    def inscribir_materia(self, nombre_materia: str, materias_disponibles):
        from Calendario.Materia import Materia
        
        tiene_fundamentacion = False
        fallo_prerrequisito = False
        intento_creditos = 0

        for materia in materias_disponibles:
            if Materia(materia).getNombre() == nombre_materia:
                if materia in self.materias_inscritas:
                    return False
                prerrequisito = Materia(materia).prerrequisito
                tiene_prerrequisito = False
                if prerrequisito is not None:
                    for materia_cursada in self.materias_cursadas:
                        if Materia(materia_cursada).getNombre() == Materia(prerrequisito).getNombre():
                            tiene_prerrequisito = True
                            break
                if prerrequisito is None or tiene_prerrequisito:
                    self.intento_materias.append(materia)
                    break
                else:
                    fallo_prerrequisito = True

        for m in self.intento_materias:
            intento_creditos += Materia(m).getCreditos()
            if Materia(m).tipo == Materia.Tipo.FUNDAMENTACION:
                tiene_fundamentacion = True

        if intento_creditos >= 6 and tiene_fundamentacion:
            for ma in self.intento_materias:
                self.__profesores_inscritos.append(Materia(ma).getProfesor())
                Materia(ma).inscribir_estudiante(self)
            self.materias_inscritas = self.intento_materias
            self.creditos_inscritos = intento_creditos

        return not fallo_prerrequisito

    def retirar_materia(self, materia):
        self.materias_inscritas.remove(materia)

    def aplicar_beca(self, estudiante):
        from Calendario.Beca import Beca
        Beca.estudiantes.append(self)

    def calcular_promedio(self):
        final_score = 0.0
        num_materias = len(self.materias_inscritas)
        for materia in self.materias_inscritas:
            materia_score = 0.0
            num_tareas = len(Materia(materia).__tareas_de_materia)
            for tarea in Materia(materia).__tareas_de_materia:
                materia_score += Tarea(tarea).get_grade(self)
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
            horario = Materia(materias_inscritas[i]).getHorario()
            hora1 = Horario(horario).getHora_inicio()
            hora2 = Horario(horario).getHora_fin()
            dia1 = Horario(horario).getDia()

            for j in range(i + 1, len(materias_inscritas)):
                horario2 = Materia(materias_inscritas[j]).getHorario()
                hora3 = Horario(horario2).getHora_inicio()
                hora4 = Horario(horario2).getHora_fin()
                dia2 = Horario(horario2).getDia()

                for k in range(len(dia1)):
                    dia11 = dia1[k]
                    for h in range(len(dia2)):
                        dia22= dia2[h]
                        if dia11 == dia22 and materias_inscritas[i] not in materias_error:
                            if hora1 == hora3 or hora2 == hora4:
                                self.falla_horario=True 
                                materias_error.append(materias_inscritas[i])
                                materias_error.append(materias_inscritas[j])
        return self.falla_horario
    
    def sugerir_horario(self, falla_horario):
        materias_sugeridas = []
        if falla_horario:
            for materia in self.materias_inscritas:
                conflicto = False
                for materia_sugerida in materias_sugeridas:

                    dias_materia = Materia(materia).getHorario().getDia()
                    dias_materia_sugerida = Materia(materia_sugerida).getHorario().getDia()
                    fallo_dias = False
                    for dia_materia in dias_materia:
                        if dia_materia in dias_materia_sugerida:
                            fallo_dias = True
                            break

                    if fallo_dias:
                        hora_inicio_materia = int(Materia(materia).getHorario().getHora_inicio())
                        hora_fin_materia = int(Materia(materia).getHorario().getHora_fin())
                        hora_inicio_materia_sugerida = int(Materia(materia_sugerida).getHorario().getHora_inicio())
                        hora_fin_materia_sugerida = int(Materia(materia_sugerida).getHorario().getHora_fin())

                        if hora_inicio_materia < hora_fin_materia_sugerida and hora_fin_materia > hora_inicio_materia_sugerida:
                            conflicto = True
                            break

                if not conflicto:
                    materias_sugeridas.append(materia)

            self.materias_inscritas = materias_sugeridas

    def sugerir_materias(self, materias_disponibles: List['Materia']):
        
        materias_recomendadas = []
        for materia in self.materias_cursadas:

            if materia.getNombre == materias_disponibles[0].getNombre and materia not in self.materias_cursadas:
                materias_recomendadas.append(materias_disponibles[0])
                self.__profesores_inscritos.append(materias_disponibles[0].getProfesor)
                materias_disponibles[0].inscribir_estudiante(self)

            elif materia.getNombre == materias_disponibles[0].getNombre and materia not in self.materias_cursadas:
                materias_recomendadas.append(materias_disponibles[1])
                self.__profesores_inscritos.append(materias_disponibles[1].getProfesor)
                materias_disponibles[1].inscribir_estudiante(self)

            elif materia.getNombre == materias_disponibles[1].getNombre and materia not in self.materias_cursadas:
                materias_recomendadas.append(materias_disponibles[2])
                self.__profesores_inscritos.append(materias_disponibles[2].getProfesor)
                materias_disponibles[2].inscribir_estudiante(self)

            if materia.getNombre == materias_disponibles[3].getNombre and materia not in self.materias_cursadas:
                materias_recomendadas.append(materias_disponibles[3])
                self.__profesores_inscritos.append(materias_disponibles[3].getProfesor)
                materias_disponibles[3].inscribir_estudiante(self)
                if self.comparar_horario(materias_recomendadas):
                    materias_recomendadas.remove(materias_disponibles[3])
                    self.__profesores_inscritos.remove(materias_disponibles[3].getProfesor)
                    materias_disponibles.pop(3).inscribir_estudiante(self)

            elif materia.getNombre == materias_disponibles[3].getNombre and materia not in self.materias_cursadas:
                materias_recomendadas.append(materias_disponibles[4])
                self.__profesores_inscritos.append(materias_disponibles[4].getProfesor)
                materias_disponibles[4].inscribir_estudiante(self)
                if self.comparar_horario(materias_recomendadas):
                    materias_recomendadas.remove(materias_disponibles[4])
                    self.__profesores_inscritos.remove(materias_disponibles[4].getProfesor)
                    materias_disponibles.pop(4).inscribir_estudiante(self)

            elif materia.getNombre == materias_disponibles[4].getNombre and materia not in self.materias_cursadas:
                materias_recomendadas.append(materias_disponibles[5])
                self.__profesores_inscritos.append(materias_disponibles[5].getProfesor)
                materias_disponibles[5].inscribir_estudiante(self)
                if self.comparar_horario(materias_recomendadas):
                    materias_recomendadas.remove(materias_disponibles[5])
                    self.__profesores_inscritos.remove(materias_disponibles[5].getProfesor)
                    materias_disponibles.pop(5).inscribir_estudiante(self)

        for i in range(6, 9):
            materias_recomendadas.append(materias_disponibles[i])
            self.__profesores_inscritos.append(materias_disponibles[i].getProfesor)
            materias_disponibles[i].inscribir_estudiante(self)
            if self.comparar_horario(materias_recomendadas):
                materias_recomendadas.remove(materias_disponibles[i])
                self.__profesores_inscritos.remove(materias_disponibles[i].getProfesor)
                materias_disponibles.pop(i).inscribir_estudiante(self)

        self.materias_inscritas = materias_recomendadas

    def calcular_porcentaje_avance(self):
        porcentaje_avance = (1.0 / 9) * len(self.materias_cursadas)
        self.porcentaje_de_avance = round(porcentaje_avance * 100.0)

    
    def __str__(self):
        return f'Estudiante: {self.getNombre}'  
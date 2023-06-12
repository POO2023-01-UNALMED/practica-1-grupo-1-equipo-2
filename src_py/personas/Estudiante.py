from typing import List

from personas.Persona import Persona
from personas.Profesor import Profesor
from Calendario.Materia import Materia
from Calendario.Beca import Beca

class Estudiante(Persona):
    def __init__(self, nombre: str, ID: int, email: str, fue_becado: bool, materias_cursadas: List['Materia']):
        super().__init__(nombre, ID, email)
        self.falla_horario = False
        self.calificacion_asignada = False
        self.fue_becado = fue_becado
        self.promedio = 0.0
        self.materias_inscritas = []
        self.materias_cursadas = materias_cursadas
        self.intento_materias = []
        self.profesores_inscritos = []

    def __init__(self, nombre: str, ID: int, email: str, fue_becado: bool):
        super().__init__(nombre, ID, email)
        self.falla_horario = False
        self.fue_becado = fue_becado
        self.promedio = 0.0
        self.materias_inscritas = []
        self.materias_cursadas = []
        self.intento_materias = []
        self.profesores_inscritos = []

    @property
    def profesores_inscritos(self) -> List['Profesor']:
        return self.__profesores_inscritos

    @profesores_inscritos.setter
    def profesores_inscritos(self, profesor: List['Profesor']):
        self.__profesores_inscritos = profesor

    @property
    def materias_inscritas(self) -> List['Materia']:
        return self.__materias_inscritas

    @materias_inscritas.setter
    def materias_inscritas(self, materias_inscritas: List['Materia']):
        self.__materias_inscritas = materias_inscritas

    @property
    def falla_horario(self) -> bool:
        return self.__falla_horario

    @falla_horario.setter
    def falla_horario(self, falla_horario: bool):
        self.__falla_horario = falla_horario

    @property
    def fue_becado(self) -> bool:
        return self.__fue_becado

    @fue_becado.setter
    def fue_becado(self, fue_becado: bool):
        self.__fue_becado = fue_becado

    @property
    def porcentaje_de_avance(self) -> float:
        return self.__porcentaje_de_avance

    @porcentaje_de_avance.setter
    def porcentaje_de_avance(self, porcentaje_de_avance: float):
        self.__porcentaje_de_avance = porcentaje_de_avance

    @property
    def materias_cursadas(self) -> List['Materia']:
        return self.__materias_cursadas

    @materias_cursadas.setter
    def materias_cursadas(self, materias_cursadas: List['Materia']):
        self.__materias_cursadas = materias_cursadas

    @property
    def calificacion_asignada(self) -> bool:
        return self.__calificacion_asignada

    @calificacion_asignada.setter
    def calificacion_asignada(self, calificacion_asignada: bool):
        self.__calificacion_asignada = calificacion_asignada

    @property
    def creditos_inscritos(self) -> int:
        return self.__creditos_inscritos

    @creditos_inscritos.setter
    def creditos_inscritos(self, creditos_inscritos: int):
        self.__creditos_inscritos = creditos_inscritos


    def inscribir_materia(self, nombre_materia: str, materias_disponibles: List['Materia']) -> bool:
        from Calendario.Materia import Materia
        
        tiene_fundamentacion = False
        fallo_prerrequisito = False
        intento_creditos = 0

        for materia in materias_disponibles:
            if materia.nombre == nombre_materia:
                if materia in self.materias_inscritas:
                    return False
                prerrequisito = materia.prerrequisito
                tiene_prerrequisito = False
                if prerrequisito is not None:
                    for materia_cursada in self.materias_cursadas:
                        if materia_cursada.nombre == prerrequisito.nombre:
                            tiene_prerrequisito = True
                            break
                if prerrequisito is None or tiene_prerrequisito:
                    self.intento_materias.append(materia)
                    break
                else:
                    fallo_prerrequisito = True

        for m in self.intento_materias:
            intento_creditos += m.creditos
            if m.tipo == Materia.Tipo.FUNDAMENTACION:
                tiene_fundamentacion = True

        if intento_creditos >= 6 and tiene_fundamentacion:
            for ma in self.intento_materias:
                self.profesores_inscritos.append(ma.profesor)
                ma.inscribir_estudiante(self)
            self.materias_inscritas = self.intento_materias
            self.creditos_inscritos = intento_creditos

        return not fallo_prerrequisito

    def retirar_materia(self, materia: 'Materia'):
        self.materias_inscritas.remove(materia)

    def aplicar_beca(self, estudiante: 'Estudiante'):
        from Calendario.Beca import Beca
        Beca.estudiantes.append(self)

    def calcular_promedio(self) -> float:
        from Calendario.Materia import Materia
        final_score = 0.0
        num_materias = len(self.materias_inscritas)
        for materia in self.materias_inscritas:
            materia_score = 0.0
            num_tareas = len(materia.tareas_de_materia)
            for tarea in materia.tareas_de_materia:
                materia_score += tarea.get_grade(self)
            if num_tareas > 0:
                materia_score /= num_tareas
            final_score += materia_score
        if num_materias > 0:
            final_score /= num_materias
        return round(final_score * 100.0) / 100.0

    def comparar_horario(self, materias_inscritas: List['Materia']) -> bool:
        from Calendario.Materia import Materia
        from Calendario.Horario import Horario
        materias_error = []
        self.falla_horario = False
        for i in range(len(materias_inscritas)):
            horario = materias_inscritas[i].horario
            hora1 = horario.hora_inicio
            hora2 = horario.hora_fin
            dia1 = horario.dia

            for j in range(i + 1, len(materias_inscritas)):
                horario2 = materias_inscritas[j].horario
                hora3 = horario2.hora_inicio
                hora4 = horario2.hora_fin
                dia2 = horario2.dia

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
    
    def sugerir_horario(self, falla_horario: bool):
        from Calendario.Materia import Materia
        materias_sugeridas = []
        if falla_horario:
            for materia in self.materias_inscritas:
                conflicto = False
                for materia_sugerida in materias_sugeridas:

                    dias_materia = materia.horario.dia
                    dias_materia_sugerida = materia_sugerida.horario.dia
                    fallo_dias = False
                    for dia_materia in dias_materia:
                        if dia_materia in dias_materia_sugerida:
                            fallo_dias = True
                            break

                    if fallo_dias:
                        hora_inicio_materia = int(materia.horario.hora_inicio)
                        hora_fin_materia = int(materia.horario.hora_fin)
                        hora_inicio_materia_sugerida = int(materia_sugerida.horario.hora_inicio)
                        hora_fin_materia_sugerida = int(materia_sugerida.horario.hora_fin)

                        if hora_inicio_materia < hora_fin_materia_sugerida and hora_fin_materia > hora_inicio_materia_sugerida:
                            conflicto = True
                            break

                if not conflicto:
                    materias_sugeridas.append(materia)

            self.materias_inscritas = materias_sugeridas

    def sugerir_materias(self, materias_disponibles: List['Materia']):
        
        materias_recomendadas = []
        for materia in self.materias_cursadas:

            if materia.nombre == materias_disponibles[0].nombre and materia not in self.materias_cursadas:
                materias_recomendadas.append(materias_disponibles[0])
                self.profesores_inscritos.append(materias_disponibles[0].profesor)
                materias_disponibles[0].inscribir_estudiante(self)

            elif materia.nombre == materias_disponibles[0].nombre and materia not in self.materias_cursadas:
                materias_recomendadas.append(materias_disponibles[1])
                self.profesores_inscritos.append(materias_disponibles[1].profesor)
                materias_disponibles[1].inscribir_estudiante(self)

            elif materia.nombre == materias_disponibles[1].nombre and materia not in self.materias_cursadas:
                materias_recomendadas.append(materias_disponibles[2])
                self.profesores_inscritos.append(materias_disponibles[2].profesor)
                materias_disponibles[2].inscribir_estudiante(self)

            if materia.nombre == materias_disponibles[3].nombre and materia not in self.materias_cursadas:
                materias_recomendadas.append(materias_disponibles[3])
                self.profesores_inscritos.append(materias_disponibles[3].profesor)
                materias_disponibles[3].inscribir_estudiante(self)
                if self.comparar_horario(materias_recomendadas):
                    materias_recomendadas.remove(materias_disponibles[3])
                    self.profesores_inscritos.remove(materias_disponibles[3].profesor)
                    materias_disponibles.remove(3).inscribir_estudiante(self)

            elif materia.nombre == materias_disponibles[3].nombre and materia not in self.materias_cursadas:
                materias_recomendadas.append(materias_disponibles[4])
                self.profesores_inscritos.append(materias_disponibles[4].profesor)
                materias_disponibles[4].inscribir_estudiante(self)
                if self.comparar_horario(materias_recomendadas):
                    materias_recomendadas.remove(materias_disponibles[4])
                    self.profesores_inscritos.remove(materias_disponibles[4].profesor)
                    materias_disponibles.remove(4).inscribir_estudiante(self)

            elif materia.nombre == materias_disponibles[4].nombre and materia not in self.materias_cursadas:
                materias_recomendadas.append(materias_disponibles[5])
                self.profesores_inscritos.append(materias_disponibles[5].profesor)
                materias_disponibles[5].inscribir_estudiante(self)
                if self.comparar_horario(materias_recomendadas):
                    materias_recomendadas.remove(materias_disponibles[5])
                    self.profesores_inscritos.remove(materias_disponibles[5].profesor)
                    materias_disponibles.remove(5).inscribir_estudiante(self)

        for i in range(6, 9):
            materias_recomendadas.append(materias_disponibles[i])
            self.profesores_inscritos.append(materias_disponibles[i].profesor)
            materias_disponibles[i].inscribir_estudiante(self)
            if self.comparar_horario(materias_recomendadas):
                materias_recomendadas.remove(materias_disponibles[i])
                self.profesores_inscritos.remove(materias_disponibles[i].profesor)
                materias_disponibles.remove(i).inscribir_estudiante(self)

        self.materias_inscritas = materias_recomendadas

    def calcular_porcentaje_avance(self):
        porcentaje_avance = (1.0 / 9) * len(self.materias_cursadas)
        self.porcentaje_de_avance = round(porcentaje_avance * 100.0)

    
    def __str__(self) -> str:
        return f'Estudiante: {self.nombre}'  
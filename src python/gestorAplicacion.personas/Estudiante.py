from typing import List
from gestorAplicacion.Calendario import Horario, Materia
from gestorAplicacion.Personas.Persona import Persona
import pickle

class Estudiante(Persona):
    def __init__(self, nombre: str, ID: int, Email: str, fueBecado: bool, materias_cursadas: List[Materia]):
        super().__init__(nombre, ID, Email)
        self.promedio = 0.0
        self.calificacionAsignada = False
        self.fueBecado = fueBecado
        self.materias_inscritas = []
        self.porcentajeDeAvance = 0.0
        self.fallaHorario = False
        self.materias_cursadas = materias_cursadas
        self.creditosInscritos = 0
        self.intentoMaterias = []
        self.profesoreInscritos = []

    def __init__(self, nombre, ID, Email, fueBecado):
        super().__init__(nombre, ID, Email)
        self.fallaHorario = False
        self.fueBecado = fueBecado
        self.promedio = 0.0
        self.materias_inscritas = []
        self.materias_cursadas = []
        self.intentoMaterias = []
        self.profesoreInscritos = []

    def setProfesoresInscritos(profesor):
        global profesoreInscritos
        profesoreInscritos = profesor

    def getProfesoresInscritos():
        return profesoreInscritos

    def getMaterias_Inscritas():
        return materias_inscritas

    def setMaterias_Inscritas(materiasInscritas):
        global materias_inscritas
        materias_inscritas = materiasInscritas

    def setfallaHorario(fallaHorario):
        global fallaHorario
        fallaHorario = fallaHorario

    def getfallaHorario():
        return fallaHorario

    def getFueBecado():
        return fueBecado

    def setFueBecado(fueBecado):
        global fueBecado
        fueBecado = fueBecado

    def getPorcentajeDeAvance():
        return porcentajeDeAvance

    def setPorcentajeDeAvance(PorcentajeDeAvance):
        global porcentajeDeAvance
        porcentajeDeAvance = PorcentajeDeAvance

    def getMateriasCursadas():
        return materias_cursadas

    def setMateriasCursadas(materias_cursadas):
        global materias_cursadas
        materias_cursadas = materias_cursadas

    def getCalificacionAsignada():
        return calificacionAsignada

    def setCalificacionAsignada(calificacionAsignada):
        global calificacionAsignada
        calificacionAsignada = calificacionAsignada

    def setCreditosInscritos(creditosInscritos):
        global creditosInscritos
        creditosInscritos = creditosInscritos

    def getCreditosInscritos():
        return creditosInscritos

    def inscribirMateria(nombreMateria, materiasDisponibles):
        global materias_inscritas, profesoreInscritos
        tieneFundamentacion = False
        falloPrerrequsito = False
        intentoCreditos = 0
        intentoMaterias = []
        for materia in materiasDisponibles:
            if materia.getNombre() == nombreMateria:
                if materia in materias_inscritas:
                    return False
                prerrequisito = materia.getPrerrequisito()
                tienePrerrequisito = False
                if prerrequisito != None:
                    for materiaCursada in materias_cursadas:
                        if materiaCursada.getNombre() == prerrequisito.getNombre():
                            tienePrerrequisito = True
                            break
                if prerrequisito == None or tienePrerrequisito:
                    intentoMaterias.append(materia)
                    break
                else:
                    falloPrerrequsito = True
        for m in intentoMaterias:
            intentoCreditos += m.getCreditos()
            if m.getTipo() == tipo.fundamentacion:
                tieneFundamentacion = True
        if intentoCreditos >= 6 and tieneFundamentacion:
            for ma in intentoMaterias:
                profesoreInscritos.append(ma.getProfesor())
                ma.inscribirEstudiante(this)
            setMaterias_Inscritas(intentoMaterias)
            setCreditosInscritos(intentoCreditos)
        return not falloPrerrequsito

    def retirarMateria(Materia):
        global materias_inscritas
        materias_inscritas.remove(Materia)

    def aplicarBeca(estudiante):
        Beca.estudiantes.append(this)

    def calcularPromedio():
        finalScore = 0.0
        numMaterias = len(materias_inscritas)
        for materia in materias_inscritas:
            materiaScore = 0.0
            numTareas = len(materia.getTareasDeMateria())
            for tarea in materia.getTareasDeMateria():
                materiaScore += tarea.getGrade(this)
            if numTareas > 0:
                materiaScore /= numTareas
            finalScore += materiaScore
        if numMaterias > 0:
            finalScore /= numMaterias
        return round(finalScore * 100.0) / 100.0

    def compararHorario(materias_inscritas):
        MateriasError = []
        fallaHorario = False
        for i in range(len(materias_inscritas)):
            horario = materias_inscritas[i].getHorario()
            hora1 = horario.getHora_inicio()
            hora2 = horario.getHora_Fin()
            dia1 = horario.getDia()
            for j in range(i + 1, len(materias_inscritas)):
                horario2 = materias_inscritas[j].getHorario()
                hora3 = horario2.getHora_inicio()
                hora4 = horario2.getHora_Fin()
                dia2 = horario2.getDia()
                for k in range(len(dia1)):
                    dia11 = dia1[k]
                    for h in range(len(dia2)):
                        dia22 = dia2[h]
                        if dia11 == dia22 and materias_inscritas[i] not in MateriasError:
                            if hora1 == hora3 or hora2 == hora4:
                                fallaHorario = True
                                MateriasError.append(materias_inscritas[i])
                                MateriasError.append(materias_inscritas[j])
        return fallaHorario

    def sugerirHorario(fallaHorario):
        materiasSugeridas = []
        if fallaHorario:
            for materia in materias_inscritas:
                conflicto = False
                for materiaSugerida in materiasSugeridas:
                    diasMateria = materia.getHorario().getDia()
                    diasMateriaSugerida = materiaSugerida.getHorario().getDia()
                    falloDias = False
                    for diaMateria in diasMateria:
                        if diaMateria in diasMateriaSugerida:
                            falloDias = True
                            break
                    if falloDias and (materia.getHorario().getHora_inicio() == materiaSugerida.getHorario().getHora_inicio() or materia.getHorario().getHora_Fin() == materiaSugerida.getHorario().getHora_Fin()):
                        conflicto = True
                        break
                if not conflicto:
                    materiasSugeridas.append(materia)
            materias_inscritas = materiasSugeridas

    def sugerirMaterias(materiasDisponibles):
        materiasRecomendadas = []
        for materia in materias_cursadas:
            if materia.getNombre().lower() == materiasDisponibles[0].getNombre().lower() and materiasDisponibles[0] not in materias_cursadas:
                materiasRecomendadas.append(materiasDisponibles[0])
                profesoreInscritos.append(materiasDisponibles[0].getProfesor())
                materiasDisponibles[0].inscribirEstudiante(self)
            elif materia.getNombre().lower() == materiasDisponibles[0].getNombre().lower() and materiasDisponibles[1] not in materias_cursadas:
                materiasRecomendadas.append(materiasDisponibles[1])
                profesoreInscritos.append(materiasDisponibles[1].getProfesor())
                materiasDisponibles[1].inscribirEstudiante(self)
            elif materia.getNombre().lower() == materiasDisponibles[1].getNombre().lower() and materiasDisponibles[2] not in materias_cursadas:
                materiasRecomendadas.append(materiasDisponibles[2])
                profesoreInscritos.append(materiasDisponibles[2].getProfesor())
                materiasDisponibles[2].inscribirEstudiante(self)
            if materia.getNombre().lower() == materiasDisponibles[3].getNombre().lower() and materiasDisponibles[3] not in materias_cursadas:
                materiasRecomendadas.append(materiasDisponibles[3])
                profesoreInscritos.append(materiasDisponibles[3].getProfesor())
                materiasDisponibles[3].inscribirEstudiante(self)
                if compararHorario(materiasRecomendadas):
                    materiasRecomendadas.remove(materiasDisponibles[3])
                    profesoreInscritos.remove(materiasDisponibles[3].getProfesor())
                    materiasDisponibles[3].inscribirEstudiante(self)
            elif materia.getNombre().lower() == materiasDisponibles[3].getNombre().lower() and materiasDisponibles[4] not in materias_cursadas:
                materiasRecomendadas.append(materiasDisponibles[4])
                profesoreInscritos.append(materiasDisponibles[4].getProfesor())
                materiasDisponibles[4].inscribirEstudiante(self)
                if compararHorario(materiasRecomendadas):
                    materiasRecomendadas.remove(materiasDisponibles[4])
                    profesoreInscritos.remove(materiasDisponibles[4].getProfesor())
                    materiasDisponibles[4].inscribirEstudiante(self)
            elif materia.getNombre().lower() == materiasDisponibles[4].getNombre().lower() and materiasDisponibles[5] not in materias_cursadas:
                materiasRecomendadas.append(materiasDisponibles[5])
                profesoreInscritos.append(materiasDisponibles[5].getProfesor())
                materiasDisponibles[5].inscribirEstudiante(self)
                if compararHorario(materiasRecomendadas):
                    materiasRecomendadas.remove(materiasDisponibles[5])
                    profesoreInscritos.remove(materiasDisponibles[5].getProfesor())
                    materiasDisponibles[5].inscribirEstudiante(self)
        for i in range(6, 9):
            materiasRecomendadas.append(materiasDisponibles[i])
            profesoreInscritos.append(materiasDisponibles[i].getProfesor())
            materiasDisponibles[i].inscribirEstudiante(self)
            if compararHorario(materiasRecomendadas):
                materiasRecomendadas.remove(materiasDisponibles[i])
                profesoreInscritos.remove(materiasDisponibles[i].getProfesor())
                materiasDisponibles[i].inscribirEstudiante(self)
        self.materias_inscritas = materiasRecomendadas

    def __str__():
        return "Estudiante: " + getNombre()

    def calcularPorcentajeAvance():
        porcentajeAvance = (1.0/9)*len(materias_cursadas)
        setPorcentajeDeAvance(round(porcentajeAvance * 100.0))

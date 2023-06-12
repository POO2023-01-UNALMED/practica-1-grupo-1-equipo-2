from personas.Estudiante import Estudiante
from Calendario.Facultad import Facultad
from Calendario.Beca import Beca
from Calendario.Tarea import Tarea



if __name__ == "__main__":
    Minas = Facultad()

    materiasDisponibles = Minas.getMaterias()

    est = Estudiante("PEPE", 67890, "pp@a.com", False, [materiasDisponibles[0], materiasDisponibles[1], materiasDisponibles[3]])
    est2 = Estudiante("JHON", 67890, "pp@a.com", False, [materiasDisponibles[0], materiasDisponibles[3]])
    est3 = Estudiante("BREADLEY", 67890, "pp@a.com", False, [materiasDisponibles[0], materiasDisponibles[3]])
    est4 = Estudiante("BAENA", 67890, "pp@a.com", False, [materiasDisponibles[0], materiasDisponibles[3]])

    est.calcular_porcentaje_avance()
    est2.calcular_porcentaje_avance()
    est3.calcular_porcentaje_avance()
    est4.calcular_porcentaje_avance()

    print(materiasDisponibles)

    print(est.porcentaje_avance)
    print(est2.porcentaje_avance)
    print(est3.porcentaje_avance)
    print(est4.porcentaje_avance)

    est.inscribirMateria("Calculo VariasVariables", materiasDisponibles)
    est2.inscribirMateria("Calculo Integral", materiasDisponibles)
    est3.inscribirMateria("Calculo Integral", materiasDisponibles)
    est4.inscribirMateria("Calculo Integral", materiasDisponibles)

    est.inscribirMateria("Catedra Apun", materiasDisponibles)
    est2.inscribirMateria("Catedra Apun", materiasDisponibles)
    est3.inscribirMateria("Catedra Apun", materiasDisponibles)
    est4.inscribirMateria("Catedra Apun", materiasDisponibles)

    est.inscribirMateria("Programacion Orientada Objetos", materiasDisponibles)
    est2.inscribirMateria("Programacion Orientada Objetos", materiasDisponibles)
    est3.inscribirMateria("Programacion Orientada Objetos", materiasDisponibles)
    est4.inscribirMateria("Programacion Orientada Objetos", materiasDisponibles)

    # print(est2.getMaterias_Inscritas())

    tallerP = Tarea(materiasDisponibles[1], "NOSE")
    tallerP.setGrade(est, 5.0)
    tallerP.setGrade(est2, 4.0)
    tallerP.setGrade(est3, 5.0)
    tallerP.setGrade(est4, 5.0)
    materiasDisponibles[1].inscribirTarea(tallerP)

    tallerP4 = Tarea(materiasDisponibles[1], "NOSE")
    tallerP4.setGrade(est, 3.0)
    tallerP4.setGrade(est2, 1.0)
    tallerP4.setGrade(est3, 3.0)
    tallerP4.setGrade(est4, 5.0)
    materiasDisponibles[1].inscribirTarea(tallerP4)

    tallerP2 = Tarea(materiasDisponibles[4], "NOSE2")
    tallerP2.setGrade(est, 5.0)
    tallerP2.setGrade(est2, 5.0)
    tallerP2.setGrade(est3, 5.0)
    tallerP2.setGrade(est4, 3.5)
    materiasDisponibles[4].inscribirTarea(tallerP2)

    tallerP3 = Tarea(materiasDisponibles[4], "NOSE3")
    tallerP3.setGrade(est, 5.0)
    tallerP3.setGrade(est2, 5.0)
    tallerP3.setGrade(est3, 4.0)
    tallerP3.setGrade(est4, 4.5)
    materiasDisponibles[4].inscribirTarea(tallerP3)

    beca = Beca("SISAS")

    Estudiante.aplicarBeca(est)
    Estudiante.aplicarBeca(est2)
    Estudiante.aplicarBeca(est3)
    Estudiante.aplicarBeca(est4)
    beca.asignarEstudiantesBeca()

    print("Admitidos a becas: ")
    print("Beca Inicial: " + beca.estudiantesAptosInicial)
    print("Beca Normal: " + beca.estudiantesAptosNormal)
    print("Beca Avanzada: " + beca.estudiantesAptosAvanzada + "\n")

    promedioEst = est.calcularPromedio()
    promedioEst2 = est2.calcularPromedio()
    promedioEst3 = est3.calcularPromedio()
    promedioEst4 = est4.calcularPromedio()

    print("Promedios: ")
    print(est + " promedio: " + promedioEst)
    print(est2 + " promedio: " + promedioEst2)
    print(est3 + " promedio: " + promedioEst3)
    print(est4 + " promedio: " + promedioEst4 + "\n")
    print(materiasDisponibles[1].calcularPromedio(est2))
    print(materiasDisponibles[1].calcularPromedio(est3))
    print(materiasDisponibles[1].Calcular_necesario_para_pasar(est2))
    print(materiasDisponibles[1].Calcular_necesario_para_pasar(est3))

    print("Horarios: ")

    nose = est.compararHorario(est.getMaterias_Inscritas())

    print("El horario de " + est + " es:")
    print(est.getMaterias_Inscritas() + "\n")

    print("El horario de " + est + " presenta fallas?")
    print(nose + "\n")

    est.sugerirMaterias(materiasDisponibles)

    print("Nuevo horario del estudiante " + est.getNombre() + ": ")
    print(est.getMaterias_Inscritas() + "\n")

    for profesor in est2.getProfesoresInscritos():
        profesor.ingresarCalificacion(3.0)

    for profesor in est3.getProfesoresInscritos():
        profesor.ingresarCalificacion(4.0)

    print("Calificación docente:")

    for profesor in est3.getProfesoresInscritos():
        profesor.evaluacionDocente()
        print(profesor.getCalificacionDocente())

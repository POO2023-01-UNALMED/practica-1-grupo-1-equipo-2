from personas.Estudiante import Estudiante
from Calendario.Facultad import Facultad
from Calendario.Beca import Beca
from Calendario.Tarea import Tarea
from Calendario.Materia import Materia
from personas.Profesor import Profesor



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


    est.inscribir_materia("Calculo VariasVariables", materiasDisponibles)
    est2.inscribir_materia("Calculo Integral", materiasDisponibles)
    est3.inscribir_materia("Calculo Integral", materiasDisponibles)
    est4.inscribir_materia("Calculo Integral", materiasDisponibles)

    est.inscribir_materia("Catedra Apun", materiasDisponibles)
    est2.inscribir_materia("Catedra Apun", materiasDisponibles)
    est3.inscribir_materia("Catedra Apun", materiasDisponibles)
    est4.inscribir_materia("Catedra Apun", materiasDisponibles)

    est.inscribir_materia("Programacion Orientada Objetos", materiasDisponibles)
    est2.inscribir_materia("Programacion Orientada Objetos", materiasDisponibles)
    est3.inscribir_materia("Programacion Orientada Objetos", materiasDisponibles)
    est4.inscribir_materia("Programacion Orientada Objetos", materiasDisponibles)

    # print(est2.getMaterias_Inscritas())

    tallerP = Tarea(materiasDisponibles[1], "NOSE")
    tallerP.set_grade(est, 5.0)
    tallerP.set_grade(est2, 4.0)
    tallerP.set_grade(est3, 5.0)
    tallerP.set_grade(est4, 5.0)
    Materia(materiasDisponibles[1]).inscribir_tarea(tallerP)

    tallerP4 = Tarea(materiasDisponibles[1], "NOSE")
    tallerP4.set_grade(est, 3.0)
    tallerP4.set_grade(est2, 1.0)
    tallerP4.set_grade(est3, 3.0)
    tallerP4.set_grade(est4, 5.0)
    Materia(materiasDisponibles[1]).inscribir_tarea(tallerP4)

    tallerP2 = Tarea(materiasDisponibles[4], "NOSE2")
    tallerP2.set_grade(est, 5.0)
    tallerP2.set_grade(est2, 5.0)
    tallerP2.set_grade(est3, 5.0)
    tallerP2.set_grade(est4, 3.5)
    Materia(materiasDisponibles[4]).inscribir_tarea(tallerP2)

    tallerP3 = Tarea(materiasDisponibles[4], "NOSE3")
    tallerP3.set_grade(est, 5.0)
    tallerP3.set_grade(est2, 5.0)
    tallerP3.set_grade(est3, 4.0)
    tallerP3.set_grade(est4, 4.5)
    Materia(materiasDisponibles[4]).inscribir_tarea(tallerP3)

    beca = Beca("SISAS")

    Estudiante.aplicar_beca(est)
    Estudiante.aplicar_beca(est2)
    Estudiante.aplicar_beca(est3)
    Estudiante.aplicar_beca(est4)
    beca.asignar_estudiantes_beca()

    print("Admitidos a becas: ")
    print("Beca Inicial: " + beca.getEstudiantes_aptos_inicial())
    print("Beca Normal: " + beca.getEstudiantes_aptos_normal())
    print("Beca Avanzada: " + beca.getEstudiantes_aptos_avanzada() + "\n")

    promedioEst = est.calcular_promedio()
    promedioEst2 = est2.calcular_promedio()
    promedioEst3 = est3.calcular_promedio()
    promedioEst4 = est4.calcular_promedio()

    print("Promedios: ")
    print(est + " promedio: " + promedioEst)
    print(est2 + " promedio: " + promedioEst2)
    print(est3 + " promedio: " + promedioEst3)
    print(est4 + " promedio: " + promedioEst4 + "\n")
    print(Materia(materiasDisponibles[1]).calcular_promedio(est2))
    print(Materia(materiasDisponibles[1]).calcular_promedio(est3))
    print(Materia(materiasDisponibles[1]).calcular_necesario_para_pasar(est2))
    print(Materia(materiasDisponibles[1]).calcular_necesario_para_pasar(est3))

    print("Horarios: ")

    nose = est.comparar_horario(est.getMaterias_inscritas())

    print("El horario de " + est + " es:")
    print(est.getMaterias_inscritas() + "\n")

    print("El horario de " + est + " presenta fallas?")
    print(nose + "\n")

    est.sugerir_materias(materiasDisponibles)

    print("Nuevo horario del estudiante " + est.getNombre() + ": ")
    print(est.getMaterias_inscritas() + "\n")

    for profesor in est2.getProfesores_inscritos():
        Profesor(profesor).ingresar_calificacion(3.0)

    for profesor in est3.getProfesores_inscritos():
        Profesor(profesor).ingresar_calificacion(4.0)

    print("Calificación docente:")

    for profesor in est3.getProfesores_inscritos():
        Profesor(profesor).evaluacion_docente()
        print(Profesor(profesor).getCalificacion_docente())

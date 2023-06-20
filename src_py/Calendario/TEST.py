from src_py.personas.Estudiante import Estudiante
from src_py.Calendario.Facultad import Facultad
from src_py.Calendario.Beca import Beca
from src_py.Calendario.Tarea import Tarea
from src_py.Calendario.Materia import Materia
from src_py.personas.Profesor import Profesor
import tkinter as tk

if __name__ == "__main__":
    Minas = Facultad()

    materiasDisponibles = Minas.getMaterias()

    est = Estudiante("PEPE", 67890, "pp@a.com", False,
                     [materiasDisponibles[0], materiasDisponibles[1], materiasDisponibles[3]])
    est2 = Estudiante("JHON", 67890, "pp@a.com", False, [materiasDisponibles[0], materiasDisponibles[3]])
    est3 = Estudiante("BREADLEY", 67890, "pp@a.com", False, [materiasDisponibles[0], materiasDisponibles[3]])
    est4 = Estudiante("BAENA", 67890, "pp@a.com", False, [materiasDisponibles[0], materiasDisponibles[3]])
    est5 = Estudiante("JOSSHUEN", 67890, "pp@a.com", False, [materiasDisponibles[0], materiasDisponibles[3]])
    est6 = Estudiante("NOSE", 67890, "pp@a.com", False,
                     [materiasDisponibles[0], materiasDisponibles[3], materiasDisponibles[6]])

    est6.sugerir_materias(materiasDisponibles)

    for materia in est6.getMaterias_inscritas():
        print(materia)

    est.calcular_porcentaje_avance()
    est2.calcular_porcentaje_avance()
    est3.calcular_porcentaje_avance()
    est4.calcular_porcentaje_avance()
    """
    for materia in materiasDisponibles:
        print(materia)
    
    print(f"{int(est.porcentaje_avance * 100)}%")
    print(f"{int(est2.porcentaje_avance * 100)}%")
    print(f"{int(est3.porcentaje_avance * 100)}%")
    print(f"{int(est4.porcentaje_avance * 100)}%")
    """

    est.inscribir_materia("Calculo Varias Variables", materiasDisponibles)
    est2.inscribir_materia('Calculo Integral', materiasDisponibles)
    est3.inscribir_materia('Calculo Integral', materiasDisponibles)
    est4.inscribir_materia('Calculo Integral', materiasDisponibles)

    est.inscribir_materia("Catedra Apun", materiasDisponibles)
    est2.inscribir_materia("Catedra Apun", materiasDisponibles)
    est3.inscribir_materia("Catedra Apun", materiasDisponibles)
    est4.inscribir_materia("Catedra Apun", materiasDisponibles)

    est.inscribir_materia("Programacion Orientada Objetos", materiasDisponibles)
    est2.inscribir_materia("Programacion Orientada Objetos", materiasDisponibles)
    est3.inscribir_materia("Programacion Orientada Objetos", materiasDisponibles)
    est4.inscribir_materia("Programacion Orientada Objetos", materiasDisponibles)

    #for materia in est.getMaterias_inscritas():
    #    print(materia)

    """
    for materia in est2.getMaterias_inscritas():
        print(materia)
    for materia in est3.getMaterias_inscritas():
        print(materia)
    for materia in est4.getMaterias_inscritas():
        print(materia)
    """
    tallerP5 = Tarea("NOSE")
    tallerP5.set_grade(est, 5.0)
    tallerP5.set_grade(est2, 4.0)
    tallerP5.set_grade(est3, 5.0)
    tallerP5.set_grade(est4, 5.0)
    materiasDisponibles[7].inscribir_tarea(tallerP5)

    tallerP6 = Tarea("NOSE")
    tallerP6.set_grade(est, 5.0)
    tallerP6.set_grade(est2, 5.0)
    tallerP6.set_grade(est3, 5.0)
    tallerP6.set_grade(est4, 5.0)
    materiasDisponibles[7].inscribir_tarea(tallerP6)

    tallerP8 = Tarea("NOSE")
    tallerP8.set_grade(est, 5.0)
    materiasDisponibles[2].inscribir_tarea(tallerP8)

    tallerP = Tarea("NOSE")
    tallerP.set_grade(est2, 4.0)
    tallerP.set_grade(est3, 5.0)
    tallerP.set_grade(est4, 5.0)
    materiasDisponibles[1].inscribir_tarea(tallerP)

    tallerP4 = Tarea("NOSE")
    tallerP4.set_grade(est2, 5.0)
    tallerP4.set_grade(est3, 3.0)
    tallerP4.set_grade(est4, 5.0)
    materiasDisponibles[1].inscribir_tarea(tallerP4)

    tallerP2 = Tarea("NOSE2")
    tallerP2.set_grade(est, 5.0)
    tallerP2.set_grade(est2, 5.0)
    tallerP2.set_grade(est3, 5.0)
    tallerP2.set_grade(est4, 3.5)
    materiasDisponibles[4].inscribir_tarea(tallerP2)

    tallerP3 = Tarea("NOSE3")
    tallerP3.set_grade(est, 5.0)
    tallerP3.set_grade(est2, 5.0)
    tallerP3.set_grade(est3, 4.0)
    tallerP3.set_grade(est4, 4.5)
    materiasDisponibles[4].inscribir_tarea(tallerP3)

    beca = Beca("SISAS")

    Estudiante.aplicar_beca(est)
    Estudiante.aplicar_beca(est2)
    Estudiante.aplicar_beca(est3)
    Estudiante.aplicar_beca(est4)
    beca.asignar_estudiantes_beca()

    """
    print("Admitidos a becas: ")
    print("Beca Inicial: ")
    for becado in beca.getEstudiantes_aptos_inicial():
        print(becado)
    print("Beca Normal: " + str(beca.getEstudiantes_aptos_normal()))
    print("Beca Avanzada: " + str(beca.getEstudiantes_aptos_avanzada()) + "\n") 
    """
    promedioEst = est.calcular_promedio()
    promedioEst2 = est2.calcular_promedio()
    promedioEst3 = est3.calcular_promedio()
    promedioEst4 = est4.calcular_promedio()

    """
    print("Promedios: ")
    print(str(est) + " promedio: " + str(promedioEst))
    print(str(est2) + " promedio: " + str(promedioEst2))
    print(str(est3) + " promedio: " + str(promedioEst3))
    print(str(est4) + " promedio: " + str(promedioEst4) + "\n")
    
    print(materiasDisponibles[1].calcular_promedio(est2))
    print(materiasDisponibles[1].calcular_promedio(est3))
    
    print(materiasDisponibles[1].calcular_necesario_para_pasar(est2))
    print(materiasDisponibles[1].calcular_necesario_para_pasar(est3))
    
    print("Horarios:")
    
    nose = est.comparar_horario(est.getMaterias_inscritas())
    
    print("El horario de " + str(est) + " es:")
    for materia in est.getMaterias_inscritas():
        print(materia)
    
    print("El horario de " + str(est) + " presenta fallas?")
    print(str(nose) + "\n")
    
    est.sugerir_horario(nose)  # Remove the argument
    
    print("Nuevo horario del estudiante " + str(est.getNombre()) + ":")
    for materia in est.getMaterias_inscritas():
        print(materia)
    print("\n")
    """

    est5.sugerir_materias(materiasDisponibles)

    #print(F"Nuevo horario sugerido por el sistema de: {est5}")

    #for materia in est5.getMaterias_inscritas():
    #    print(materia)

    #for profesor in est2.getProfesores_inscritos():
    #    profesor.ingresar_calificacion(3.0)

    #for profesor in est3.getProfesores_inscritos():
    #    profesor.ingresar_calificacion(4.0)

    """
    print("Calificación docente:")
    
    for profesor in est3.getProfesores_inscritos():
        profesor.evaluacion_docente()
        print(profesor.getCalificacion_docente())
    """
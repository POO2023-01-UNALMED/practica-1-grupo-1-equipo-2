from tkinter import *
from src_py.personas.Profesor import *
from src_py.Calendario.Materia import *
from PIL import Image, ImageTk
from src_py.personas.Estudiante import Estudiante
from tkinter import Button
from src_py.Calendario.gestionDatos import gestionDatos
from src_py.Calendario.Facultad import Facultad


def menuProfesor(profesor: Profesor):
    ventanaInicio = Tk()
    ventanaInicio.title("Información usuario")
    ventanaInicio.geometry("800x600")
    ventanaInicio.configure(background="white")

    menu_bar = Menu(ventanaInicio)
    ventanaInicio.config(menu=menu_bar)

    deseo_menu = Menu(menu_bar, tearoff=0)
    menu_bar.add_cascade(label="Deseo", menu=deseo_menu)

    salir_del_sistema(datos_sistema)

    opciones = [
        "Ver materias asignadas para el semestre actual",
        "Volver al menu principal"
    ]

    def clearFrame():
        for widget in frameVentanaInicio.winfo_children():
            widget.destroy()

    ventanaInicio.columnconfigure(0, weight=1)  # Expand column 0 to fill the available space
    ventanaInicio.rowconfigure(0, weight=1)  # Expand row 0 to fill the available space

    frameVentanaInicio = Frame(ventanaInicio, background="white", borderwidth=2, highlightthickness=2)
    frameVentanaInicio.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

    frameVentanaInicio.columnconfigure(0, weight=1)  # Expand column 0 in frameVentanaInicio
    frameVentanaInicio.columnconfigure(1, weight=1)  # Expand column 1 in frameVentanaInicio
    frameVentanaInicio.rowconfigure(5, weight=1)  # Expand row 5 in frameVentanaInicio

    def ventanaPrincipal():
        clearFrame()
        name = Label(frameVentanaInicio, text="Nombre del Profesor: ")
        name.config(font=("Times New Roman", 12, "bold"))
        name.pack()

        nombre = Label(frameVentanaInicio, text=profesor.getNombre())
        nombre.config(font=("Times New Roman", 12))
        nombre.pack()
        show_id = Label(frameVentanaInicio, text="ID del Profesor: ")
        show_id.config(font=("Times New Roman", 12, "bold"))
        show_id.pack()

        iD = Label(frameVentanaInicio, text=int(profesor.getID()))
        iD.config(font=("Times New Roman", 12, "bold"))
        iD.pack()

        show_correo = Label(frameVentanaInicio, text="Correo del Profesor: ")
        show_correo.config(font=("Times New Roman", 12, "bold"))
        show_correo.pack()

        correo = Label(frameVentanaInicio, text=str(profesor.getEmail()))
        correo.config(font=("Times New Roman", 12, "bold"))
        correo.pack()

        salir_del_sistema(datos_sistema)

    opcionSeleccionada = StringVar(ventanaInicio)
    opcionSeleccionada.set(opciones[0])

    for opcion in opciones:
        deseo_menu.add_command(label=opcion, command=lambda opcion=opcion: seleccionarOpcion(opcion))

    def seleccionarOpcion(opcion):
        if opcion =="Ver materias asignadas para el semestre actual":
            verMateriasSemestre()
        elif opcion == "Volver al menu principal":
            ventanaPrincipal()

    def verMateriasSemestre():
        clearFrame()
        nombre = Label(frameVentanaInicio, text="Las materias inscritas para este semestre son: ")
        nombre.config(font=("Times New Roman", 12))
        nombre.pack()

        salir_del_sistema(datos_sistema)

        def on_button_click():
            clearFrame()
            nombres = [
                "Crear tarea de la materia",
                "Eliminar tarea de la materia",
                "Visualizar las tareas creadas",
                "Ingresar calificaciones en las tareas",
                "Ver detalles de la materia",
                "Volver al menu del docente"
            ]

            def on_button_1_click():
                clearFrame()
                nombre_label = Label(frameVentanaInicio, text="Ingrese el nombre de la tarea que desea crear:")
                nombre_label.config(font=("Times New Roman", 12))
                nombre_label.pack()

                tarea_nombre = StringVar()
                entry_tarea_nombre = Entry(frameVentanaInicio)
                entry_tarea_nombre.pack()


                def on_guardar_click():
                    materia.inscribir_tarea(entry_tarea_nombre.get())
                    nombre_label.config(text=f"Nombre de la tarea: {entry_tarea_nombre.get()} quedo registrada correctamente")
                    print(f"Nombre de la tarea: {entry_tarea_nombre.get()} quedo registrada correctamente")

                boton_guardar = Button(frameVentanaInicio, text="Guardar", command=on_guardar_click)
                boton_guardar.pack()

                salir_del_sistema(datos_sistema)

            def on_button_2_click():
                clearFrame()
                nombre = Label(frameVentanaInicio, text="Seleccione la tarea que desea eliminar")
                nombre.config(font=("Times New Roman", 12))
                nombre.pack()

                def on_button_click(tarea):
                    materia.retirar_tarea(tarea)
                    print(f"Tarea {tarea} eliminada correctamente")

                for tarea in materia.tareas_de_materia:
                    button_tarea = Button(frameVentanaInicio, text=tarea,
                                          command=lambda tarea=tarea: on_button_click(tarea))
                    button_tarea.pack()

                salir_del_sistema(datos_sistema)

            def on_button_3_click():
                clearFrame()
                nombre = Label(frameVentanaInicio, text=f"lista de tarea de la materia {materia.getNombre()}")
                nombre.config(font=("Times New Roman", 12))
                nombre.pack()

                for tarea in materia.tareas_de_materia:
                    label_tarea = Label(frameVentanaInicio, text=tarea)
                    label_tarea.config(font=("Times New Roman", 12))
                    label_tarea.pack()

                salir_del_sistema(datos_sistema)

            def on_button_4_click():
                clearFrame()
                nombre = Label(frameVentanaInicio, text=f"ingresar calificaciones en las tareas")
                nombre.config(font=("Times New Roman", 12))
                nombre.pack()

                nombre2 = Label(frameVentanaInicio, text=f"lista de tarea de la materia {materia.getNombre()}")
                nombre2.config(font=("Times New Roman", 12))
                nombre2.pack()

                def on_button_click(tarea):
                    clearFrame()
                    for estudiante in materia.getEstudiantes_inscritos():
                        label_estudiante = Label(frameVentanaInicio, text=estudiante.getNombre())
                        label_estudiante.pack()

                for tarea in materia.tareas_de_materia:
                    button_tarea = Button(frameVentanaInicio, text=tarea,
                                          command=lambda tarea=tarea: on_button_click(tarea))
                    button_tarea.pack()

                salir_del_sistema(datos_sistema)

            def on_button_5_click():
                clearFrame()
                nombre = Label(frameVentanaInicio, text=f"detalles de la materia {materia.getNombre()}")
                nombre.config(font=("Times New Roman", 12))
                nombre.pack()

                nombre2 = Label(frameVentanaInicio, text=materia.getHorario())
                nombre2.config(font=("Times New Roman", 12))
                nombre2.pack()

                salir_del_sistema(datos_sistema)

                pass

            def on_button_6_click():
                clearFrame()
                ventanaPrincipal()
                salir_del_sistema(datos_sistema)

                pass

            button_functions = [
                on_button_1_click,
                on_button_2_click,
                on_button_3_click,
                on_button_4_click,
                on_button_5_click,
                on_button_6_click
            ]

            for i, nombre in enumerate(nombres):
                button = Button(frameVentanaInicio, text=f'{str(nombre)} {str(materia.getNombre())}',
                                command=button_functions[i])
                button.pack()

        for materia in profesor.getMaterias_asignadas():
            button_materia = Button(frameVentanaInicio, text=materia.getNombre(), command=on_button_click)
            button_materia.pack()

    ventanaPrincipal()
    ventanaInicio.mainloop()

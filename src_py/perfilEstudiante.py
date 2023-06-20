from tkinter import *
from PIL import Image, ImageTk
from src_py.personas.Estudiante import Estudiante
from src_py.personas.Profesor import Profesor
from tkinter import Button, messagebox
from src_py.Calendario.gestionDatos import gestionDatos
from src_py.Calendario.Facultad import Facultad
from src_py.Calendario.Materia import Materia
from PIL import ImageTk, Image
from tkinter import messagebox
from src_py.baseDatos.Serializador import Serializador


def menuEstudiante(estudiante: Estudiante):
    ventanaInicio = Tk()
    ventanaInicio.title("Información usuario")
    ventanaInicio.geometry("800x600")
    ventanaInicio.configure(background="white")

    datos_sistema1 = gestionDatos()

    # Create the menu bar
    menu_bar = Menu(ventanaInicio)
    ventanaInicio.config(menu=menu_bar)

    # Create the Deseo menu
    deseo_menu = Menu(menu_bar, tearoff=0)
    menu_bar.add_cascade(label="Deseo", menu=deseo_menu)

    # Add options to the Deseo menu
    opciones = [
        "Inscribir asignaturas",
        "Ver materias inscritas",
        "Realizar calificacion de docente",
        "Ver horario",
        "Materias cursadas anteriormente",
        "Ver calificacion docente",
        "Volver al menu principal"
    ]

    def VentanaPrincipal():
        clearFrame()
        name = Label(frameVentanaInicio, text="Nombre del Estudiante: ")
        name.config(font=("Times New Roman", 12, "bold"))
        name.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        nombre = Label(frameVentanaInicio, text=estudiante.getNombre())
        nombre.config(font=("Times New Roman", 12))
        nombre.grid(row=1, column=0, padx=10, pady=10, sticky="w")

        show_id = Label(frameVentanaInicio, text="ID del Estudiante: ")
        show_id.config(font=("Times New Roman", 12, "bold"))
        show_id.grid(row=2, column=0, padx=10, pady=10, sticky="w")

        iD = Label(frameVentanaInicio, text=int(estudiante.getID()))
        iD.config(font=("Times New Roman", 12, "bold"))
        iD.grid(row=3, column=0, padx=10, pady=10, sticky="w")

        show_correo = Label(frameVentanaInicio, text="Correo del Estudiante: ")
        show_correo.config(font=("Times New Roman", 12, "bold"))
        show_correo.grid(row=4, column=0, padx=10, pady=10, sticky="w")

        correo = Label(frameVentanaInicio, text=str(estudiante.getEmail()))
        correo.config(font=("Times New Roman", 12, "bold"))
        correo.grid(row=5, column=0, padx=10, pady=10, sticky="w")

        materia = Label(frameVentanaInicio, text=str(estudiante.getMaterias_cursadas()))
        materia.config(font=("Times New Roman", 12, "bold"))
        materia.grid(row=6, column=0, padx=10, pady=10, sticky="w")

    opcionSeleccionada = StringVar(ventanaInicio)
    opcionSeleccionada.set(opciones[0])  # Set the default option

    def mostrarInscribirAsignaturas():
        clearFrame()
        label = Label(frameVentanaInicio, text="Inscribir asignaturas")
        label.config(font=("Times New Roman", 30, "bold"))
        label.pack(side="top", pady=20)

        # Create a new frame to contain the Checkbutton widgets
        checkbutton_frame = Frame(frameVentanaInicio)
        checkbutton_frame.pack(anchor="center")

        # Obtener las materias disponibles
        facultad = Facultad()
        materias_disponibles = facultad.getMaterias()

        # Crear una variable StringVar para cada materia
        for i, materia in enumerate(materias_disponibles):
            materias_vars[materia.getNombre()] = StringVar(value="No inscrita")
            checkbox = Checkbutton(checkbutton_frame, text=materia.getNombre(),
                                   variable=materias_vars[materia.getNombre()],
                                   onvalue="Inscrita", offvalue="No inscrita",
                                   command=lambda materia=materia: seleccionarMateria(materia))
            checkbox.config(font=("Times New Roman", 20))
            checkbox.pack(side="top")

        def seleccionarMateria(materia):
            if materias_vars[materia.getNombre()].get() == "No inscrita":
                materias_vars[materia.getNombre()].set("Inscrita")
            else:
                materias_vars[materia.getNombre()].set("No inscrita")
        # Función para imprimir la lista de materias inscritas
        def imprimirMateriasInscritas():
            materias_seleccionadas = [materia for materia, estado in materias_vars.items() if
                                      estado.get() == "Inscrita"]
            if not materias_seleccionadas:
                messagebox.showerror("Erorr!", "Por favor, escoja las materias que desea inscribir.")
                ventanaInicio.destroy()
            else:
                materias_seleccionadas = [materia for materia, estado in materias_vars.items() if
                                          estado.get() == "Inscrita"]
                materias_encontradas = []

                for materia_seleccionada in materias_seleccionadas:
                    for materia in datos_sistema1.getMaterias():
                        if materia_seleccionada == materia.getNombre():
                            materias_encontradas.append(materia)

                for materia_sel in materias_encontradas:
                    estudiante.inscribir_materia(materia_sel.getNombre(), datos_sistema1.getMaterias())

                salir_del_sistema(datos_sistema1)

                if not estudiante.getMaterias_inscritas():
                    messagebox.showerror("Erorr!", "Verifique que ya haya cursado el prerrequisito de las materias que intenta inscribir.")
                    ventanaInicio.destroy()


        # Botón para confirmar la inscripción y mostrar la lista de materias inscritas
        confirmar_btn = Button(frameVentanaInicio, text="Confirmar inscripción", command=imprimirMateriasInscritas)
        confirmar_btn.config(font=("Times New Roman", 12, "bold"))
        confirmar_btn.pack(side="bottom", pady=10)

    def seleccionarOpcion(opcion):
        if opcion == "Inscribir asignaturas":
            mostrarInscribirAsignaturas()
        elif opcion == "Ver materias inscritas":
            mostrarMateriasInscritas()
        elif opcion == "Realizar calificacion de docente":
            realizarCalificacionDocente()
        elif opcion == "Ver horario":
            mostrarHorario()
        elif opcion == "Materias cursadas anteriormente":
            mostrarMateriasCursadas()
        elif opcion == "Ver calificacion docente":
            mostrarCalificacionDocente()
        elif opcion == "Volver al menu principal":
            volverAlMenuPrincipal()

    for opcion in opciones:
        deseo_menu.add_command(label=opcion, command=lambda opcion=opcion: seleccionarOpcion(opcion))

    ventanaInicio.columnconfigure(0, weight=1)  # Expand column 0 to fill the available space
    ventanaInicio.rowconfigure(0, weight=1)  # Expand row 0 to fill the available space

    frameVentanaInicio = Frame(ventanaInicio, background="white", borderwidth=2, highlightthickness=2)
    frameVentanaInicio.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

    frameVentanaInicio.columnconfigure(0, weight=1)  # Expand column 0 in frameVentanaInicio
    frameVentanaInicio.columnconfigure(1, weight=1)  # Expand column 1 in frameVentanaInicio
    frameVentanaInicio.rowconfigure(5, weight=1)  # Expand row 5 in frameVentanaInicio

    materias_vars = {}

    def clearFrame():
        for widget in frameVentanaInicio.winfo_children():
            widget.destroy()

    def mostrarMateriasInscritas():
            clearFrame()
            label = Label(frameVentanaInicio, text="Ver materias inscritas")
            label.config(font=("Times New Roman", 12, "bold"))
            label.pack()

            # Obtener las materias inscritas por el estudiante
            materias_inscritas = estudiante.getMaterias_inscritas()
            respuesta_booleano = False
            # Verificar si el estudiante tiene materias inscritas
            if len(materias_inscritas) == 0:
                respuesta = messagebox.askyesno("No tienes materias inscritas",
                                                "No se encuentran materias inscritas por usted en el sistema. ¿Quieres que te proporcione materias dependiendo de lo ya visto?")

                if respuesta:
                    # El usuario seleccionó "Sí"
                    # Realizar la lógica para proporcionar las materias dependiendo de lo ya visto
                    # ...

                    # Establecer el valor del booleano
                    respuesta_booleano = True
                else:
                    # El usuario seleccionó "No"
                    # Establecer el valor del booleano
                    respuesta_booleano = False

                    if not respuesta_booleano:
                        # Devolver al estudiante al menú principal
                        volverAlMenuPrincipal()
                        return

                # Continuar con el resto de la lógica o mostrar otra ventana según sea necesario
            else:
                # Mostrar las materias inscritas
                for materia in materias_inscritas:
                    materia_label = Label(frameVentanaInicio, text=materia.getNombre())
                    materia_label.config(font=("Times New Roman", 12, "bold"))
                    materia_label.pack()

                # Establecer el valor del booleano (en este caso no se muestra la ventana emergente, asumimos que el estudiante ya tiene las materias inscritas)
                respuesta_booleano = False

            # Botón para volver al menú principal
            volver_btn = Button(frameVentanaInicio, text="Volver al menú principal", command=volverAlMenuPrincipal)
            volver_btn.config(font=("Times New Roman", 12, "bold"))
            volver_btn.pack()

    def realizarCalificacionDocente():
        clearFrame()

        # Aquí puedes agregar la lógica para realizar la calificación del docente
        def submit():
            calificacion = int(entry_calificacion.get())
            estudiante.calificacion_docente.append(calificacion)
            messagebox.showinfo("Éxito", "Calificación registrada correctamente")
            entry_calificacion.delete(0, END)

        label_calificacion = Label(frameVentanaInicio, text="Calificación del docente (1-5): ")
        label_calificacion.config(font=("Times New Roman", 12, "bold"))
        label_calificacion.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        entry_calificacion = Entry(frameVentanaInicio)
        entry_calificacion.grid(row=0, column=1, padx=10, pady=10, sticky="w")

        btn_submit = Button(frameVentanaInicio, text="Enviar", command=submit)
        btn_submit.grid(row=1, column=0, padx=10, pady=10)

    def mostrarHorario():
        clearFrame()
        label = Label(frameVentanaInicio, text="Horario inscrito")
        label.config(font=("Times New Roman", 12, "bold"))
        label.pack()

        # Obtener el horario del estudiante
        horario = estudiante.getMaterias_inscritas()

        # Verificar si el estudiante tiene un horario asignado
        if not horario:
            mensaje = Label(frameVentanaInicio, text="No tienes un horario asignado")
            mensaje.config(font=("Times New Roman", 12, "bold"))
            mensaje.pack()
        else:
            # Mostrar el horario del estudiante
            for materia in horario:
                dia = materia.getHorario().getDia()
                horas = f"{materia.getHorario().getHora_inicio()} - {materia.getHorario().getHora_fin()}"

                dia_label = Label(frameVentanaInicio, text=f"Día: {dia}")
                dia_label.config(font=("Times New Roman", 12, "bold"))
                dia_label.pack()

                horas_label = Label(frameVentanaInicio, text=f"Horas: {horas}")
                horas_label.config(font=("Times New Roman", 12))
                horas_label.pack()

        # Botón para volver al menú principal
        volver_btn = Button(frameVentanaInicio, text="Volver al menú principal", command=volverAlMenuPrincipal)
        volver_btn.config(font=("Times New Roman", 12, "bold"))
        volver_btn.pack()


    def mostrarMateriasCursadas():
        datos_sistema = gestionDatos()
        clearFrame()
        label = Label(frameVentanaInicio, text="Materias cursadas anteriormente")
        label.config(font=("Times New Roman", 12, "bold"))
        label.pack()
        label2 = Label(frameVentanaInicio, text="Usted ha cursado: ")
        label2.config(font=("Times New Roman", 12, "bold"))
        label2.pack()

        materias_cursadas = estudiante.getMaterias_cursadas()

        for i, materia in enumerate(materias_cursadas):
            label_materia = Label(frameVentanaInicio, text=materia)
            label_materia.config(font=("Times New Roman", 12, "bold"))
            label_materia.pack()

    def mostrarCalificacionDocente():
        clearFrame()
        calificaciones = profesor.evaluacion_docente()

        if not calificaciones:
            label_sin_calificaciones = Label(frameVentanaInicio, text="No se han registrado calificaciones de docentes")
            label_sin_calificaciones.config(font=("Times New Roman", 12, "bold"))
            label_sin_calificaciones.grid(row=0, column=0, padx=10, pady=10)
        else:
            for i, calificacion in enumerate(calificaciones):
                label_calificacion = Label(frameVentanaInicio, text=f"Calificación {i + 1}: {calificacion}")
                label_calificacion.config(font=("Times New Roman", 12))
                label_calificacion.grid(row=i, column=0, padx=10, pady=10)

        btn_volver = Button(frameVentanaInicio, text="Volver al menú principal", command=menuEstudiante)
        btn_volver.grid(row=len(calificaciones) + 1, column=0, padx=10, pady=10)

    def volverAlMenuPrincipal():
        clearFrame()
        VentanaPrincipal()

    VentanaPrincipal()
    ventanaInicio.mainloop()
from tkinter import *
from PIL import Image, ImageTk
from src_py.personas.Estudiante import Estudiante


def menuEstudiante(estudiante: Estudiante):
    ventanaInicio = Tk()
    ventanaInicio.title("Información usuario")
    ventanaInicio.geometry("800x600")
    ventanaInicio.configure(background="white")

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
        "Ver perfil estudiante",
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

        iD = Label(frameVentanaInicio, text=estudiante.getID())
        iD.config(font=("Times New Roman", 12, "bold"))
        iD.grid(row=3, column=0, padx=10, pady=10, sticky="w")

        show_correo = Label(frameVentanaInicio, text="Correo del Estudiante: ")
        show_correo.config(font=("Times New Roman", 12, "bold"))
        show_correo.grid(row=4, column=0, padx=10, pady=10, sticky="w")

        correo = Label(frameVentanaInicio, text=estudiante.getEmail())
        correo.config(font=("Times New Roman", 12, "bold"))
        correo.grid(row=5, column=0, padx=10, pady=10, sticky="w")

        imagenEst = ImageTk.PhotoImage(Image.open("Images/sis4.png").resize((200, 350)).convert("RGBA"))
        imagen = Label(frameVentanaInicio, image=imagenEst, highlightthickness=2)
        imagen.image = imagenEst  # Guardar una referencia para evitar que la imagen se recolecte con el garbage collector
        imagen.grid(row=0, column=1, rowspan=5, padx=10, pady=10, sticky="nsew")

    opcionSeleccionada = StringVar(ventanaInicio)
    opcionSeleccionada.set(opciones[0])  # Set the default option

    def seleccionarOpcion(opcion):
        if opcion == "Inscribir asignaturas":
            mostrarInscribirAsignaturas()
        elif opcion == "Ver materias inscritas":
            mostrarMateriasInscritas()
        elif opcion == "Realizar calificacion de docente":
            mostrarCalificacionDocente()
        elif opcion == "Ver horario":
            mostrarHorario()
        elif opcion == "Ver perfil estudiante":
            mostrarPerfilEstudiante()
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

    def clearFrame():
        for widget in frameVentanaInicio.winfo_children():
            widget.destroy()

    def mostrarInscribirAsignaturas():
        clearFrame()
        # Code to create and display widgets for "Inscribir asignaturas" option
        label = Label(frameVentanaInicio, text="Inscribir asignaturas")
        label.config(font=("Times New Roman", 12, "bold"))
        label.pack()

    def mostrarMateriasInscritas():
        clearFrame()
        # Code to create and display widgets for "Ver materias inscritas" option
        label = Label(frameVentanaInicio, text="Ver materias inscritas")
        label.config(font=("Times New Roman", 12, "bold"))
        label.pack()

    def mostrarCalificacionDocente():
        clearFrame()
        # Code to create and display widgets for "Realizar calificacion de docente" option
        label = Label(frameVentanaInicio, text="Realizar calificacion de docente")
        label.config(font=("Times New Roman", 12, "bold"))
        label.pack()

    def mostrarHorario():
        clearFrame()
        # Code to create and display widgets for "Ver horario" option
        label = Label(frameVentanaInicio, text="Ver horario")
        label.config(font=("Times New Roman", 12, "bold"))
        label.pack()

    def mostrarPerfilEstudiante():
        clearFrame()
        # Code to create and display widgets for "Ver perfil estudiante" option
        label = Label(frameVentanaInicio, text="Ver perfil estudiante")
        label.config(font=("Times New Roman", 12, "bold"))
        label.pack()

    def mostrarMateriasCursadas():
        clearFrame()
        # Code to create and display widgets for "Materias cursadas anteriormente" option
        label = Label(frameVentanaInicio, text="Materias cursadas anteriormente")
        label.config(font=("Times New Roman", 12, "bold"))
        label.pack()

    def mostrarCalificacionDocente():
        clearFrame()
        # Code to create and display widgets for "Ver calificacion docente" option
        label = Label(frameVentanaInicio, text="Ver calificacion docente")
        label.config(font=("Times New Roman", 12, "bold"))
        label.pack()

    def volverAlMenuPrincipal():
        clearFrame()
        VentanaPrincipal()

    VentanaPrincipal()
    ventanaInicio.mainloop()


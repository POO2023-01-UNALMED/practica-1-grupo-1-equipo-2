from tkinter import *
from PIL import Image, ImageTk
from src_py.personas.Estudiante import Estudiante
from tkinter import Button

from src_py.Calendario.Facultad import Facultad
from src_py.Calendario.Materia import Materia


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

    def mostrarInscribirAsignaturas():
        clearFrame()
        from src_py.Calendario.gestionDatos import gestionDatos
        datos_sistema = gestionDatos()

        label = Label(frameVentanaInicio, text="Inscribir asignaturas")
        label.config(font=("Times New Roman", 12, "bold"))
        label.pack()

        label2 = Label(frameVentanaInicio, text="Seleccione las materias a inscribir:")
        label2.config(font=("Times New Roman", 12))
        label2.pack()

        materias_vars = {}  # Dictionary to store the subject checkbutton variables
        row_counter = 5  # Variable to keep track of the current row for grid positioning

        for i, materia in enumerate(datos_sistema.getMaterias()):
            var = BooleanVar()
            var.set(False)
            materias_vars[materia] = var
            Checkbutton(frameVentanaInicio, text=materia.getNombre(), variable=var).pack()

        def guardarSelecciones():
            materias_seleccionadas = [materia for materia, var in materias_vars.items() if var.get()]
            # Aquí puedes hacer lo que desees con las materias seleccionadas, como guardarlas en el estudiante, etc.
            estudiante.setMaterias_inscritas(materias_seleccionadas)
            print("Materias seleccionadas:", materias_seleccionadas)

        boton_guardar = Button(frameVentanaInicio, text="Guardar selecciones", command=guardarSelecciones)
        boton_guardar.pack(side=BOTTOM)

    def mostrarMateriasInscritas():
        clearFrame()
        label = Label(frameVentanaInicio, text="Ver materias inscritas")
        label.config(font=("Times New Roman", 12, "bold"))
        label.pack()
        label2 = Label(frameVentanaInicio, text="Estas son tus Materias Inscritas")
        label2.config(font=("Times New Roman", 12, "bold"))
        label2.pack()

        materias_inscritas = estudiante.getMaterias_inscritas()

        for i, materia in enumerate(materias_inscritas):
            label_materia = Label(frameVentanaInicio, text=f"{i + 1}. {materia.getNombre()}")
            label_materia.config(font=("Times New Roman", 12))
            label_materia.pack()

    def mostrarCalificacionDocente():
        clearFrame()
        label = Label(frameVentanaInicio, text="Realizar calificacion de docente")
        label.config(font=("Times New Roman", 12, "bold"))
        label.pack()

    def mostrarHorario():
        clearFrame()
        label = Label(frameVentanaInicio, text="Ver horario")
        label.config(font=("Times New Roman", 12, "bold"))
        label.pack()
        label2 = Label(frameVentanaInicio, text="Tu horario es:")
        label2.config(font=("Times New Roman", 12, "bold"))
        label2.pack()

        label_texto = Label(frameVentanaInicio, text=common.horario(), background="white")
        label_texto.config(font=("Times New Roman", 10, "bold"))
        label_texto.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")


    def mostrarMateriasCursadas():
        clearFrame()
        label = Label(frameVentanaInicio, text="Materias cursadas anteriormente")
        label.config(font=("Times New Roman", 12, "bold"))
        label.pack()

    def mostrarCalificacionDocente():
        clearFrame()
        label = Label(frameVentanaInicio, text="Ver calificacion docente")
        label.config(font=("Times New Roman", 12, "bold"))
        label.pack()

    def volverAlMenuPrincipal():
        clearFrame()
        VentanaPrincipal()

    VentanaPrincipal()
    ventanaInicio.mainloop()


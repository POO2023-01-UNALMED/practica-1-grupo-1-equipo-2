from tkinter import *
from PIL import Image, ImageTk
from src_py.Calendario.gestionDatos import gestionDatos
from src_py.baseDatos.Serializador import Serializador
from src_py.personas.Estudiante import Estudiante
from src_py.Calendario.Facultad import Facultad
from src_py.personas.Profesor import Profesor
from src_py.Calendario.Tarea import Tarea
import random
import sys
import tkinter as tk
import os
from PIL import ImageTk, Image
from tkinter import messagebox

# Crear la ventana principal
root = Tk()
root.title("Ventana de Inicio")
root.geometry("800x600")
root.configure(background="white")

root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)

# Función para convertir valores RGB a hexadecimal
def rgb_to_hex(rgb):
    return '#%02x%02x%02x' % rgb

# Convertir los valores RGB a hexadecimal
color_rgb = (148, 180, 59)
color_rgb1 =(166,28,49)
color_fondo =(177,178,176)
color_hex2 = rgb_to_hex(color_fondo)
color_hex1 =rgb_to_hex(color_rgb1)
color_hex = rgb_to_hex(color_rgb)


# Espacios de Frame
frame = Frame(root,background=color_hex, borderwidth=2, highlightthickness=2)
frame.grid(row=0, column=0, sticky="nsew")
frame2 = Frame(root,background=color_hex1, borderwidth=2, highlightthickness=2)
frame2.grid(row=0, column=1, sticky="nsew")
frame3 = Frame(root,background=color_hex1, borderwidth=2, highlightthickness=2)
frame3.grid(row=1, column=1, sticky="nsew")
frame4 = Frame(root,background=color_hex,borderwidth=2, highlightthickness=2)
frame4.grid(row=1, column=0, sticky="nsew")

# Configurar la cuadrícula de los frames
for i in range(2):
    root.grid_rowconfigure(i, weight=1)
    root.grid_columnconfigure(i, weight=1)

# Crear un label para el saludo de bienvenida
saludo = Label(frame, text="Bienvenido al Sistema de Gestión Universitaria",
               background="white")
saludo.config(font=("Times New Roman", 12, "bold"))
saludo.grid(row=0, column=0, padx=10, pady=10, sticky="n")

# Lista de títulos y textos
titulos = [" --> Juan <--", " --> Breadley <--", " --> Jhon <--", " --> Baena <--"]
textos = [
    """-- Estudiante de ING de Sistemas de la UNAL --\n
=> Gustos: Me gusta ayudar a los demas, 
superarme a mi mismo y siempre
ver todo con una sonrisa.\n
=> Virtudes: carismatico, fuerte en 
la solución de problemas, amante de
la programación orientada a objetos\n
=> Contacto: jtrejosg@unal.edu.co\n
""",
    """-- Estudiante de C. de la Computación de la UNAL --\n 
=> Gustos: Resolución de problemas, 
VideoJuegos competitivos, fútbol 
y el chocolate en grandes cantidades.\n
=> Virtudes: Amabilidad, estar atento a 
las necesidades de los demás, adaptable 
y con habilidad recursiva.\n 
=> Contacto: brmarinv@unal.edu.co\n""",
    """-- Estudiante de ING de Sistemas de la UNAL --\n
=> Gustos: los retos, ponen a prueba mi 
capacidad de solucionar problemas 
y me ayudan a crecer como persona.\n
=> Virtudes: Soy responsable, comprometido, 
bueno en la resolución de problemas
y en la comunicación con el equipo.\n
=> Contacto: jhpintoh@unal.edu.co\n""",
    """-- Estudiante de ING de Sistemas de la UNAL --\n
=> Gustos: aprender nuevas ideas sobre 
diversas áreas del conocimiento, 
también proponer soluciones a problemas.\n
=> Virtudes: facilidad para tomar decisiones,
y la adaptación rápida a nuevos entornos.\n 
=> Contacto: jubaenag@unal.edu.co\n"""
]

# Lista de imágenes
imagenes = [
    ImageTk.PhotoImage(Image.open("Images/imagen1.png").resize((150, 120)).convert("RGBA")),
    ImageTk.PhotoImage(Image.open("Images/imagen2.png").resize((150, 120)).convert("RGBA")),
    ImageTk.PhotoImage(Image.open("Images/imagen3.png").resize((150, 120)).convert("RGBA")),
    ImageTk.PhotoImage(Image.open("Images/imagen4.png").resize((150, 120)).convert("RGBA")),
]

# Variables para almacenar el índice actual
indice_actual = 0

# Función que cambia el título, el texto y las imágenes
def cambiar_texto():
    global indice_actual
    indice_actual = (indice_actual + 1) % len(titulos)
    tituloHojaVida.config(text=titulos[indice_actual])
    label_texto.config(text=textos[indice_actual])
    label_imagen.config(image=imagenes[indice_actual])
    label_imagen2.config(image=imagenes[(indice_actual + 1) % len(imagenes)])
    label_imagen3.config(image=imagenes[(indice_actual + 2) % len(imagenes)])
    label_imagen4.config(image=imagenes[(indice_actual + 3) % len(imagenes)])

# Configurar la cuadrícula del frame2
frame2.grid_rowconfigure(0, weight=1)
frame2.grid_rowconfigure(1, weight=1)
frame2.grid_columnconfigure(0, weight=1)

# Centrar los elementos dentro del frame2
tituloHojaVida = Label(frame2, text=titulos[indice_actual], background="white")
tituloHojaVida.config(font=("Times New Roman", 12, "bold"))
tituloHojaVida.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

label_texto = Label(frame2, text=textos[indice_actual], background="white")
label_texto.config(font=("Times New Roman", 10, "bold"))
label_texto.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")
label_texto.bind("<Button-1>", lambda event: cambiar_texto())

# Imágenes en labels de los desarrolladores
label_imagen = Label(frame3, image=imagenes[indice_actual])
label_imagen.grid(row=1, column=1, padx=10, pady=10, sticky="nsew")
label_imagen2 = Label(frame3, image=imagenes[(indice_actual + 1) % len(imagenes)])
label_imagen2.grid(row=1, column=2, padx=10, pady=10, sticky="nsew")
label_imagen3 = Label(frame3, image=imagenes[(indice_actual + 2) % len(imagenes)])
label_imagen3.grid(row=2, column=1, padx=10, pady=10, sticky="nsew")
label_imagen4 = Label(frame3, image=imagenes[(indice_actual + 3) % len(imagenes)])
label_imagen4.grid(row=2, column=2, padx=10, pady=10, sticky="nsew")

# Configurar el peso de las filas y columnas adicionales
frame3.grid_rowconfigure(0, weight=1)
frame3.grid_rowconfigure(3, weight=1)
frame3.grid_columnconfigure(0, weight=1)
frame3.grid_columnconfigure(3, weight=1)

# Crear imágenes asociadas al sistema
imagen_sis1 = ImageTk.PhotoImage(Image.open("Images/sis1.png").resize((100, 120)).convert("RGBA"))
imagen_sis2 = ImageTk.PhotoImage(Image.open("Images/sis2.png").resize((100, 120)).convert("RGBA"))
imagen_sis3 = ImageTk.PhotoImage(Image.open("Images/sis3.png").resize((100, 120)).convert("RGBA"))
imagen_sis4 = ImageTk.PhotoImage(Image.open("Images/sis4.png").resize((100, 120)).convert("RGBA"))
imagen_sis5 = ImageTk.PhotoImage(Image.open("Images/sis5.png").resize((100, 120)).convert("RGBA"))

# Imágenes en labels asociadas al sistema
label_imagen_sis1 = Label(frame4, image=imagen_sis1,highlightthickness=2)
label_imagen_sis1.grid(row=0, column=1, padx=5, pady=10, sticky="nsew")
label_imagen_sis2 = Label(frame4, image=imagen_sis2,highlightthickness=2)
label_imagen_sis2.grid(row=0, column=2, padx=5, pady=10, sticky="nsew")
label_imagen_sis3 = Label(frame4, image=imagen_sis3,highlightthickness=2)
label_imagen_sis3.grid(row=0, column=3, padx=5, pady=10, sticky="nsew")
label_imagen_sis4 = Label(frame4, image=imagen_sis4,highlightthickness=2)
label_imagen_sis4.grid(row=1, column=1, padx=5, pady=10, sticky="nsew")
label_imagen_sis5 = Label(frame4, image=imagen_sis5)
label_imagen_sis5.grid(row=1, column=3, padx=5, pady=10, sticky="nsew")

# Configurar el peso de las filas y columnas adicionales
frame4.grid_rowconfigure(0, weight=1)
frame4.grid_rowconfigure(2, weight=1)
frame4.grid_columnconfigure(0, weight=1)
frame4.grid_columnconfigure(4, weight=1)

def salir_aplicacion():
    root.destroy()

def mostrar_descripcion():
    messagebox.showinfo("Descripción del sistema", "El sistema es una aplicación diseñada para...")


# Crear el menú
menubar = tk.Menu(root)
root.config(menu=menubar)

# Menú Inicio
menu_inicio = tk.Menu(menubar, tearoff=0)
menu_inicio.add_command(label="Salir de la aplicación", command=salir_aplicacion)
menu_inicio.add_command(label="Descripción del sistema", command=mostrar_descripcion)

# Agregar los menús al menú principal
menubar.add_cascade(label="Inicio", menu=menu_inicio)

datos_sistema = gestionDatos()

datos_sistema.getSistemaBecas().asignar_estudiantes_beca()

for estudiante in datos_sistema.getEstudiantes():
    estudiante.aplicar_beca()

def salir_del_sistema(gestor):
    print("Proceso terminado")
    Serializador.serializar(gestor)


def menuEstudiante(estudiante: Estudiante):


    ventanaInicio = Tk()
    ventanaInicio.title("Información usuario")
    ventanaInicio.geometry("800x600")
    ventanaInicio.configure(background="white")

    datos_sistema1 = gestionDatos()

    estudiante.calcular_porcentaje_avance()

    for materia in estudiante.getMaterias_inscritas():
        tarea = Tarea("Example Task")
        grade = random.uniform(4.0, 5.0)
        tarea.set_grade(estudiante, grade)
        materia.inscribir_tarea(tarea)

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
        "Visualizar becados",
        "Volver al menu principal"
    ]

    def VentanaPrincipal():
        clearFrame()

        # Estilos
        font_title = ("Times New Roman", 10, "bold")
        font_label = ("Times New Roman", 10)

        # Nombre del Estudiante
        name_label = Label(frameVentanaInicio, text="Nombre del Estudiante:", font=font_title)
        name_label.grid(row=0, column=0, padx=10, pady=10, sticky="e")

        nombre = Label(frameVentanaInicio, text=estudiante.getNombre(), font=font_label)
        nombre.grid(row=0, column=1, padx=10, pady=10, sticky="w")

        # ID del Estudiante
        id_label = Label(frameVentanaInicio, text="ID del Estudiante:", font=font_title)
        id_label.grid(row=1, column=0, padx=10, pady=10, sticky="e")

        iD = Label(frameVentanaInicio, text=int(estudiante.getID()), font=font_label)
        iD.grid(row=1, column=1, padx=10, pady=10, sticky="w")

        # Correo del Estudiante
        correo_label = Label(frameVentanaInicio, text="Correo del Estudiante:", font=font_title)
        correo_label.grid(row=2, column=0, padx=10, pady=10, sticky="e")

        correo = Label(frameVentanaInicio, text=str(estudiante.getEmail()), font=font_label)
        correo.grid(row=2, column=1, padx=10, pady=10, sticky="w")

        # Promedio del estudiante
        Promedio_label = Label(frameVentanaInicio, text="Promedio actual del estudiante:", font=font_title)
        Promedio_label.grid(row=3, column=0, padx=10, pady=10, sticky="e")

        Promedio = Label(frameVentanaInicio, text=str(estudiante.calcular_promedio()), font=font_label)
        Promedio.grid(row=3, column=1, padx=10, pady=10, sticky="w")

        # Porcentaje de avance del estudiante
        Porcentaje_label = Label(frameVentanaInicio, text="Porcentaje de avance actual del estudiante:", font=font_title)
        Porcentaje_label.grid(row=4, column=0, padx=10, pady=10, sticky="e")



        Porcentaje = Label(frameVentanaInicio, text=str(estudiante.getPorcentaje_de_avance()), font=font_label)
        Porcentaje.grid(row=4, column=1, padx=10, pady=10, sticky="w")



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
                messagebox.showerror("Error!", "Por favor, escoja materias que desea inscribir.")
                ventanaInicio.destroy()
            elif estudiante.getMaterias_inscritas():
                messagebox.showerror("Error!", "Usted ya ha inscrito las materias para este semestre.")
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

                salir_del_sistema(datos_sistema)

                if not estudiante.getMaterias_inscritas():
                    messagebox.showerror("Erorr!",
                                         "Verifique que ya haya cursado el prerrequisito de las materias que intenta inscribir.")
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
        elif opcion == "Visualizar becados":
            visualizarBecados()
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
    def visualizarBecados():
            clearFrame()
            label = Label(frameVentanaInicio, text="Estudiantes seleccionados para Beca")
            label.config(font=("Times New Roman", 12, "bold"))
            label.pack()

            # Beca Inicial
            label1 = Label(frameVentanaInicio, text="Beca Inicial:", font=("Times New Roman", 12, "bold"))
            label1.pack()
            for becado in datos_sistema.getSistemaBecas().getEstudiantes_aptos_inicial():
                becado_label = Label(frameVentanaInicio, text=str(becado))
                becado_label.config(font=("Times New Roman", 12))
                becado_label.pack()

            # Beca Normal
            label2 = Label(frameVentanaInicio, text="Beca Normal:", font=("Times New Roman", 12, "bold"))
            label2.pack()
            for becado in datos_sistema.getSistemaBecas().getEstudiantes_aptos_normal():
                becado_label = Label(frameVentanaInicio, text=str(becado))
                becado_label.config(font=("Times New Roman", 12))
                becado_label.pack()

            # Beca Avanzada
            label3 = Label(frameVentanaInicio, text="Beca Avanzada:", font=("Times New Roman", 12, "bold"))
            label3.pack()
            for becado in datos_sistema.getSistemaBecas().getEstudiantes_aptos_avanzada():
                becado_label = Label(frameVentanaInicio, text=str(becado))
                becado_label.config(font=("Times New Roman", 12))
                becado_label.pack()

            # Botón para volver al menú principal
            volver_btn = Button(frameVentanaInicio, text="Volver al menú principal", command=volverAlMenuPrincipal)
            volver_btn.config(font=("Times New Roman", 12, "bold"))
            volver_btn.pack()
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

        # Verificar si el estudiante tiene materias inscritas
        if len(materias_inscritas) == 0:
            mensaje_label = Label(frameVentanaInicio, text="No tienes materias inscritas")
            mensaje_label.config(font=("Times New Roman", 12))
            mensaje_label.pack()

            # Agregar un botón para inscribir materias sugeridas
            inscribir_btn = Button(frameVentanaInicio, text="Inscribir materias sugeridas",
                                   command=inscribirMateriasSugeridas)
            inscribir_btn.config(font=("Times New Roman", 12, "bold"))
            inscribir_btn.pack()
        else:
            # Verificar si hay conflictos de horario
            if estudiante.comparar_horario(materias_inscritas):
                mensaje_label = Label(frameVentanaInicio, text="Hay conflictos de horario en las materias inscritas, por lo que hemos eliminado el conflicto")
                mensaje_label.config(font=("Times New Roman", 12))
                mensaje_label.pack()

                # Corregir el horario sugiriendo nuevas materias
                estudiante.sugerir_horario(falla_horario=True)

                # Obtener las materias inscritas actualizadas
                materias_inscritas = estudiante.getMaterias_inscritas()

                # Mostrar las materias inscritas actualizadas
                for materia in materias_inscritas:
                    materia_label = Label(frameVentanaInicio, text=materia.getNombre())
                    materia_label.config(font=("Times New Roman", 12, "bold"))
                    materia_label.pack()
            else:
                # Mostrar las materias inscritas
                for materia in materias_inscritas:
                    materia_label = Label(frameVentanaInicio, text=materia.getNombre())
                    materia_label.config(font=("Times New Roman", 12, "bold"))
                    materia_label.pack()

        # Botón para volver al menú principal
        volver_btn = Button(frameVentanaInicio, text="Volver al menú principal", command=volverAlMenuPrincipal)
        volver_btn.config(font=("Times New Roman", 12, "bold"))
        volver_btn.pack()

    def inscribirMateriasSugeridas():
        # Obtener las materias disponibles del sistema
        materias_disponibles = datos_sistema.getMaterias()

        # Inscribir las materias sugeridas
        estudiante.sugerir_materias(materias_disponibles)

        # Verificar si hay conflictos de horario en las materias inscritas
        if estudiante.comparar_horario(estudiante.getMaterias_inscritas()):
            # Corregir el horario sugiriendo nuevas materias
            estudiante.sugerir_horario(falla_horario=True)

        # Obtener las materias inscritas actualizadas
        materias_inscritas = estudiante.getMaterias_inscritas()

        # Limpiar la ventana
        clearFrame()

        # Verificar si el estudiante tiene materias inscritas después de la sugerencia
        if len(materias_inscritas) == 0:
            mensaje_label = Label(frameVentanaInicio, text="No se pudieron inscribir materias sugeridas")
            mensaje_label.config(font=("Times New Roman", 12))
            mensaje_label.pack()
        else:
            # Mostrar las materias inscritas actualizadas
            for materia in materias_inscritas:
                materia_label = Label(frameVentanaInicio, text=materia.getNombre())
                materia_label.config(font=("Times New Roman", 12, "bold"))
                materia_label.pack()

        # Botón para volver al menú principal
        volver_btn = Button(frameVentanaInicio, text="Volver al menú principal", command=volverAlMenuPrincipal)
        volver_btn.config(font=("Times New Roman", 12, "bold"))
        volver_btn.pack()

    selected_profesor = None  # Initialize selected_profesor variable globally

    def realizarCalificacionDocente():
        clearFrame()

        # Create a label at the top of the frame
        label_top = Label(frameVentanaInicio, text="Haga click sobre el docente que quisiera calificar")
        label_top.config(font=("Times New Roman", 12, "bold"))
        label_top.pack(fill=X, padx=10, pady=10)

        # Create a list of teacher names and a variable to store the selected teacher
        teacher_names = [profesor.getNombre() for profesor in estudiante.getProfesores_inscritos()]
        selected_teacher = None

        # Function to update the selected teacher when a button is clicked
        def update_selected_teacher(name):
            nonlocal selected_teacher
            for profesor in estudiante.getProfesores_inscritos():
                if profesor.getNombre() == name:
                    selected_teacher = profesor
                    break

            # Check if the student has already submitted a score for this teacher
            if selected_teacher in estudiante.getProfesores_calificados():
                messagebox.showerror("Error", "Ya has realizado la evaluación docente.")
                return

            # Clear the frame and create a new frame for entering the score
            clearFrame()
            label_calificacion = Label(frameVentanaInicio,
                                       text=f"Ingrese la calificación para el docente {selected_teacher.getNombre()}: ")
            label_calificacion.config(font=("Times New Roman", 12, "bold"))
            label_calificacion.pack(fill=X, padx=10, pady=10)

            entry_calificacion = Entry(frameVentanaInicio)
            entry_calificacion.pack(fill=X, padx=10, pady=10)

            btn_submit = Button(frameVentanaInicio, text="Enviar", command=lambda: submit(entry_calificacion))
            btn_submit.pack(fill=X, padx=10, pady=10)

            btn_back = Button(frameVentanaInicio, text="Atrás", command=realizarCalificacionDocente)
            btn_back.pack(fill=X, padx=10, pady=10)

        # Create buttons for each teacher
        for i, name in enumerate(teacher_names):
            button = Button(frameVentanaInicio, text=name, command=lambda name=name: update_selected_teacher(name))
            button.pack(fill=X, padx=10, pady=10)

        # Function to submit the score for the selected teacher
        def submit(entry_calificacion):
            calificacion = int(entry_calificacion.get())
            selected_teacher.ingresar_calificacion(calificacion)
            estudiante.addProfesor_calificado(selected_teacher)  # Add the selected teacher to the list of calificados
            success_label = Label(frameVentanaInicio, text="Calificación registrada correctamente")
            success_label.pack(fill=X, padx=10, pady=10)
            entry_calificacion.delete(0, END)

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
                dia = materia.getHorario()

                dia_label = Label(frameVentanaInicio, text=f"Día: {dia}")
                dia_label.config(font=("Times New Roman", 12, "bold"))
                dia_label.pack(pady=(0, 20))

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

        salir_del_sistema(datos_sistema)

    def mostrarCalificacionDocente():
        clearFrame()
        profesores = estudiante.getProfesores_inscritos()

        if not profesores:
            label_sin_calificaciones = Label(frameVentanaInicio, text="No se han registrado calificaciones de docentes")
            label_sin_calificaciones.config(font=("Times New Roman", 12, "bold"))
            label_sin_calificaciones.grid(row=0, column=0, padx=10, pady=10)
        else:
            for i, profesor in enumerate(profesores):
                calificacion = profesor.evaluacion_docente()
                if calificacion is None:
                    calificacion = "No disponible"
                label_calificacion = Label(frameVentanaInicio,
                                           text=f"{profesor.getNombre()}: Calificación actual del docente: {calificacion}")
                label_calificacion.config(font=("Times New Roman", 15))
                label_calificacion.grid(row=i, column=0, padx=10, pady=10)

        salir_del_sistema(datos_sistema)


    def volverAlMenuPrincipal():
        salir_del_sistema(datos_sistema)
        clearFrame()
        VentanaPrincipal()

    VentanaPrincipal()
    ventanaInicio.mainloop()

def ingresar_sistema():

    for widget in root.winfo_children():
        widget.destroy()

    # Eventos
    def sign_in():
        documento = documento_entry.get()
        if documento == "":
            messagebox.showerror("Error", "Para iniciar sesión, ingrese su documento en el espacio.")
        else:
            if documento in datos_sistema.getDocumentos():
                estudianteSeleccionado = None
                for estudiante in datos_sistema.getEstudiantes():
                    if estudiante.getID() == documento:
                        estudianteSeleccionado = estudiante
                        break
                menuEstudiante(estudianteSeleccionado)
            if int(documento) in datos_sistema.getDocumentosProfesores():
                profesorSeleccionado = None
                for profesor in datos_sistema.getProfesores():
                    if profesor.getID() == int(documento):
                        profesorSeleccionado = profesor
                        break
                menuProfesor(profesorSeleccionado)

            else:
                messagebox.showerror("Error", "Documento no registrado. Registrese antes de ingresar al sistema.")

    def sign_up():

        for widget in root.winfo_children():
            widget.destroy()

        def register():
            nombre = nombre_entry.get()
            documento = id_entry.get()
            email = email_entry.get()
            fue_becado = fue_becado_var.get()
            selected_materias = [materia.getNombre() for materia, var in materias_vars.items() if var.get()]
            materias_encontradas1 = []
            for materia_seleccionada in selected_materias:
                for materia in datos_sistema.getMaterias():
                    if materia_seleccionada == materia.getNombre():
                        materias_encontradas1.append(materia)

            if nombre == "" or documento == "" or email == "":
                messagebox.showerror("Error", "Por favor, rellene todos los espacios para registrarse.")
                #ventana_registro.destroy()
            elif documento in datos_sistema.getDocumentos():
                messagebox.showerror("Error", "El documento que estas tratando de ingresar ya ha sido registrado en el sistema.")
            else:
                datos_sistema.nuevoEstudiante(nombre, documento, email, fue_becado, materias_encontradas1)
                print("Selected Materias:", materias_encontradas1)
                for estudiante in datos_sistema.getEstudiantes():
                    print(estudiante.getID())
                print("Registro realizado con exito")
                salir_del_sistema(datos_sistema)

        registro_frame = Frame(root)
        registro_frame.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

        nombre_label = Label(registro_frame, text="Nombre:")
        nombre_label.grid(row=0, column=0, padx=10, pady=10)

        nombre_entry = Entry(registro_frame)
        nombre_entry.grid(row=0, column=1, padx=10, pady=10)

        id_label = tk.Label(registro_frame, text="ID:")
        id_label.grid(row=1, column=0, padx=10, pady=10)

        id_entry = tk.Entry(registro_frame)
        id_entry.grid(row=1, column=1, padx=10, pady=10)

        email_label = Label(registro_frame, text="Email:")
        email_label.grid(row=2, column=0, padx=10, pady=10)

        email_entry = Entry(registro_frame)
        email_entry.grid(row=2, column=1, padx=10, pady=10)

        fue_becado_var = BooleanVar()
        fue_becado_var.set(False)
        fue_becado_label = Label(registro_frame, text="¿Fue becado anteriormente?")
        fue_becado_label.grid(row=3, column=0, padx=10, pady=10)
        fue_becado_yes = Radiobutton(registro_frame, text="Sí", variable=fue_becado_var, value=True)
        fue_becado_yes.grid(row=3, column=1, padx=10, pady=10)
        fue_becado_no = Radiobutton(registro_frame, text="No", variable=fue_becado_var, value=False)
        fue_becado_no.grid(row=3, column=2, padx=10, pady=10)

        materias_label = tk.Label(registro_frame, text="Materias del programa académico:")
        materias_label.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

        materias_vars = {}  # Dictionary to store the subject checkbutton variables
        row_counter = 5  # Variable to keep track of the current row for grid positioning

        for i, materia in enumerate(datos_sistema.getMaterias()):
            var = tk.BooleanVar()
            var.set(False)
            materias_vars[materia] = var
            tk.Checkbutton(registro_frame, text=materia.getNombre(), variable=var).grid(row=row_counter, column=0,
                                                                                        columnspan=2, padx=10,
                                                                                     pady=5, sticky="w")
            row_counter += 1

        register_button = tk.Button(registro_frame, text="Registrarse", command=register)
        register_button.grid(row=row_counter, column=0, columnspan=3, padx=10, pady=10)

        registro_frame.tkraise()

    font = ("Times New Roman", 15, "bold")

    contenido_principal = Label(root, text="¡Bienvenido a la Ventana Principal del Sistema!", font=font)
    contenido_principal.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

    documento_label = Label(root, text="ID:", font=font)
    documento_label.grid(row=1, column=0, padx=10, pady=10)

    documento_entry = Entry(root, font=font)
    documento_entry.grid(row=1, column=1, padx=10, pady=10)

    sign_in_button = Button(root, text="Iniciar Sesión", font=font, command=sign_in)
    sign_in_button.grid(row=2, column=0, padx=10, pady=10)

    sign_up_button = Button(root, text="Registrarse", font=font, command=sign_up)
    sign_up_button.grid(row=2, column=1, padx=10, pady=10)


# Boton "ingresar"
boton_ingresar = Button(frame4, text="Ingresar", command=ingresar_sistema)
boton_ingresar.grid(row=4, column=2, padx=10, pady=10, sticky="s")


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
        if opcion == "Ver materias asignadas para el semestre actual":
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
                    nombre_label.config(
                        text=f"Nombre de la tarea: {entry_tarea_nombre.get()} quedo registrada correctamente")
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

                for tarea in materia.getTareas_de_materia():
                    label_tarea = Label(frameVentanaInicio, text=tarea)
                    label_tarea.config(font=("Times New Roman", 12))
                    label_tarea.pack()

                salir_del_sistema(datos_sistema)

            def on_button_4_click():
                clearFrame()
                nombre = Label(frameVentanaInicio, text=f"ingresar calificaciones en las tareas")
                nombre.config(font=("Times New Roman", 12))
                nombre.pack()

                nombre2 = Label(frameVentanaInicio, text=f"lista de tareas de la materia {materia.getNombre()}")
                nombre2.config(font=("Times New Roman", 12))
                nombre2.pack()

                for tarea in materia.getTareas_de_materia():
                    button_tarea = Button(frameVentanaInicio, text=tarea,
                                          command=lambda tarea=tarea: on_button_click(tarea))
                    button_tarea.pack()

                def on_button_click(tarea):
                    clearFrame()
                    for estudiante in materia.getEstudiantes_inscritos():
                        label_estudiante = Label(frameVentanaInicio, text=estudiante.getNombre())
                        label_estudiante.pack()
                        button_estudiante = Button(frameVentanaInicio, text=f"Enter grade for {estudiante.getNombre()}",
                                                   command=lambda estudiante=estudiante: on_student_button_click(
                                                       estudiante))
                        button_estudiante.pack()

                def on_student_button_click(estudiante):
                    clearFrame()
                    label = Label(frameVentanaInicio, text=f"Enter grade for {estudiante.getNombre()}")
                    label.pack()
                    entry = Entry(frameVentanaInicio)
                    entry.pack()
                    submit_button = Button(frameVentanaInicio, text="Submit",
                                           command=lambda: submit_grade(entry.get(), estudiante))
                    submit_button.pack()

                def submit_grade(grade, estudiante):
                    tarea.set_grade(estudiante, float(grade))
                    print(f"Grade entered for {estudiante.getNombre()}: {grade}")

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

    for estudiante in datos_sistema.getEstudiantes():
        for materia in estudiante.getMaterias_inscritas():
            tarea = Tarea("Example Task")
            for estudiante in materia.getEstudiantes_inscritos():
                grade = random.uniform(1.0, 5.0)
                tarea.set_grade(estudiante, grade)
            materia.inscribir_tarea(tarea)



    ventanaPrincipal()
    ventanaInicio.mainloop()


root.mainloop()
from tkinter import *
from PIL import Image, ImageTk
from src_py.Calendario.gestionDatos import gestionDatos
from src_py.baseDatos.Serializador import Serializador
from src_py.personas.Estudiante import Estudiante
from src_py.Calendario.Facultad import Facultad
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
=> Gustos: Amines, monas chinas y 
super fan de Boku no pico, además 
de siempre andar arrecho\n
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

def salir_del_sistema(gestor):
    print("Proceso terminado")
    Serializador.serializar(gestor)


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
                messagebox.showerror("Erorr!", "Por favor, escoja materias que desea inscribir.")
                ventanaInicio.destroy()
            elif estudiante.getMaterias_inscritas():
                messagebox.showerror("Erorr!", "Usted ya ha inscrito las materias para este semestre.")
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


    contenido_principal = Label(root, text="¡Bienvenido a la Ventana Principal del Sistema!")
    contenido_principal.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

    documento_label = Label(root, text="ID:")
    documento_label.grid(row=1, column=0, padx=10, pady=10)

    documento_entry = Entry(root)
    documento_entry.grid(row=1, column=1, padx=10, pady=10)

    sign_in_button = Button(root, text="Iniciar Sesion", command=sign_in)
    sign_in_button.grid(row=2, column=0, padx=10, pady=10)

    sign_up_button = Button(root, text="Registrarse", command=sign_up)
    sign_up_button.grid(row=2, column=1, padx=10, pady=10)

# Boton "ingresar"
boton_ingresar = Button(frame4, text="Ingresar", command=ingresar_sistema)
boton_ingresar.grid(row=4, column=2, padx=10, pady=10, sticky="s")

root.mainloop()

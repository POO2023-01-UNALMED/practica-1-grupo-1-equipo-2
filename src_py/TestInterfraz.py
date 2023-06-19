from tkinter import *
from PIL import Image, ImageTk
from src_py.Calendario.gestionDatos import gestionDatos
from src_py.baseDatos.Serializador import Serializador
from src_py.perfilEstudiante import *
import sys
import tkinter as tk
import os
from PIL import ImageTk, Image
from tkinter import messagebox

# Crear la ventana principal
root = Tk()
root.title("Ventana de Inicio")
root.geometry("800x600")
root.configure(background="light blue")

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
frame = Frame(root,background=color_hex,borderwidth=2,highlightthickness=2)
frame.grid(row=0, column=0, sticky="nsew")
frame2 = Frame(root,background=color_hex1,borderwidth=2,highlightthickness=2)
frame2.grid(row=0, column=1, sticky="nsew")
frame3 = Frame(root,background=color_hex1,borderwidth=2,highlightthickness=2)
frame3.grid(row=1, column=1, sticky="nsew")
frame4 = Frame(root,background=color_hex ,borderwidth=2,highlightthickness=2)
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
    """-- Estudiante de ING de Sistemas de la UNAL --
=> gustos:
=> Virtudes:
=> Contacto: Correo@unal.edu.co
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

def salir_del_sistema(gestor):
    print("Proceso terminado")
    # Serialize the 'gestor' object
    Serializador.serializar(gestor)
    # Exit the application
    sys.exit(0)

def ingresar_sistema():
    datos_sistema = gestionDatos()

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
                ventana_principal.destroy()
                menuEstudiante(estudianteSeleccionado)


            else:
                messagebox.showerror("Error", "Documento no registrado. Registrese antes de ingresar al sistema.")


    def sign_up():
        def register():
            nombre = nombre_entry.get()
            documento = id_entry.get()
            email = email_entry.get()
            fue_becado = fue_becado_var.get()
            selected_materias = [materia.getNombre() for materia, var in materias_vars.items() if var.get()]

            if nombre == "" or documento == "" or email == "":
                messagebox.showerror("Error", "Por favor, rellene todos los espacios para registrarse.")
                #ventana_registro.destroy()
            elif documento in datos_sistema.getDocumentos():
                messagebox.showerror("Error", "El documento que estas tratando de ingresar ya ha sido registrado en el sistema.")
            else:
                datos_sistema.nuevoEstudiante(nombre, documento, email, fue_becado, selected_materias)
                print("Selected Materias:", selected_materias)
                for estudiante in datos_sistema.getEstudiantes():
                    print(estudiante.getID())
                print("Registro realizado con exito")
                salir_del_sistema(datos_sistema)

        registro_frame = tk.Frame(root)
        registro_frame.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

        nombre_label = tk.Label(registro_frame, text="Nombre:")
        nombre_label.grid(row=0, column=0, padx=10, pady=10)

        nombre_entry = tk.Entry(registro_frame)
        nombre_entry.grid(row=0, column=1, padx=10, pady=10)

        id_label = tk.Label(registro_frame, text="ID:")
        id_label.grid(row=1, column=0, padx=10, pady=10)

        id_entry = tk.Entry(registro_frame)
        id_entry.grid(row=1, column=1, padx=10, pady=10)

        email_label = tk.Label(registro_frame, text="Email:")
        email_label.grid(row=2, column=0, padx=10, pady=10)

        email_entry = tk.Entry(registro_frame)
        email_entry.grid(row=2, column=1, padx=10, pady=10)

        fue_becado_var = tk.BooleanVar()
        fue_becado_var.set(False)
        fue_becado_label = tk.Label(registro_frame, text="¿Fue becado anteriormente?")
        fue_becado_label.grid(row=3, column=0, padx=10, pady=10)
        fue_becado_yes = tk.Radiobutton(registro_frame, text="Sí", variable=fue_becado_var, value=True)
        fue_becado_yes.grid(row=3, column=1, padx=10, pady=10)
        fue_becado_no = tk.Radiobutton(registro_frame, text="No", variable=fue_becado_var, value=False)
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

    ventana_principal = tk.Tk()
    ventana_principal.title("Ventana Principal del Sistema")

    contenido_principal = tk.Label(ventana_principal, text="¡Bienvenido a la Ventana Principal del Sistema!")
    contenido_principal.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

    documento_label = tk.Label(ventana_principal, text="ID:")
    documento_label.grid(row=1, column=0, padx=10, pady=10)

    documento_entry = tk.Entry(ventana_principal)
    documento_entry.grid(row=1, column=1, padx=10, pady=10)

    sign_in_button = tk.Button(ventana_principal, text="Iniciar Sesion", command=sign_in)
    sign_in_button.grid(row=2, column=0, padx=10, pady=10)

    sign_up_button = tk.Button(ventana_principal, text="Registrarse", command=sign_up)
    sign_up_button.grid(row=2, column=1, padx=10, pady=10)

    root.destroy()
    ventana_principal.mainloop()

# Boton "ingresar"
boton_ingresar = Button(frame4, text="Ingresar", command=ingresar_sistema)
boton_ingresar.grid(row=4, column=2, padx=10, pady=10, sticky="s")

root.mainloop()
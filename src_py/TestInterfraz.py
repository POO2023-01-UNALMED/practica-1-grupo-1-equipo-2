from tkinter import *
from PIL import Image, ImageTk

# Crear la ventana principal
root = Tk()
root.title("Ventana de Inicio")
root.geometry("800x600")

root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)

# Espacios de Frame
frame = Frame(root)
frame.grid(row=0, column=0, sticky="nsew")
frame2 = Frame(root)
frame2.grid(row=0, column=1, sticky="nsew")
frame3 = Frame(root)
frame3.grid(row=1, column=1, sticky="nsew")
frame4 = Frame(root)
frame4.grid(row=1, column=0, sticky="nsew")

# Configurar la cuadrícula de los frames
for i in range(2):
    root.grid_rowconfigure(i, weight=1)
    root.grid_columnconfigure(i, weight=1)

# Crear un label para el saludo de bienvenida
saludo = Label(frame, text="Bienvenido al Sistema de Gestión Universitaria")
saludo.grid(row=0, column=0, padx=10, pady=10, sticky="n")

# Lista de títulos y textos
titulos = ["Juan", "Breadley", "Jhon", "Baena"]
textos = [
    """Estudiante de ING de Sistemas de la UNAL
gustos:
Virtudes:
Contacto: Correo@unal.edu.co
""",
    """Estudiante de C. de la Computación de la UNAL 
gustos: jugar VideoJuegos, fútbol
Virtudes: Amable, Atento, Recursivo 
Contacto: brmarinv@unal.edu.co""",
    """Estudiante de ING de Sistemas de la UNAL 
gustos:
Virtudes:
Contacto: Correo@unal.edu.co""",
    """Estudiante de ING de Sistemas de la UNAL 
gustos:
Virtudes: 
Contacto: Correo@unal.edu.co"""
]

# Lista de imágenes
imagenes = [
    ImageTk.PhotoImage(Image.open("src_py/Images/imagen1.png").resize((100, 100))),
    ImageTk.PhotoImage(Image.open("src_py/Images/imagen2.png").resize((100, 100))),
    ImageTk.PhotoImage(Image.open("src_py/Images/imagen3.png").resize((100, 100))),
    ImageTk.PhotoImage(Image.open("src_py/Images/imagen4.png").resize((100, 100))),
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
tituloHojaVida = Label(frame2, text=titulos[indice_actual])
tituloHojaVida.grid(row=0, column=0, padx=10, pady=10, sticky="n")

label_texto = Label(frame2, text=textos[indice_actual])
label_texto.grid(row=1, column=0, padx=10, pady=1, sticky="nsew")
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
imagen_sis1 = ImageTk.PhotoImage(Image.open("src_py/Images/sis1.png").resize((100, 100)))
imagen_sis2 = ImageTk.PhotoImage(Image.open("src_py/Images/sis2.png").resize((100, 100)))
imagen_sis3 = ImageTk.PhotoImage(Image.open("src_py/Images/sis3.png").resize((100, 100)))
imagen_sis4 = ImageTk.PhotoImage(Image.open("src_py/Images/sis4.png").resize((100, 100)))
imagen_sis5 = ImageTk.PhotoImage(Image.open("src_py/Images/sis5.png").resize((100, 100)))

# Imágenes en labels asociadas al sistema
label_imagen_sis1 = Label(frame4, image=imagen_sis1)
label_imagen_sis1.grid(row=0, column=1, padx=1, pady=0, sticky="nsew")
label_imagen_sis2 = Label(frame4, image=imagen_sis2)
label_imagen_sis2.grid(row=0, column=2, padx=1, pady=0, sticky="nsew")
label_imagen_sis3 = Label(frame4, image=imagen_sis3)
label_imagen_sis3.grid(row=0, column=3, padx=1, pady=0, sticky="nsew")
label_imagen_sis4 = Label(frame4, image=imagen_sis4)
label_imagen_sis4.grid(row=1, column=1, padx=1, pady=0, sticky="nsew")
label_imagen_sis5 = Label(frame4, image=imagen_sis5)
label_imagen_sis5.grid(row=1, column=3, padx=1, pady=0, sticky="nsew")

# Configurar el peso de las filas y columnas adicionales
frame4.grid_rowconfigure(0, weight=1)
frame4.grid_rowconfigure(2, weight=1)
frame4.grid_columnconfigure(0, weight=1)
frame4.grid_columnconfigure(4, weight=1)


# Boton "ingresar"
boton_ingresar = Button(frame4, text="Ingresar")
boton_ingresar.grid(row=4, column=2, padx=10, pady=10, sticky="s")

root.mainloop()

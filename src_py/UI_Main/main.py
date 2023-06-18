from src_py.personas.Estudiante import Estudiante
from src_py.Calendario.Facultad import Facultad
from src_py.Calendario.Beca import Beca
from src_py.Calendario.Tarea import Tarea
from src_py.Calendario.Materia import Materia
from src_py.personas.Profesor import Profesor
from src_py.Calendario.gestionDatos import gestionDatos
from src_py.baseDatos.Serializador import Serializador
import sys
import tkinter as tk
import os
from PIL import ImageTk, Image
from tkinter import messagebox

if __name__ == "__main__":

    ventana = tk.Tk()
    ventana.geometry("600x400")
    ventana.title("Sistema Academico Universitario")

    hojas_de_vida = [
        "Desarrollador 1:\n\nBreve descripción de la experiencia y habilidades del desarrollador 1.",
        "Desarrollador 2:\n\nBreve descripción de la experiencia y habilidades del desarrollador 2.",
        "Desarrollador 3:\n\nBreve descripción de la experiencia y habilidades del desarrollador 3.",
        "Desarrollador 4:\n\nBreve descripción de la experiencia y habilidades del desarrollador 4.",

    ]


    def salir_del_sistema(gestor):
        print("Proceso terminado")
        # Serializar the 'gestor' object
        Serializador.serializador(gestor)
        # Exit the application
        sys.exit(0)

    def cambiar_hoja(event):
        global contador_hojas
        contador_hojas = (contador_hojas + 1) % len(hojas_de_vida)
        texto_hoja.config(text=hojas_de_vida[contador_hojas])

    def ingresar_sistema():
        datos_sistema = gestionDatos()

        #Eventos
        def sign_in():
            documento = documento_entry.get()
            if documento == "":
                messagebox.showerror("Error", "Para iniciar sesión, ingrese su documento en el espacio.")
            else:
                if documento in datos_sistema.getEstudiantes():
                    # Open a new window or perform desired actions for successful sign-in
                    messagebox.showinfo("Success", "Sign In successful! Opening new window...")
                    # Add your code here to open a new window or perform desired actions
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
                    ventana_registro.destroy()
                else:
                    datos_sistema.nuevoEstudiante(nombre, documento, email, fue_becado, selected_materias)
                    print("Selected Materias:", selected_materias)
                    print("Registro realizado con exito")
                    salir_del_sistema(datos_sistema)


            # Create the sign-up window
            ventana_registro = tk.Toplevel()
            ventana_registro.title("Registro")

            # Labels
            tk.Label(ventana_registro, text="Nombre:").grid(row=0, column=0, padx=10, pady=10)
            tk.Label(ventana_registro, text="ID:").grid(row=1, column=0, padx=10, pady=10)
            tk.Label(ventana_registro, text="Email:").grid(row=2, column=0, padx=10, pady=10)
            tk.Label(ventana_registro, text="¿Fue becado anteriormente?").grid(row=3, column=0, padx=10, pady=10)

            # Materias label
            materias_label = tk.Label(ventana_registro, text="Materias del programa académico:")
            materias_label.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

            # Entry fields
            nombre_entry = tk.Entry(ventana_registro)
            nombre_entry.grid(row=0, column=1, padx=10, pady=10)

            id_entry = tk.Entry(ventana_registro)
            id_entry.grid(row=1, column=1, padx=10, pady=10)

            email_entry = tk.Entry(ventana_registro)
            email_entry.grid(row=2, column=1, padx=10, pady=10)

            # Radio buttons for "Fue becado anteriormente?"
            fue_becado_var = tk.BooleanVar()
            fue_becado_var.set(False)
            tk.Radiobutton(ventana_registro, text="Sí", variable=fue_becado_var, value=True).grid(row=3, column=1,
                                                                                                  padx=10, pady=10)
            tk.Radiobutton(ventana_registro, text="No", variable=fue_becado_var, value=False).grid(row=3, column=2,
                                                                                                   padx=10, pady=10)

            #Checkbuttons for subjects
            materias_vars = {}  # Dictionary to store the subject checkbutton variables
            row_counter = 6  # Variable to keep track of the current row for grid positioning

            for i, materia in enumerate(datos_sistema.getMaterias()):
                var = tk.BooleanVar()
                var.set(False)
                materias_vars[materia] = var
                tk.Checkbutton(ventana_registro, text=materia.getNombre(), variable=var).grid(row=row_counter, column=0,
                                                                                             columnspan=2, padx=10,
                                                                                             pady=5, sticky="w")
                row_counter += 1

            # Register button
            register_button = tk.Button(ventana_registro, text="Registrarse", command=register)
            register_button.grid(row=row_counter, column=0, columnspan=3, padx=10, pady=10)

            # Show materias button
            #show_materias_button = tk.Button(ventana_registro, text="Mostrar materias", command=show_materias)
            #show_materias_button.grid(row=7, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

            ventana_registro.mainloop()

        ventana.destroy()
        ventana_principal = tk.Tk()
        ventana_principal.geometry("600x400")

        #Etiquetas
        contenido_principal = tk.Label(ventana_principal, text="¡Bienvenido a la Ventana Principal del Sistema!")
        contenido_principal.pack(padx=10, pady=10)

        # "Documento" label
        documento_label = tk.Label(ventana_principal, text="ID:")
        documento_label.pack(pady=10)

        # Entry field for the document
        documento_entry = tk.Entry(ventana_principal)
        documento_entry.pack(pady=10)

        #Espacios de Inicio de Sesion
        sign_in_button = tk.Button(ventana_principal, text="Sign In", command=sign_in)
        sign_in_button.pack(pady=10)

        sign_up_button = tk.Button(ventana_principal, text="Sign Up", command=sign_up)
        sign_up_button.pack(pady=10)

        ventana_principal.mainloop()

    def salir_aplicacion():
        ventana.destroy()

    def mostrar_descripcion():
        messagebox.showinfo("Descripción del sistema", "El sistema es una aplicación diseñada para...")

    # Crear el menú
    menubar = tk.Menu(ventana)
    ventana.config(menu=menubar)


    # Menú Inicio
    menu_inicio = tk.Menu(menubar, tearoff=0)
    menu_inicio.add_command(label="Salir de la aplicación", command=salir_aplicacion)
    menu_inicio.add_command(label="Descripción del sistema", command=mostrar_descripcion)

    # Agregar los menús al menú principal
    menubar.add_cascade(label="Inicio", menu=menu_inicio)

    # Etiqueta para mostrar el contenido de la ventana principal
    contenido_principal = tk.Label(ventana, text="¡Bienvenido a la Ventana Principal del Usuario!")
    contenido_principal.pack(padx=10, pady=10)

    # Crear una etiqueta para mostrar el saludo de bienvenida
    saludo = tk.Label(ventana, text="¡Bienvenido al sistema!")
    saludo.pack(anchor="nw", padx=10,
                pady=10)  # Posicionamiento en la esquina superior izquierda con un espacio de margen

    texto_hoja = tk.Label(ventana, text=hojas_de_vida[0], justify="left")
    texto_hoja.pack(anchor="ne", padx=10,
                    pady=10)  # Posicionamiento en la esquina superior derecha con un espacio de margen

    # Contador para rastrear la hoja de vida actual
    contador_hojas = 0

    # Asociar la función de cambio de hoja al evento de clic del ratón
    texto_hoja.bind("<Button-1>", cambiar_hoja)

    # Etiqueta para mostrar el saludo de bienvenida
    saludo = tk.Label(ventana, text="¡Bienvenido al sistema!")
    saludo.pack(anchor="nw", padx=10, pady=10)

    # Botón para ingresar al sistema
    boton_ingresar = tk.Button(ventana, text="Ingresar", command=ingresar_sistema)
    boton_ingresar.pack(side="bottom", padx=10, pady=10)

    # Ejecutar el bucle principal de la ventana
    ventana.mainloop()



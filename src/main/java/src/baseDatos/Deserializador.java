package baseDatos;

import java.io.FileInputStream;
import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;
import java.io.IOException;
import java.io.ObjectInput;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.util.ArrayList;
import java.util.List;

import uiMain.Main;
import gestorAplicacion.*;
import gestorAplicacion.Calendario.Beca;
import gestorAplicacion.Calendario.Facultad;
import gestorAplicacion.Calendario.Horario;
import gestorAplicacion.Calendario.Materia;
import gestorAplicacion.Calendario.Tarea;
import gestorAplicacion.Calendario.TareaEstudiante;
import gestorAplicacion.Calendario.gestionDatos;
import gestorAplicacion.personas.Estudiante;
import gestorAplicacion.personas.Persona;
import gestorAplicacion.personas.Profesor;


public class Deserializador{

    public static void deserializar(gestionDatos gestor) {
    	deserializarEstudiantes(gestor,new File("src\\baseDatos\\temp\\Estudiantes.txt"));
    	deserializarProfesores(gestor,new File("src\\baseDatos\\temp\\Profesores.txt"));
    	deserializarMaterias(gestor,new File("src\\baseDatos\\temp\\Materias.txt"));
    	deserializarBeca(gestor,new File("src\\baseDatos\\temp\\Beca.txt"));
    }

    public static void deserializarEstudiantes(gestionDatos gestor, File ruta) {
        try {
            FileInputStream file = new FileInputStream(ruta);
            ObjectInputStream in = new ObjectInputStream(file);
            gestor.setEstudiantes((ArrayList<Estudiante>) in.readObject());

        } catch (IOException | ClassNotFoundException e) {
            System.out.println("Error en la serializacion" + e);
        }
    }

    public static void deserializarProfesores(gestionDatos gestor, File ruta) {
        try {
            FileInputStream file = new FileInputStream(ruta);
            ObjectInputStream in = new ObjectInputStream(file);
            gestor.setProfesores((ArrayList<Profesor>) in.readObject());

        } catch (IOException | ClassNotFoundException e) {
            System.out.println("Error en la serializacion" + e);
        }
    }

    public static void deserializarMaterias(gestionDatos gestor, File ruta) {
        try {
            FileInputStream file = new FileInputStream(ruta);
            ObjectInputStream in = new ObjectInputStream(file);
            gestor.setMaterias((ArrayList<Materia>) in.readObject());

        } catch (IOException | ClassNotFoundException e) {
            System.out.println("Error en la serializacion" + e);
        }
    }

    public static void deserializarBeca(gestionDatos gestor, File ruta) {
        try {
            FileInputStream file = new FileInputStream(ruta);
            ObjectInputStream in = new ObjectInputStream(file);
            gestor.setSistemaBecas((Beca) in.readObject());

        } catch (IOException | ClassNotFoundException e) {
            System.out.println("Error en la serializacion" + e);
        }
    }

}



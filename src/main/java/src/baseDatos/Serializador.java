package baseDatos;

import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.ObjectOutputStream;
import java.io.PrintWriter;
import java.util.ArrayList;

import gestorAplicacion.personas.*;
import gestorAplicacion.Calendario.*;


public class Serializador {

	    public static void serializar(gestionDatos gestor) {
	    	serializarEstudiantes(gestor,new File("src\\baseDatos\\temp\\Estudiantes.txt"));
	    	serializarProfesores(gestor,new File("src\\baseDatos\\temp\\Profesores.txt"));
	    	serializarMaterias(gestor,new File("src\\baseDatos\\temp\\Materias.txt"));
	    	serializarBeca(gestor,new File("src\\baseDatos\\temp\\Beca.txt"));
	    }

	    public static void serializarEstudiantes(gestionDatos gestor, File ruta) {
	        try {
	            PrintWriter pw = new PrintWriter(ruta);
	            FileOutputStream file = new FileOutputStream(ruta);
	            ObjectOutputStream out = new ObjectOutputStream(file);
	            out.writeObject(gestor.getEstudiantes());
	            out.close();
	            file.close();

	        } catch (IOException e) {
	            System.out.println("Error en la serializacion" + e);
	        }
	    }

	    public static void serializarProfesores(gestionDatos gestor, File ruta) {
	        try {
	            PrintWriter pw = new PrintWriter(ruta);
	            FileOutputStream file = new FileOutputStream(ruta);
	            ObjectOutputStream out = new ObjectOutputStream(file);
	            out.writeObject(gestor.getProfesores());
	            out.close();
	            file.close();

	        } catch (IOException e) {
	            System.out.println("Error en la serializacion" + e);
	        }
	    }

	    public static void serializarMaterias(gestionDatos gestor, File ruta) {
	        try {
	            PrintWriter pw = new PrintWriter(ruta);
	            FileOutputStream file = new FileOutputStream(ruta);
	            ObjectOutputStream out = new ObjectOutputStream(file);
	            
	            
	            out.writeObject(gestor.getMaterias());
	            out.close();
	            file.close();

	        } catch (IOException e) {
	            System.out.println("Error en la serializacion" + e);
	        }
	    }

	    public static void serializarBeca(gestionDatos gestor, File ruta) {
	        try {
	            PrintWriter pw = new PrintWriter(ruta);
	            FileOutputStream file = new FileOutputStream(ruta);
	            ObjectOutputStream out = new ObjectOutputStream(file);
	            out.writeObject(gestor.getSistemaBecas());
	            out.close();
	            file.close();

	        } catch (IOException e) {
	            System.out.println("Error en la serializacion" + e);
	        }
	    }

	}



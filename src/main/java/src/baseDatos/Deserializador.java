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
	/** 
	static File file = new File("");
	    
	 public static ArrayList<Beca> deserializarBecas(){
	        try {
	            FileInputStream f = new FileInputStream(new File(file.getAbsolutePath()+
	                    "\\src\\baseDatos\\temp\\Becas.txt"));
	            ObjectInputStream o = new ObjectInputStream(f);

	            ArrayList<Beca> listaDeBecas = (ArrayList) o.readObject();

	            f.close();
	            o.close();
	            return listaDeBecas;

	        }catch(FileNotFoundException e){
	            return new ArrayList<Beca>();
	        }
	        catch(IOException e){
	            return new ArrayList<Beca>();
	        }
	        catch(ClassNotFoundException e) {
	            return new ArrayList<Beca>();
	        }
	    }
	 public static ArrayList<Facultad> deserializarFacultades(){
	        try {
	            FileInputStream f = new FileInputStream(new File(file.getAbsolutePath()+
	                    "\\src\\baseDatos\\temp\\Facultades.txt"));
	            ObjectInputStream o = new ObjectInputStream(f);

	            ArrayList<Facultad> listaDeFacultades = (ArrayList) o.readObject();

	            f.close();
	            o.close();
	            return listaDeFacultades;

	        }catch(FileNotFoundException e){
	            return new ArrayList<Facultad>();
	        }
	        catch(IOException e){
	            return new ArrayList<Facultad>();
	        }
	        catch(ClassNotFoundException e) {
	            return new ArrayList<Facultad>();
	        }
	    }
	 public static ArrayList<Horario> deserializarHorarios(){
	        try {
	            FileInputStream f = new FileInputStream(new File(file.getAbsolutePath()+
	                    "\\src\\baseDatos\\temp\\Horarios.txt"));
	            ObjectInputStream o = new ObjectInputStream(f);

	            ArrayList<Horario> listaDeHorarios = (ArrayList) o.readObject();

	            f.close();
	            o.close();
	            return listaDeHorarios;

	        }catch(FileNotFoundException e){
	            return new ArrayList<Horario>();
	        }
	        catch(IOException e){
	            return new ArrayList<Horario>();
	        }
	        catch(ClassNotFoundException e) {
	            return new ArrayList<Horario>();
	        }
	    }

	 public static ArrayList<Materia> deserializarMaterias(){
	        try {
	            FileInputStream f = new FileInputStream(new File(file.getAbsolutePath()+
	                    "\\src\\baseDatos\\temp\\Materias.txt"));
	            ObjectInputStream o = new ObjectInputStream(f);

	            ArrayList<Materia> listaDeMaterias = (ArrayList) o.readObject();

	            f.close();
	            o.close();
	            return listaDeMaterias;

	        }catch(FileNotFoundException e){
	            return new ArrayList<Materia>();
	        }
	        catch(IOException e){
	            return new ArrayList<Materia>();
	        }
	        catch(ClassNotFoundException e) {
	            return new ArrayList<Materia>();
	        }
	    }

	 public static ArrayList<Tarea> deserializarTareas(){
	        try {
	            FileInputStream f = new FileInputStream(new File(file.getAbsolutePath()+
	                    "\\src\\baseDatos\\temp\\Tareas.txt"));
	            ObjectInputStream o = new ObjectInputStream(f);

	            ArrayList<Tarea> listaDeTareas = (ArrayList) o.readObject();

	            f.close();
	            o.close();
	            return listaDeTareas;

	        }catch(FileNotFoundException e){
	            return new ArrayList<Tarea>();
	        }
	        catch(IOException e){
	            return new ArrayList<Tarea>();
	        }
	        catch(ClassNotFoundException e) {
	            return new ArrayList<Tarea>();
	        }
	    }

	 public static ArrayList<TareaEstudiante> deserializarTareaEstudiante(){
	        try {
	            FileInputStream f = new FileInputStream(new File(file.getAbsolutePath()+
	                    "\\src\\baseDatos\\temp\\TareaEstudiante.txt"));
	            ObjectInputStream o = new ObjectInputStream(f);

	            ArrayList<TareaEstudiante> listaDeTareaEstudiante = (ArrayList) o.readObject();

	            f.close();
	            o.close();
	            return listaDeTareaEstudiante;

	        }catch(FileNotFoundException e){
	            return new ArrayList<TareaEstudiante>();
	        }
	        catch(IOException e){
	            return new ArrayList<TareaEstudiante>();
	        }
	        catch(ClassNotFoundException e) {
	            return new ArrayList<TareaEstudiante>();
	        }
	    }

	 public static ArrayList<Persona> deserializarPersona(){
	        try {
	            FileInputStream f = new FileInputStream(new File(file.getAbsolutePath()+
	                    "\\src\\baseDatos\\temp\\Personas.txt"));
	            ObjectInputStream o = new ObjectInputStream(f);

	            ArrayList<Persona> listaDePersonas = (ArrayList) o.readObject();

	            f.close();
	            o.close();
	            return listaDePersonas;

	        }catch(FileNotFoundException e){
	            return new ArrayList<Persona>();
	        }
	        catch(IOException e){
	            return new ArrayList<Persona>();
	        }
	        catch(ClassNotFoundException e) {
	            return new ArrayList<Persona>();
	        }
	    }

	 public static ArrayList<Estudiante> deserializarEstudiantes(){
	        try {
	            FileInputStream f = new FileInputStream(new File(file.getAbsolutePath()+
	                    "\\src\\baseDatos\\temp\\Estudiantes.txt"));
	            ObjectInputStream o = new ObjectInputStream(f);

	            ArrayList<Estudiante> listaDeEstudiantes = (ArrayList) o.readObject();

	            f.close();
	            o.close();
	            return listaDeEstudiantes;

	        }catch(FileNotFoundException e){
	            return new ArrayList<Estudiante>();
	        }
	        catch(IOException e){
	            return new ArrayList<Estudiante>();
	        }
	        catch(ClassNotFoundException e) {
	            return new ArrayList<Estudiante>();
	        }
	    }

	 public static ArrayList<Profesor> deserializarProfesores(){
	        try {
	            FileInputStream f = new FileInputStream(new File(file.getAbsolutePath()+
	                    "\\src\\baseDatos\\temp\\Profesores.txt"));
	            ObjectInputStream o = new ObjectInputStream(f);

	            ArrayList<Profesor> listaDeProfesores = (ArrayList) o.readObject();

	            f.close();
	            o.close();
	            return listaDeProfesores;

	        }catch(FileNotFoundException e){
	            return new ArrayList<Profesor>();
	        }
	        catch(IOException e){
	            return new ArrayList<Profesor>();
	        }
	        catch(ClassNotFoundException e) {
	            return new ArrayList<Profesor>();
	        }
	    }
	**/
	private static File rutaTemp =  new File("src\\main\\practica1\\src\\baseDatos\\temp");
	
	public static void deserializar(gestionDatos gestor) {
		File[] docs = rutaTemp.listFiles();
		FileOutputStream fis;
		ObjectOutputStream ois;
		
		for (File file : docs) {
			if (file.getAbsolutePath().contains("estudiantes")) {
				try {
					fis = new FileOutputStream(file);
					ois = new ObjectOutputStream(fis);
					gestor.setEstudiantes((List<Estudiante>) ((ObjectInput) ois).readObject());
					
				} catch (FileNotFoundException e) {
					e.printStackTrace();
				} catch (IOException e) {
					e.printStackTrace();
				}
				catch (ClassNotFoundException e) {
					e.printStackTrace();
				}
			}
			else if (file.getAbsolutePath().contains("materias")) {
				try {
					fis = new FileOutputStream(file);
					ois = new ObjectOutputStream(fis);
					gestor.setMaterias((List<Materia>) ((ObjectInput) ois).readObject());
					
				} catch (FileNotFoundException e) {
					e.printStackTrace();
				} catch (IOException e) {
					e.printStackTrace();
				}
				catch (ClassNotFoundException e) {
					e.printStackTrace();
				}
			}
			else if (file.getAbsolutePath().contains("profesores")) {
				try {
					fis = new FileOutputStream(file);
					ois = new ObjectOutputStream(fis);
					gestor.setProfesores((List<Profesor>) ((ObjectInput) ois).readObject());
					
				} catch (FileNotFoundException e) {
					e.printStackTrace();
				} catch (IOException e) {
					e.printStackTrace();
				}
				catch (ClassNotFoundException e) {
					e.printStackTrace();
				}
			}
			else if (file.getAbsolutePath().contains("sistemaBecas")) {
				try {
					fis = new FileOutputStream(file);
					ois = new ObjectOutputStream(fis);
					gestor.setSistemaBecas((Beca) ((ObjectInput) ois).readObject());
					
				} catch (FileNotFoundException e) {
					e.printStackTrace();
				} catch (IOException e) {
					e.printStackTrace();
				}
				catch (ClassNotFoundException e) {
					e.printStackTrace();
				}
			}
		}
	}
}


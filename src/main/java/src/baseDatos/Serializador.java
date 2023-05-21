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
	/**
	static File file = new File ("");
	
	
	public static void serializarBecas(ArrayList<Beca> listaDeBecas) {
		try {
            FileOutputStream f = new FileOutputStream(new File(file.getAbsolutePath()+
                    "\\src\\baseDatos\\temp\\Becas.txt"));
            ObjectOutputStream o = new ObjectOutputStream(f);

            o.writeObject(listaDeBecas);

            o.close();
            f.close();

        }catch(FileNotFoundException e){
            System.out.println("No se encuentra el archivo"+e.getMessage());
        }
        catch(IOException e) {
            System.out.println("No se encuentra en archivo");
        }

    }
	
	public static void serializarFacultades(ArrayList<Facultad> listaDeFacultades) {
		try {
            FileOutputStream f = new FileOutputStream(new File(file.getAbsolutePath()+
                    "\\src\\baseDatos\\temp\\Facultades.txt"));
            ObjectOutputStream o = new ObjectOutputStream(f);

            o.writeObject(listaDeFacultades);

            o.close();
            f.close();

        }catch(FileNotFoundException e){
            System.out.println("No se encuentra el archivo"+e.getMessage());
        }
        catch(IOException e) {
            System.out.println("No se encuentra en archivo");
        }

    }
	
	public static void serializarHorarios(ArrayList<Horario> listaDeHorarios) {
		try {
            FileOutputStream f = new FileOutputStream(new File(file.getAbsolutePath()+
                    "\\src\\baseDatos\\temp\\Horarios.txt"));
            ObjectOutputStream o = new ObjectOutputStream(f);

            o.writeObject(listaDeHorarios);

            o.close();
            f.close();

        }catch(FileNotFoundException e){
            System.out.println("No se encuentra el archivo"+e.getMessage());
        }
        catch(IOException e) {
            System.out.println("No se encuentra en archivo");
        }

    }
	
	public static void serializarMaterias(ArrayList<Materia> listaDeMaterias) {
		try {
            FileOutputStream f = new FileOutputStream(new File(file.getAbsolutePath()+
                    "\\src\\baseDatos\\temp\\Materias.txt"));
            ObjectOutputStream o = new ObjectOutputStream(f);

            o.writeObject(listaDeMaterias);

            o.close();
            f.close();

        }catch(FileNotFoundException e){
            System.out.println("No se encuentra el archivo"+e.getMessage());
        }
        catch(IOException e) {
            System.out.println("No se encuentra en archivo");
        }

    }
	
	public static void serializarTareas(ArrayList<Tarea> listaDeTareas) {
		try {
            FileOutputStream f = new FileOutputStream(new File(file.getAbsolutePath()+
                    "\\src\\baseDatos\\temp\\Tareas.txt"));
            ObjectOutputStream o = new ObjectOutputStream(f);

            o.writeObject(listaDeTareas);

            o.close();
            f.close();

        }catch(FileNotFoundException e){
            System.out.println("No se encuentra el archivo"+e.getMessage());
        }
        catch(IOException e) {
            System.out.println("No se encuentra en archivo");
        }

    }

	public static void serializarTareaEstudiante(ArrayList<TareaEstudiante> listaDeTareaEstudiante) {
		try {
            FileOutputStream f = new FileOutputStream(new File(file.getAbsolutePath()+
                    "\\src\\baseDatos\\temp\\TareaEstudiante.txt"));
            ObjectOutputStream o = new ObjectOutputStream(f);

            o.writeObject(listaDeTareaEstudiante);

            o.close();
            f.close();

        }catch(FileNotFoundException e){
            System.out.println("No se encuentra el archivo"+e.getMessage());
        }
        catch(IOException e) {
            System.out.println("No se encuentra en archivo");
        }

    }

	public static void serializarPersona(ArrayList<Persona> listaDePersonas) {
		try {
            FileOutputStream f = new FileOutputStream(new File(file.getAbsolutePath()+
                    "\\src\\baseDatos\\temp\\Personas.txt"));
            ObjectOutputStream o = new ObjectOutputStream(f);

            o.writeObject(listaDePersonas);

            o.close();
            f.close();

        }catch(FileNotFoundException e){
            System.out.println("No se encuentra el archivo"+e.getMessage());
        }
        catch(IOException e) {
            System.out.println("No se encuentra en archivo");
        }

    }

	public static void serializarEstudiantes(ArrayList<Estudiante> listaDeEstudiantes) {
		try {
            FileOutputStream f = new FileOutputStream(new File(file.getAbsolutePath()+
                    "\\src\\baseDatos\\temp\\Estudiantes.txt"));
            ObjectOutputStream o = new ObjectOutputStream(f);

            o.writeObject(listaDeEstudiantes);

            o.close();
            f.close();

        }catch(FileNotFoundException e){
            System.out.println("No se encuentra el archivo"+e.getMessage());
        }
        catch(IOException e) {
            System.out.println("No se encuentra en archivo");
        }

    }

	public static void serializarProfesores(ArrayList<Profesor> listaDeProfesores) {
		try {
            FileOutputStream f = new FileOutputStream(new File(file.getAbsolutePath()+
                    "\\src\\baseDatos\\temp\\Profesores.txt"));
            ObjectOutputStream o = new ObjectOutputStream(f);

            o.writeObject(listaDeProfesores);

            o.close();
            f.close();

        }catch(FileNotFoundException e){
            System.out.println("No se encuentra el archivo"+e.getMessage());
        }
        catch(IOException e) {
            System.out.println("No se encuentra en archivo");
        }

    }
	**/
	private static File rutaTemp = new File("src//baseDatos//temp");

	public static void serializar(gestionDatos gestor) {
		FileOutputStream fos;
		ObjectOutputStream oos;
		File[] docs = rutaTemp.listFiles();
		PrintWriter pw;
		
		for (File file : docs) {
			try {
				pw = new PrintWriter(file);
			}
			
			catch (FileNotFoundException e) {
				e.printStackTrace();
			}
		
		}
		
		for (File file : docs) {
			if (file.getAbsolutePath().contains("estudiantes")) {
				try {
					fos = new FileOutputStream(file);
					oos = new ObjectOutputStream(fos);
					oos.writeObject(gestor.getEstudiantes());
				} catch (FileNotFoundException e) {
					e.printStackTrace();
				} catch (IOException e) {
					e.printStackTrace();
				}
			}
			else if(file.getAbsolutePath().contains("materias")) {
				try {
					fos = new FileOutputStream(file);
					oos = new ObjectOutputStream(fos);
					oos.writeObject(gestor.getMaterias());
				} catch (FileNotFoundException e) {
					e.printStackTrace();
				} catch (IOException e) {
					e.printStackTrace();
				}
			}
			else if(file.getAbsolutePath().contains("profesores")) {
				try {
					fos = new FileOutputStream(file);
					oos = new ObjectOutputStream(fos);
					oos.writeObject(gestor.getProfesores());
				} catch (FileNotFoundException e) {
					e.printStackTrace();
				} catch (IOException e) {
					e.printStackTrace();
				}
			}
			else if(file.getAbsolutePath().contains("sistemaBecas")) {
				try {
					fos = new FileOutputStream(file);
					oos = new ObjectOutputStream(fos);
					oos.writeObject(gestor.getSistemaBecas());
				} catch (FileNotFoundException e) {
					e.printStackTrace();
				} catch (IOException e) {
					e.printStackTrace();
				}
			}
		}
	}
}


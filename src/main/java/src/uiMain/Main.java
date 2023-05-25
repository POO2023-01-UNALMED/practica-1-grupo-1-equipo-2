package uiMain;

import java.util.ArrayList;
import java.util.InputMismatchException;
import java.util.Scanner;

import baseDatos.Deserializador;
import baseDatos.Serializador;
import gestorAplicacion.*;
import gestorAplicacion.Calendario.Materia;
import gestorAplicacion.Calendario.Tarea;
import gestorAplicacion.Calendario.gestionDatos;
import gestorAplicacion.Calendario.Beca;
import gestorAplicacion.personas.Estudiante;
import gestorAplicacion.personas.Profesor;

public class Main {


	static Scanner sc = new Scanner(System.in);
	static long readLong() {
		return sc.nextLong();
	}
	static String readln() {
		sc.nextLine();
		return sc.nextLine();
	}
	private static void salirDelSistema(gestionDatos gestor) {
		System.out.println("Proceso terminado");
		Serializador.serializar(gestor);
		System.exit(0);
	}
	static void isncripcionEstudiante(gestionDatos gestor) {
		System.out.println("Nombre: ");
		String nombre = readln();
		
		System.out.println("ID: ");
		int ID = (int) readLong();
		
		System.out.println("Email: ");
		String Email = readln();

		
		System.out.println("¿Fue becado anteriormente?: ");
		System.out.println("1: Si");
		System.out.println("2: No");
		boolean fueBecado = false;
		int opcion = (int) readLong();
		sc.nextLine();
		if (opcion == 1) {
		    fueBecado = true;
		}
		
		System.out.println("¿Vio materias del programa academico anteriormente?: ");
		System.out.println("1: Si");
		System.out.println("2: No");
		int opcion2 = (int) readLong();
		Estudiante nuevoEstudiante;
		switch(opcion2) {
			case 1:   
				for (int i = 0; i<gestor.getMaterias().size();i++) {	
					System.out.println((i+1)+". "+gestor.getMaterias().get(i));
					}
				System.out.println("Ingrese el nombre de la materia que vio: ");
				String opcion3 =  readln();
				ArrayList<Materia> materiasCursadas = new ArrayList<Materia>();
				for (Materia materia : gestor.getMaterias()) {
					if(materia.getNombre().equals(opcion3)) {
						materiasCursadas.add(materia);
					}
				}
				System.out.println("Ingrese el nombre de las demas materias que vio o ingrese hecho para terminar: ");
				String opcion4 =  sc.nextLine();
				while (!opcion4.toLowerCase().equals("hecho")) {
				    boolean found = false;
				    for (Materia materia : gestor.getMaterias()) {
				        if(materia.getNombre().equals(opcion4)) {
				            found = true;
				            if (!materiasCursadas.contains(materia)) {
				                materiasCursadas.add(materia);
				            } else {
				                System.out.println("La materia que esta intentando ingresar ya fue inscrita en sus materias cursadas");
				            }
				            break;
				        }
				    }
				    if (!found) {
				        System.out.println("La materia ingresada no se encuentra en el sistema");
				    }
				    System.out.println("Ingrese el nombre de las demas materias que vio o ingrese hecho para terminar: ");
				    opcion4 = sc.nextLine();
				}
				nuevoEstudiante=gestor.nuevoEstudiante(nombre, ID, Email, fueBecado, materiasCursadas);
				; break;
			case 2: nuevoEstudiante= gestor.nuevoEstudiante(nombre, ID, Email, fueBecado); ;break;
			
		
			default:
	            nuevoEstudiante = null;
	            break;
	    }
	    if (nuevoEstudiante != null) {
	        nuevoEstudiante.calcularPorcetajeAvance();
	        System.out.println("Estudiante matriculado");
	    } else {
	        System.out.println("Opción inválida");
	    }
	}
	
	static void materiasVistas() {
		
	}
	
	
	static void verEstudiantes(gestionDatos gestor) {
		System.out.println("Estudiantes matriculados en el sistema: ");
		for (Estudiante estudiante : gestor.getEstudiantes()) {	
			System.out.println(estudiante);
			}
	}
	static void verMateriasDisponibles(gestionDatos gestor) {
		System.out.println("Materias disponibles para cursar en el sistema: ");
		for (int i = 0; i<gestor.getMaterias().size();i++) {	
			System.out.println((i+1)+". "+gestor.getMaterias().get(i));
			System.out.println("*. "+gestor.getMaterias().get(i).getEstudiantesInscritos());
			}
	}
	static void verProfosresInscritos(gestionDatos gestor) {
		System.out.println("Profesores inscritos en el sistema: ");
		for (Profesor profesor : gestor.getProfesores()) {	
			System.out.println(profesor);
			}
	}
	static void accederProfesor(gestionDatos gestor) {
		System.out.println("Ingrese su ID de docente: ");
		int opcion = (int) readLong();
		Profesor profesorSeleccionado = null;
		for(Profesor profesor : gestor.getProfesores()) {
			if (profesor.getID() == opcion) {
				profesorSeleccionado = profesor;
			}
		}
		if (profesorSeleccionado == null) {
			System.out.println("EL ID ingresado no se encuentra en el sistema");
			}
		else {
			System.out.println("Bienvenido/a al sistema academico universitario "+"querido docente "+profesorSeleccionado.getNombre()+"\n");
			System.out.println("¿Que desea realizar el dia de hoy? \n");
			int opcionDocente;
			do {
				System.out.println("1. Perfil del docente");
				System.out.println("2. Ver materias asignadas para el semestre actual");
				System.out.println("3. Volver al menu principal");
				opcionDocente = (int) readLong();
				
				switch(opcionDocente) {
				case 1: 
					profesorSeleccionado.evaluacionDocente();
					System.out.println("Docente: "+profesorSeleccionado.getNombre()+"\n");
					System.out.println("Calificacion actual del docente: "+profesorSeleccionado.getCalificacionDocente()+"\n");
					
					;break;
				case 2: 
					
					System.out.println("Las materias que le fueron inscritas para el semestre actual son: \n");
					
					int cont = 1;
					for (Materia materia: profesorSeleccionado.getMaterias_Asignadas()) {
					    System.out.println(cont+". "+materia.getNombre());
					    cont++;
					}
					System.out.println(cont + ". Salir \n");
					int opcionmateriaSeleccionada;
					int opcion2A;
					Materia materiaSeleccionada = null;
					boolean exit = false;
					do {
					    opcionmateriaSeleccionada = (int) readLong();
					    if (opcionmateriaSeleccionada >= 1 && opcionmateriaSeleccionada <= profesorSeleccionado.getMaterias_Asignadas().size()) {
					        materiaSeleccionada = profesorSeleccionado.getMaterias_Asignadas().get(opcionmateriaSeleccionada - 1);
					        do {
					            System.out.println("¿Que desea realizar con respecto a la materia "+materiaSeleccionada.getNombre()+"? \n");
					            System.out.println("1. Crear tarea de la materia "+materiaSeleccionada.getNombre());
					            System.out.println("2. Eliminar tarea de la materia "+materiaSeleccionada.getNombre());
					            System.out.println("3. Visualizar las tareas creadas");
					            System.out.println("4. Ingresar calificaciones en las tareas");
					            System.out.println("5. Ver detalles de la materia");
					            System.out.println("6. Volver al menu del docente \n");
					            opcion2A = (int) readLong();
					            sc.nextLine();
					            
					            if (opcion2A == 6) {
					                exit = true;
					            }
							
					    switch(opcion2A) {
					    case 1:
					        System.out.println("Ingrese el nombre de la tarea que desea asignar \n");
					        //sc.nextLine(); 
					        String nombreTarea = sc.nextLine();
						    do {   
						    	//Materia MateriaEnGestor = null;
						    	for (Materia materia: gestor.getMaterias()) {
						    		if(materiaSeleccionada.getNombre().equalsIgnoreCase(materia.getNombre())) {
						    			Tarea tarea = new Tarea(materia,nombreTarea);
						    			materia.inscribirTarea(tarea);
								        System.out.println("Tarea inscrita correctamente.");
								        break;
						    		}
						    	}
						    	
						        break;
					        	
						    } while (nombreTarea != "");
					        break;

					    case 2:
					    	

					    	for (Materia materia: gestor.getMaterias()) {
					    		if(materiaSeleccionada.getNombre().equalsIgnoreCase(materia.getNombre())) {
		    		
					    	System.out.println("Tareas registradas en la materia\n");
					    	int contt1 = 1;
					    	for(Tarea tarea1: materia.getTareasDeMateria()) {
					    		System.out.println(contt1+". "+tarea1);
					    		contt1++;
					    			}
					    	break;
					    		}
					    	}
					    	System.out.println("\n");
					    	System.out.println("Seleccione el número de la tarea que desea retirar: \n");
					    	int tareaIndex = (int) readLong() - 1;

					    	for (Materia materia: gestor.getMaterias()) {
					    	    if(materiaSeleccionada.getNombre().equalsIgnoreCase(materia.getNombre())) {
					    	        if (tareaIndex >= 0 && tareaIndex < materia.getTareasDeMateria().size()) {
					    	            Tarea tareaa = materia.getTareasDeMateria().get(tareaIndex);
					    	            materia.retirarTarea(tareaa);
					    	            System.out.println("Tarea retirada de la materia " + materia.getNombre() + " correctamente \n");
					    	        } else {
					    	            System.out.println("Opción inválida. Por favor ingrese una opción válida.");
					    	        }
					    	        break;
					    	    }
					    	}

					        break;
					    case 3: 
					    	for (Materia materia: gestor.getMaterias()) {
					    		if(materiaSeleccionada.getNombre().equalsIgnoreCase(materia.getNombre())) {
		    		
					    	System.out.println("Tareas registradas en la materia\n");
					    	int contt1 = 1;
					    	for(Tarea tarea1: materia.getTareasDeMateria()) {
					    		System.out.println(contt1+". "+tarea1);
					    		contt1++;
					    			}
					    	break;
					    		}
					    	};
					    	break;
					    
					    	
					    case 4:
					        for (Materia materia: gestor.getMaterias()) {
					            if(materiaSeleccionada.getNombre().equalsIgnoreCase(materia.getNombre())) {
					                System.out.println("Seleccione la tarea para la que desea ingresar notas: \n");
					                int contt = 1;
					                for (Tarea tarea1 : materia.getTareasDeMateria()) {
					                    System.out.println(contt + ". " +tarea1);
					                    contt++;
					                }
					                int tareaIndexA = (int) readLong() - 1;
					                if (tareaIndexA >= 0 && tareaIndexA < materia.getTareasDeMateria().size()) {
					                    Tarea tareaSeleccionada = materia.getTareasDeMateria().get(tareaIndexA);
					                    System.out.println("Seleccione el estudiante al que desea ingresar la nota: \n");
					                    int contt2 = 1;
					                    for (Estudiante estudiante : materia.getEstudiantesInscritos()) {
					                        System.out.println(contt2 + ". " + estudiante.getNombre());
					                        contt2++;
					                    }
					                    int estudianteIndex = (int) readLong() - 1;
					                    if (estudianteIndex >= 0 && estudianteIndex < materia.getEstudiantesInscritos().size()) {
					                        Estudiante estudianteSeleccionado = materia.getEstudiantesInscritos().get(estudianteIndex);
					                        System.out.println("Ingrese la nota para " + estudianteSeleccionado.getNombre() + ": ");
					                        double nota = 0;
					                        boolean validInput = false;
					                        while (!validInput) {
					                            try {
					                                nota = sc.nextDouble();
					                                validInput = true;
					                            } catch (InputMismatchException e) {
					                                System.out.println("Por favor ingrese una nota válida.");
					                                sc.nextLine();
					                            }
					                        }
					                        
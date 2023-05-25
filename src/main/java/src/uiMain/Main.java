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
					        String nombreTarea = sc.nextLine();
						    do {   
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
					                        if (nota >= 0 && nota <= 5) {
					                            tareaSeleccionada.setGrade(estudianteSeleccionado, nota);
					                            System.out.println("Nota ingresada correctamente.");
					                        } else {
					                            System.out.println("Por favor ingrese una nota en el rango entre 0 y 5.");
					                        }
					                    } else {
					                        System.out.println("Opción inválida. Por favor ingrese una opción válida.");
					                    }
					                } else {
					                    System.out.println("Opción inválida. Por favor ingrese una opción válida.");
					                }
					                break;
					            }
					        }
					        break;


					    
					    case 5: 
					    	System.out.println(materiaSeleccionada);
					    	break;
					    	
					    		}
					        }while (opcion2A != 6 && !exit);
					    } 
					    else if (opcionmateriaSeleccionada != cont + 1) {
					        System.out.println("Opcion invalida. Por favor ingrese una opcion valida.");
					    }
				}
					while(opcionmateriaSeleccionada != cont && !exit);
					 
				break;
				}
			} while(opcionDocente != 3);
		}
	}
	static void asignarBecas(gestionDatos gestor) {
	    Beca beca = new Beca("Beca Académica");
	    for(Estudiante estudiante: gestor.getEstudiantes()) {
	    	estudiante.aplicarBeca(estudiante);
	    	
	    }
	    beca.asignarEstudiantesBeca();
	    
	    System.out.println("Admitidos a becas: ");
		System.out.println("Beca Inicial: "+beca.getEstudiantesAptosInicial());
		System.out.println("Beca Normal: "+beca.getEstudiantesAptosNormal());
		System.out.println("Beca Avanzada: "+beca.getEstudiantesAptosAvanzada()+"\n");
	}

	static void accederEstudiante(gestionDatos gestor) {
		System.out.println("Ingrese su ID: ");
		int opcion = (int) readLong();
		Estudiante estudianteSeleccionado = null;
		for(Estudiante estudiante : gestor.getEstudiantes()) {
			if (estudiante.getID() == opcion) {
				estudianteSeleccionado = estudiante;
			}
		}
		if (estudianteSeleccionado == null) {System.out.println("EL ID ingresado no se encuentra en el sistema");}
		else {
			System.out.println("Bienvenido/a al sistema academico universitario"+" "+estudianteSeleccionado.getNombre()+"\n");
			System.out.println("¿Que desea realizar el dia de hoy? \n");
			int opcion1;
			do {
				System.out.println("1. Inscribir asignaturas");
				System.out.println("2. Ver materias inscritas");
				System.out.println("3. Realizar calificacion de docente");
				System.out.println("4. Ver horario");
				System.out.println("5. Ver perfil estudiante");
				System.out.println("6. Materias cursadas anteiormente");
				System.out.println("7. Ver calificacion docente");
				System.out.println("8. Volver al menu principal");
				opcion1 = (int) readLong();
				sc.nextLine(); 
				
				switch(opcion1) {
				case 1:
				    verMateriasDisponibles(gestor);
				    System.out.println("\n");
				    String nombreMateria;
				    do {
				        System.out.println("Ingrese el nombre de la materia que desea inscribir o 'salir' para terminar: \n");
				        nombreMateria = sc.nextLine();
				        if (!nombreMateria.equals("salir")) {
				            boolean yaInscrita = false;
				            boolean yaVista = false;
				            for (Materia materia : estudianteSeleccionado.getMaterias_Inscritas()) {
				                if (materia.getNombre().equals(nombreMateria)) {
				                    yaInscrita = true;
				                    break;
				                }
				            }
				            for (Materia materia : estudianteSeleccionado.getMateriasCursadas()) {
				                if (materia.getNombre().equals(nombreMateria)) {
				                	yaVista = true;
				                    break;
				                }
				        	}
				            if (yaInscrita) {
				                System.out.println("Ya has inscrito esta materia");
				            } else if(yaVista){
				            	System.out.println("Ya has visto esta materia en semestres anteriores");
				            } 
				            else {
				            	boolean success = estudianteSeleccionado.inscribirMateria(nombreMateria, gestor.getMaterias());
				                if (!success) {
				                    System.out.println("No puedes inscribir esta materia porque no has cursado el prerrequisito.");
				                }
				            }
				        }
				    } while (!nombreMateria.equals("salir"));
				    break;
				case 2:
				    if (!estudianteSeleccionado.getMaterias_Inscritas().isEmpty()) {
				        System.out.println("Materias inscritas para el semestre actual: \n");
				        int cont = 1;
				        for (Materia materia : estudianteSeleccionado.getMaterias_Inscritas()) {
				            if (cont != estudianteSeleccionado.getMaterias_Inscritas().size()) {
				                System.out.println(cont+". "+materia);
				            } else {
				                System.out.println(cont+". "+materia+"\n");
				            }
				            cont++;
				        }

				        System.out.println("¿Ingrese la opcion de la materia a la que desea acceder? \n");
				        int opcionmateriaSeleccionada;
				        int opcion2A;
				        Materia materiaSeleccionada = null;
				        boolean exit = false;
				        do {
				            opcionmateriaSeleccionada = (int) readLong();
				            if (opcionmateriaSeleccionada >= 1 && opcionmateriaSeleccionada <= estudianteSeleccionado.getMaterias_Inscritas().size()) {
				                materiaSeleccionada = estudianteSeleccionado.getMaterias_Inscritas().get(opcionmateriaSeleccionada - 1);
				                do {
				                    System.out.println("¿Que desea conocer o realizar respecto a la materia"+materiaSeleccionada.getNombre()+"? \n");
				                    System.out.println("1. Ver detalles de la materia");
				                    System.out.println("2. Ver tareas asignadas para la materia");
				                    System.out.println("3. Ver nota necesaria en la siguiente tarea para pasar la materia");
				                    System.out.println("4. Volver al menu del estudiante");
				                    opcion2A = (int) readLong();

				                    if (opcion2A == 4) {
				                        exit = true;
				                    }

				                    switch(opcion2A) {
				                        case 1:
				                        	for (Materia materia: gestor.getMaterias()) {
									    		if(materiaSeleccionada.getNombre().equalsIgnoreCase(materia.getNombre())) {
									    			System.out.println(materiaSeleccionada.getNombre());
									    			System.out.println("Horario: "+materiaSeleccionada.getHorario());
									    			double materiaScore = 0.0;
									    	        int numTareas = materiaSeleccionada.getTareasDeMateria().size();
									    	        for (Tarea tarea : materiaSeleccionada.getTareasDeMateria()) {
									    	            materiaScore += tarea.getGrade(estudianteSeleccionado);
									    	        }
									    	        if (numTareas > 0) {
									    	            materiaScore /= numTareas;
									    	        }
									    	        double PROM = Math.round(materiaScore * 100.0) / 100.0;
									    			System.out.println("Promedio actual del estudiante en la materia: "+PROM);
									    		}
									    	}
				                            break;
				                        case 2:
				                        	for (Materia materia: gestor.getMaterias()) {
									    		if(materiaSeleccionada.getNombre().equalsIgnoreCase(materia.getNombre())) {
						    		
									    			System.out.println("Tareas registradas en la materia"+materiaSeleccionada.getNombre()+"\n");
									    			int contt1 = 1;
									    			for(Tarea tarea1: materia.getTareasDeMateria()) {
									    				System.out.println(contt1+". "+tarea1);
									    				contt1++;
									    				
									    			}
									    		break;
									    		}
									    	};
									    	break;
				                        case 3:
				                        	System.out.println("Para pasar la materia el estudiante debe obtener la siguiente calificacionen en la siguiente tarea: \n");
				                        		if (materiaSeleccionada.Calcular_necesario_para_pasar(estudianteSeleccionado) == 0) {
				                        			System.out.println("Felicidades estudiante no necesita nota en la siguiente tarea para pasar, continue dando lo mejor de usted! \n");
				                        		}
				                        	else {
				                        	System.out.println("Calificacion: "+materiaSeleccionada.Calcular_necesario_para_pasar(estudianteSeleccionado)); 
				                        	}
				                        	break;
				                        	
				                    }
				                } while(opcion2A != 4);
				            } else {
				                System.out.println("Opcion invalida. Por favor ingrese una opcion valida.");
				            }
				        } while(opcionmateriaSeleccionada != estudianteSeleccionado.getMaterias_Inscritas().size() + 1 && !exit);
				    } else {
				        System.out.println("No se han encontrado materias inscritas para este semestre en el sistema \n");
				        
				        int opcionA;
						do {
						    System.out.println("Debido a que no se encuentran materias incritas...");
						    System.out.println("Le gustaria que el sistema genere un horario para usted en base a las materias vistas y faltantes por ver \n");;

						    System.out.println("1. Si");
						    System.out.println("2. No");

						    opcionA = (int)readLong();

						    switch(opcionA) {
						        case 1:
						            estudianteSeleccionado.sugerirMaterias(gestor.getMaterias());
						            System.out.println("Inscipcion automatica realizada con exito");
						            int cont = 1;
						            for(Materia materia : estudianteSeleccionado.getMaterias_Inscritas()) {    						                
						            	if (cont != estudianteSeleccionado.getMaterias_Inscritas().size()) {
											System.out.println(cont+". "+materia);
										}
										else {
											System.out.println(cont+". "+materia+"\n");
										}
						                cont++;
						            }
						            break;
						    }
						} while (opcionA != 2 && opcionA != 1);
				    }
				    break;

				case 3: 
					System.out.println("Bienvenido/a al sistema de calificacion de docentes \n");
					if (!estudianteSeleccionado.getCalificacionAsignada()) {
					for (Materia materia : estudianteSeleccionado.getMaterias_Inscritas()) {
					    Profesor profesorSeleccionado = materia.getProfesor();
					    System.out.println("Ingrese la calificación para " + materia.getProfesor() + ": ");
					    double calificacion;
					    boolean validInput = false;
					    do {
					        String input = sc.nextLine();
					        try {
					            calificacion = Double.parseDouble(input);
					            if (calificacion >= 1 && calificacion <= 5) {
					                System.out.println("Calificación ingresada correctamente.");
					                materia.getProfesor().ingresarCalificacion(calificacion);
					                validInput = true;
					            }
					            else {
					                System.out.println("Por favor ingrese una calificacion en el rango entre 1 y 5");
					            }
					        } catch (NumberFormatException e) {
					            System.out.println("Por favor ingrese un número válido");
					        }
					    } while (!validInput);
					}estudianteSeleccionado.setCalificacionAsignada(true); 
					} else {
						System.out.println("Usted ya realizo la calificacion de docentes anteriormente");
					}
					break;

				case 4: 
					if (!estudianteSeleccionado.getMaterias_Inscritas().isEmpty()) {
					boolean fallaHorario = estudianteSeleccionado.compararHorario(estudianteSeleccionado.getMaterias_Inscritas());
					if(fallaHorario) {
						int opcionA;
						do {
						    System.out.println("Advertencia! Su horario presenta errores en las horas y dias de las materias \n");
						    System.out.println("¿Le gustaria que este sea corregido por el sistema? \n");

						    System.out.println("1. Si");
						    System.out.println("2. No");

						    opcionA = (int)readLong();

						    switch(opcionA) {
						        case 1:
						            estudianteSeleccionado.sugerirHorario(fallaHorario);
						            System.out.println("Horario corregido con exito");
						            int cont = 1;
						            for(Materia materia : estudianteSeleccionado.getMaterias_Inscritas()) {    						                
						            	if (cont != estudianteSeleccionado.getMaterias_Inscritas().size()) {
											System.out.println(cont+". "+materia);
										}
										else {
											System.out.println(cont+". "+materia+"\n");
										}
						                cont++;
						            }
						            break;
						        case 2: 
						            //faltante
						        	;
						            break;
						    }
						} while (opcionA != 2 && opcionA != 1);
						
					} else {
						int cont = 1;
						for(Materia materia : estudianteSeleccionado.getMaterias_Inscritas()) {	
							if (cont != estudianteSeleccionado.getMaterias_Inscritas().size()) {
								System.out.println(cont+". "+materia);
							}
							else {
								System.out.println(cont+". "+materia+"\n");
							}
							cont++;}
					}
					;}
					else {
						System.out.println("No se han encontrado materias inscritas, por lo tanto no puede hacer uso de la funcion ver horario");
					}; break;
				case 5: 
					
					System.out.println("Nombre: " + estudianteSeleccionado.getNombre());
				    System.out.println("Correo: " + estudianteSeleccionado.getEmail());
				    System.out.println("Promedio: " + estudianteSeleccionado.calcularPromedio());
				    System.out.println("Porcentaje de avance: " + estudianteSeleccionado.getPorcentajeDeAvance() + "%");
				    Beca beca = new Beca("Beca Académica");
				    System.out.println("Revise si su nombre se encuentra enlistado en alguna de las becas\n");
				    asignarBecas(gestor);
				   ;
				    break;
					
					 
				case 6: 
					System.out.println("Materias cursadas previamente por el estudiante");
					int cont = 1;
					for(Materia materia : estudianteSeleccionado.getMateriasCursadas()) {
						if (cont != (estudianteSeleccionado.getMateriasCursadas().size()))	{
							System.out.println(cont+". "+materia);
						} else {
							System.out.println(cont+". "+materia+"\n");
						}
						
						cont++;
					}
				; break;
				case 7:
				    System.out.println("Ver calificación del docente");
				    int opcionProfesor1;
				    int j;
				    do {
				        System.out.println("Seleccione el profesor cuya calificación desea ver: ");
				         j = 1;
				        for (Materia materia : estudianteSeleccionado.getMaterias_Inscritas()) {
				            System.out.println(j + ". " + materia.getProfesor().getNombre());
				            j++;
				        }
				        System.out.println(j + ". Volver al menu del estudiante");
				        opcionProfesor1 = (int) readLong();
				        if (opcionProfesor1 != j) {
				            Profesor profesorSeleccionado1 = estudianteSeleccionado.getMaterias_Inscritas().get(opcionProfesor1 - 1).getProfesor();
				            profesorSeleccionado1.evaluacionDocente();
				            System.out.println("La calificación promedio de " + profesorSeleccionado1.getNombre() + " es: " + profesorSeleccionado1.getCalificacionDocente());
				        }
				    } while (opcionProfesor1 != j);
				    break;

				}
			} while (opcion1 != 8);
			
		} 
		
	}

	public static void main(String args[]) {

		
		gestionDatos gestor = new gestionDatos();
		int opcion;
		do {
			System.out.println("Que desea hacer?");
			System.out.println("1. Matricular alumno");
			System.out.println("2. Estudiantes matriculados");
			System.out.println("3. Materias disponibles");
			System.out.println("4. Acceder Estudiante");
			System.out.println("5. Acceder Profesor");
			System.out.println("6. Ver profesores inscritos");
			System.out.println("7. Asignar becas");
			System.out.println("8. Terminar");
			opcion = (int) readLong();
			
			switch(opcion) {
			case 1: isncripcionEstudiante(gestor); break;
			case 2: verEstudiantes(gestor); break;
			case 3: verMateriasDisponibles(gestor); break;
			case 4: accederEstudiante(gestor); break;
			case 5: accederProfesor(gestor); break;
			case 6: verProfosresInscritos(gestor); break;
			case 7: asignarBecas(gestor); break;
			case 8: salirDelSistema(gestor); break;
			}
		} while (opcion != 8);
	
	}
}
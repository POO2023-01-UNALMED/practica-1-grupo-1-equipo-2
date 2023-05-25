package gestorAplicacion.personas;

import java.util.ArrayList;
import java.util.HashSet;
import java.util.Set;
import gestorAplicacion.Calendario.*;
import gestorAplicacion.Calendario.Horario.dias;
import gestorAplicacion.Calendario.Materia.tipo;
import java.io.Serializable;

public class Estudiante extends Persona implements Serializable{
	
	//atributos
	private double promedio;
	private boolean calificacionAsignada;
	private boolean fueBecado;
	public ArrayList<Materia> materias_inscritas;
	private double porcentajeDeAvance;
	private boolean fallaHorario;
	protected ArrayList<Materia> materias_cursadas;
	private int creditosInscritos = 0;
	private ArrayList<Materia> intentoMaterias;
	private ArrayList<Profesor> profesoreInscritos;
		
	//constructor
	public Estudiante(String nombre, int ID, String Email, boolean fueBecado, ArrayList<Materia> materias_cursadas){
		super (nombre, ID, Email);
		this.fallaHorario = false;
		this.calificacionAsignada = false;
		this.fueBecado = fueBecado;
		this.promedio =  0.0;
		materias_inscritas = new ArrayList<Materia>();
		this.materias_cursadas=materias_cursadas;
		intentoMaterias = new ArrayList<Materia>();
		profesoreInscritos= new ArrayList<Profesor>();

	}
	public Estudiante(String nombre, int ID, String Email, boolean fueBecado){
		super (nombre, ID, Email);
		this.fallaHorario = false;
		this.fueBecado = fueBecado;
		this.promedio =  0.0;
		materias_inscritas = new ArrayList<Materia>();
		materias_cursadas = new ArrayList<Materia>();
		intentoMaterias = new ArrayList<Materia>();
		profesoreInscritos= new ArrayList<Profesor>();
	}
	//Metodos get y set
	
	public void setProfesoresInscritos(ArrayList<Profesor> profesor) {
		profesoreInscritos = profesor;
	}
	
	public ArrayList<Profesor> getProfesoresInscritos(){
		return profesoreInscritos;
	}
	
	public ArrayList<Materia> getMaterias_Inscritas(){
		return materias_inscritas;
	}
	
	public void setMaterias_Inscritas(ArrayList<Materia> materiasInscritas) {
		materias_inscritas = materiasInscritas;
	}
	
	
	public void setfallaHorario(boolean fallaHorario) {
		this.fallaHorario= fallaHorario;
	}
	public boolean getfallaHorario() {
		return fallaHorario;
	}
	
	
	public boolean getFueBecado() {
        return fueBecado;
    }
	public void setFueBecado(boolean fueBecado) {
        this.fueBecado = fueBecado;
    }
	
	
	public double getPorcentajeDeAvance() {
	 	return porcentajeDeAvance;
 	}
	public void setPorcentajeDeAvance(double PorcentajeDeAvance) {
	 	porcentajeDeAvance = PorcentajeDeAvance;
 	}	 
	 public ArrayList<Materia> getMateriasCursadas() {
	        return materias_cursadas;
	    }
	 public void setMateriasCursadas(ArrayList<Materia> materias_cursadas) {
			this.materias_cursadas=materias_cursadas;
	    }
	 
	 public boolean getCalificacionAsignada() {
			return calificacionAsignada;
		}
		public void setCalificacionAsignada(boolean calificacionAsignada) {
			this.calificacionAsignada = calificacionAsignada;
		}
	 
	 public void setCreditosInscritos(int creditosInscritos) {
			this.creditosInscritos= creditosInscritos;
		}
		public int getCreditosInscritos() {
			return creditosInscritos;
		}
	 
		
	//metodos de la clase
		public boolean inscribirMateria(String nombreMateria, ArrayList<Materia> materiasDisponibles) {
		    boolean tieneFundamentacion = false;
		    boolean falloPrerrequsito = false;
		    int intentoCreditos = 0;

		    for (Materia materia : materiasDisponibles) {
		        if (materia.getNombre().equals(nombreMateria)) {
		            if (materias_inscritas.contains(materia)) {
		                return false;
		            }
		            Materia prerrequisito = materia.getPrerrequisito();
		            boolean tienePrerrequisito = false;
		            if (prerrequisito != null) {
		                for (Materia materiaCursada : materias_cursadas) {
		                    if (materiaCursada.getNombre().equals(prerrequisito.getNombre())) {
		                        tienePrerrequisito = true;
		                        break;
		                    }
		                }
		            }
		            if (prerrequisito == null || tienePrerrequisito) {
		                intentoMaterias.add(materia);
		                break;
		            } else {
		                falloPrerrequsito = true;
		            } 
		        }
		    }

		    for (Materia m : intentoMaterias) {
		        intentoCreditos += m.getCreditos();
		        if (m.getTipo() == tipo.fundamentacion) {
		            tieneFundamentacion = true;
		        }
		    }

		    if (intentoCreditos >= 6 && tieneFundamentacion) {
		        for(Materia ma: intentoMaterias) {
		            profesoreInscritos.add(ma.getProfesor());
		            ma.inscribirEstudiante(this);
		        }
		        setMaterias_Inscritas(intentoMaterias);
		        setCreditosInscritos(intentoCreditos);
		    }

		    return !falloPrerrequsito;
		}
	        
	
	public void retirarMateria(Materia Materia) {
		materias_inscritas.remove(Materia);
	}
	
	
	public void aplicarBeca (Estudiante estudiante) {
		Beca.estudiantes.add(this);
	}
	
	
	public double calcularPromedio() {
	    double finalScore = 0.0;
	    int numMaterias = materias_inscritas.size();
	    for (Materia materia : materias_inscritas) {
	        double materiaScore = 0.0;
	        int numTareas = materia.getTareasDeMateria().size();
	        for (Tarea tarea : materia.getTareasDeMateria()) {
	            materiaScore += tarea.getGrade(this);
	        }
	        if (numTareas > 0) {
	            materiaScore /= numTareas;
	        }
	        finalScore += materiaScore;
	    }
	    if (numMaterias > 0) {
	        finalScore /= numMaterias;
	    }
	    return Math.round(finalScore * 100.0) / 100.0;
	}
	
	//funcionalidades 1. Detectar problemas con franja horaria
	public boolean compararHorario(ArrayList<Materia> materias_inscritas){
		ArrayList<Materia>MateriasError = new ArrayList<Materia>();
		fallaHorario = false;
		for(int i = 0; i < materias_inscritas.size(); i++ ) {
			Horario horario = materias_inscritas.get(i).getHorario();
			String hora1 = horario.getHora_inicio();
			String hora2 = horario.getHora_Fin();
			ArrayList<dias> dia1 = horario.getDia();
			
			for (int j = i + 1; j < materias_inscritas.size(); j++) {
				Horario horario2 = materias_inscritas.get(j).getHorario();
				String hora3 = horario2.getHora_inicio();
				String hora4 = horario2.getHora_Fin();
				ArrayList<dias> dia2 = horario2.getDia();
			
				for (int k = 0; k < dia1.size(); k++) {
					dias dia11 = dia1.get(k);
					for (int h = 0; h < dia2.size(); h++) {
						dias dia22= dia2.get(h);
					if (dia11 == dia22 && !MateriasError.contains(materias_inscritas.get(i)))  {
						if (hora1 == hora3 || hora2 == hora4) {
							 fallaHorario=true; 
							 MateriasError.add(materias_inscritas.get(i));
							 MateriasError.add(materias_inscritas.get(j));
							}
						}
					}
				}
			}
		}
		return fallaHorario;
	}
	// Funcionalidad 2: Sugerir Horario y materia
	public void sugerirHorario(boolean fallaHorario) {
	    ArrayList<Materia> materiasSugeridas = new ArrayList<Materia>();
	    if (fallaHorario) {
	        for (Materia materia : materias_inscritas) {
	            boolean conflicto = false;
	            for (Materia materiaSugerida : materiasSugeridas) {
	                
	                ArrayList<dias> diasMateria = materia.getHorario().getDia();
	                ArrayList<dias> diasMateriaSugerida = materiaSugerida.getHorario().getDia();
	                boolean falloDias = false;
	                for (dias diaMateria : diasMateria) {
	                    if (diasMateriaSugerida.contains(diaMateria)) {
	                    	falloDias = true;
	                        break;
	                    }
	                }
	                
	                if (falloDias &&
	                    (materia.getHorario().getHora_inicio().equals(materiaSugerida.getHorario().getHora_inicio()) ||
	                     materia.getHorario().getHora_Fin().equals(materiaSugerida.getHorario().getHora_Fin()))) {
	                    conflicto = true;
	                    break;
	                }
	            }
	            if (!conflicto) {
	                materiasSugeridas.add(materia);
	            }
	        }
	      this.materias_inscritas = materiasSugeridas;
	    }
	}
	
	//Funcionalidad 3: Crear un horario en base a las materias vistas
	public void sugerirMaterias(ArrayList<Materia> materiasDisponibles) {  
		ArrayList<Materia> materiasRecomendadas = new ArrayList<Materia>();
		for (Materia materia : materias_cursadas) {
			
			if(materia.getNombre().equalsIgnoreCase(materiasDisponibles.get(0).getNombre()) && !(materias_cursadas.contains(materiasDisponibles.get(0)))){
				materiasRecomendadas.add(materiasDisponibles.get(0));
				profesoreInscritos.add(materiasDisponibles.get(0).getProfesor());
				materiasDisponibles.get(0).inscribirEstudiante(this);
			}
			
			else if(materia.getNombre().equalsIgnoreCase(materiasDisponibles.get(0).getNombre()) && !(materias_cursadas.contains(materiasDisponibles.get(1)))) {
				materiasRecomendadas.add(materiasDisponibles.get(1));
				profesoreInscritos.add(materiasDisponibles.get(1).getProfesor());
				materiasDisponibles.get(1).inscribirEstudiante(this);
			}
			else if(materia.getNombre().equalsIgnoreCase(materiasDisponibles.get(1).getNombre()) && !(materias_cursadas.contains(materiasDisponibles.get(2)))) {
				materiasRecomendadas.add(materiasDisponibles.get(2));
				profesoreInscritos.add(materiasDisponibles.get(2).getProfesor());
				materiasDisponibles.get(2).inscribirEstudiante(this);
			}
		
			if (materia.getNombre().equalsIgnoreCase(materiasDisponibles.get(3).getNombre()) && !(materias_cursadas.contains(materiasDisponibles.get(3)))) {
				materiasRecomendadas.add(materiasDisponibles.get(3));
				profesoreInscritos.add(materiasDisponibles.get(3).getProfesor());
				materiasDisponibles.get(3).inscribirEstudiante(this);
				if(compararHorario(materiasRecomendadas)) {
					materiasRecomendadas.remove(materiasDisponibles.get(3));
					profesoreInscritos.remove(materiasDisponibles.get(3).getProfesor());
					materiasDisponibles.remove(3).inscribirEstudiante(this);
				}
			}
			
			else if (materia.getNombre().equalsIgnoreCase(materiasDisponibles.get(3).getNombre()) && !(materias_cursadas.contains(materiasDisponibles.get(4)))) {
				materiasRecomendadas.add(materiasDisponibles.get(4));
				profesoreInscritos.add(materiasDisponibles.get(4).getProfesor());
				materiasDisponibles.get(4).inscribirEstudiante(this);
				if(compararHorario(materiasRecomendadas)) {
					materiasRecomendadas.remove(materiasDisponibles.get(4));
					profesoreInscritos.remove(materiasDisponibles.get(4).getProfesor());
					materiasDisponibles.remove(4).inscribirEstudiante(this);
				}
			}
			else if(materia.getNombre().equalsIgnoreCase(materiasDisponibles.get(4).getNombre()) && !(materias_cursadas.contains(materiasDisponibles.get(5)))) {
				materiasRecomendadas.add(materiasDisponibles.get(5));
				profesoreInscritos.add(materiasDisponibles.get(5).getProfesor());
				materiasDisponibles.get(5).inscribirEstudiante(this);
				if(compararHorario(materiasRecomendadas)) {
					materiasRecomendadas.remove(materiasDisponibles.get(5));
					profesoreInscritos.remove(materiasDisponibles.get(5).getProfesor());
					materiasDisponibles.remove(5).inscribirEstudiante(this);
				}
			}
		}
		
		for (int i = 6; i<9;i++) {
			materiasRecomendadas.add(materiasDisponibles.get(i));
			profesoreInscritos.add(materiasDisponibles.get(i).getProfesor());
			materiasDisponibles.get(i).inscribirEstudiante(this);
			if(compararHorario(materiasRecomendadas)) {
				materiasRecomendadas.remove(materiasDisponibles.get(i));
				profesoreInscritos.remove(materiasDisponibles.get(i).getProfesor());
				materiasDisponibles.remove(i).inscribirEstudiante(this);
			}
		}
		this.materias_inscritas = materiasRecomendadas;
	}
	
	
	public String toString () {
		return "Estudiante: " + getNombre();
		}
	
	public void calcularPorcetajeAvance() {
		double porcentajeAvance = (1.0/9)*materias_cursadas.size();
		setPorcentajeDeAvance(Math.round(porcentajeAvance * 100.0) );
	}
	
	
	
	
	
}

		
	
	

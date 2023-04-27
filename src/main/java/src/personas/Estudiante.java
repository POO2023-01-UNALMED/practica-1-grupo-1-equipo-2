package personas;

import java.util.ArrayList;
import java.util.HashSet;
import java.util.Set;
import Calendario.*;
import Calendario.Horario.dias;
import Calendario.Materia.tipo;

public class Estudiante extends Persona{
	
	//atributos
	private double promedio;
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
		this.fueBecado = fueBecado;
		this.promedio =  0.0;
		materias_inscritas = new ArrayList<Materia>();
		this.materias_cursadas=materias_cursadas;
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
	 
	 
	 public void setCreditosInscritos(int creditosInscritos) {
			this.creditosInscritos= creditosInscritos;
		}
		public int getCreditosInscritos() {
			return creditosInscritos;
		}
	 
		
	//metodos de la clase
		public void inscribirMateria(String nombreMateria, ArrayList<Materia> materiasDisponibles) {
	        boolean tieneFundamentacion = false;
	        int intentoCreditos = 0;

	        for (Materia materia : materiasDisponibles) {
	            if (materia.getNombre().equals(nombreMateria)) {
	                Materia prerrequisito = materia.getPrerrequisito();
	                if (prerrequisito == null || materias_cursadas.contains(prerrequisito)) {
	                    intentoMaterias.add(materia);
	                    break;
	                }
	            }
	        }
	        for (Materia m : intentoMaterias) {
	            intentoCreditos += m.getCreditos();
	            if (m.getTipo() == tipo.fundamentacion) {
	                tieneFundamentacion = true;
	            }
	        }
	        if (intentoCreditos >= 10 && tieneFundamentacion) {
	            for(Materia ma: intentoMaterias) {
	            	profesoreInscritos.add(ma.getProfesor());
	            }
	        	setMaterias_Inscritas(intentoMaterias);
	            setCreditosInscritos(intentoCreditos);
	        }
	    }
	
	
	        
	
	public void retirarMateria(Materia Materia) {
		materias_inscritas.remove(Materia);
	}
	
	
	public static void aplicarBeca (Estudiante estudiante) {
		Beca.estudiantes.add(estudiante);
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
	public void sugerirMaterias(ArrayList<Materia> materiasDisponibles) {  
		ArrayList<Materia> materiasRecomendadas = new ArrayList<Materia>();
		for (Materia materia : materias_cursadas) {
			if(materia == materiasDisponibles.get(0) && !(materias_cursadas.contains(materiasDisponibles.get(1)))) {
				materiasRecomendadas.add(materiasDisponibles.get(1));
			}
			else if(materia == materiasDisponibles.get(1) && !(materias_cursadas.contains(materiasDisponibles.get(2)))) {
				materiasRecomendadas.add(materiasDisponibles.get(2));
			}
		
			if (materia == materiasDisponibles.get(3) && !(materias_cursadas.contains(materiasDisponibles.get(4)))) {
				materiasRecomendadas.add(materiasDisponibles.get(4));
				if(compararHorario(materiasRecomendadas)) {
					materiasRecomendadas.remove(materiasDisponibles.get(4));
				}
			}
			else if(materia == materiasDisponibles.get(4) && !(materias_cursadas.contains(materiasDisponibles.get(5)))) {
				materiasRecomendadas.add(materiasDisponibles.get(5));
				if(compararHorario(materiasRecomendadas)) {
					materiasRecomendadas.remove(materiasDisponibles.get(5));
				}
			}
		}
		
		for (int i = 6; i<9;i++) {
			materiasRecomendadas.add(materiasDisponibles.get(i));
			if(compararHorario(materiasRecomendadas)) {
				materiasRecomendadas.remove(materiasDisponibles.get(i));
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

		
	
	

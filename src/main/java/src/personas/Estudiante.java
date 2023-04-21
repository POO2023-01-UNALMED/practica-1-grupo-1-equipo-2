package personas;

import java.util.ArrayList;
import java.util.HashSet;
import java.util.Set;

import Calendario.*;

public class Estudiante extends Persona{
	
	//atributos
	private double promedio;
	private boolean fueBecado;
	public ArrayList<Materia> materias_inscritas;
	private int porcentajeDeAvance;
	private boolean fallaHorario;
		
	//constructor
	public Estudiante(String nombre, int ID, String Email, boolean fueBecado, int porcentajeDeAvance){
		super (nombre, ID, Email);
		this.fallaHorario = false;
		this.fueBecado = fueBecado;
		this.promedio =  0.0;
		this.porcentajeDeAvance = porcentajeDeAvance;
		materias_inscritas = new ArrayList<Materia>();
	}
	
	//Metodos get y set
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
	
	public int getPorcentajeDeAvance() {
	 	return porcentajeDeAvance;
 	}
	
	public void setPorcentajeDeAvance(int PorcentajeDeAvance) {
	 	porcentajeDeAvance = PorcentajeDeAvance;
 	}	 
	
	//metodos de la clase
	public void asignarMateria  (Materia nuevaMateria) {
		materias_inscritas.add(nuevaMateria);
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
	public ArrayList<Materia> compararHorario(){
		ArrayList<Materia>MateriasError = new ArrayList<Materia>();
		for(int i = 0; i < materias_inscritas.size(); i++ ) {
			Horario horario = materias_inscritas.get(i).getHorario();
			String hora1 = horario.getHora_inicio();
			String hora2 = horario.getHora_Fin();
			Horario.dias dia1 = horario.getDia();
			
			for (int j = i + 1; j < materias_inscritas.size();) {
				Horario horario2 = materias_inscritas.get(j).getHorario();
				String hora3 = horario2.getHora_inicio();
				String hora4 = horario2.getHora_Fin();
				Horario.dias dia2 = horario2.getDia();
			
				if (dia1 == dia2 && !MateriasError.contains(materias_inscritas.get(i)))  {
					if (hora1 == hora3 || hora2 == hora4) {
						 this.fallaHorario=true; 
						 MateriasError.add(materias_inscritas.get(i));
						 MateriasError.add(materias_inscritas.get(j));
						}
			}
			}
		}
		return MateriasError;
		}
	public String sugerirHorario(ArrayList<Materia> materiaR) {
	    ArrayList<Materia> materiasSugeridas = new ArrayList<Materia>();
	    Set<Horario> uniqueHorario = new HashSet<Horario>();
		String p = "";
	    if (fallaHorario) {
			for (Materia materia : materias_inscritas) {
				if (!uniqueHorario.contains(materia.getHorario())) {
	                uniqueHorario.add(materia.getHorario());
	                materiasSugeridas.add(materia);
	            }
	        }
			for(Materia materia: materiasSugeridas) {
				p+= materia;
			}
	    	return p;	
	    	}
		return "No hay sugerencias";
	    }
	
	public String toString () {
		return "Estudiante: " + getNombre();
	}
	
	}

		
	
	

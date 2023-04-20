package personas;

import java.util.ArrayList;

import Calendario.*;

public class Estudiante extends Persona{
	
	
	//atributos
	private double promedio;
	private boolean fueBecado;
	public static ArrayList<Materia> materias_inscritas;
	private int porcentajeDeAvance;
	
	//atributos de clase
	//private static int porcentajeDeAvance = 0;
	
		
	//constructor
	public Estudiante(String nombre, int ID, String Email, boolean fueBecado, int porcentajeDeAvance){
		super (nombre, ID, Email);
		this.fueBecado = fueBecado;
		this.promedio =  0.0;
		this.porcentajeDeAvance = porcentajeDeAvance;
		materias_inscritas = new ArrayList<Materia>();
		aplicarBeca(this);
	}
	
	
	//Metodos get y set
	public ArrayList<Materia> getMaterias_Inscritas(){
		return materias_inscritas;
	}
	public void setMaterias_Inscritas(ArrayList<Materia> materiasInscritas) {
		this.materias_inscritas = materiasInscritas;
	}
	
	public boolean getFueBecado() {
        return fueBecado;
    }
	public void setFueBecado(boolean fueBecado) {
        this.fueBecado = fueBecado;
    }
	
	public double getPromedio() {
        return promedio;
    }
	public void setPromedio(double finalProm) {
        this.promedio = finalProm;
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
	
	public void aplicarBeca  (Estudiante estudiante) {
		Beca.estudiantes.add(estudiante);
	}
	
	
	public void calcularPromedio(){
		double finalprom = 0.0;
		int contador = 0;
		for (Materia materia: materias_inscritas) {
			finalprom+=materia.getPromedio();
			contador+=1;
		this.promedio = finalprom/contador;
		}
	}
	
	
	
	//funcionalidades 1. Detectar problemas con franja horaria
	public boolean compararHorario(){
		boolean f = false;
		for(int i = 0; i < materias_inscritas.size(); i++ ) {
			Horario horario = materias_inscritas.get(i).getHorario();
			String hora1 = horario.getHora_inicio();
			String hora2 = horario.getHora_Fin();
			Horario.dias dia1 = horario.getDia();
			
			for (int j = i + 1; j < materias_inscritas.size(); j ++) {
				Horario horario2 = materias_inscritas.get(j).getHorario();
				String hora3 = horario2.getHora_inicio();
				String hora4 = horario2.getHora_Fin();
				Horario.dias dia2 = horario2.getDia();
				
				if (dia1 == dia2) {
					if (hora1 == hora3 || hora2 == hora4) {
						return true; 
						}
					else {return false;}
					}
				else {return false;}
				}
			}
		return f;
		}		
	}
	
	

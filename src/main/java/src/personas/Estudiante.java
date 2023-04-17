package personas;

import java.util.ArrayList;

import Calendario.*;

public class Estudiante extends Persona{
	
	
	//atributos
	protected static ArrayList<Materia> materias_inscritas;
	
	
	//constructor
	public Estudiante(String nombre, int ID, String Email){
		super (nombre, ID, Email);
	}
	
	
	//Metodos get y set
	public ArrayList<Materia> getMaterias_Inscritas(){
		return materias_inscritas;
	}
	public void setMaterias_Inscritas(ArrayList<Materia> materiasInscritas) {
		this.materias_inscritas = materiasInscritas;
	}
	
	//metodos de la clase
	public void asignarMateria  (Materia nuevaMateria) {
		materias_inscritas.add(nuevaMateria);
	}
	public void retirarMateria(Materia Materia) {
		materias_inscritas.remove(Materia);
	}
	
	//funcionalidades 1. Detectar problemas con franja horaria
	public static boolean compararHorario(){
		boolean f = false;
		for(int i = 0; i < materias_inscritas.size(); i++ ) {
			Horario horario = materias_inscritas.get(i).getHorario();
			String hora1 = horario.getHora_inicio();
			String hora2 = horario.getHora_Fin();
			Horario.dias dia1 = horario.getDia();
			
			for (int j = i + 1; j < materias_inscritas.size(); j ++) {
				Horario horario2 = materias_inscritas.get(j).getHorario();
				String hora3 = horario.getHora_inicio();
				String hora4 = horario.getHora_Fin();
				Horario.dias dia2 = horario.getDia();
				
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
	
	

package personas;

import java.util.ArrayList;

import Calendario.*;

public class Estudiante extends Persona{
	
	
	//atributos
	protected ArrayList<Materia> materias_inscritas;
	
	
	//constructor
	public Estudiante(String nombre, int ID, String Email){
		super (nombre, ID, Email);
	}
	
	
	//Metodos get y set
	public ArrayList<Materia> getMaterias_Inscritas(){
		return materias_inscritas;
	}
	public void setMaterias_Inscritas(ArrayList<Materia> materiasInsctritas) {
		this.materias_inscritas = materiasInsctritas;
	}
	
	//metodos de la clase
	public void asignarMateria  (Materia nuevaMateria) {
		materias_inscritas.add(nuevaMateria);
	}
	public void retirarMateria(Materia Materia) {
		materias_inscritas.remove(Materia);
	}
}
package personas;

import java.util.ArrayList;

import Calendario.*;

public class Estudiante extends Persona{
	public String nombre;
	public int ID_estudiante;
	public Materia materias_insctritas;
	
	protected ArrayList<Materia> materias_Asignadas;
	
	
	//public Estudiante ( String nombre, int ID_estudiante,  Materia materias_insctritas) {
		//this.nombre = nombre;
		//this.ID_estudiante = ID_estudiante;
		//this.materias_insctritas = materias_insctritas;
	//}
	public Estudiante(String nombre, int ID_estudiante, String Email){
		this.nombre = nombre;
		this.ID_estudiante = ID_estudiante;
		this.Email = Email;
		
	}
	
	
	//Metodos get y set
	public String getNombre() {
		return nombre;
	}
	public void setNombre(String nombre) {
		this.nombre = nombre;
	}
	
	
	public int getID_Estudiante() {
		return ID_estudiante;
	}
	public void setID_Estudiante(int ID_estudiante) {
		this.ID_estudiante = ID_estudiante;
	}
	
	
	//public Materia getMaterias_inscritas() {
		//return materias_insctritas;
	//}
	//public void setMaterias_Insctritas(Materia materias_inscritas) {
		//this.materias_insctritas = materias_inscritas;
	//}
	
	
	public void asignarMateria  (Materia nuevaMateria) {
		materias_Asignadas.add(nuevaMateria);
	}
	public void retirarMateria(Materia Materia) {
		materias_Asignadas.remove(Materia);
	}
}
package personas;

import java.util.ArrayList;

import Calendario.*;

public class Estudiante extends Persona{
	public String nombre;
	public int ID_estudiante;
	public ArrayList<Materia> materias_insctritas;
	
	protected ArrayList<Materia> materias_inscritas;
	
	
	//public Estudiante ( String nombre, int ID_estudiante,  Materia materias_insctritas) {
		//this.nombre = nombre;
		//this.ID_estudiante = ID_estudiante;
		//this.materias_insctritas = materias_insctritas;
	//}
	public Estudiante(String nombre, int ID, String Email){
		this.nombre = nombre;
		this.ID_estudiante = ID;
		this.Email = Email;
		
	}
	
	
	//Metodos get y set
	public String getNombre() {
		return nombre;
	}
	public void setNombre(String nombre) {
		this.nombre = nombre;
	}
	
	
	public int getID() {
		return ID;
	}
	public void setID(int ID) {
		this.ID = ID;
	}
	
	
	public String getEmail() {
		return Email;
	}
	public void setEmail(String Email) {
		this.Email = Email;
	}
	
	
	//public Materia getMaterias_inscritas() {
		//return materias_insctritas;
	//}
	//public void setMaterias_Insctritas(Materia materias_inscritas) {
		//this.materias_insctritas = materias_inscritas;
	//}
	
	public ArrayList<Materia> getMaterias_Inscritas(){
		return materias_insctritas;
	}
	public void setMaterias_Inscritas(ArrayList<Materia> materiasInsctritas) {
		this.materias_insctritas = materiasInsctritas;
	}
	
	
	public void asignarMateria  (Materia nuevaMateria) {
		materias_insctritas.add(nuevaMateria);
	}
	public void retirarMateria(Materia Materia) {
		materias_insctritas.remove(Materia);
	}
}
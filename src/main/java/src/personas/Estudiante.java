package personas;

import Calendario.*;

public class Estudiante extends personas{
	public String nombre;
	public int ID_estudiante;
	public Materia materias_insctritas;
	
	
	public Estudiante ( String nombre, int ID_estudiante,  Materia materias_insctritas) {
		this.nombre = nombre;
		this.ID_estudiante = ID_estudiante;
		this.materias_insctritas = materias_insctritas;
	}
	
	
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
	
	
	public Materia getMaterias_inscritas() {
		return materias_insctritas;
	}
	public void setMaterias_Insctritas(Materia materias_inscritas) {
		this.materias_insctritas = materias_inscritas;
	}
	
	
	
}
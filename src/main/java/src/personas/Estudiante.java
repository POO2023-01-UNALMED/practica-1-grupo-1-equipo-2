package personas;

public class Estudiante extends personas{
	public String nombre;
	public int ID_estudiante;
	public materia materias_insctritas;
	
	
	public Estudiante ( String nombre, int ID_estudiante,  materia materias_insctritas) {
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
	
	
	public materia getMaterias_inscritas() {
		return materias_insctritas;
	}
	public void setMaterias_Insctritas(materia materias_inscritas) {
		this.materias_insctritas = materias_inscritas;
	}
	
	
	
}
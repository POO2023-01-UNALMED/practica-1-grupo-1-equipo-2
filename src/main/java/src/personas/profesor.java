package personas;
import Calendario.*;

public class profesor extends personas {
	
	//atributos de instancia
	public String nombre;
	public int ID_profesor;
	public Materia materias_asignadas;
	public String Email;
	
	//constructor
	public profesor (String nombre, int ID_profesor, Materia materias_asignadas) {
		this.nombre=nombre;
		this.ID_profesor = ID_profesor;
		this.materias_asignadas= materias_asignadas;
		this.Email=Email;
	}
	//metodos set y get
	public String getNombre() {
		return nombre;
	}
	public void setNombre(String nombre) {
		this.nombre = nombre;
	}
	public int getID_profesor() {
		return ID_profesor;
	}
	public void setID_profesor(int ID_profesor) {
		this.ID_profesor = ID_profesor;
	}
	
	public String getEmail() {
		return Email;
	}
	public void setEmail(String Email) {
		this.Email=Email;
	}
	
	public Materia getMaterias_asignadas() {
		return materias_asignadas;
	}
	public void setMaterias_asignadas(Materia materias_asignadas) {
		this.materias_asignadas = materias_asignadas;
	}
	

}

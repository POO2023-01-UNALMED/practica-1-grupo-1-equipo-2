package personas;
import Calendario.*;
import java.util.ArrayList;


public class Profesor extends Persona {
	
	//atributos de instancia
	protected ArrayList<Materia> materias_Asignadas;
	
	//constructor
	public Profesor (String nombre, int ID, String Email) {
		super(nombre, ID, Email);
	}
	//metodos set y get
	
	
	public ArrayList<Materia> getMaterias_Asignadas(){
		return materias_Asignadas;
	}
	
	public void setMaterias_Asignadas(ArrayList<Materia> materiasAsignadas) {
		this.materias_Asignadas= materiasAsignadas;
	}
	
	//metodos de clase
	
	public void asignarMateria(Materia nuevaMateria) {
		materias_Asignadas.add(nuevaMateria);
	}
	public void retirarMateria(Materia Materia) {
		materias_Asignadas.remove(Materia);
	}
}

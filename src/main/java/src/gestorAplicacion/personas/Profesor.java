package gestorAplicacion.personas;
import gestorAplicacion.Calendario.*;
import java.util.ArrayList;
import java.io.Serializable;

public class Profesor extends Persona{
	
	//atributos de instancia
	protected ArrayList<Materia> materias_Asignadas;
	private ArrayList<Double> calificacionesDocente;
	private double calificacionDocente;
	
	//constructor
	public Profesor (String nombre, int ID, String Email) {
		super(nombre, ID, Email);
		calificacionesDocente = new ArrayList<Double>();
		materias_Asignadas = new ArrayList<Materia>();
		calificacionDocente = 0;
	}
	//metodos set y get
	
	public void setCalificacionDocente(double calificacion) {
		this.calificacionDocente = calificacion;
	}
	
	public double getCalificacionDocente() {
		return calificacionDocente;
	}
	
	public void setCalificacionesDocente(ArrayList<Double> calificacionDocente) {
		this.calificacionesDocente=calificacionDocente;
	}
	
	public ArrayList<Double> getCalificacionesDocente() {
		return calificacionesDocente;
	}
	
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
	
	public void ingresarCalificacion(double calificacion) {
		calificacionesDocente.add(calificacion);
	}
	
	public void retirarCalificacion(double calificacion) {
		calificacionesDocente.remove(calificacion);
	}
	// Funcionalidad 4: Evaluacion docente
	public void evaluacionDocente() {
		double totalCalificaiones = 0;
		for(double calificacion: calificacionesDocente) {
			totalCalificaiones += calificacion;
		}
		calificacionDocente = Math.round((totalCalificaiones/calificacionesDocente.size())*10)/10.0;
	}
	
	public String toString() {
		return "Docente "+getNombre();
	}
	
}

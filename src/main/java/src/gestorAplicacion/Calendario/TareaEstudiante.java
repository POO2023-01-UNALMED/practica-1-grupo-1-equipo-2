package gestorAplicacion.Calendario;

import gestorAplicacion.personas.Estudiante;
import java.io.Serializable;

public class TareaEstudiante implements Serializable{
    private Tarea tarea;
    private Estudiante estudiante;
    private double grade;

    public TareaEstudiante(Tarea tarea, Estudiante estudiante, double grade) {
        this.tarea=tarea;
        this.estudiante=estudiante;
        this.grade=grade;
    }

	public Estudiante getEstudiante() {
		return estudiante;
	}

	public void setEstudiante(Estudiante estudiante) {
		this.estudiante = estudiante;
	}

	public double getGrade() {
		return grade;
	}

	public void setGrade(double grade) {
		this.grade = grade;
	}

	public Tarea getTarea() {
		return tarea;
	}

	public void setTarea(Tarea tarea) {
		this.tarea = tarea;
	}

    
}
package gestorAplicacion.Calendario;

import java.util.ArrayList;

import gestorAplicacion.personas.Estudiante;
import java.io.Serializable;

public class Tarea implements Serializable{
	
	//atributos
	public ArrayList<TareaEstudiante> tareaEstudiantes;
	protected String descripcion;
	protected String fecha_Entrega;
	protected String fecha_Inicio;

	
	//constructor
	public Tarea(String descripcion, Materia materia, String fecha_Entrega, String fecha_Inicio) {
		this.descripcion = descripcion;
		this.fecha_Entrega = fecha_Entrega;
		this.fecha_Inicio = fecha_Inicio;
		tareaEstudiantes = new ArrayList<>();

	}
	//constructor 2
	public Tarea(Materia materia, String descripcion) {
		this.descripcion = descripcion;
		tareaEstudiantes = new ArrayList<>();
	}
	
	public ArrayList<TareaEstudiante> getTareaEstudiantes(){
		return tareaEstudiantes;
	}
	
	public void setTareaEstudiantes(ArrayList<TareaEstudiante> tareaEstudiantes) {
		this.tareaEstudiantes = tareaEstudiantes;
	}
	public void setDescripcion(String descripcion) {
		this.descripcion=descripcion;
	}
	
	public String getDescripcion() {
		return descripcion;
	}
		
	public void setFecha_Entrega(String fecha_Entrega) {
		this.fecha_Entrega=fecha_Entrega;
	}
	
	public String getFecha_Entrega() {
		return fecha_Entrega;
	}
	
	public void setFecha_Intrega(String fecha_Inicio) {
		this.fecha_Inicio=fecha_Inicio;
	}

	public String getFecha_Inicio() {
		return fecha_Inicio;
	}
	
	public void setGrade(Estudiante estudiante, double grade) {
	    boolean found = false;
	    for (TareaEstudiante tareaEstudiante : tareaEstudiantes) {
	        if (tareaEstudiante.getEstudiante().equals(estudiante)) {
	            tareaEstudiante.setGrade(grade);
	            found = true;
	            break;
	        }
	    }
	    if (!found) {
	        tareaEstudiantes.add(new TareaEstudiante(this, estudiante, grade));
	    }
	}


    public double getGrade(Estudiante estudiante) {
        for (TareaEstudiante tareaEstudiante : tareaEstudiantes) {
            if (tareaEstudiante.getEstudiante().equals(estudiante)) {
                return tareaEstudiante.getGrade();
            }
        }
        return 0.0;
    }
 public String toString() {
	 return "Tarea sobre "+descripcion;
 }
}

package gestorAplicacion.Calendario;

import java.util.ArrayList;

import gestorAplicacion.personas.Estudiante;

public class Tarea {
	
	//atributos
	private ArrayList<TareaEstudiante> tareaEstudiantes;
	protected String descipcion;
	protected String fecha_Entrega;
	protected String fecha_Inicio;

	
	//constructor
	public Tarea(String descripcion, Materia materia, String fecha_Entrega, String fecha_Inicio) {
		this.descipcion =descripcion;
		this.fecha_Entrega = fecha_Entrega;
		this.fecha_Inicio = fecha_Inicio;
		tareaEstudiantes = new ArrayList<>();

	}
	//constructor 2
	public Tarea(Materia materia, String fecha_Entrega) {
		fecha_Inicio = "fecha";
		this.fecha_Entrega = fecha_Entrega;
		tareaEstudiantes = new ArrayList<>();
	}
	
	public void setDescripcion(String descripcion) {
		this.descipcion=descripcion;
	}
	
	public String getDescripcion() {
		return descipcion;
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
    	tareaEstudiantes.add(new TareaEstudiante(this, estudiante, grade));
    }

    public double getGrade(Estudiante estudiante) {
        for (TareaEstudiante tareaEstudiante : tareaEstudiantes) {
            if (tareaEstudiante.getEstudiante().equals(estudiante)) {
                return tareaEstudiante.getGrade();
            }
        }
        return 0.0;
    }

}

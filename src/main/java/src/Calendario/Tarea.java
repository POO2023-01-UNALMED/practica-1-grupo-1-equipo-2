package Calendario;

import personas.*;

public class Tarea {
	
	//atributos
	protected String descipcion;
	protected Materia materia;
	protected String fecha_Entrega;
	protected String fecha_Inicio;
	protected double calificacion;
	private Estudiante estudiante;
	
	//constructor
	public Tarea(String descripcion, Materia materia, String fecha_Entrega, String fecha_Inicio, double calificacion,Estudiante estudiante) {
		this.descipcion =descripcion;
		this.materia = materia;
		this.fecha_Entrega = fecha_Entrega;
		this.fecha_Inicio = fecha_Inicio;
		this.calificacion = calificacion;
		this.estudiante = estudiante;
	}
	//constructor 2
	public Tarea(Materia materia, String fecha_Entrega, double calificacion) {
		fecha_Inicio = "fecha";
		//calificaciones
		this.materia = materia;
		this.fecha_Entrega = fecha_Entrega;
		this.calificacion = calificacion;
		ingresarTarea(this);
	}
	
	public void setDescripcion(String descripcion) {
		this.descipcion=descripcion;
	}
	
	public String getDescripcion() {
		return descipcion;
	}
	
	public void setMateria(Materia materia) {
		this.materia=materia;
	}
	
	public Materia getMateria() {
		return materia;
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
	
	public void setCalificacion(double calificacion) {
		this.calificacion=calificacion;
	}
	
	public double getCalificacion() {
		return calificacion;
	}
	
	public static void ingresarTarea(Tarea tarea) {
		Materia.tareas_de_materia.add(tarea);
	}
	
	public static void eliminarTarea(Tarea tarea) {
		Materia.tareas_de_materia.remove(tarea);
	}

}

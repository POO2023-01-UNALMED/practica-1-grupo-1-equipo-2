package Calendario;

public class Tarea {
	
	//atributos
	protected String descipcion;
	protected Materia materia;
	protected String fecha_Entrega;
	protected String fecha_Inicio;
	protected Calificacion calificaciones;
	
	//constructor
	public Tarea(String descripcion, Materia materia, String fecha_Entrega, String fecha_Inicio, Calificacion calificaciones) {
		this.descipcion =descripcion;
		this.materia = materia;
		this.fecha_Entrega = fecha_Entrega;
		this.fecha_Inicio = fecha_Inicio;
		this.calificaciones = calificaciones;
	}
	//constructor 2
	public Tarea(Materia materia, String fecha_Entrega) {
		fecha_Inicio = "fecha";
		//calificaciones
		this.materia = materia;
		this.fecha_Entrega = fecha_Entrega;		
	}

	//métodos
	public void agregarTarea() {
		
		
	}
	
	public void eliminarTarea() {
		
	}
	public void agregarCalificacion() {
		
	}
}

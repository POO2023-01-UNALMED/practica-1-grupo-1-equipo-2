package Calendario;

public class Tarea {
	
	//atributos
	protected String descipcion;
	protected Materia materia;
	protected String fecha_Entrega;
	protected String fecha_Inicio;
	protected double calificacion;
	
	//constructor
	public Tarea(String descripcion, Materia materia, String fecha_Entrega, String fecha_Inicio, double calificacion) {
		this.descipcion =descripcion;
		this.materia = materia;
		this.fecha_Entrega = fecha_Entrega;
		this.fecha_Inicio = fecha_Inicio;
		this.calificacion = calificacion;
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

	public double getCalificacion() {
		return calificacion;
	}
	
	//métodos
	public void agregarTarea() {
		
		
	}
	
	public static void ingresarTarea(Tarea tarea) {
		Materia.tareas_de_materia.add(tarea);
	}
	
	public void eliminarTarea() {
		
	}
	public void agregarCalificacion() {
		
	}
}

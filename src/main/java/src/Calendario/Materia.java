package Calendario;

import personas.*;
import java.util.ArrayList;

public class Materia {
	
	//atributos de instancia
	private int codigo;
	private String nombre;
	private Profesor profesor;
	private Horario horario;
	private int creditos;
	protected ArrayList<Estudiante> estudiantes_inscritos;
	protected static ArrayList<Tarea> tareas_de_materia;
	
	
	//atributos de clase
	private static int porcentajeDeAvance = 0;
	
	//constructor
	public Materia(int codigo, String nombre, Profesor profesor, Horario horario, int creditos) {
        this.codigo = codigo;
        this.nombre = nombre;
        this.profesor = profesor;
        this.horario = horario;
        this.creditos = creditos;
        tareas_de_materia = new ArrayList<Tarea>();
        estudiantes_inscritos = new ArrayList<Estudiante>();
	}
	
	
	//metodos get y set
	 public int getCodigo() {
	        return codigo;
	    }
	 public void setCodigo(int codigo) {
	        this.codigo = codigo;
	    }
	 
	 
	 public String getNombre() {
	        return nombre;
	    }
	 public void setNombre(String nombre) {
	        this.nombre = nombre;
	    }

	 
	 public Profesor getProfesor() {
	        return profesor;
	    }
	 public void setProfesor(Profesor profesor) {
	        this.profesor = profesor;
	    }

	 
	 public Horario getHorario() {
	        return horario;
	    }
	 public void setHorario(Horario horario) {
	        this.horario = horario;
	    }

	 
	 public int getCreditos() {
	        return creditos;
	    }
	 public void setCreditos(int creditos) {
	        this.creditos = creditos;
	    }
	 
	 
	 public ArrayList<Estudiante> getEstudiantesInscritos() {
	        return estudiantes_inscritos;
	    }
	 public void setEstudiantesInscritos(ArrayList<Estudiante> estudiantesInscritos) {
	        this.estudiantes_inscritos = estudiantesInscritos;
	    }

	 
	 public static ArrayList<Tarea> getTareasDeMateria() {
	        return tareas_de_materia;
	    }
	 public void setTareasDeMateria(ArrayList<Tarea> nuevasTareas) {
	        this.tareas_de_materia = nuevasTareas;
	    }
	
	 
	 public static int getPorcentajeDeAvance() {
		 	return porcentajeDeAvance;
	 	}
	 public static void setPorcentajeDeAvance(int PorcentajeDeAvance) {
		 	porcentajeDeAvance = PorcentajeDeAvance;
	 	}	 
	 
	 
	 //metodos de la clase
	 public void inscribirEstudiante(Estudiante nuevoEstudiante) {
		 estudiantes_inscritos.add(nuevoEstudiante);
	 }
	 public void retirarEstudiante(Estudiante Estudiante) {
		 estudiantes_inscritos.remove(Estudiante);
	 }	 
	 
	 
	 public static double calcularPromedio() {
		 
		 double finalProm = 0.0;
		 //int i=0;i<tareas.size();i++
		 
		 for (Tarea tarea : tareas_de_materia) {
			 finalProm+=tarea.getCalificacion();
		 }
		 
		 return finalProm/tareas_de_materia.size();
	 }
}

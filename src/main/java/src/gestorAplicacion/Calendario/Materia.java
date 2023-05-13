package gestorAplicacion.Calendario;

import gestorAplicacion.personas.Estudiante;
import gestorAplicacion.personas.Profesor;
import java.util.ArrayList;

public class Materia {
	
	//atributos de instancia
	private int codigo;
	private String nombre;
	private Profesor profesor;
	private Horario horario;
	private int creditos;
	//private Estudiante estudiante;
	private ArrayList<TareaEstudiante> promedios;
	private boolean aprobado;
	protected ArrayList<Estudiante> estudiantes_inscritos;
	protected ArrayList<Tarea> tareas_de_materia;
	public enum tipo{ 
		fundamentacion,
		disciplinar,
		libreEleccion
	}
	private tipo tipo;
	protected Materia prerrequisito;
	
	
	//constructor
	public Materia(int codigo, String nombre, Profesor profesor, Horario horario, int creditos,Materia prerrequisito, tipo tipo) {
        this.codigo = codigo;
        this.nombre = nombre;
        this.profesor = profesor;
        this.horario = horario;
        this.creditos = creditos;
        //this.estudiante = estudiante;
        this.aprobado = false;
        tareas_de_materia = new ArrayList<Tarea>();
        estudiantes_inscritos = new ArrayList<Estudiante>();
        this.prerrequisito=prerrequisito;
        this.tipo = tipo;
	}
	public Materia(int codigo, String nombre, Profesor profesor, Horario horario, int creditos, tipo tipo) {
        this.codigo = codigo;
        this.nombre = nombre;
        this.profesor = profesor;
        this.horario = horario;
        this.creditos = creditos;
        //this.estudiante = estudiante;
        this.aprobado = false;
        tareas_de_materia = new ArrayList<Tarea>();
        estudiantes_inscritos = new ArrayList<Estudiante>();
        this.tipo = tipo;
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
	 
	 public ArrayList<TareaEstudiante> getPromedio() {
	        return promedios;
	    }
	 public void setPromedio(ArrayList<TareaEstudiante> promedios) {
	        this.promedios = promedios;
	    }
	 
	 public ArrayList<Estudiante> getEstudiantesInscritos() {
	        return estudiantes_inscritos;
	    }
	 public void setEstudiantesInscritos(ArrayList<Estudiante> estudiantesInscritos) {
	        this.estudiantes_inscritos = estudiantesInscritos;
	    }

	 
	 public ArrayList<Tarea> getTareasDeMateria() {
	        return tareas_de_materia;
	    }
	 public void setTareasDeMateria(ArrayList<Tarea> nuevasTareas) {
	        this.tareas_de_materia = nuevasTareas;
	    }
	 public Materia getPrerrequisito() {
	        return prerrequisito;
	    }
	 public void setPrerrequisito(Materia prerrequisito) {
	        this.prerrequisito = prerrequisito;
	    }
	 
	 
	 public tipo getTipo() {
	        return tipo;
	    }
	 public void setTipo(tipo tipo) {
	        this.tipo = tipo;
	    }
	 
	 
	 //metodos de la clase
	 public void inscribirEstudiante(Estudiante nuevoEstudiante) {
		 estudiantes_inscritos.add(nuevoEstudiante);
	 }
	 public void retirarEstudiante(Estudiante Estudiante) {
		 estudiantes_inscritos.remove(Estudiante);
	 }	 
	 
	 public void inscribirTarea(Tarea tarea) {
		 tareas_de_materia.add(tarea);
	 }
	 public void retirarTarea(Tarea tarea) {
		 tareas_de_materia.remove(tarea);
	 }	 
	 
	 public double calcularPromedio(Estudiante estudiante) {
		 double totalScore = 0;
	        int contador = 0;
	        for (Tarea tarea : tareas_de_materia) {
	        	contador ++;
	            totalScore += tarea.getGrade(estudiante);
	        }
	        return Math.round((totalScore/contador) * 100.0) / 100.0;
	 }
	        
	 public String toString() {
		 return nombre + " " + horario;
	 }
	//5. Metodo calcular nota restante para pasar la materia

	 public double Calcular_necesario_para_pasar(Estudiante estudiante) {
		 double totalScore = 0;
	        int contador = 0;
	        for (Tarea tarea : tareas_de_materia) {
	        	contador ++;
	            totalScore += tarea.getGrade(estudiante);
	        }
	        double nota= Math.round((totalScore/contador) * 100.0) / 100.0;
	 
		 double Nota_necesaria = 0.0;
		 
		 if (nota < 3) {
			 Nota_necesaria = 3*(contador+1)-totalScore;
			 
		 } return Nota_necesaria;
			
		}

}

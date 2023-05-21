package gestorAplicacion.Calendario;

import java.io.Serializable;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

import baseDatos.Deserializador;
import gestorAplicacion.personas.Estudiante;
import gestorAplicacion.personas.Profesor;

public class gestionDatos implements Serializable{
	
	private static final long serialVersionUID = 1L;
	
	private Facultad facultadMinas = new Facultad();
	private List<Estudiante> estudiantes = new ArrayList<Estudiante>();
	private List<Materia> materias = facultadMinas.getMaterias();
	private List<Profesor> profesores = facultadMinas.getProfesores();
	private Beca sistemaBecas = new Beca("");
	
	public gestionDatos() {
			Deserializador.deserializar(this);
		}
	
	//getters y setters
		public List<Materia> getMaterias () {
			return materias;
		}
		public void setMaterias (List<Materia> materias) {
			this.materias = materias;
		}
		public List<Estudiante> getEstudiantes () {
			return estudiantes;
		}
		public void setEstudiantes (List<Estudiante> estudiantes) {
			this.estudiantes = estudiantes;
		}
		public List<Profesor> getProfesores() {
			return profesores;
		}
		public void setProfesores (List<Profesor> profesores) {
			this.profesores=profesores;
		}
		public Beca getSistemaBecas () {
			return sistemaBecas;
		}
		public void setSistemaBecas (Beca sistemaBecas) {
			this.sistemaBecas=sistemaBecas;
		}
		
		
		//metodos
		public Estudiante nuevoEstudiante(String nombre, int ID, String Email, boolean fueBecado, ArrayList<Materia> materias_cursadas) {
			Estudiante nuevoEstudiante = new Estudiante(nombre, ID, Email, fueBecado, materias_cursadas);
			estudiantes.add(nuevoEstudiante);
			return nuevoEstudiante;
		}
		public Estudiante nuevoEstudiante(String nombre, int ID, String Email, boolean fueBecado) {
			Estudiante nuevoEstudiante = new Estudiante(nombre, ID, Email, fueBecado);
			estudiantes.add(nuevoEstudiante);
			return nuevoEstudiante;
		}

}
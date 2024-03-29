package gestorAplicacion.Calendario;
import java.util.ArrayList;
import java.util.Arrays;
import gestorAplicacion.Calendario.Materia.tipo;
import gestorAplicacion.Calendario.*;
import gestorAplicacion.Calendario.Horario.dias;
import gestorAplicacion.personas.Profesor;
import java.io.Serializable;

//Atributos de clase
public class Facultad{
	private String nombre;
	private String carrera;
	protected ArrayList<Materia> materias;
	protected ArrayList<Profesor> profesores;
//Constructor de la clase
	public Facultad(){
		this.nombre = "Minas";
		this.carrera = "Ingenieria de Sistemas";
		materias = new ArrayList<>();
		profesores = new ArrayList<>();
		
		Horario horario1 = new Horario(new ArrayList<dias>(Arrays.asList(dias.lunes, dias.miercoles, dias.viernes)),"8","10");
		Profesor Guillermo = new Profesor("Juan Guillermo", 10, "guille@unal.edu.co");
		Materia Calculo_Diferencial = new Materia(10012,"Calculo Diferencial",Guillermo,horario1,4, tipo.fundamentacion);
		//Guillermo.asignarMateria(Calculo_Diferencial);
		
		Horario horario2 = new Horario(new ArrayList<dias>(Arrays.asList(dias.lunes, dias.martes, dias.jueves)),"8","10");
		Profesor Diego = new Profesor("Diego", 11, "diego@unal.edu.co");
		Materia Calculo_Integral = new Materia(10013, "Calculo Integral", Diego, horario2, 4, Calculo_Diferencial, tipo.fundamentacion);
		
		Horario horario3 = new Horario(new ArrayList<dias>(Arrays.asList(dias.lunes, dias.martes, dias.jueves)),"14","16");
		Profesor Marcos = new Profesor("Marcos", 12, "marcos@unal.edu.co");
		Materia Calculo_VariasVariables = new Materia(10014, "Calculo Varias Variables", Marcos, horario3, 4, Calculo_Integral, tipo.fundamentacion);
		
		Horario horario4 = new Horario(new ArrayList<dias>(Arrays.asList(dias.martes, dias.jueves)),"18","20");
		Profesor Nelson = new Profesor("Nelson", 13, "nelson@unal.edu.co");
		Materia Fundamentos_Programacion = new Materia(10015, "Fundamentos Programacion", Nelson, horario4, 3, tipo.disciplinar);
		
		Horario horario5 = new Horario(new ArrayList<dias>(Arrays.asList(dias.martes, dias.jueves)),"14","16");
		Profesor Jaime = new Profesor("Jaime", 14, "jaime@unal.edu.co");
		Materia Programacion_Orientada_Objetos = new Materia(10016, "Programacion Orientada Objetos", Jaime, horario5, 3, Fundamentos_Programacion, tipo.disciplinar);
		
		Horario horario6 = new Horario(new ArrayList<dias>(Arrays.asList(dias.miercoles, dias.viernes)),"8","10");
		Profesor Julian = new Profesor("Julian", 15, "julian@unal.edu.co");
		Materia Estructura_Datos = new Materia(10017, "Estructura Datos", Julian, horario6, 3, Programacion_Orientada_Objetos, tipo.disciplinar);
		
		Horario horario7 = new Horario(new ArrayList<dias>(Arrays.asList(dias.lunes)),"14","16");
		Profesor Sierra = new Profesor("Sierra", 16, "sierra@unal.edu.co");
		Materia Catedra_Antioquia = new Materia(10018, "Catedra Antioquia", Sierra, horario7, 3, tipo.libreEleccion);
		
		Horario horario8 = new Horario(new ArrayList<dias>(Arrays.asList(dias.sabado)),"8","10");
		Materia Catedra_Apun = new Materia(10019, "Catedra Apun", Sierra, horario8, 3, tipo.libreEleccion);
		
		Horario horario9 = new Horario(new ArrayList<dias>(Arrays.asList(dias.martes)),"8","10");
		Profesor Marisol = new Profesor("Marisol", 17, "marisol@unal.edu.co");
		Materia Catedra_Felicidad = new Materia(10019, "Catedra Felicidad", Marisol, horario9, 3, tipo.libreEleccion);
		
		
		materias.add(Calculo_Diferencial);
		materias.add(Calculo_Integral);
		materias.add(Calculo_VariasVariables);
		materias.add(Fundamentos_Programacion);
		materias.add(Programacion_Orientada_Objetos);
		materias.add(Estructura_Datos);
		materias.add(Catedra_Antioquia);
		materias.add(Catedra_Apun);
		materias.add(Catedra_Felicidad);
		
		for (int i = 0; i<materias.size();i++) {
			Profesor profesor = materias.get(i).getProfesor();
			if (!profesores.contains(profesor))
				profesores.add(profesor);
			profesor.asignarMateria(materias.get(i));
		}
		
	}
	
//Metodos get y set
	public String getNombre() {
		return nombre;
	}
	public void setNombre(String nombre) {
		this.nombre=nombre;
	}
	
	public String getCarrera() {
		return carrera;
	}
	
	public void setCarrera(String carrera) {
		this.carrera=carrera;
	}
	public ArrayList<Materia> getMaterias() {
		return materias;
	}
	
	public void setMaterias (ArrayList<Materia> materias) {
		this.materias=materias;
	}
	public ArrayList<Profesor> getProfesores() {
		return profesores;
	}
	
	public void setProfesores (ArrayList<Profesor> profesores) {
		this.profesores=profesores;
	}
	
}

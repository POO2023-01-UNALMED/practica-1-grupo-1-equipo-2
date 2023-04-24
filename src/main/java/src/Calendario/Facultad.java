package Calendario;
import personas.*;
import java.util.ArrayList;
import java.util.Arrays;

import Calendario.*;
import Calendario.Horario.dias;

//Atributos de clase
public class Facultad {
	private String nombre;
	private String carrera;
	protected ArrayList<Materia> materias;
	protected ArrayList<Profesor> profesores;
//Constructor de la clase
	public Facultad(){
		this.nombre = "Minas";
		this.carrera = "IngenieriaSistemas";
		materias = new ArrayList<>();
		profesores = new ArrayList<>();
		
		Horario horario1 = new Horario(new ArrayList<dias>(Arrays.asList(dias.lunes, dias.miercoles, dias.viernes)),"8","10");
		Profesor Guillermo = new Profesor("Juan Guillermo", 0001, "guille@unal.edu.co");
		Materia Calculo_Diferencial = new Materia(10012,"Calculo_Diferencial",Guillermo,horario1,4);
		
		Horario horario2 = new Horario(new ArrayList<dias>(Arrays.asList(dias.lunes, dias.martes, dias.jueves)),"8","10");
		Profesor Diego = new Profesor("Diego", 0002, "diego@unal.edu.co");
		Materia Calculo_Integral = new Materia(10013, "Calculo_Integral", Diego, horario2, 4, Calculo_Diferencial);
		
		Horario horario3 = new Horario(new ArrayList<dias>(Arrays.asList(dias.lunes, dias.martes, dias.jueves)),"14","16");
		Profesor Marcos = new Profesor("Marcos", 0003, "marcos@unal.edu.co");
		Materia Calculo_VariasVariables = new Materia(10014, "Calculo_VariasVariables", Marcos, horario3, 4, Calculo_Integral);
		
		Horario horario4 = new Horario(new ArrayList<dias>(Arrays.asList(dias.martes, dias.jueves)),"18","20");
		Profesor Nelson = new Profesor("Nelson", 0004, "nelson@unal.edu.co");
		Materia Fundamentos_Programacion = new Materia(10015, "Fundamentos_Programacion", Nelson, horario4, 3);
		
		Horario horario5 = new Horario(new ArrayList<dias>(Arrays.asList(dias.martes, dias.jueves)),"14","16");
		Profesor Jaime = new Profesor("Jaime", 0005, "jaime@unal.edu.co");
		Materia Programacion_Orientada_Objetos = new Materia(10016, "Programacion_Orientada_Objetos", Jaime, horario5, 3, Fundamentos_Programacion);
		
		Horario horario6 = new Horario(new ArrayList<dias>(Arrays.asList(dias.martes, dias.jueves)),"16","18");
		Profesor Julian = new Profesor("Julian", 0006, "julian@unal.edu.co");
		Materia Estructura_Datos = new Materia(10017, "Estructura_Datos", Julian, horario6, 3, Programacion_Orientada_Objetos);
		
		Horario horario7 = new Horario(new ArrayList<dias>(Arrays.asList(dias.lunes)),"14","16");
		Profesor Sierra = new Profesor("Sierra", 0007, "sierra@unal.edu.co");
		Materia Catedra_Antioquia = new Materia(10018, "Catedra_Antioquia", Sierra, horario7, 3);
		
		
		Horario horario8 = new Horario(new ArrayList<dias>(Arrays.asList(dias.sabado)),"8","10");
		Materia Catedra_Apun = new Materia(10019, "Catedra_Apun", Sierra, horario8, 3);
		
		Horario horario9 = new Horario(new ArrayList<dias>(Arrays.asList(dias.martes)),"8","10");
		Profesor Marisol = new Profesor("Marisol", 0011, "marisol@unal.edu.co");
		Materia Catedra_Felicidad = new Materia(10019, "Catedra_Felicidad", Marisol, horario9, 2);
		
		
		
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

	
//Enum con las materias y su categoria
		//Calculo_Diferencial, 
		//Calculo_Integral,
		//Calculo_VariasVariables,
		//Fundamentos_Programacion,
		//Programacion_Orientada_Objetos,
		//Estructura_Datos,
		//Catedra_Antioquia,
		//Catedra_Felicidad,
		//Catedra_Apun,

}

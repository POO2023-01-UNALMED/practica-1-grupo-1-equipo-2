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
		this.nombre="Minas";
		this.carrera="IngenieriaSistemas";
		materias=new ArrayList<>();
		profesores=new ArrayList<>();
		
		Horario horario1 = new Horario(new ArrayList<dias>(Arrays.asList(dias.lunes, dias.miercoles, dias.viernes)),"6","8");
		Profesor Guillermo = new Profesor("Juan Guillermo", 0001, "Guille@unal.edu.co");
		Materia Calculo_Diferencial = new Materia(10012,"Calculo_Diferencial",Guillermo,horario1,4);
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

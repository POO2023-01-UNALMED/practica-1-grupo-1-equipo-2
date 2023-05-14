package gestorAplicacion.Calendario;

import java.io.Serializable;
import java.util.ArrayList;
import java.util.Arrays;

import gestorAplicacion.personas.Estudiante;
import gestorAplicacion.personas.Profesor;

public class gestionDatos implements Serializable{
	
	public static final Facultad Minas =  new Facultad();

	public static void main(String[] args) {
	
	Facultad Minas = new Facultad();
	
	ArrayList<Materia> materiasDisponibles = Minas.getMaterias();

	Estudiante estudiante = new Estudiante("PEPE", 67890, "pp@a.com",false,new ArrayList<Materia>(Arrays.asList(materiasDisponibles.get(0),materiasDisponibles.get(1),materiasDisponibles.get(3))));
	Estudiante estudiante2 = new Estudiante("JHON", 67890, "pp@a.com",false,new ArrayList<Materia>(Arrays.asList(materiasDisponibles.get(0),materiasDisponibles.get(3))));
	Estudiante estudiante3 = new Estudiante("BREADLEY", 67890, "pp@a.com",false,new ArrayList<Materia>(Arrays.asList(materiasDisponibles.get(0),materiasDisponibles.get(3))));
	Estudiante estudiante4 = new Estudiante("BAENA", 67890, "pp@a.com",false,new ArrayList<Materia>(Arrays.asList(materiasDisponibles.get(0),materiasDisponibles.get(3))));

	
	Beca beca = new Beca("Becas Semestre 2023-1s");
	
	ArrayList<Tarea> TareasMaterias = new ArrayList<Tarea>();
	
	//FUNDAMENTACION
	ArrayList<Tarea> TareasCD = new ArrayList<Tarea>();
	Tarea tallerPractico1CD = new Tarea(materiasDisponibles.get(0),"Taller Practico N1");
	TareasCD.add(tallerPractico1CD);
	Tarea tallerPractico2CD = new Tarea(materiasDisponibles.get(0),"Taller Practico N2");
	TareasCD.add(tallerPractico2CD);
	Tarea parcialPracticoCD = new Tarea(materiasDisponibles.get(0),"Parcial Practico");
	TareasCD.add(parcialPracticoCD);
	TareasMaterias.addAll(TareasCD);
	
	
	ArrayList<Tarea> TareasCI = new ArrayList<Tarea>();
	Tarea tallerPractico1CI = new Tarea(materiasDisponibles.get(1),"Taller Practico N1");
	TareasCI.add(tallerPractico1CI);
	Tarea tallerPractico2CI = new Tarea(materiasDisponibles.get(1),"Taller Practico N2");
	TareasCI.add(tallerPractico2CI);
	Tarea parcialPracticoCI = new Tarea(materiasDisponibles.get(1),"Parcial Practico");
	TareasCI.add(parcialPracticoCI);
	TareasMaterias.addAll(TareasCI);
	
	/**
	Tarea tallerPractico1CV = new Tarea(materiasDisponibles.get(2),"Taller Practico N1");
	Tarea tallerPractico2CV = new Tarea(materiasDisponibles.get(2),"Taller Practico N2");
	Tarea parcialPracticoCV = new Tarea(materiasDisponibles.get(2),"Parcial Practico");
	
	//DISCIPLINAR
	Tarea tallerPractico1FP = new Tarea(materiasDisponibles.get(3),"Taller Practico N1");
	Tarea tallerPractico2FP = new Tarea(materiasDisponibles.get(3),"Taller Practico N2");
	Tarea parcialPracticoFP = new Tarea(materiasDisponibles.get(3),"Parcial Practico");
	
	
	Tarea tallerPractico1POO = new Tarea(materiasDisponibles.get(4),"Taller Practico N1");
	Tarea tallerPractico2POO = new Tarea(materiasDisponibles.get(4),"Taller Practico N2");
	Tarea parcialPracticoPOO = new Tarea(materiasDisponibles.get(4),"Parcial Practico");

	
	Tarea tallerPractico1ED = new Tarea(materiasDisponibles.get(5),"Taller Practico N1");
	Tarea tallerPractico2ED = new Tarea(materiasDisponibles.get(5),"Taller Practico N2");
	Tarea parcialPracticoED = new Tarea(materiasDisponibles.get(5),"Parcial Practico");
	
	
	//LIBRE ELECCION
	Tarea tallerPracticoCA = new Tarea(materiasDisponibles.get(6),"Taller Practico N1");
	Tarea tallerPractico2CA = new Tarea(materiasDisponibles.get(6),"Taller Practico N2");
	Tarea parcialPracticoCA = new Tarea(materiasDisponibles.get(6),"Parcial Practico");


	Tarea tallerPracticoCAP = new Tarea(materiasDisponibles.get(7),"Taller Practico N1");
	Tarea tallerPractico2CAP = new Tarea(materiasDisponibles.get(7),"Taller Practico N2");
	Tarea parcialPracticoCAP = new Tarea(materiasDisponibles.get(7),"Parcial Practico");


	Tarea tallerPracticoCF = new Tarea(materiasDisponibles.get(8),"Taller Practico N1");
	Tarea tallerPractico2CF = new Tarea(materiasDisponibles.get(8),"Taller Practico N2");
	Tarea parcialPracticoCF = new Tarea(materiasDisponibles.get(8),"Parcial Practico");
	**/
	
	
	
	}

}
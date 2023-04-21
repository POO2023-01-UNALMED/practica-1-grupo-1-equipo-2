package Calendario;

import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;

import personas.Estudiante;

public class Beca {

	
	private String nombre;
	private tipos tipo;
	private enum tipos {becaInicial, becaNormal, becaAvanzada};
	public static ArrayList<Estudiante> estudiantes;
	protected ArrayList<Estudiante> estudiantesAptosInicial;
	protected ArrayList<Estudiante> estudiantesAptosNormal;
	protected ArrayList<Estudiante> estudiantesAptosAvanzada;
	
	
	public Beca(String nombre) {
		this.nombre = nombre;
		estudiantes = new ArrayList<Estudiante>();
		estudiantesAptosInicial = new ArrayList<Estudiante>();
		estudiantesAptosNormal = new ArrayList<Estudiante>();
		estudiantesAptosAvanzada = new ArrayList<Estudiante>();
	}
	
	
	public void asignarEstudiantesBeca() {
		estudiantesAptosInicial = new ArrayList<Estudiante>();
		estudiantesAptosNormal = new ArrayList<Estudiante>();
		estudiantesAptosAvanzada = new ArrayList<Estudiante>();
	        
		for (Estudiante estudiante : estudiantes) {
	            if (estudiante.getPorcentajeDeAvance() >= 20 && estudiante.getPorcentajeDeAvance() < 40 &&
	            		estudiante.calcularPromedio() >= 4.5 &&
	            		estudiante.getFueBecado() == false) {
	            	estudiantesAptosInicial.add(estudiante);
	            	}
	            
	            else if (estudiante.getPorcentajeDeAvance() >= 40 && estudiante.getPorcentajeDeAvance() < 60 &&
	            		estudiante.calcularPromedio() >= 4.0 &&
	            		estudiante.getFueBecado() == false) {
	            	estudiantesAptosNormal.add(estudiante);
			    	
				}
			    else {
			    	estudiantesAptosAvanzada.add(estudiante);
			    }
	        }
	        Collections.sort(estudiantesAptosInicial, Comparator.comparingDouble(Estudiante::calcularPromedio).reversed());
	        Collections.sort(estudiantesAptosNormal, Comparator.comparingDouble(Estudiante::calcularPromedio).reversed());
	        Collections.sort(estudiantesAptosAvanzada, Comparator.comparingDouble(Estudiante::calcularPromedio).reversed());
	        
	        for (int i = 0; i<2;i++) {
	        	this.estudiantesAptosInicial.add(estudiantesAptosInicial.get(i));
	        	this.estudiantesAptosNormal.add(estudiantesAptosNormal.get(i));
	        	this.estudiantesAptosAvanzada.add(estudiantesAptosAvanzada.get(i));
	        }
		}
}
	




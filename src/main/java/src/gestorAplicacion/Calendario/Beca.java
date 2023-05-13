package gestorAplicacion.Calendario;

import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;

import gestorAplicacion.personas.Estudiante;
import java.io.Serializable;

public class Beca implements Serializable{

	//Funcionalidad 3: asignación de becas Becas
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
	
	
	public ArrayList<Estudiante> getEstudiantes() {
	    return estudiantes;
	}

	public void setEstudiantes(ArrayList<Estudiante> estudiantes) {
	    Beca.estudiantes = estudiantes;
	}
	
	
	public void asignarEstudiantesBeca() {
		ArrayList<Estudiante>estudiantesAptosInicial2 = new ArrayList<Estudiante>();
		ArrayList<Estudiante>estudiantesAptosNormal2 = new ArrayList<Estudiante>();
		ArrayList<Estudiante>estudiantesAptosAvanzada2 = new ArrayList<Estudiante>();
	        
		for (Estudiante estudiante : estudiantes) {
	            if (estudiante.getPorcentajeDeAvance() >= 20 && estudiante.getPorcentajeDeAvance() < 40 &&
	            		estudiante.calcularPromedio() >= 4.5 &&
	            		estudiante.getFueBecado() == false) {
	            	estudiantesAptosInicial2.add(estudiante);
	            	}
	            
	            else if (estudiante.getPorcentajeDeAvance() >= 40 && estudiante.getPorcentajeDeAvance() < 60 &&
	            		estudiante.calcularPromedio() >= 4.0 &&
	            		estudiante.getFueBecado() == false) {
	            	estudiantesAptosNormal2.add(estudiante);
			    	
				}
			    else if(estudiante.getPorcentajeDeAvance() >= 60 && estudiante.getPorcentajeDeAvance() < 100 &&
	            		estudiante.calcularPromedio() >= 3.5 &&
	            		estudiante.getFueBecado() == false){
			    	estudiantesAptosAvanzada2.add(estudiante);
			    }
	        }
	        Collections.sort(estudiantesAptosInicial2, Comparator.comparingDouble(Estudiante::calcularPromedio).reversed());
	        Collections.sort(estudiantesAptosNormal2, Comparator.comparingDouble(Estudiante::calcularPromedio).reversed());
	        Collections.sort(estudiantesAptosAvanzada2, Comparator.comparingDouble(Estudiante::calcularPromedio).reversed());
	        
	        if (estudiantesAptosInicial2.size()>=2) {
	        	for (int i = 0; i<2;i++) {
		        	this.estudiantesAptosInicial.add(estudiantesAptosInicial2.get(i));
	        	}     
	       }
	        else if (estudiantesAptosInicial2.size()==1) {
        		this.estudiantesAptosInicial.add(estudiantesAptosInicial2.get(0));
	        }
	        
	        if (estudiantesAptosNormal2.size()>=2) {
	        	for (int i =0; i<2; i++) {
		        	this.estudiantesAptosNormal.add(estudiantesAptosNormal2.get(i));

	        	}
	        }
	     
	        else if (estudiantesAptosNormal2.size()==1) {
	        	this.estudiantesAptosNormal.add(estudiantesAptosNormal2.get(0));
	        }
	        
	        if (estudiantesAptosAvanzada2.size()>=2) {
	        	for (int i =0; i<2; i++) {
	        		this.estudiantesAptosAvanzada.add(estudiantesAptosAvanzada2.get(i));
	        	}
	        }
	        
	        else if (estudiantesAptosAvanzada2.size()==1) {
	        	this.estudiantesAptosAvanzada.add(estudiantesAptosAvanzada2.get(0));
	        }
		}
}
	




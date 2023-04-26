
package Calendario;

import java.util.ArrayList;
import java.util.Arrays;

import personas.*;

public class TEST {

	public static void main(String[] args) {
		
		Facultad Minas = new Facultad();
		
		ArrayList<Materia> materiasDisponibles = Minas.getMaterias();
		
		Estudiante est = new Estudiante("PEPE", 67890, "pp@a.com",false,20,new ArrayList<Materia>(Arrays.asList(materiasDisponibles.get(0),materiasDisponibles.get(1),materiasDisponibles.get(3))));
		Estudiante est2 = new Estudiante("JHON", 67890, "pp@a.com",false,20,new ArrayList<Materia>(Arrays.asList(materiasDisponibles.get(0),materiasDisponibles.get(3))));
		Estudiante est3 = new Estudiante("BREADLEY", 67890, "pp@a.com",false,45,new ArrayList<Materia>(Arrays.asList(materiasDisponibles.get(0),materiasDisponibles.get(3))));
		Estudiante est4 = new Estudiante("BAENA", 67890, "pp@a.com",false,65,new ArrayList<Materia>(Arrays.asList(materiasDisponibles.get(0),materiasDisponibles.get(3))));
		
		
		//System.out.println(materiasDisponibles);
		
		
		est.inscribirMateria("Calculo VariasVariables",materiasDisponibles);
		est2.inscribirMateria("Calculo Integral",materiasDisponibles);
		est3.inscribirMateria("Calculo Integral",materiasDisponibles);
		est4.inscribirMateria("Calculo Integral",materiasDisponibles);
		
		est.inscribirMateria("Programacion Orientada Objetos",materiasDisponibles);
		est2.inscribirMateria("Programacion Orientada Objetos",materiasDisponibles);
		est3.inscribirMateria("Programacion Orientada Objetos",materiasDisponibles);
		est4.inscribirMateria("Programacion Orientada Objetos",materiasDisponibles);
		
		
		Tarea tallerP = new Tarea(materiasDisponibles.get(1),"NOSE");
		tallerP.setGrade(est,5.0);
		tallerP.setGrade(est2,2.0);
		tallerP.setGrade(est3,1.0);
		tallerP.setGrade(est4,3.5);
		materiasDisponibles.get(1).inscribirTarea(tallerP);

		
		Tarea tallerP2 = new Tarea(materiasDisponibles.get(4),"NOSE2");
		tallerP2.setGrade(est,5.0);
		tallerP2.setGrade(est2,1.0);
		tallerP2.setGrade(est3,1.0);
		tallerP2.setGrade(est4,3.5);
		materiasDisponibles.get(4).inscribirTarea(tallerP2);
		
		Tarea tallerP3 = new Tarea(materiasDisponibles.get(4),"NOSE3");
		tallerP3.setGrade(est,5.0);
		tallerP3.setGrade(est2,1.1);
		tallerP3.setGrade(est3,1.0);
		tallerP3.setGrade(est4,3.5);
		materiasDisponibles.get(4).inscribirTarea(tallerP3); 

		
		Beca beca = new Beca("SISAS");
		
		Estudiante.aplicarBeca(est);
		Estudiante.aplicarBeca(est2);
		Estudiante.aplicarBeca(est3);
		Estudiante.aplicarBeca(est4);
		beca.asignarEstudiantesBeca();
		
		System.out.println("Admitidos a becas: ");
		System.out.println("Beca Inicial: "+beca.estudiantesAptosInicial);
		System.out.println("Beca Normal: "+beca.estudiantesAptosNormal);
		System.out.println("Beca Avanzada: "+beca.estudiantesAptosAvanzada+"\n");
		
		double promedioEst = est.calcularPromedio();
		double promedioEst2 = est2.calcularPromedio();
		double promedioEst3 = est3.calcularPromedio();
		double promedioEst4= est4.calcularPromedio();
		
		System.out.println("Promedios: ");
		System.out.println(est+" promedio: "+promedioEst);
		System.out.println(est2+" promedio: "+promedioEst2);
		System.out.println(est3+" promedio: "+promedioEst3);
		System.out.println(est4+" promedio: "+promedioEst4+"\n");
		
		System.out.println("Horarios: ");
		
		boolean nose = est.compararHorario(est.getMaterias_Inscritas());
		
		System.out.println("El horario de "+est+" es:");
		System.out.println(est.getMaterias_Inscritas()+"\n");
		
		System.out.println("El horario de "+est+" presenta fallas?");
		System.out.println(nose+"\n");
		
		est.sugerirMaterias(materiasDisponibles);
		
		System.out.println("Nuevo horario del estudiante "+est.getNombre()+": ");
		System.out.println(est.getMaterias_Inscritas()+"\n");
		
		
	}

}

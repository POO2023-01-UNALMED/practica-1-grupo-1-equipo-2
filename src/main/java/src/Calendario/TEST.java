
package Calendario;

import personas.*;

public class TEST {

	public static void main(String[] args) {
		
		Estudiante est = new Estudiante("PEPE", 67890, "pp@a.com",false,20);
		Estudiante est2 = new Estudiante("JHON", 67890, "pp@a.com",false,20);
		Estudiante est3 = new Estudiante("BRADLEY", 67890, "pp@a.com",false,20);
		Estudiante est4 = new Estudiante("BAENA", 67890, "pp@a.com",false,65);
		
		
		Profesor pro = new Profesor("PABLO",12345,"jjk@a.com");
		Horario ho = new Horario(Horario.dias.martes ,"2","3");
		Horario ho1 = new Horario(Horario.dias.miercoles, "2", "3" );
		
		Materia MD = new Materia (456, "MD", pro, ho1, 4);
		Materia GVA = new Materia(123,"GVA",pro,ho,4);
		
		MD.inscribirEstudiante(est);
		MD.inscribirEstudiante(est2);
		MD.inscribirEstudiante(est3);
		MD.inscribirEstudiante(est4);


		
		//Materia MDP = new Materia (456, "MD", pro, ho1, 4,est2);
		//Materia GVAP = new Materia(123,"GVA",pro,ho,4,est2);
		
		//Materia MDB = new Materia (456, "MD", pro, ho1, 4,est3);
		//Materia GVAB = new Materia(123,"GVA",pro,ho,4,est3);
		
		//Materia MDBBA = new Materia (456, "MD", pro, ho1, 4,est4);
		//Materia GVABA = new Materia(123,"GVA",pro,ho,4,est4);
		
		
		Tarea tallerP = new Tarea(GVA,"NOSE");
		tallerP.setGrade(est,5.0);
		tallerP.setGrade(est2,2.0);
		tallerP.setGrade(est3,3.5);
		tallerP.setGrade(est4,2.8);
		GVA.inscribirTarea(tallerP);

		
		Tarea tallerP2 = new Tarea(GVA,"NOSE2");
		tallerP2.setGrade(est,3.0);
		tallerP2.setGrade(est2,1.0);
		tallerP2.setGrade(est3,2.8);
		tallerP2.setGrade(est4,1.5);
		MD.inscribirTarea(tallerP2);
		
		Tarea tallerP3 = new Tarea(GVA,"NOSE3");
		tallerP3.setGrade(est,4.0);
		tallerP3.setGrade(est2,1.1);
		tallerP3.setGrade(est3,0.4);
		tallerP3.setGrade(est4,4.5);
		MD.inscribirTarea(tallerP3); 

		
		//Tarea tallerJ = new Tarea(GVA,"NOSE",4.5);
		//Tarea tallerJ2 = new Tarea(GVA,"NOSE2",4.5);
		
		
		//Tarea tallerB = new Tarea(GVA,"NOSE",4.8);
		//Tarea tallerB2 = new Tarea(GVA,"NOSE2",4.8);
		
	
		//Tarea tallerBA = new Tarea(GVA,"NOSE",4);
		//Tarea tallerBA2 = new Tarea(GVA,"NOSE2",4);
		
		//Beca beca = new Beca("SISAS");
		//beca.asignarEstudiantesBeca();
		
		//System.out.println(beca.estudiantes);
		//System.out.println(beca.estudiantesAptosInicial);
		//System.out.println(beca.estudiantesAptosNormal);
		//System.out.println(beca.estudiantesAptosAvanzada);
		double promedioEst = est.calcularPromedio();
		double promedioEst2 = est2.calcularPromedio();
		double promedioEst3 = est3.calcularPromedio();
		double promedioEst4= est4.calcularPromedio();
		
		System.out.println(promedioEst+ promedioEst2 + promedioEst3 + promedioEst4);

		
		
		
		
		//Estudiante est = new Estudiante("PEPE", 67890, "pp@a.com");
		//System.out.println(Materia.calcularPromedio());
		//System.out.println(Estudiante.compararHorario());
	}

}

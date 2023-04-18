
package Calendario;

import personas.*;

public class TEST {

	public static void main(String[] args) {
		Estudiante est = new Estudiante("PEPE", 67890, "pp@a.com");
		Profesor pro = new Profesor("PABLO",12345,"jjk@a.com");
		Horario ho = new Horario(Horario.dias.martes ,"2","3");
		Horario ho1 = new Horario(Horario.dias.miercoles, "2", "3" );
		Materia MD = new Materia (456, "MD", pro, ho1, 4,est);
		Materia GVA = new Materia(123,"GVA",pro,ho,4,est);
		Tarea taller1 = new Tarea(GVA,"NOSE",3.0);
		Tarea taller2 = new Tarea(GVA,"NOSE2",2.5);
		//Estudiante est = new Estudiante("PEPE", 67890, "pp@a.com");
		//System.out.println(Materia.calcularPromedio());
		System.out.println(Estudiante.compararHorario());
	}

}

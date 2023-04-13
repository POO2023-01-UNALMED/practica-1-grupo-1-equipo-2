
package Calendario;

import personas.*;

public class TEST {

	public static void main(String[] args) {
		
		Profesor pro = new Profesor("PABLO",12345,"jjk@a.com");
		Horario ho = new Horario("1","2","3");
		
		Materia GVA = new Materia(123,"GVA",pro,ho,4);
		Tarea taller1 = new Tarea(GVA,"NOSE",3.0);
		Tarea taller2 = new Tarea(GVA,"NOSE2",2.5);
		
		System.out.println(Materia.calcularPromedio());
	}

}

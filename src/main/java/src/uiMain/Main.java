package uiMain;

import java.util.Scanner;

import baseDatos.Deserializador;
import baseDatos.Serializador;
import gestorAplicacion.*;
import gestorAplicacion.Calendario.gestionDatos;

public class Main {


	static Scanner sc = new Scanner(System.in);
	static long readLong() {
		return sc.nextLong();
	}
	static String readln() {
		sc.nextLine();
		return sc.nextLine();
	}
	private static void salirDelSistema(gestionDatos gestor) {
		System.out.println("Proceso terminado");
		Serializador.serializar(gestor);
		System.exit(0);
	}
	static void test(gestionDatos gestor) {
		System.out.println("Nombre: ");
		String nombre = readln();
		
		System.out.println("ID: ");
		int ID = (int) readLong();
		
		System.out.println("Email: ");
		String Email = readln();


		System.out.println("¿Fue becado anteriormente?: ");
		System.out.println("1: Si");
		System.out.println("2: No");
		boolean fueBecado = false;
		String opcion = readln();
		if (opcion == "1") {fueBecado = true;}
		
		gestor.nuevoEstudiante(nombre, ID, Email, fueBecado);
		System.out.println("Estudiante matriculado");
	}
	public static void main(String args[]) {

		
		gestionDatos gestor = new gestionDatos();
		int opcion;
		do {
			System.out.println("Que desea hacer?");
			System.out.println("1. Matricular alumno");
			System.out.println("5. Terminar");
			opcion = (int) readLong();
			
			switch(opcion) {
			case 1: test(gestor); break;
			case 5: salirDelSistema(gestor); break;
			}
		} while (opcion != 5);
	
	}
}
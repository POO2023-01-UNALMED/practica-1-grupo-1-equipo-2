package Calendario;

import personas.*;

public class Calificacion{
	private Materia materia;
	private Estudiante estudiante;
	public int NOTA;
	
	public Calificacion(Materia materia, Estudiante estudiante, int nota) {
		this.materia = materia;
		this.estudiante = estudiante;
		this.NOTA= nota;
	}
	public void actualizarNota(int NOTA) {
		this.NOTA= NOTA;
	}
	public int verNota() {
		return NOTA;
	}
}

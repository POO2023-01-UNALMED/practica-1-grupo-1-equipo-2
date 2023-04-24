package Calendario;

import java.util.ArrayList;

public class Horario {
	
	protected ArrayList<dias> dia;
	private String hora_inicio;
	private String hora_Fin;
	public enum dias {lunes, martes, miercoles, jueves, viernes, sabado, domingo};
	
	
	public Horario(ArrayList<dias> dia,String hora_inicio,String hora_Fin) {
		
		this.dia = dia;
		this.hora_inicio = hora_inicio;
		this.hora_Fin = hora_Fin;
		
	}
	
	
	public ArrayList<dias> getDia() {
        return dia;
    }

    public void setDia(ArrayList<dias> dia) {
        this.dia = dia;
    }

    public String getHora_inicio() {
        return hora_inicio;
    }

    public void setHora_inicio(String hora_inicio) {
        this.hora_inicio = hora_inicio;
    }

    public String getHora_Fin() {
        return hora_Fin;
    }

    public void setHoraFinal(String hora_Fin) {
        this.hora_Fin = hora_Fin;
    }
    
    public String toString() {
    	return dia + " de " + hora_inicio + " a " + hora_Fin;
    }
}



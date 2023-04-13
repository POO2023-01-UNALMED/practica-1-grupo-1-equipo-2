package Calendario;

public class Horario {
	
	private dias dia;
	private String hora_inicio;
	private String hora_Fin;
	public enum dias {lunes, martes, miercoles, jueves, viernes, sabado, domingo};
	
	
	public Horario(dias dia,String hora_inicio,String hora_Fin) {
		
		this.dia = dia;
		this.hora_inicio = hora_inicio;
		this.hora_Fin = hora_Fin;	 	
	}
	
	
	public dias getDia() {
        return dia;
    }

    public void setDia(dias dia) {
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
}



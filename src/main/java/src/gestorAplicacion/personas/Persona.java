package gestorAplicacion.personas;

public abstract class Persona {
	//Atributos clase abstracta
	public String nombre;
	public long ID;
	public String Email;
	
	public Persona (String nombre, long ID, String Email) {
		this.nombre=nombre;
		this.ID = ID;
		this.Email=Email;
	}
	
	//metodos get y set 
	public String getNombre() {
		return nombre;
	}
	public void setNombre(String nombre) {
		this.nombre = nombre;
	}
	public long getID() {
		return ID;
	}
	public void setID(long ID) {
		this.ID=ID;
	}
	
	public String getEmail() {
		return Email;
	}
	public void setEmail(String Email) {
		this.Email=Email;
	}
}

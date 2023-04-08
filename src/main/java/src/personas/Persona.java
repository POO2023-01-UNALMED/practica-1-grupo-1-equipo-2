package personas;

public abstract class Persona {
	//Atributos clase abstracta
	public String nombre;
	public int ID;
	public String Email;
	
	
	//metodos get y set 
	public String getNombre() {
		return nombre;
	}
	public void setNombre(String nombre) {
		this.nombre = nombre;
	}
	public int getID() {
		return ID;
	}
	public void setID(int ID) {
		this.ID=ID;
	}
	
	public String getEmail() {
		return Email;
	}
	public void setEmail(String Email) {
		this.Email=Email;
	}
//aa
}

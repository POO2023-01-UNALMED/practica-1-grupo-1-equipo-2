package baseDatos;

import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.ObjectOutputStream;
import java.util.List;

import 
import
import

public class Deserializador{
	private static File rutaTemp = new File("scr\\baseDatos\\temp");
	
	private static void deserializar (Departamento dpto) {
		File[] docs = rutaTemp.listFiles();
		FileInputStream fis;
		ObjectInputStram ois;
		
		for(File file : docs) {
			if (file.getAbsolutePath().contains("asignaturas")){
				try {
					fis = new FileInputStream(file);
					ois = new ObjectInputStream (fis);
					
					dpto.setAsignaturas((List<Asignaturas>) ois.readObject());
				}catch(FileNotFoundException e) {
					e.printStackTrace();
				}catch (IOException e) {
					e.printStackTrace();
				}catch (ClassNotFoundException e) {
					e.printStackTrace();
				}
			} else if (file.getAbsolutePath().contains("alumnos")) {
				try {
					fis = new FileInputStream(file);
					ois = new ObjectInputSream(fis);
					
					dpto.setAlumnos ((List<Alumno>) ois.readObject());
					
				}catch (FileNotFoundException e) {
					e.printStackTrace();
				}catch (IOException e) {
					e.printStackTrace();
				}catch (ClassNotFoundException e) {
					e.printStackTrace();
				}
			}
		}
	}
}


package baseDatos;

import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.ObjectOutputStream;
import java.io.PrintWriter;

import Calendario. ;

public class Serializador {
	private static File rutaTemp = new File ("scr\\baseDatos\\temp");
	
	public static void serializar(Departamento departamento) {
		FileOutputStream fos;
		ObjectOutputStream oos;
		File[] docs = rutaTemp.listFiles();
		PrintWriter pw;
		
		
	for (File file : docs) {
		try {
			pw = new PrintWriter(file);
		}catch(FileNotFoundException e) {
			e.printStackTrace();
		}
	}
	
	for (File file :docs) {
		if (file.getAbsolutePath().contains("asignaturas")) {
			try {
				fos = new FileOutputStream(file);
				oos = new ObjectOutputStream(fos);
				oos.writeObject(dpto.getAsignaturas());
			}catch (FileNotFoundException e) {
				e.printStackTrace();
			}catch (IOException e) {
				e.printStackTrace();
			}
		}else if (file.getAbsolutePath().contains("alumnos")) {
			try {
				fos = new FileOutputStream(file);
				oos = new ObjectOutputStream(fos);
				oos.writerObject(dpto.getAlumnos());
			}catch (FileNotFoundException e) {
				e.printStackTrace();
			}catch (IOException e) {
				e.printStackTrace();
			} 
		}
	}
}

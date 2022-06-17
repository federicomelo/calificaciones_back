package controler;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.File;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.io.PrintWriter;

public abstract class ArchiveManager {
	
	public static boolean createTXT(String path) {
		boolean loCreo;
		File archivo = new File(path);
		try {
			loCreo = archivo.createNewFile();
		} catch (IOException e) {
			System.out.println("Error: No se pudo crear el TXT.");
			loCreo = false;
			e.printStackTrace();
		}
		return loCreo;
	}

	
	/**
	 * Takes in as parameters the path to a TXT file, and the name of a field (e.g. "Final Grade: ").
	 * Returns the value of that field, that is, whatever is in front of it on the TXT file.
	 * 
	 * For example, if the TXT has the line "Final Grade: 4.75", calling the method for "Final Grade: "
	 * returns "4.75".
	 * 
	 * @param	path	path to a TXT file as String
	 * @param	field	field to be read as String
	 * @return	value	read for the given field. If there is no such field on the TXT file, the return is "".
	 */
	public static String readField(String path, String field) {
		String valorCampo = "";
		BufferedReader lector = null;
		try {
			lector = new BufferedReader(new FileReader(path));
			String lineaActual = lector.readLine();
			while (lineaActual != null) {
				if (lineaActual.contains(field)) {
					valorCampo = lineaActual.substring(field.length());
					break;
				}
				lineaActual = lector.readLine();
			}
		} catch (IOException e) {
			   e.printStackTrace();
		} finally {
			try {
			    if (lector != null) {
			    	lector.close();
			    }
			} catch (IOException ex) {
			    ex.printStackTrace();
			}
		}
		return valorCampo;
	}
	
	
	/**
	 * Takes in as parameters the path to a TXT file, the name of a field (e.g. "Final Grade: "), and
	 * a new value for said field.
	 * The method changes the value of the given field, which is whatever is in front of it on the TXT file.
	 * 
	 * @param	path	path to a TXT file, as a String
	 * @param	field	field to be modified, as a String
	 * @param	newValue	new value for the given field
	 */
	public static void modifyField(String path, String field, String newValue) {
		String infoArchivo = "";
		File archivo = new File(path);
		BufferedReader lector = null;
		FileWriter writer = null;
		try {
			lector = new BufferedReader(new FileReader(path));
			String lineaActual = lector.readLine();
			while (lineaActual != null) {			
				if (lineaActual.contains(field)) {
					infoArchivo = infoArchivo + field + newValue + System.lineSeparator();
				} else {
					infoArchivo = infoArchivo + lineaActual + System.lineSeparator();
				}
				lineaActual = lector.readLine();
			}
			writer = new FileWriter(archivo);
			writer.write(infoArchivo);
		} catch (IOException e) {
			System.out.println("Error: No se pudo modificar el campo. ");
			e.printStackTrace();
		} finally {
			try {
			    if (lector != null) {
			    	lector.close();
			    }
			    if (writer != null) {
			    	writer.close();
			    }
			} catch (IOException ex) {
			    ex.printStackTrace();
			}
		}
	}
	
	
	/**
	 * Identical to the previous method, but instead of modifiyng the field it just adds writes more text on 
	 * in front of the value it already has.
	 * 
	 * @param	field	field to be modified, as a String. If it is an empty String, "", the method writes
	 * at the end of the TXT file.
	 */
	public static void addToField(String path, String campo, String valorAdicional) {
		if (campo != "") {
			String infoArchivo = "";  // Aca se recrea todo el archivo como TXT, cambiando la linea que es
			File archivo = new File(path);
			BufferedReader lector = null;
			FileWriter writer = null;
			try {
				lector = new BufferedReader(new FileReader(path));
				String lineaActual = lector.readLine();
				while (lineaActual != null) {			
					if (lineaActual.contains(campo)) {
						infoArchivo = infoArchivo + lineaActual + valorAdicional + System.lineSeparator();
					} else {
						infoArchivo = infoArchivo + lineaActual + System.lineSeparator();
					}
					lineaActual = lector.readLine();
				}
				writer = new FileWriter(archivo);
				writer.write(infoArchivo);
			} catch (IOException e) {
				System.out.println("Error: No se pudo anhadir informacion al campo.");
				e.printStackTrace();
			} finally {
				try {
				    if (lector != null) {
				    	lector.close();
				    }
				    if (writer != null) {
				    	writer.close();
				    }
				} catch (IOException ex) {
					System.out.println("Error: No se cerró alguno de los writers al anhadir informacion al campo");
				    ex.printStackTrace();
				}
			}
		} else {
			FileWriter fileW = null;
			BufferedWriter buferW = null;
			PrintWriter writer = null; 
	        try {
	        	fileW = new FileWriter(path, true);
	        	buferW = new BufferedWriter(fileW);
	            writer = new PrintWriter(buferW);
	            
	            writer.println(valorAdicional);
	        } catch (IOException e) {
	        	System.out.println("Error: No se pudo anhadir informacion al final del archivo.");
	            e.printStackTrace();
	        } finally {
	        	try {
	        		writer.close();
	        		buferW.close();
	        		fileW.close();
	        	} catch (IOException ex) {
	        		System.out.println("Error: No se cerro alguno de los writers al anhadir informacion al final del archivo.");
	        		ex.printStackTrace();
	        	}
	        }
		}
	}
	
}

package controler;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;

public abstract class GradesReader {

	public static ArrayList<String[]> readTSV(String path) {
		ArrayList<String[]> fileData = new ArrayList<String[]>();
		BufferedReader lector = null;
		try {
			lector = new BufferedReader(new FileReader(path));
			String currentLine = lector.readLine();
			while (currentLine != null) {
	            String[] lineItems = currentLine.split("\t");
	            fileData.add(lineItems);
				currentLine = lector.readLine();
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
		return fileData;
	}


}

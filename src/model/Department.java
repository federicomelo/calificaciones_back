package model;

import java.util.Map;

import controler.GeneralInfo;
import controler.GradesReader;

import java.io.File;
import java.util.ArrayList;
import java.util.HashMap;

public class Department implements GeneralInfo{
	private Map<String, String> departments = new HashMap<String, String>();
	private String code;
	private String name;
	
	public Department(String code) throws Exception {
		fillMap();
		this.code = code;
		if (departments.containsKey(code)) {
			this.name = departments.get(code);
		} else {
			this.name = "Departamento o facultad desconocida";
			throw new Exception("El departamento o facultad que ofrece la materia no está en la lista de departamentos.");
		}
	}
	
	
	private void fillMap() {
		ArrayList<String[]> departmentsFile = GradesReader.readTSV(DATA.getAbsolutePath()+File.separator+"departamentos.tsv");
		for (String[] line: departmentsFile) {
			if (line.length > 1) {
				this.departments.put(line[0], line[1]);
			}
		}
	}


	public String getCode() {
		return code;
	}


	public String getName() {
		return name;
	}
}

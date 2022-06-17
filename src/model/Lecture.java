package model;

import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.io.PrintWriter;
import java.util.ArrayList;


public class Lecture extends Course {

	private String name;
	private int credits;
	private String section;
	private String code;
	private Department department;
	private String[] professors;
	private Semester semester;
	private ArrayList<Discussion> discussions = new ArrayList<Discussion>();

	
	public Lecture(String name, String departmentCode, String subjectCode, String section, int credits, String[] professors, Semester semester) {
		this.name = name;
		try {
			this.department = new Department(departmentCode);
		} catch (Exception e) {
			System.out.println(e.getMessage());
			e.printStackTrace();
		}
		this.code = subjectCode;
		this.section = section;
		this.credits = credits;
		this.professors = professors;
		this.semester = semester;
	}
	

	public static Lecture readLectureFromLines(String[] lectureLine, String[] creditsLine, String[] professorsLine, Semester semester) {
		String s = lectureLine[0];
		int colonPosition = s.indexOf(":");
		int comaPosition = s.indexOf(",");
		String departmentCode = s.substring(0, 4);
		String courseCode = s.substring(5, 9);
		String section = s.substring(comaPosition+1, colonPosition).strip();
		String subjectName = s.substring(colonPosition+1).strip();
		
		int credits = Integer.valueOf(creditsLine[0]);

		Lecture lecture = new Lecture(subjectName, departmentCode, courseCode, section, credits, professorsLine, semester);
		return lecture;
	}
	
	
	public static boolean lineIsLecture(String[] line) {
		boolean isLecture = false;
		if (line.length>0) {
			if (line[0].length()>4) {
				String departmentCode = line[0].substring(0, 4);
				if (Department.codeIsDepartment(departmentCode)) {
					isLecture = true;
				}
			}
		}
		return isLecture;
	}
	
	
	public void writeTXT() {
		FileWriter fileWriter;
		try {
			String path = this.locateFile().getAbsolutePath();
			fileWriter = new FileWriter(path);
			PrintWriter printWriter = new PrintWriter(fileWriter);	
			
			String titulo = this.getFormatedName();
			String nombre = this.getName();
			String profesores = String.join(", ", this.getProfessors());
			String semestre = this.getSemester().getYearAndPeriod();
			String departamento = this.getDepartment().getName()+" ("+this.getDepartment().getCode()+")";
			String codigo = this.getCode();
			String seccion = this.getSection();
			String notaFinal = String.valueOf(this.getFinalGrade());
			String trabajos = "";
			for (Assignment assignment: assignments) {
				trabajos += assignment.writeAssignment();
			}
			
			printWriter.printf("%s \n\n"
					 		 + "---------------------------Información de la materia---------------------------\n\n"
							 + "Nombre: %s\n"
							 + "Profesor(es): %s\n"
							 + "Semestre: %s\n"
							 + "Departamento: %s\n"
							 + "Código: %s\n"
							 + "Sección: %s\n\n"
							 + "---------------------------------Calificaciones--------------------------------\n\n"
							 + "Nota final sin aproximaciones ni bonos: \n"
							 + "Bonos:\n"
							 + "Política de aproximación:\n"
							 + "Nota final: %s\n"
							 + "----------------------------------Asignaciones---------------------------------\n"
							 + "[Nombre del trabajo: nota (ponderación)]\n\n%s",
							   titulo, nombre, profesores, semestre, departamento, codigo, seccion, notaFinal, 
							   trabajos);
			printWriter.close();
			
		} catch (IOException e) {
			System.out.println("Error: No se pudo escribir el TXT de la materia "+this.getFormatedName()+".");
			e.printStackTrace();
		}
	}
	
	
	public File locateFile() {
		File semesterPath = getSemester().locateDirectory();
		File path = new File(semesterPath.getAbsolutePath()+File.separator+this.getFormatedName()+".txt");
		return path;
	}
	
	
	
	public String getFormatedName() {
		String formatedName = department.getCode() + " " + code + ", " + String.valueOf(section) + ": " + name;
		return formatedName;
	}


	public String getName() {
		return name;
	}


	public int getCredits() {
		return credits;
	}


	public String getSection() {
		return section;
	}


	public String getCode() {
		return code;
	}


	public Department getDepartment() {
		return department;
	}



	public String[] getProfessors() {
		return professors;
	}


	public void addDiscussion(Discussion discussion) {
		this.discussions.add(discussion);
	}


	public Semester getSemester() {
		return semester;
	}


}

package model;

import java.util.ArrayList;


public class Lecture extends Course {

	private String name;
	private int credits;
	private String section;
	private String code;
	private Department department;
	private String[] professors;
	private Discussion discussion;
	private Discussion laboratory;

	
	public Lecture(String name, String departmentCode, String subjectCode, String section, int credits, String[] professors) {
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
	}
	

	public static Lecture readLectureFromLines(String[] lectureLine, String[] creditsLine, String[] professorsLine) {
		String s = lectureLine[1];
		int colonPosition = s.indexOf(":");
		int comaPosition = s.indexOf(",");
		String departmentCode = s.substring(0, 4);
		String courseCode = s.substring(5, 9);
		String section = s.substring(comaPosition+1, colonPosition).strip();
		String subjectName = s.substring(colonPosition+1).strip();
		
		int credits = Integer.valueOf(creditsLine[1]);
		
		String[] professors = new String[professorsLine.length-1];
		int i = 0;
		while (i < professors.length) {
			professors[i] = professorsLine[i+1];
			i++;
		}

		Lecture lecture = new Lecture(subjectName, departmentCode, courseCode, section, credits, professors);
		return lecture;
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


}

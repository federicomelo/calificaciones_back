package model;

import java.util.ArrayList;

import controler.GeneralInfo;

public class Subject implements GeneralInfo {

	private String name;
	private String nickname; 
	private int credits;
	private String section;
	private String code;
	private String motiveExtraPoints;
	private Department department;
	private double finalGrade;
	private String[] professors;
	private double extraPoints;
	private double completionPercentage;
	private GradeRoundingPolicy gradeRoundingPolicy = new GradeRoundingPolicy();
	private ArrayList<Assignment> assignments = new ArrayList<Assignment>();
	
	
	public static Subject createSubject(String[] subjectLine, String[] creditsLine, String[] professorsLine) {
		String s = subjectLine[1];
		int colonPosition = s.indexOf(":");
		int comaPosition = s.indexOf(",");
		String departmentCode = s.substring(0, 4);
		String subjectCode = s.substring(5, 9);
		String section = s.substring(comaPosition+1, colonPosition).strip();
		String subjectName = s.substring(colonPosition+1).strip();
		
		int credits = Integer.valueOf(creditsLine[1]);
		
		String[] professors = new String[professorsLine.length-1];
		int i = 0;
		while (i < professors.length) {
			professors[i] = professorsLine[i+1];
			i++;
		}

		Subject subject = new Subject(subjectName, departmentCode, subjectCode, section, credits, professors);
		return subject;
	}
	
	
	public void createAssignment(String[] currentLine) {
		if (currentLine.length >= 3) {
			String name = currentLine[0];
			double grade = Double.valueOf(currentLine[1]);
			double value = Double.valueOf(currentLine[2]);
			Assignment assignment = new Assignment(name, value, grade);
			addAssignment(assignment);
		}
	}
	
	
	public void giveExtraPoints(String[] currentLine) {
		this.extraPoints = Double.valueOf(currentLine[1]);
		motiveExtraPoints = currentLine[2].strip();
	}
	
	
	public void defineGradeRoundingPolicy(String[] currentLine) {
		this.gradeRoundingPolicy = new GradeRoundingPolicy(currentLine[1]);
	}
	

	public Subject(String name, String departmentCode, String subjectCode, String section, int credits, String[] professors) {
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
	
	
	public void addAssignment(Assignment assignment) {
		assignments.add(assignment);
		computeFinalGrade();
	}
	
	
	public String getFormatedName() {
		String formatedName = department.getCode() + " " + code + ", " + String.valueOf(section) + ": " + name;
		return formatedName;
	}

	
	public void computeFinalGrade() {
		double finalGrade = 0.;
		double completionPercentage = 0.;
		for (Assignment assignment: assignments) {
			finalGrade += GradeRoundingPolicy.roundToHundredth(assignment.getGrade())*assignment.getValue();
			completionPercentage += assignment.getValue();
		}
		finalGrade += this.extraPoints;
		this.finalGrade = gradeRoundingPolicy.round(finalGrade/completionPercentage);
		this.completionPercentage = completionPercentage;
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


	public double getFinalGrade() {
		computeFinalGrade();
		return finalGrade;
	}

	
	public double getCompletionPercentage() {
		computeFinalGrade();
		return completionPercentage;
	}


	public String[] getProfessors() {
		return professors;
	}
	
	
	public ArrayList<Assignment> getAssignments() {
		return assignments;
	}


	public String getMotiveExtraPoints() {
		return motiveExtraPoints;
	}
	

}

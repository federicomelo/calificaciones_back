package model;

public class Discussion extends Course {
	private String name;
	private String professor;
	private double value;
	
	
	public Discussion(String name, String professor, double value) {
		this.name = name;
		this.value = value;
		this.professor = professor;
	}
	

	public String getName() {
		return name;
	}


	public String getProfessor() {
		return professor;
	}


	public double getValue() {
		return value;
	}
}

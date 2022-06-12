package model;

public class Assignment {
	private String name;
	private double grade;
	private double value;


	public Assignment(String name, double value, double grade) {
		this.name = name;
		this.value = value;
		this.grade = grade;
	}


	public Assignment(String name, double value) {
		this.name = name;
		this.value = value;
	}


	public String getName() {
		return name;
	}


	public double getGrade() {
		return grade;
	}


	public void setGrade(double grade) {
		this.grade = grade;
	}


	public double getValue() {
		return value;
	}


	public void setValue(double value) {
		this.value = value;
	}


}

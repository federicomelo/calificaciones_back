package model;

public class Assignment {
	private String name;
	private double grade;
	private double value;
	private String comment;


	public Assignment(String name, double value, double grade) {
		this.name = name;
		this.value = value;
		this.grade = grade;
	}
	
	
	public Assignment(String name, String comment) {
		this.name = name;
		this.comment = comment;
		this.value = 0.;
		this.grade = 0.;
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


	public double getValue() {
		return value;
	}
	
	
	public String getComment() {
		return comment;
	}
	
	
	public String writeAssignment() {
		String trabajo;
		if (getGrade() > 0.) {
			trabajo = getName()+": "+String.valueOf(getGrade())+" ("+String.valueOf(getValue())+")\n";
		} else {
			trabajo = getName()+": "+getComment()+"\n";
		}
		return trabajo;
	}


}

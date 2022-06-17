package model;

import java.util.ArrayList;

public abstract class Course {
	
	protected double finalGrade;
	protected double completionPercentage;
	protected double extraPoints;
	protected String motiveExtraPoints;
	protected GradeRoundingPolicy gradeRoundingPolicy = new GradeRoundingPolicy();
	protected ArrayList<Assignment> assignments = new ArrayList<Assignment>();

	
	public void createAssignment(String[] currentLine) {
		if (currentLine.length >= 3) {
			String name = currentLine[0];
		    try {
		    	double grade = Double.valueOf(currentLine[1]);
		    	try {
		    		double value = Double.valueOf(currentLine[2]);
		    		Assignment assignment = new Assignment(name, value, grade);
					addAssignment(assignment);
		    	} catch (NumberFormatException nfe) {
		    		/* The percentage value of the assignment is given as a quotient. 
		    		It probably evaluates to a periodic decimal */
		    		try {
		    			double value = evaluateDivisionFromString(currentLine[2]);
		    			Assignment assignment = new Assignment(name, value, grade);
						addAssignment(assignment);
		    		} catch (Exception exc) {
		    			exc.printStackTrace();
		    		}
		    	}
		    } catch (NumberFormatException nfe) {
		        String comment = currentLine[1];
		        Assignment assignment = new Assignment(name, comment);
				addAssignment(assignment);
		    }
			
			
		}
	}
	
	
	private double evaluateDivisionFromString(String string) throws Exception {
		if (string.contains("/")) {
			int operator = string.indexOf("/");
			double operand1 = Double.valueOf(string.substring(0, operator).strip());
			double operand2 = Double.valueOf(string.substring(operator+1).strip());
			double answ = operand1 / operand2;
			return answ;
		} else {
			throw new Exception("The string inputed as arithmetic expression is not simple division and cannot be evaluated.");
		}
	}


	public void defineGradeRoundingPolicy(String[] currentLine) {
		this.gradeRoundingPolicy = new GradeRoundingPolicy(currentLine[1]);
	}
	
	
	protected void computeFinalGrade() {
		double finalGrade = 0.;
		double completionPercentage = 0.;
		for (Assignment assignment: assignments) {
			finalGrade += GradeRoundingPolicy.roundToHundredth(assignment.getGrade())*assignment.getValue();
			completionPercentage += assignment.getValue();
		}
		finalGrade += this.extraPoints;
		try {
			this.finalGrade = gradeRoundingPolicy.round(finalGrade/completionPercentage);
		} catch (Exception e) {
			e.printStackTrace();
		}
		this.completionPercentage = completionPercentage;
	}
	
	
	public double getFinalGrade() {
		computeFinalGrade();
		return finalGrade;
	}

	
	public double getCompletionPercentage() {
		computeFinalGrade();
		return completionPercentage;
	}
	
	
	public void giveExtraPoints(String[] currentLine) {
		motiveExtraPoints = currentLine[1].strip();
		this.extraPoints = Double.valueOf(currentLine[2]);
	}
	
	
	public ArrayList<Assignment> getAssignments() {
		return assignments;
	}


	public String getMotiveExtraPoints() {
		return motiveExtraPoints;
	}
	
	
	public void addAssignment(Assignment assignment) {
		this.assignments.add(assignment);
	}
	
	
}

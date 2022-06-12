package model;

public class GradeRoundingPolicy {

	private static final String ROUND_TO_POINT5 = "al .5";
	private static final String ROUND_TO_POINT25 = "al .25";
	private static final String ROUND_TO_TENTH = "al .1";
	private String name;
	
	public GradeRoundingPolicy() {
		// No rounding policy! Rounds to hundredth by default
	}
	
	
	public GradeRoundingPolicy(String name) {
		this.name = name;
	}
	
	
	public double round(double grade) {
		/* Rounds to hundredth by default, following the University's policies. */
		double roundedGrade = GradeRoundingPolicy.roundToHundredth(grade);  // 4.756 => 4.76;
		if (this.name != null) {
			if (name.equals(ROUND_TO_POINT5)) {
				roundedGrade = Math.round(grade);  // 4.756 => 5.00
			} else if (name.equals(ROUND_TO_POINT25)) {
				roundedGrade = Math.round(grade*2)/2;  // 4.30 => 4.50
			} else if (name.equals(ROUND_TO_TENTH)) {
				roundedGrade = Math.round(grade*10.)/10.;  // 4.656 => 4.70
			} 
		}
		return roundedGrade;
	}
	
	
	public static double roundToHundredth(double grade) {
		return Math.round(grade*100.)/100.;
	}
	
}

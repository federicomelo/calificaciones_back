package model;

public class GradeRoundingPolicy {

	private static final String ROUND_TO_POINT5 = "al .5";
	private static final String ROUND_TO_TENTH = "al .1";
	private String name;
	
	public GradeRoundingPolicy() {
		// No rounding policy! Rounds to hundredth by default
	}
	
	
	public GradeRoundingPolicy(String name) {
		this.name = name;
	}
	
	
	public double round(double grade) throws Exception {
		/* Rounds to hundredth by default, conforming to University's policies. */
		double roundedGrade = GradeRoundingPolicy.roundToHundredth(grade);  // 4.756 => 4.76;
		if (this.name != null) {
			if (name.equals(ROUND_TO_POINT5)) {
				roundedGrade = Math.round(grade*2.) / 2.;  // 4.58 => 4.50
			} else if (name.equals(ROUND_TO_TENTH)) {
				roundedGrade = Math.round(grade*10.)/10.;  // 4.656 => 4.70
			} else {
				throw new Exception("Rounding policy name "+name+" is not recognized");
			}
		}
		if (roundedGrade > 5) {
			roundedGrade = 5.;
		}
		return roundedGrade;
	}
	
	
	public static double roundToHundredth(double grade) {
		return Math.round(grade*100.)/100.;
	}
	
}

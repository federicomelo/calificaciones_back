package model;

public class GradeRoundingPolicy {

	private static final String ROUND_TO_POINT5 = "al .5";
	private static final String ROUND_TO_TENTH = "al .1";
	private String whichPolicy;
	private String name;
	
	public GradeRoundingPolicy() {
		// No rounding policy! round method rounds to hundredth by default.
		this.name = "La materia no cuenta con política de aproximación. Se aproxima a la centésima.";
	}
	
	
	public GradeRoundingPolicy(String name) {
		this.whichPolicy = name;
	}
	
	
	public double round(double grade) throws Exception {
		/* Rounds to hundredth by default, conforming to University's policies. */
		double roundedGrade = GradeRoundingPolicy.roundToHundredth(grade);  // 4.756 => 4.76;
		if (this.whichPolicy != null) {
			if (whichPolicy.equals(ROUND_TO_POINT5)) {
				roundedGrade = Math.round(grade*2.) / 2.;  // 4.58 => 4.50
				this.name = "Aproximación a la media unidad más cercana.";
			} else if (whichPolicy.equals(ROUND_TO_TENTH)) {
				roundedGrade = Math.round(grade*10.)/10.;  // 4.656 => 4.70
				this.name = "Aproximación al primer decimal.";
			} else {
				throw new Exception("Rounding policy "+whichPolicy+" is not recognized");
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


	public String getName() {
		return name;
	}
	
}

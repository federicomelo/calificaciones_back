package model;

import java.io.File;
import java.time.LocalDate;
import java.util.ArrayList;

public class Semester {
	private String yearAndPeriod;
	private String name;
	private String whichSemester;
	private int semesterCount;
	private LocalDate startingDate;
	private LocalDate endingDate;
	private int year;
	private int period;
	double average;
	int credits;
	private ArrayList<Lecture> lectures = new ArrayList<Lecture>();
	
	
	public Semester(int year, int period) {
		this.year = year;
		this.period = period;
		this.yearAndPeriod = String.valueOf(year)+"-"+String.valueOf(period);
		defineName(year, period);
	}

	
	public File locateDirectory() {
		File path = new File(System.getProperty("user.dir")+File.separator+"data"+File.separator+yearAndPeriod);
		return path;
	}
	
	
	private void computeAverage() {
		double average = 0.;
		int creditCount = 0;
		for (Lecture lecture: lectures) {
			creditCount += lecture.getCredits();
			average += lecture.getFinalGrade()*lecture.getCredits();
		}
		this.average = GradeRoundingPolicy.roundToHundredth(average / creditCount);
	}
	
	
	public static double computeGPA(ArrayList<Semester> semesters) {
		double gpa = 0;
		double creditCount = 0;
		for (Semester semester: semesters) {
			for (Lecture lecture: semester.getSubjects()) {
				creditCount += lecture.getCredits();
				gpa += (lecture.getFinalGrade()*lecture.getCredits());
			}
		}
		gpa = GradeRoundingPolicy.roundToHundredth(gpa/creditCount);
		return gpa;
	}
		
	
	public static double computeGPABySemester(ArrayList<Semester> semesters) {
		double gpa = 0;
		double avrg = 0.;
		double cred = 0.;
		for (Semester semester: semesters) {
			cred += semester.getCredits();
			avrg += semester.getAverage()*semester.getCredits();
		}
		gpa = GradeRoundingPolicy.roundToHundredth(avrg/cred);
		return gpa;
	}
	
	
	
	private void defineName(int year, int period) {
		int semesterShift = 0;
		if (period==20) {
			semesterShift = 1;
		}
		
		String name;
		try {
			name = darTipoDeSemestre(period)+" del año "+String.valueOf(year);
			this.name = name;
		} catch (Exception e1) {
			e1.printStackTrace();
		}

		/* The following formula assigns a number to a given semester based on its year.
		 * The formula numbers each semester in order since my first semester, 2020-20.
		 */
		this.semesterCount = (year - 2020)*2 + semesterShift;  
		try {
			this.whichSemester = obtenerOrdinal(semesterCount)+" semestre cursado";
		} catch (Exception e) {
			e.printStackTrace();
		}
	}
	
	
	private String darTipoDeSemestre(int period) throws Exception {
		String tipoSemestre;
		if (period == 10) {
			tipoSemestre = "Primer semestre";
		} else if (period == 20) {
			tipoSemestre = "Segundo semestre";
		} else if (period == 19) {
			tipoSemestre = "Periodo intersemestral";
		} else {  // Should never happen
			throw new Exception("No se conoce el tipo de semestre para el número dado.");
		}
		return tipoSemestre;
	}
	
	
	private String obtenerOrdinal(int i) throws Exception {
		String ordinal;
		if (i==1) {
			ordinal = "Primer";
		} else if (i==2) {
			ordinal = "Segundo";
		} else if (i==3) {
			ordinal = "Tercer";
		} else if (i==4) {
			ordinal = "Cuarto";
		} else if (i==5) {
			ordinal = "Quinto";
		} else if (i==6) {
			ordinal = "Sexto";
		} else if (i==7) {
			ordinal = "Séptimo";
		} else if (i==8) {
			ordinal = "Octavo";
		} else if (i==9) {
			ordinal = "Noveno";
		} else if (i==10) {
			ordinal = "Décimo";
		} else {  // Should never happen
			throw new Exception("No se conoce el ordinal para el número dado.");
		}
		return ordinal;
	}


	public void addSubject(Lecture lecture) {
		lectures.add(lecture);
		this.credits += lecture.getCredits();
	}
	
	
	
	public double getAverage() {
		computeAverage();
		return this.average;
	}
	
	
	public ArrayList<Lecture> getSubjects() {
		return this.lectures;
	}

	
	public String getName() {
		return this.name;
	}
	
	
	public String getWhichSemester() {
		return this.whichSemester;
	}
	
	public int getSemesterCount() {
		return this.semesterCount;
	}

	
	public int getCredits() {
		return credits;
	}
	

	public int getYear() {
		return year;
	}


	public int getPeriod() {
		return period;
	}


	public String getYearAndPeriod() {
		return yearAndPeriod;
	}
}

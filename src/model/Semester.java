package model;

import java.time.LocalDate;
import java.util.ArrayList;

public class Semester {
	
	String name;
	String whichSemester;
	int semesterCount;
	private LocalDate startingDate;
	private LocalDate endingDate;
	private int year;
	private int period;
	double average;
	private ArrayList<Lecture> lectures = new ArrayList<Lecture>();
	
	
	public Semester(int year, int period) {
		this.year = year;
		this.period = period;
		defineName(year, period);
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
			ordinal = "Tercero";
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


	public int getYear() {
		return year;
	}


	public int getPeriod() {
		return period;
	}
}

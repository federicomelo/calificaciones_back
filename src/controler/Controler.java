package controler;

import java.io.File;
import java.util.ArrayList;

import model.Semester;
import model.Lecture;

public class Controler implements GeneralInfo {
	
	private ArrayList<Semester> semesters = new ArrayList<Semester>();


	public static void main(String[] args) {
		Controler controler = new Controler();
		String[] ss = {"2020-20", "2022-10"};
		for (String s: ss) {
			controler.
			readSemester(s);
		}
		controler.printRecord();
	}
	
	
	private void readSemester(String sSemester) {
		int year = Integer.valueOf(sSemester.substring(0,4));
		int period = Integer.valueOf(sSemester.substring(5));
		Semester semester = new Semester(year, period);
		
		ArrayList<String[]> semesterFile = GradesReader.readTSV(APP+File.separator+"data"+File.separator+sSemester+File.separator+sSemester+".tsv");
		readSemesterFile(semester, semesterFile);
	}
	

	private void readSemesterFile(Semester semester, ArrayList<String[]> semesterFile) {
		String[] subjectLine = null;
		String[] creditsLine = null;
		String[] professorsLine = null;
		Lecture lecture = null;
		
		int i = 0;
		while (i < semesterFile.size()) {
			String[] line = semesterFile.get(i);
			
			/* Checks if everything that is needed to declare an instance of Subject is ready.
			 * If so, the instance is declared*/
			if ((subjectLine != null) && (creditsLine != null) && (professorsLine != null)) {
				lecture = Lecture.readLectureFromLines(subjectLine, creditsLine, professorsLine);
				semester.addSubject(lecture);
				subjectLine = null;
				creditsLine = null;
				professorsLine = null;
			}
			
			/* Checks if the line that is about to be read corresponds to a Subject,
			 * the number of credits, the professors, or an assignment */
			if (line.length > 0) {
				if (line[0].equals(SUBJECT)) {
					subjectLine = line;
				} else if (line[0].equals(CREDITS)) {
					creditsLine = line;
				} else if (line[0].equals(PROFESSOR)) {
					professorsLine = line;
				} else if (line[0].equals(EXTRA_POINTS)) {
					lecture.giveExtraPoints(line);
				} else if (line[0].equals(GRADE_ROUNDING_POLICY)) {
					lecture.defineGradeRoundingPolicy(line);
				} else {
					lecture.createAssignment(line);
				}
			}
			
			i++;	
		}
		
		this.semesters.add(semester);
	}


	public void printRecord() {
		for (Semester semester: semesters) {
			System.out.println(semester.getWhichSemester());
			for (Lecture lecture: semester.getSubjects()) {
				System.out.println(lecture.getFormatedName());
				System.out.println(lecture.getFinalGrade());
			}
			System.out.println(semester.getAverage());
		}
	}
	
}





package controler;

import java.io.File;
import java.util.ArrayList;

import model.Semester;
import model.Assignment;
import model.Discussion;
import model.Lecture;

public class Controler implements GeneralInfo {
	
	private ArrayList<Semester> semesters = new ArrayList<Semester>();


	public static void main(String[] args) {
		Controler controler = new Controler();
		String[] ss = {"2020-20", "2021-20", "2021-10", "2022-10"};
		for (String s: ss) {
			controler.
			readSemester(s);
			controler.write();
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
		ArrayList<String> discussions = new ArrayList<String>();
		
		int i = 0;
		while (i < semesterFile.size()) {
			String[] line = semesterFile.get(i);

			if (!lineIsEmpty(line)) {

				if (Lecture.lineIsLecture(line)) {
					/* If the line corresponds to the name of a lecture, the two lines below
					 * correspond two its number of credits and its professors, in that order.
					 * That suffices to declare an instance of the Lecture class.
					 */
					subjectLine = line;
					creditsLine = semesterFile.get(i+1);
					professorsLine = semesterFile.get(i+2);
					lecture = Lecture.readLectureFromLines(subjectLine, creditsLine, professorsLine, semester);
					
					/* Below the lecture's information are the assignments, and possibly lines with information
					 * regarding the subject's grade rounding policy or extra points obtained in it.
					 * There may also be information regarding discussion classes associated to the lecture.
					 */
					
					i = i+3;
					line = semesterFile.get(i);
					while(!lineIsEmpty(line) && i< semesterFile.size()-1) {  // < size-1 because at the end i is incremented before a get operation
						if (line[0].equals(GRADE_ROUNDING_POLICY)) {
							lecture.defineGradeRoundingPolicy(line);
						} else if (line[0].equals(EXTRA_POINTS)) {
							lecture.giveExtraPoints(line);
						} else if (line[0].equals(DISCUSSION)) {
							discussions.add(line[1]);
						} else if (line.length>=2){
							lecture.createAssignment(line);
						}
						i++;
						line = semesterFile.get(i);
					}
					
					/* By this point, the instance of Lecture has been declared and all the information that 
					 * pertains it has been read and added. The Lecture is added to the semester.
					 */
					semester.addSubject(lecture);
				} 
			}
			i++;
		}
		
		this.semesters.add(semester);
	}

	
	private boolean lineIsEmpty(String[] line) {
		boolean isEmpty = true;
		if (line != null) {
			if (line.length > 0) {
				for (String element: line) {
					if (!element.strip().equals("")) {
						isEmpty = false;
					}
				}
			}
		}
		return isEmpty;
	}
	

	public void printRecord() {
		for (Semester semester: semesters) {
			System.out.println(semester.getWhichSemester());
			for (Lecture lecture: semester.getSubjects()) {
				if (semester.getSemesterCount()==3) {
					System.out.println(lecture.getFormatedName());
					System.out.println(lecture.getFinalGrade());
				}
			}
			System.out.println(semester.getAverage());
		}
		
		
		System.out.println("\n\n");
		System.out.println(Semester.computeGPA(semesters));
		System.out.println(Semester.computeGPABySemester(semesters));
	}
	


	public void write() {
		for (Semester semester: semesters) {
			File fSemester = new File(APP+File.separator+"data"+File.separator+semester.getYearAndPeriod());
			for (Lecture lecture: semester.getSubjects()) {
				lecture.writeTXT();
			}
		}
	
	}
}





package controler;

import java.io.File;
import java.time.format.DateTimeFormatter;
import java.time.format.DateTimeFormatterBuilder;
import java.util.Locale;

public interface GeneralInfo {

	public static final File APP = new File(System.getProperty("user.dir"));	
	public static final DateTimeFormatter FORMATO_FECHA = new DateTimeFormatterBuilder().parseCaseInsensitive().appendPattern("EEEE d MMMM uuuu HH:mm:ss").toFormatter(new Locale("es", "ES")); 
	public static final File DATA = new File(APP.getAbsolutePath()+File.separator+"data");
	public static final String SUBJECT = "SUBJECT";
	public static final String CREDITS = "CREDITS";
	public static final String PROFESSOR = "PROFESSOR";
	public static final String EXTRA_POINTS = "EXTRA";
	public static final String GRADE_ROUNDING_POLICY = "ROUND";
}


package edu.ucalgary.oop;

import java.time.LocalDate;
import java.time.format.DateTimeFormatter;

public interface DateValidator {
    boolean invalidDate(String date);
}

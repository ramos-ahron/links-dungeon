package edu.ucalgary.oop;

import java.time.LocalDate;
import java.time.format.DateTimeFormatter;

public class DateValidator {
    /**
     * Checks if the provided date string has an invalid format.
     *
     * @param date the date string to check
     * @return true if the date string has an invalid format, otherwise false
     */
    public boolean invalidDateFormat(String date) {
        try {
            LocalDate.parse(date, DateTimeFormatter.ISO_DATE);
            return false;
        } catch (Exception e) {
            return true;
        }
    }
}

package edu.ucalgary.oop;

import java.time.LocalDate;
import java.time.format.DateTimeFormatter;
import java.time.format.DateTimeParseException;

public class Inquiry implements DateValidator {
    private String date;
    private String info;

    /**
     * Constructs a new Inquiry object with the provided date and information.
     *
     * @param date the date of the inquiry
     * @param info additional information provided in the inquiry
     * @throws IllegalArgumentException if the provided date is invalid
     */
    public Inquiry(String date, String info) {
        if (invalidDate(date)) {
            throw new IllegalArgumentException("Invalid entry date");
        }
        this.date = date;
        this.info = info;
    }


    /**
     * Constructs a new Inquiry object with the current date and the provided information.
     *
     * @param info additional information provided in the inquiry
     */
    public Inquiry(String info) {
        this.date = LocalDate.now().toString();
        this.info = info;
    }


    /**
     * Checks if the provided date string has a valid format and represents a date before or equal to the current date.
     *
     * @param dateToCheck the date string to check, formatted as "YYYY-MM-DD"
     * @return true if the date string has a valid format and represents a date before or equal to the current date, otherwise false
     */
    @Override
    public boolean invalidDate(String dateToCheck) {
        DateTimeFormatter formatter = DateTimeFormatter.ISO_DATE;
        try {
            LocalDate date = LocalDate.parse(dateToCheck, formatter);
            LocalDate currentDate = LocalDate.now();

            LocalDate minValidDate = currentDate.minusYears(150);
            return date.isBefore(minValidDate) || date.isAfter(currentDate);
        } catch (DateTimeParseException e) {
            return true;
        }
    }

    /**
     * Retrieves the date associated with this inquiry.
     *
     * @return the date of the inquiry
     */
    public String getDate() {
        return date;
    }


    /**
     * Retrieves additional information associated with this inquiry.
     *
     * @return the additional information provided with the inquiry
     */
    public String getInfo() {
        return info;
    }


    /**
     * Sets the additional information associated with this inquiry.
     *
     * @param info the additional information to be set
     */
    public void setInfo(String info) {
        this.info = info;
    }
}

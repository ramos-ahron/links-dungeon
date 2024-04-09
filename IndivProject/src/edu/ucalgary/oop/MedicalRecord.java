package edu.ucalgary.oop;

import java.time.LocalDate;
import java.time.format.DateTimeFormatter;

public class MedicalRecord implements DateValidator {
    private Location location;
    private String treatmentDetails;
    private String dateOfTreatment;


    /**
     * Constructs a medical record with the specified location.
     *
     * @param location the location where the treatment took place
     */
    public MedicalRecord(Location location) {
        this.location = location;
    }


    /**
     * Constructs a MedicalRecord object with the specified location, treatment details, and date of treatment.
     *
     * @param location         the location where the treatment took place
     * @param dateOfTreatment  the date of the treatment in the format "YYYY-MM-DD"
     * @throws IllegalArgumentException if the provided date of treatment is not in the format "YYYY-MM-DD"
     */
    public MedicalRecord(Location location, String dateOfTreatment) throws IllegalArgumentException {
        this.location = location;

        if (invalidDate(dateOfTreatment)) {
            throw new IllegalArgumentException("Invalid date format for date of treatment. Expected format: YYYY-MM-DD");
        }

        this.dateOfTreatment = dateOfTreatment;
    }


    /**
     * Constructs a MedicalRecord object with the specified location, treatment details, and date of treatment.
     *
     * @param location         the location where the treatment took place
     * @param treatmentDetails the details of the treatment
     * @param dateOfTreatment  the date of the treatment in the format "YYYY-MM-DD"
     * @throws IllegalArgumentException if the provided date of treatment is not in the format "YYYY-MM-DD"
     */
    public MedicalRecord(Location location, String treatmentDetails, String dateOfTreatment) throws IllegalArgumentException {
        this.location = location;
        this.treatmentDetails = treatmentDetails;

        if (invalidDate(dateOfTreatment)) {
            throw new IllegalArgumentException("Invalid date format for date of treatment. Expected format: YYYY-MM-DD");
        }

        this.dateOfTreatment = dateOfTreatment;
    }


    /**
     * Gets the location associated with this medical record.
     *
     * @return the location where the medical treatment took place
     */
    public Location getLocation() {
        return location;
    }


    /**
     * Sets the location associated with this medical record.
     *
     * @param location the location where the medical treatment took place
     */
    public void setLocation(Location location) {
        this.location = location;
    }


    /**
     * Gets the details of the treatment associated with this medical record.
     *
     * @return the treatment details
     */
    public String getTreatmentDetails() {
        return treatmentDetails;
    }


    /**
     * Sets the details of the treatment associated with this medical record.
     *
     * @param treatmentDetails the treatment details to set
     */
    public void setTreatmentDetails(String treatmentDetails) {
        this.treatmentDetails = treatmentDetails;
    }


    /**
     * Gets the date of the treatment associated with this medical record.
     *
     * @return the date of the treatment
     */
    public String getDateOfTreatment() {
        return dateOfTreatment;
    }


    /**
     * Sets the date of the treatment associated with this medical record.
     *
     * @param dateOfTreatment the date of the treatment to set, formatted as "YYYY-MM-DD"
     * @throws IllegalArgumentException if the provided date format is invalid
     */
    public void setDateOfTreatment(String dateOfTreatment) throws IllegalArgumentException {
        if (invalidDate(dateOfTreatment)) {
            throw new IllegalArgumentException("Invalid date format. Expected format: YYYY-MM-DD");
        }
        this.dateOfTreatment = dateOfTreatment;
    }

    /**
     * Checks if the provided date string has an invalid format.
     *
     * @param date the date string to check
     * @return true if the date string has an invalid format, otherwise false
     */
    @Override
    public boolean invalidDate(String date) {
        try {
            LocalDate.parse(date, DateTimeFormatter.ISO_DATE);
            return false;
        } catch (Exception e) {
            return true;
        }
    }
}
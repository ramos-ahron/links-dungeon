package edu.ucalgary.oop;

import java.time.LocalDate;
import java.time.format.DateTimeFormatter;
import java.time.format.DateTimeParseException;
import java.time.LocalDate;
import java.time.format.DateTimeFormatter;

public class Inquirer extends Person implements DateValidator {
    private String phoneNumber;
    private String info;
    private String date;
    private InquirerLog inquiries = new InquirerLog();

    /**
     * Constructs an Inquirer object with the specified first name, last name, phone number, and additional information.
     *
     * @param firstName   the first name of the inquirer
     * @param lastName    the last name of the inquirer
     * @param phoneNumber the phone number of the inquirer
     * @param info        additional information about the inquirer
     * @throws IllegalArgumentException if the provided phone number is not in the format "000-000-0000"
     */
    public Inquirer(String firstName, String lastName, String phoneNumber, String info) throws IllegalArgumentException {
        super(firstName, lastName);
        if (invalidPhoneNumber(phoneNumber)) {
            throw new IllegalArgumentException("Invalid Phone Number");
        }
        this.phoneNumber = phoneNumber;
        this.info = info;
        this.date = LocalDate.now().toString();
        inquiries.addInquirer(new Inquiry(date, info));
    }

    /**
     * Constructs a new Inquirer object with the provided information.
     *
     * @param firstName the first name of the inquirer
     * @param lastName the last name of the inquirer
     * @param phoneNumber the phone number of the inquirer
     * @param date the date of the inquiry
     * @param info additional information provided by the inquirer
     * @throws IllegalArgumentException if the provided phone number or date is invalid
     */
    public Inquirer(String firstName, String lastName, String phoneNumber, String date, String info) {
        super(firstName, lastName);
        if (invalidPhoneNumber(phoneNumber)) {
            throw new IllegalArgumentException("Invalid Phone Number");
        }
        this.phoneNumber = phoneNumber;
        if (invalidDate(date)) {
            throw new IllegalArgumentException("Invalid entry date");
        }
        this.date = date;
    }


        /**
         * Constructs an Inquirer object with the specified first name, last name, and phone number.
         *
         * @param firstName   the first name of the inquirer
         * @param lastName    the last name of the inquirer
         * @param phoneNumber the phone number of the inquirer
         * @throws IllegalArgumentException if the provided phone number is not in the format "000-000-0000"
         */
    public Inquirer(String firstName, String lastName, String phoneNumber) throws IllegalArgumentException {
        // Call the appropriate superclass constructor based on whether lastName is provided
        super(lastName == null || lastName.isEmpty() ? firstName : firstName, lastName);

        // Check the validity of the phone number
        if (invalidPhoneNumber(phoneNumber)) {
            throw new IllegalArgumentException("Invalid Phone Number");
        }

        // Initialize the remaining instance variables
        this.phoneNumber = phoneNumber;
        this.date = LocalDate.now().toString();

        // Assuming `inquiries` is an instance of `InquirerLog`, you should call `addInquirer` on it
        inquiries.addInquirer(new Inquiry(date, info));
    }

    public void addInquiry(String date, String info) {
        if (invalidDate(date)) {
            throw new IllegalArgumentException("Invalid entry date");
        }

        for (Inquiry inquiry : getInquiries().getInquirerList()) {
            if (inquiry.getDate().equals(date) && inquiry.getInfo().equals(info)) {
                throw new IllegalArgumentException("Inquiry already exists");
            }
        }

        getInquiries().addInquirer(new Inquiry(date, info));
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

    public InquirerLog getInquiries() {
        return inquiries;
    }

    public void setInquiries(InquirerLog inquiries) {
        this.inquiries = inquiries;
    }

    /**
     * Retrieves the phone number associated with the services.
     *
     * @return the phone number associated with the services
     */
    public String getPhoneNumber() {
        return phoneNumber;
    }


    /**
     * Sets the phone number of the inquirer.
     *
     * @param phoneNumber the phone number to set for the inquirer
     */
    public void setPhoneNumber(String phoneNumber) throws IllegalArgumentException {
        if (invalidPhoneNumber(phoneNumber)) {
            throw new IllegalArgumentException("Invalid Phone Number");
        }
        this.phoneNumber = phoneNumber;
    }


    /**
     * Retrieves additional information about the inquirer.
     *
     * @return the additional information about the inquirer
     */
    public String getInfo() {
        return info;
    }


    /**
     * Sets additional information about the inquirer.
     *
     * @param info additional information to set about the inquirer
     */
    public void setInfo(String info) {
        this.info = info;
    }

    /**
     * Checks if the provided phone number is in the format "000-000-0000".
     *
     * @param number the phone number to validate
     * @return true if the phone number is in the correct format, false otherwise
     */
    private boolean invalidPhoneNumber(String number) {
        if (number.length() != 12 || number.charAt(3) != '-' || number.charAt(7) != '-') {
            return true;
        }
        for (int i = 0; i < number.length(); i++) {
            if (i != 3 && i != 7 && !Character.isDigit(number.charAt(i))) {
                return true;
            }
        }
        return false;
    }
}



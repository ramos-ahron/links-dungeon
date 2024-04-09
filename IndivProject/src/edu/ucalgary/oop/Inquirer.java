package edu.ucalgary.oop;

public class Inquirer extends Person {
    private String phoneNumber;
    private String info;

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
        super(firstName, lastName);
        if (invalidPhoneNumber(phoneNumber)) {
            throw new IllegalArgumentException("Invalid Phone Number");
        }
        this.phoneNumber = phoneNumber;
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
    public void setPhoneNumber(String phoneNumber) {
        this.phoneNumber = phoneNumber;
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
     * Retrieves additional information.
     *
     * @return the additional information
     */
    public String getInfo() {
        return info;
    }

    /**
     * Checks if the provided phone number is in the format "000-000-0000".
     *
     * @param number the phone number to validate
     * @return true if the phone number is in the correct format, false otherwise
     */
    private boolean invalidPhoneNumber(String number) {
        // Check if the length is 12 characters and if the hyphens are at the correct positions
        if (number.length() != 12 || number.charAt(3) != '-' || number.charAt(7) != '-') {
            return true;
        }

        // Check if all characters before and after the hyphens are digits
        for (int i = 0; i < number.length(); i++) {
            if (i != 3 && i != 7 && !Character.isDigit(number.charAt(i))) {
                return true;
            }
        }

        // If all conditions are met, the number is considered valid
        return false;
    }
}



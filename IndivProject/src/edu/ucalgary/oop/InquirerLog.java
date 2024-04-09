package edu.ucalgary.oop;

import java.util.HashSet;

public class InquirerLog {
    private static final HashSet<Inquirer> inquirerList = new HashSet<>();

    /**
     * Adds an Inquirer object to the list of inquirers.
     *
     * @param inquirer the Inquirer object to be added
     * @throws IllegalArgumentException if the provided Inquirer object is null or if an Inquirer with the same first name, last name, and phone number already exists in the list
     */
    public static void addInquirer(Inquirer inquirer) throws IllegalArgumentException {
        if (inquirer == null) {
            throw new IllegalArgumentException("Inquirer object cannot be null");
        }

        for (Inquirer existingInquirer : inquirerList) {
            if (existingInquirer.getFirstName().equals(inquirer.getFirstName()) &&
                    existingInquirer.getLastName().equals(inquirer.getLastName()) &&
                    existingInquirer.getPhoneNumber().equals(inquirer.getPhoneNumber())) {
                throw new IllegalArgumentException("Inquirer already exists in the list");
            }
        }

        inquirerList.add(inquirer);
    }

    /**
     * Removes an Inquirer object from the list of inquirers.
     *
     * @param inquirer the Inquirer object to be removed
     * @throws IllegalArgumentException if the provided Inquirer object is null or if no Inquirer with the same first name, last name, and phone number exists in the list
     */
    public static void removeInquirer(Inquirer inquirer) {
        if (inquirer == null) {
            throw new IllegalArgumentException("Inquirer object cannot be null");
        }

        boolean removed = false;
        for (Inquirer existingInquirer : inquirerList) {
            if (existingInquirer.getFirstName().equals(inquirer.getFirstName()) &&
                    existingInquirer.getLastName().equals(inquirer.getLastName()) &&
                    existingInquirer.getPhoneNumber().equals(inquirer.getPhoneNumber())) {
                inquirerList.remove(existingInquirer);
                removed = true;
                break;
            }
        }

        if (!removed) {
            throw new IllegalArgumentException("Inquirer is not in the list");
        }
    }

    /**
     * Retrieves the HashSet containing the list of inquirers.
     *
     * @return the HashSet containing the list of inquirers
     */
    public static HashSet<Inquirer> getInquirerList() {
        return inquirerList;
    }

    /**
     * Sets the list of inquirers to a new HashSet of Inquirer objects.
     *
     * @param newList the new HashSet of Inquirer objects to set as the list of inquirers
     * @throws IllegalArgumentException if the provided HashSet of Inquirer objects is null
     */
    public static void setInquirerList(HashSet<Inquirer> newList) {
        inquirerList.clear();
        inquirerList.addAll(newList);
    }
}

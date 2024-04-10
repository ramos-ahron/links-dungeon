package edu.ucalgary.oop;

import java.util.HashSet;
import java.util.Objects;

public class InquirerLog {
    private final HashSet<Inquiry> inquirerList = new HashSet<>();

    /**
     * Adds an Inquirer object to the list of inquirers.
     *
     * @param inquiry the inquiry object to be added
     * @throws IllegalArgumentException if the provided Inquirer object is null or if an Inquirer with the same first name, last name, and phone number already exists in the list
     */
    public void addInquirer(Inquiry inquiry) throws IllegalArgumentException {
        if (inquiry == null) {
            throw new IllegalArgumentException("Inquiry object cannot be null");
        }

        for (Inquiry existingInquiry : inquirerList) {
            if (Objects.equals(existingInquiry.getDate(), inquiry.getDate()) && Objects.equals(existingInquiry.getInfo(), inquiry.getInfo())) {
                throw new IllegalArgumentException("Inquirer already exists in the list");
            }
        }

        inquirerList.add(inquiry);
    }

    /**
     * Removes an Inquirer object from the list of inquirers.
     *
     * @param inquiry the Inquiry object to be removed
     * @throws IllegalArgumentException if the provided Inquirer object is null or if no Inquirer with the same first name, last name, and phone number exists in the list
     */
    public void removeInquirer(Inquiry inquiry) {
        if (inquiry == null) {
            throw new IllegalArgumentException("Inquirer object cannot be null");
        }

        boolean removed = false;
        for (Inquiry existingInquiry : inquirerList) {
            if (existingInquiry.getDate().equals(inquiry.getDate()) &&
                    existingInquiry.getInfo().equals(inquiry.getInfo())) {
                inquirerList.remove(existingInquiry);
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
    public HashSet<Inquiry> getInquirerList() {
        return inquirerList;
    }

    /**
     * Sets the list of inquirers to a new HashSet of Inquirer objects.
     *
     * @param newList the new HashSet of Inquirer objects to set as the list of inquirers
     * @throws IllegalArgumentException if the provided HashSet of Inquirer objects is null
     */
    public void setInquirerList(HashSet<Inquiry> newList) {
        inquirerList.clear();
        inquirerList.addAll(newList);
    }
}

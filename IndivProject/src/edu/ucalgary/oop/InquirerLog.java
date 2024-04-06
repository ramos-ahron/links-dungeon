package edu.ucalgary.oop;

import java.util.HashSet;

public class InquirerLog {
    private HashSet<Inquirer> inquirerList;

    public InquirerLog() {
        this.inquirerList = new HashSet<>();
    }

    public void setInquirerList(HashSet<Inquirer> inquirerList) {
        this.inquirerList = inquirerList;
    }

    public HashSet<Inquirer> getInquirerList() {
        return inquirerList;
    }

    public void addInquirer(Inquirer inquirer) {
        inquirerList.add(inquirer);
    }

    public void removeInquirer(Inquirer inquirer) {
        inquirerList.remove(inquirer);
    }

    public boolean searchInquirerList(Inquirer inquirer) {
        return inquirerList.contains(inquirer);
    }

    public void createInquirer() {
        // Logic to create a new Inquirer object and add it to the list
    }
}

package edu.ucalgary.oop;

import java.util.HashSet;
import java.util.ArrayList;

public class DisasterVictim extends Person {
    private static int counter = 0;
    private String dateOfBirth;
    private int ASSIGNED_SOCIAL_ID;
    private HashSet<FamilyRelation> familyConnections;
    private ArrayList<MedicalRecord> medicalRecords = new ArrayList<>();
    private ArrayList<Supply> personalBelongings = new ArrayList<>();
    private String ENTRY_DATE;
    private String gender;
    private GenderOption genderChecker;
    private String comments;
    private Location location;

    public DisasterVictim(String firstName, String lastName, String ENTRY_DATE) {
        super(firstName, lastName);
        this.ENTRY_DATE = ENTRY_DATE;
        this.ASSIGNED_SOCIAL_ID = counter ++;
    }

    public static int generateSocialID() {
        // Implementation of generateSocialID method
        return 0; // Placeholder return value
    }

    public static boolean isValidDateFormat(String date) {
        // Implementation of isValidDateFormat method
        return false; // Placeholder return value
    }

    public void addPersonalBelonging(Supply supply) {
        personalBelongings.add(supply);
    }

    public void removePersonalBelonging(Supply unwantedSupply) {
        // Implementation to remove personal belongings
    }

    public void addFamilyConnection(FamilyRelation record) {
        // Implementation to add family connections
    }

    public void removeFamilyConnection(FamilyRelation exRelation) {
        // Implementation to remove family connections
    }

    public void addMedicalRecord(MedicalRecord record) {
        // Implementation to add medical records
        medicalRecords.add(record);
    }

    // Other methods as per your requirements

    // Getter and setter methods for the additional fields

    public int getCounter() {
        return counter;
    }

    public void setCounter(int counter) {
        this.counter = counter;
    }

    public String getDateOfBirth() {
        return dateOfBirth;
    }

    public void setDateOfBirth(String dateOfBirth) {
        this.dateOfBirth = dateOfBirth;
    }

    public int getAssignedSocialID() {
        return ASSIGNED_SOCIAL_ID;
    }

    public void setASSIGNED_SOCIAL_ID(int ASSIGNED_SOCIAL_ID) {
        this.ASSIGNED_SOCIAL_ID = ASSIGNED_SOCIAL_ID;
    }

    public HashSet<FamilyRelation> getFamilyConnections() {
        return familyConnections;
    }

    public void setFamilyConnections(HashSet<FamilyRelation> familyConnections) {
        this.familyConnections = familyConnections;
    }

    public ArrayList<MedicalRecord> getMedicalRecords() {
        return medicalRecords;
    }

    public void setMedicalRecords(ArrayList<MedicalRecord> medicalRecords) {
        this.medicalRecords = medicalRecords;
    }

    public ArrayList<Supply> getPersonalBelongings() {
        return personalBelongings;
    }

    public void setPersonalBelongings(ArrayList<Supply> personalBelongings) {
        this.personalBelongings = personalBelongings;
    }

    public String getENTRY_DATE() {
        return ENTRY_DATE;
    }

    public void setENTRY_DATE(String ENTRY_DATE) {
        this.ENTRY_DATE = ENTRY_DATE;
    }

    public String getGender() {
        return gender;
    }

    public void setGender(String gender) {
        this.gender = gender;
    }

    public GenderOption getGenderChecker() {
        return genderChecker;
    }

    public Location getLocation() {
        return location;
    }

    public void setLocation(Location location) {
        this.location = location;
    }

    public void setGenderChecker(GenderOption genderChecker) {
        this.genderChecker = genderChecker;
    }

    public String getComments() {
        return comments;
    }

    public void setComments(String comments) {
        this.comments = comments;
    }

    public String getEntryDate() {return this.ENTRY_DATE;}



}

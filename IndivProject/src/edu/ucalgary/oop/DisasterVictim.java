package edu.ucalgary.oop;

import java.io.IOException;
import java.time.DateTimeException;
import java.time.LocalDate;
import java.time.Period;
import java.time.format.DateTimeFormatter;
import java.util.ArrayList;
import java.util.HashSet;

public class DisasterVictim extends Person {
    private static int counter = 0;
    private final int ASSIGNED_SOCIAL_ID;
    private final String ENTRY_DATE;
    private final HashSet<FamilyRelation> familyConnections = new HashSet<>();
    private final ArrayList<MedicalRecord> medicalRecords = new ArrayList<>();
    private final ArrayList<Supply> personalBelongings = new ArrayList<>();
    private int age;
    private String gender;
    private String comments;
    private String dateOfBirth;
    private Location location;


    /**
     * Constructs a DisasterVictim object with the specified first name, last name, and entry date.
     *
     * @param firstName  the first name of the disaster victim
     * @param lastName   the last name of the disaster victim
     * @param ENTRY_DATE the entry date of the disaster victim in the format "YYYY-MM-DD"
     * @throws IllegalArgumentException if the provided entry date is invalid
     */
    public DisasterVictim(String firstName, String lastName, String ENTRY_DATE) throws IllegalArgumentException {
        super(firstName, lastName);
        if (!validDate(ENTRY_DATE)) {
            throw new IllegalArgumentException("Invalid entry date");
        }
        this.ENTRY_DATE = ENTRY_DATE;
        this.ASSIGNED_SOCIAL_ID = counter++;
    }


    /**
     * Constructs a DisasterVictim object with the specified first name and last name.
     * The entry date is set to the current date.
     *
     * @param firstName the first name of the disaster victim
     * @param lastName  the last name of the disaster victim
     */
    public DisasterVictim(String firstName, String lastName) {
        super(firstName, lastName);
        this.ENTRY_DATE = LocalDate.now().toString();
        this.ASSIGNED_SOCIAL_ID = counter++;
    }


    /**
     * Constructs a DisasterVictim object with the specified first name and entry date.
     *
     * @param firstName  the first name of the disaster victim
     * @param ENTRY_DATE the entry date of the disaster victim
     * @throws IllegalArgumentException if the provided entry date is invalid
     */
    public DisasterVictim(String firstName, LocalDate ENTRY_DATE) {
        super(firstName);
        if (!validDate(ENTRY_DATE)) {
            throw new IllegalArgumentException("Invalid entry date");
        }
        this.ENTRY_DATE = ENTRY_DATE.toString();
        this.ASSIGNED_SOCIAL_ID = counter++;
    }


    /**
     * Constructs a DisasterVictim object with the specified first name.
     * The entry date is set to the current date.
     *
     * @param firstName the first name of the disaster victim
     */
    public DisasterVictim(String firstName) {
        super(firstName);
        this.ENTRY_DATE = LocalDate.now().toString();
        this.ASSIGNED_SOCIAL_ID = counter++;
    }


    public static void main(String[] args) {
        DisasterVictim test = new DisasterVictim("a", "b", "2020-02-30");

        test.addPersonalBelonging(new Supply("water", 2));
        test.removePersonalBelonging(new Supply("water", 2));

        System.out.println(test.personalBelongings.get(0).getQuantity());
    }


    /**
     * Adds a Supply object to the personal belongings list.
     * If a Supply object with the same type already exists in the list, its quantity is increased.
     *
     * @param supply the Supply object to add to the personal belongings list
     */
    public void addPersonalBelonging(Supply supply) {
        Supply supplyToAdd = inPersonalBelonging(supply);

        if (supplyToAdd != null) {
            supplyToAdd.add(supply.getQuantity());
        } else {
            personalBelongings.add(supply);
        }
    }


    /**
     * Removes a specified quantity of a Supply object from the personal belongings list.
     * If the Supply object is found in the list, its quantity is reduced by the specified quantity.
     * If the quantity becomes 0 after removal, the Supply object is removed from the list.
     *
     * @param supply the Supply object to remove from the personal belongings list
     * @throws IllegalArgumentException if the specified supply is not found in the personal belongings list
     */
    public void removePersonalBelonging(Supply supply) throws IllegalArgumentException {
        Supply supplyToRemove = inPersonalBelonging(supply);

        if (supplyToRemove != null) {
            supplyToRemove.add(-(supply.getQuantity()));
            refreshSupplies(personalBelongings);
        } else {
            throw new IllegalArgumentException("Supply is not in personal belongings");
        }
    }


    /**
     * Adds a family relationship between this DisasterVictim and another DisasterVictim.
     *
     * @param victim2      the other DisasterVictim involved in the relationship
     * @param relationType the type of relationship to add
     * @throws IllegalArgumentException if a relationship of the specified type already exists between the two victims
     */
    public void addFamilyRelationship(DisasterVictim victim2, RelationshipType relationType) throws IllegalArgumentException {
        for (FamilyRelation existingRelation : this.familyConnections) {
            if (existingRelation.getPersonTwo().equals(victim2) && existingRelation.getRelationshipType() == relationType) {
                throw new IllegalArgumentException("Relationship already exists");
            }
        }

        // Create a new FamilyRelation object for both victims
        FamilyRelation relation1 = new FamilyRelation(this, victim2, relationType);
        FamilyRelation relation2 = new FamilyRelation(victim2, this, relationType);

        this.familyConnections.add(relation1);
        victim2.familyConnections.add(relation2);
    }


    /**
     * Removes a family relationship between this DisasterVictim and another DisasterVictim.
     *
     * @param victim2      the other DisasterVictim involved in the relationship
     * @param relationType the type of relationship to remove
     * @throws IllegalArgumentException if the specified relationship does not exist between the two victims
     */
    public void removeFamilyRelationship(DisasterVictim victim2, RelationshipType relationType) throws IllegalArgumentException {
        // Check if the relationship exists
        FamilyRelation relationToRemove = null;
        for (FamilyRelation existingRelation : this.familyConnections) {
            if (existingRelation.getPersonTwo().equals(victim2) && existingRelation.getRelationshipType() == relationType) {
                relationToRemove = existingRelation;
                break;
            }
        }

        // If the relationship exists, remove it from both victims
        if (relationToRemove != null) {
            boolean removed = this.familyConnections.remove(relationToRemove);
            if (!removed) {
                throw new IllegalArgumentException("Relationship not found in the list");
            }

            boolean removedFromVictim2 = victim2.familyConnections.removeIf(relation -> relation.getPersonTwo().equals(this) && relation.getRelationshipType() == relationType);
            if (!removedFromVictim2) {
                throw new IllegalArgumentException("Relationship not found in the list of the second victim");
            }
        } else {
            throw new IllegalArgumentException("Relationship not found in the list");
        }
    }


    /**
     * Adds a medical record to the list of medical records for this DisasterVictim.
     *
     * @param medicalRecord the medical record to add
     * @throws IllegalArgumentException if a medical record with the same location, treatment details, and date of treatment already exists for this victim
     */
    public void addMedicalRecord(MedicalRecord medicalRecord) throws IllegalArgumentException {
        for (MedicalRecord existingRecord : medicalRecords) {
            if (existingRecord.getLocation().equals(medicalRecord.getLocation()) &&
                    existingRecord.getTreatmentDetails().equals(medicalRecord.getTreatmentDetails()) &&
                    existingRecord.getDateOfTreatment().equals(medicalRecord.getDateOfTreatment())) {
                throw new IllegalArgumentException("Medical record already exists");
            }
        }
        medicalRecords.add(medicalRecord);
    }


    /**
     * Removes a medical record from the list of medical records for this DisasterVictim.
     *
     * @param medicalRecord the medical record to remove
     * @throws IllegalArgumentException if the specified medical record does not exist in the list of medical records for this victim
     */
    public void removeMedicalRecord(MedicalRecord medicalRecord) throws IllegalArgumentException {
        // Check if the medical record exists
        boolean removed = medicalRecords.remove(medicalRecord);
        if (!removed) {
            throw new IllegalArgumentException("Medical record not found");
        }
    }


    /**
     * Checks if the provided date string has a valid format and represents a date before or equal to the current date.
     *
     * @param dateToCheck the date string to check, formatted as "YYYY-MM-DD"
     * @return true if the date string has a valid format and represents a date before or equal to the current date, otherwise false
     */
    private boolean validDate(String dateToCheck) {
        DateTimeFormatter formatter = DateTimeFormatter.ISO_DATE;
        try {
            LocalDate date = LocalDate.parse(dateToCheck, formatter);
            LocalDate currentDate = LocalDate.now();
            return date.isBefore(currentDate) || date.isEqual(currentDate);
        } catch (DateTimeException e) {
            return false;
        }
    }


    /**
     * Checks if the provided date is before or equal to the current date.
     *
     * @param dateToCheck the date to check
     * @return true if the provided date is before or equal to the current date, otherwise false
     */
    private boolean validDate(LocalDate dateToCheck) {
        LocalDate currentDate = LocalDate.now();
        return dateToCheck.isBefore(currentDate) || dateToCheck.isEqual(currentDate);
    }


    /**
     * Searches for a Supply object with the same type as the specified element within the personal belongings list.
     *
     * @param elementToFind the Supply object to search for
     * @return the first matching Supply object found, or null if no match is found
     */
    private Supply inPersonalBelonging(Supply elementToFind) {
        for (Supply element : personalBelongings) {
            if (element.getType().equals(elementToFind.getType())) {
                return element;
            }
        }
        return null;
    }


    /**
     * Removes Supply objects with a quantity of 0 from the specified list.
     *
     * @param list the list of Supply objects to refresh
     */
    private void refreshSupplies(ArrayList<Supply> list) {
        list.removeIf(supply -> supply.getQuantity() == 0);
    }


    /**
     * Calculates the age of the disaster victim based on the provided date of birth.
     *
     * @return the age of the disaster victim in years
     * @throws DateTimeException if the date of birth is not in the expected format
     */
    private int calculateAge() throws DateTimeException {
        LocalDate birthDate = LocalDate.parse(dateOfBirth, DateTimeFormatter.ISO_DATE);
        LocalDate currentDate = LocalDate.now();
        Period period = Period.between(birthDate, currentDate);
        return period.getYears();
    }


    /**
     * Checks if the provided gender is valid by comparing it to a list of predefined gender options.
     *
     * @param gender the gender to validate
     * @return true if the provided gender is valid, otherwise false
     * @throws IOException if an I/O error occurs while reading the gender options file
     */
    private boolean validGender(String gender) throws IOException {
        GenderOption options = new GenderOption("./src/edu/ucalgary/oop/GenderOptions.txt");

        ArrayList<String> genderOptions = options.getOptions();
        return genderOptions.contains(gender);
    }


    /**
     * Gets the counter value.
     *
     * @return the counter value
     */
    public int getCounter() {
        return counter;
    }


    /**
     * Gets the date of birth of the disaster victim.
     *
     * @return the date of birth
     */
    public String getDateOfBirth() {
        return dateOfBirth;
    }


    /**
     * Sets the date of birth of the disaster victim.
     *
     * @param dateOfBirth the date of birth to set, formatted as "YYYY-MM-DD"
     * @throws IllegalArgumentException if the provided date of birth is invalid
     */
    public void setDateOfBirth(String dateOfBirth) throws IllegalArgumentException {
        if (!validDate(dateOfBirth)) {
            throw new IllegalArgumentException("Invalid date of birth");
        }
        this.dateOfBirth = dateOfBirth;
        this.age = calculateAge();
    }


    /**
     * Retrieves the assigned social ID of the disaster victim.
     *
     * @return the assigned social ID
     */
    public int getAssignedSocialID() {
        return ASSIGNED_SOCIAL_ID;
    }


    /**
     * Retrieves the set of family connections associated with the disaster victim.
     *
     * @return the set of family connections
     */
    public HashSet<FamilyRelation> getFamilyConnections() {
        return familyConnections;
    }


    /**
     * Sets the family connections associated with the disaster victim.
     *
     * @param familyConnections the set of family connections to set
     */
    public void setFamilyConnections(HashSet<FamilyRelation> familyConnections) {
        this.familyConnections.clear();
        this.familyConnections.addAll(familyConnections);
    }


    /**
     * Gets the list of medical records associated with the disaster victim.
     *
     * @return the list of medical records
     */
    public ArrayList<MedicalRecord> getMedicalRecords() {
        return medicalRecords;
    }


    /**
     * Sets the list of medical records associated with the disaster victim.
     *
     * @param medicalRecords the list of medical records to set
     */
    public void setMedicalRecords(ArrayList<MedicalRecord> medicalRecords) {
        this.medicalRecords.clear();
        this.medicalRecords.addAll(medicalRecords);
    }


    /**
     * Retrieves the list of personal belongings associated with the disaster victim.
     *
     * @return the list of personal belongings
     */
    public ArrayList<Supply> getPersonalBelongings() {
        return personalBelongings;
    }


    /**
     * Sets the list of personal belongings for the disaster victim.
     *
     * @param personalBelongings the list of personal belongings to set
     */
    public void setPersonalBelongings(ArrayList<Supply> personalBelongings) {
        this.personalBelongings.clear();
        this.personalBelongings.addAll(personalBelongings);
    }


    /**
     * Retrieves the entry date of the disaster victim.
     *
     * @return the entry date of the disaster victim
     */
    public String getEntryDate() {
        return ENTRY_DATE;
    }


    /**
     * Retrieves the gender of the disaster victim.
     *
     * @return the gender of the disaster victim
     */
    public String getGender() {
        return gender;
    }


    /**
     * Sets the gender of the disaster victim.
     *
     * @param gender the gender to set for the disaster victim
     * @throws IOException              if an I/O error occurs while reading the gender options file
     * @throws IllegalArgumentException if the provided gender is invalid
     */
    public void setGender(String gender) throws IOException, IllegalArgumentException {
        if (!validGender(gender)) {
            throw new IllegalArgumentException("Invalid gender");
        }
        this.gender = gender;
    }


    /**
     * Gets the location of the disaster victim.
     *
     * @return the location of the disaster victim
     */
    public Location getLocation() {
        return location;
    }


    /**
     * Sets the location of the disaster victim.
     *
     * @param location the location to set
     */
    public void setLocation(Location location) {
        this.location = location;
    }


    /**
     * Retrieves the comments associated with the disaster victim.
     *
     * @return the comments
     */
    public String getComments() {
        return comments;
    }


    /**
     * Sets the comments associated with the disaster victim.
     *
     * @param comments the comments to set
     */
    public void setComments(String comments) {
        this.comments = comments;
    }
}

package edu.ucalgary.oop;

import org.junit.Test;

import java.io.IOException;
import java.time.LocalDate;
import java.time.format.DateTimeFormatter;
import java.util.ArrayList;
import java.util.HashSet;

import static org.junit.Assert.*;

public class DisasterVictimTest {
    DisasterVictim testVictim = new DisasterVictim("Name");

    @Test
    public void testObjectCreation() {
        DisasterVictim test1 = new DisasterVictim("First");
        DisasterVictim test2 = new DisasterVictim("First", "Last");
        DisasterVictim test3 = new DisasterVictim("First", LocalDate.now());
        DisasterVictim test4 = new DisasterVictim("First", "Last", LocalDate.now().toString());
        assertNotNull(test1);
        assertNotNull(test2);
        assertNotNull(test3);
        assertNotNull(test4);
    }

    @Test
    public void testInvalidStringObjectCreationConstructorFirstName() {
        String invalidName = "";

        boolean correctValueEmpty = false;
        String failureReasonEmpty = "no exception was thrown";

        boolean correctValueNull = false;
        String failureReasonNull = "no exception was thrown";

        try {
            new DisasterVictim(invalidName);
        } catch (NullPointerException e) {
            correctValueEmpty = true;
        } catch (Exception e) {
            failureReasonEmpty = "the wrong type of exception was thrown";
        }

        try {
            new DisasterVictim(invalidName, "Random");
        } catch (NullPointerException e) {
            correctValueNull = true;
        } catch (Exception e) {
            failureReasonNull = "the wrong type of exception was thrown";
        }

        String messageEmpty = "DisasterVictim() should throw an IllegalArgumentException if '' is tried to be created as name but " + failureReasonEmpty;

        String messageNull = "DisasterVictim() should throw an IllegalArgumentException if '' is tried to be created as name but " + failureReasonNull;

        assertTrue(messageEmpty, correctValueEmpty);
        assertTrue(messageNull, correctValueNull);
    }

    @Test
    public void testInvalidStringObjectCreationConstructorLastName() {
        String invalidName = "";

        boolean correctValueEmpty = false;
        String failureReasonEmpty = "no exception was thrown";

        boolean correctValueNull = false;
        String failureReasonNull = "no exception was thrown";

        try {
            new DisasterVictim("Random", invalidName);
        } catch (NullPointerException e) {
            correctValueEmpty = true;
        } catch (Exception e) {
            failureReasonEmpty = "the wrong type of exception was thrown";
        }

        try {
            new DisasterVictim("Random", invalidName, LocalDate.now().toString());
        } catch (NullPointerException e) {
            correctValueNull = true;
        } catch (Exception e) {
            failureReasonNull = "the wrong type of exception was thrown";
        }

        String messageEmpty = "DisasterVictim() should throw an IllegalArgumentException if '' is tried to be created as name but " + failureReasonEmpty;

        String messageNull = "DisasterVictim() should throw an IllegalArgumentException if '' is tried to be created as name but " + failureReasonNull;

        assertTrue(messageEmpty, correctValueEmpty);
        assertTrue(messageNull, correctValueNull);
    }

    @Test
    public void testInvalidDateObjectCreationConstructor() {
        String futureDate = LocalDate.of(2025, 1, 1).toString();

        boolean correctValueFuture = false;
        String failureReasonFuture = "no exception was thrown";

        boolean correctValueInvalid = false;
        String failureReasonInvalid = "no exception was thrown";

        try {
            new DisasterVictim("Random", LocalDate.parse(futureDate, DateTimeFormatter.ISO_DATE));
        } catch (IllegalArgumentException e) {
            correctValueFuture = true;
        } catch (Exception e) {
            failureReasonFuture = "the wrong type of exception was thrown";
        }

        try {
            new DisasterVictim("Random", "Name", futureDate);
        } catch (IllegalArgumentException e) {
            correctValueInvalid = true;
        } catch (Exception e) {
            failureReasonInvalid = "the wrong type of exception was thrown";
        }

        String messageFuture = "DisasterVictim() should throw an IllegalArgumentException if date provided as entry date is in the future but " + failureReasonFuture;

        String messageInvalid = "DisasterVictim() should throw an IllegalArgumentException if date provided as entry date is in the future but " + failureReasonInvalid;

        assertTrue(messageFuture, correctValueFuture);
        assertTrue(messageInvalid, correctValueInvalid);
    }

    @Test
    public void testAddPersonalBelonging() {
        testVictim.getPersonalBelongings().clear();

        testVictim.addPersonalBelonging(new Supply("Water", 10));

        boolean inList = inSupplies(testVictim.getPersonalBelongings(), new Supply("Water"));

        testVictim.addPersonalBelonging(new Supply("Water", 2));

        boolean uniqueInList = testVictim.getPersonalBelongings().size() == 1 && testVictim.getPersonalBelongings().get(0).getQuantity() == 12;

        assertTrue("addPersonalBelonging() should update values of personalBelongings", inList);

        assertTrue("addPersonalBelonging() update old supply values", uniqueInList);
    }

    @Test
    public void testRemovePersonalBelonging() {
        testVictim.getPersonalBelongings().clear();

        testVictim.addPersonalBelonging(new Supply("Water", 10));

        testVictim.removePersonalBelonging(new Supply("Water", 2));

        assertEquals("removePersonalBelonging() should update supply already in personalBelongings", 8, testVictim.getPersonalBelongings().get(0).getQuantity());
    }

    @Test
    public void testInvalidRemovePersonalBelonging() {
        testVictim.getPersonalBelongings().clear();

        boolean correctValue = false;
        String failureReason = "no exception was thrown";

        try {
            testVictim.removePersonalBelonging(new Supply("Blanket", 2));
        } catch (IllegalArgumentException e) {
            correctValue = true;
        } catch (Exception e) {
            failureReason = "wrong exception was thrown";
        }

        String message = "removePersonalBelonging() should throw an IllegalArgumentException if supply provided is not in personalBelongings but " + failureReason;

        assertTrue(message, correctValue);
    }

    @Test
    public void testAddFamilyRelationship() {
        DisasterVictim testVictim1 = new DisasterVictim("John");
        DisasterVictim testVictim2 = new DisasterVictim("Cena");

        testVictim1.addFamilyRelationship(testVictim2, RelationshipType.SIBLING);

        boolean testVictimRelations1 = false;
        boolean testVictimRelations2 = false;

        for (FamilyRelation relation : testVictim1.getFamilyConnections()) {
            if (relation.getPersonTwo().equals(testVictim2) && relation.getRelationshipType() == RelationshipType.SIBLING) {
                testVictimRelations1 = true;
                break;
            }
        }

        for (FamilyRelation relation : testVictim2.getFamilyConnections()) {
            if (relation.getPersonTwo().equals(testVictim1) && relation.getRelationshipType() == RelationshipType.SIBLING) {
                testVictimRelations2 = true;
                break;
            }
        }

        assertTrue("addFamilyRelationship() should add a relationship for both victims", testVictimRelations1);
        assertTrue("addFamilyRelationship() should add a relationship for both victims", testVictimRelations2);
    }

    @Test
    public void testAddExistingFamilyRelationship() {
        DisasterVictim testVictim1 = new DisasterVictim("John");
        DisasterVictim testVictim2 = new DisasterVictim("Cena");

        boolean correctValue = false;
        String failureReason = "no exception was thrown";

        try {
            testVictim1.addFamilyRelationship(testVictim2, RelationshipType.SIBLING);
            testVictim1.addFamilyRelationship(testVictim2, RelationshipType.SIBLING);

        } catch (IllegalArgumentException e) {
            correctValue = true;
        } catch (Exception e) {
            failureReason = "wrong exception was thrown";
        }

        String message = "addFamilyRelationship() should throw an IllegalArgumentException if relationship already exists but " + failureReason;

        assertTrue(message, correctValue);
    }

    @Test
    public void testTriangleRelationships() {
        DisasterVictim testVictim1 = new DisasterVictim("John");
        DisasterVictim testVictim2 = new DisasterVictim("Cena");
        DisasterVictim testVictim3 = new DisasterVictim("Taylor");

        testVictim1.addFamilyRelationship(testVictim2, RelationshipType.SIBLING);
        testVictim3.addFamilyRelationship(testVictim2, RelationshipType.SIBLING);

        boolean correctValue1 = false;
        boolean correctValue2 = false;


        for (FamilyRelation relation : testVictim1.getFamilyConnections()) {
            if (relation.getPersonTwo().equals(testVictim3) && relation.getRelationshipType().equals(RelationshipType.SIBLING)) {
                correctValue1 = true;
                break;
            }
        }

        for (FamilyRelation relation : testVictim3.getFamilyConnections()) {
            if (relation.getPersonTwo().equals(testVictim1) && relation.getRelationshipType().equals(RelationshipType.SIBLING)) {
                correctValue2 = true;
                break;
            }
        }

        assertTrue("addFamilyRelationship() should create a relationship between testVictim1 and testVictim3 through testVictim2", correctValue1);
        assertTrue("addFamilyRelationship() should create a relationship between testVictim1 and testVictim3 through testVictim2", correctValue2);

    }

    @Test
    public void testRemoveFamilyRelationship() {
        DisasterVictim testVictim1 = new DisasterVictim("John");
        DisasterVictim testVictim2 = new DisasterVictim("Cena");

        testVictim1.addFamilyRelationship(testVictim2, RelationshipType.SIBLING);
        testVictim1.removeFamilyRelationship(testVictim2, RelationshipType.SIBLING);


        boolean testVictimRelations1 = true;
        boolean testVictimRelations2 = true;

        for (FamilyRelation relation : testVictim1.getFamilyConnections()) {
            if (relation.getPersonTwo().equals(testVictim2) && relation.getRelationshipType() == RelationshipType.SIBLING) {
                testVictimRelations1 = false;
                break;
            }
        }

        for (FamilyRelation relation : testVictim2.getFamilyConnections()) {
            if (relation.getPersonTwo().equals(testVictim1) && relation.getRelationshipType() == RelationshipType.SIBLING) {
                testVictimRelations2 = false;
                break;
            }
        }

        assertTrue("removeFamilyRelationship() should remove relationship for both victims", testVictimRelations1);
        assertTrue("removeFamilyRelationship() should remove relationship for both victim", testVictimRelations2);
    }

    @Test
    public void testRemoveInvalidFamilyRelationship() {
        DisasterVictim testVictim1 = new DisasterVictim("John");
        DisasterVictim testVictim2 = new DisasterVictim("Cena");

        boolean correctValue = false;
        String failureReason = "no exception was thrown";

        try {
            testVictim1.removeFamilyRelationship(testVictim2, RelationshipType.SIBLING);
        }  catch (IllegalArgumentException e) {
            correctValue = true;
        } catch (Exception e) {
            failureReason = "wrong exception was thrown";
        }

        String message = "removeFamilyRelationship() should throw an IllegalArgumentException if relationship already does not exists but " + failureReason;

        assertTrue(message, correctValue);
    }

    @Test
    public void testNotCascadeRemoveFamilyRelations() {
        DisasterVictim testVictim1 = new DisasterVictim("John");
        DisasterVictim testVictim2 = new DisasterVictim("Cena");
        DisasterVictim testVictim3 = new DisasterVictim("Taylor");

        testVictim1.addFamilyRelationship(testVictim2, RelationshipType.SIBLING);
        testVictim3.addFamilyRelationship(testVictim2, RelationshipType.SIBLING);

        testVictim1.removeFamilyRelationship(testVictim2, RelationshipType.SIBLING);

        boolean correctValue1 = true;
        boolean correctValue2 = false;


        for (FamilyRelation relation : testVictim2.getFamilyConnections()) {
            if (relation.getPersonTwo().equals(testVictim1) && relation.getRelationshipType().equals(RelationshipType.SIBLING)) {
                correctValue1 = false;
                break;
            }
        }

        for (FamilyRelation relation : testVictim3.getFamilyConnections()) {
            if (relation.getPersonTwo().equals(testVictim1) && relation.getRelationshipType().equals(RelationshipType.SIBLING)) {
                correctValue2 = true;
                break;
            }
        }

        assertTrue("removeFamilyRelationship() should remove relationship between testVictim1 and testVictim2", correctValue1);
        assertTrue("removeFamilyRelationship() should not remove relationship between testVictim1 and testVictim3", correctValue2);
    }

    @Test
    public void testAddValidMedicalRecord() {
        Location location = new Location("Hospital", "Address");
        MedicalRecord medicalRecord = new MedicalRecord(location, "2024-04-08");
        DisasterVictim victim = new DisasterVictim("John");

        victim.addMedicalRecord(medicalRecord);

        assertTrue("Medical record should be added successfully", victim.getMedicalRecords().contains(medicalRecord));
    }

    @Test
    public void testAddDuplicateMedicalRecord() {
        Location location = new Location("Hospital", "Address");
        MedicalRecord medicalRecord = new MedicalRecord(location, "2024-04-08");
        DisasterVictim victim = new DisasterVictim("John");

        boolean correctValue = false;
        String failureReason = "no exception was thrown";

        try {
            victim.addMedicalRecord(medicalRecord);
            victim.addMedicalRecord(medicalRecord);
        } catch (IllegalArgumentException e) {
            correctValue = true;
        } catch (Exception e) {
            failureReason = "wrong exception was thrown";
        }

        String message = "addMedicalRecord() should throw IllegalArgumentException if it already exists in victim's records but " + failureReason;
        assertTrue(message, correctValue);
    }

    @Test
    public void testRemoveValidMedicalRecord() {
        Location location = new Location("Hospital", "Address");
        MedicalRecord medicalRecord = new MedicalRecord(location, "2024-04-08");
        DisasterVictim victim = new DisasterVictim("John");

        victim.addMedicalRecord(medicalRecord);
        victim.removeMedicalRecord(medicalRecord);

        assertFalse("Medical record should be removed successfully", victim.getMedicalRecords().contains(medicalRecord));
    }

    @Test
    public void testRemoveNonExistingMedicalRecord() {
        Location location = new Location("Hospital", "Address");
        MedicalRecord medicalRecord = new MedicalRecord(location, "2024-04-08");
        DisasterVictim victim = new DisasterVictim("John");

        boolean correctValue = false;
        String failureReason = "no exception was thrown";

        try {
            victim.removeMedicalRecord(medicalRecord);
        } catch (IllegalArgumentException e) {
            correctValue = true;
        } catch (Exception e) {
            failureReason = "wrong exception was thrown";
        }

        String message = "removeMedicalRecord() should throw IllegalArgumentException if it already does not exist in victim's records but " + failureReason;
        assertTrue(message, correctValue);
    }

    @Test
    public void testSetValidDateOfBirth() {
        DisasterVictim victim = new DisasterVictim("John");
        String validDateOfBirth = "1990-01-01";

        try {
            victim.setDateOfBirth(validDateOfBirth);
            assertEquals(validDateOfBirth, victim.getDateOfBirth());
        } catch (Exception e) {
            fail("Valid date of birth should not throw an exception");
        }
    }

    @Test
    public void testSetEdgeDateOfBirth() {
        DisasterVictim victim = new DisasterVictim("John");

        String edgeDateOfBirth = LocalDate.now().minusYears(100).toString();
        try {
            victim.setDateOfBirth(edgeDateOfBirth);
            assertEquals(edgeDateOfBirth, victim.getDateOfBirth());
        } catch (Exception e) {
            fail("Edge date of birth should not throw an exception");
        }

        edgeDateOfBirth = "1800-01-01";
        boolean correctValue = false;
        String failureReason = "no exception was thrown";

        try {
            victim.setDateOfBirth(edgeDateOfBirth);
        } catch (IllegalArgumentException e) {
            correctValue = true;
        } catch (Exception e) {
            failureReason = "wrong exception was thrown";
        }

        String message = "setDateOfBirth() should throw IllegalArgumentException if date provided as date of birth is far in the past but " + failureReason;
        assertTrue(message, correctValue);
    }

    @Test
    public void testValidDateOfBirth() {
        DisasterVictim victim = new DisasterVictim("Test");
        victim.setDateOfBirth(LocalDate.now().minusYears(45).toString());
        assertEquals(45, victim.getAge());
    }

    @Test
    public void testSetAndGetDietaryRestrictions() {
        DisasterVictim victim = new DisasterVictim("Test");
        HashSet<DietaryRestriction> restrictions = new HashSet<>();
        restrictions.add(DietaryRestriction.AVML);
        restrictions.add(DietaryRestriction.DBML);
        victim.setDietaryRestrictions(restrictions);

        assertEquals("setDietaryRestrictions should update and getDietaryRestrictions should return the new dietaryRestrictions", restrictions, victim.getDietaryRestrictions());
    }

    @Test
    public void testGetAssignedSocialID() {
        DisasterVictim victim = new DisasterVictim("Test");
        int expectedSocialID = DisasterVictim.getCounter() - 1;

        assertEquals(expectedSocialID, victim.getAssignedSocialID());
    }

    @Test
    public void testUniqueAssignedSocialID() {
        DisasterVictim victim1 = new DisasterVictim("Test");
        DisasterVictim victim2 = new DisasterVictim("Name");

        int socialID1 = victim1.getAssignedSocialID();
        int socialID2 = victim2.getAssignedSocialID();

        assertNotEquals("Two victims should have different social IDs", socialID1, socialID2);
    }

    @Test
    public void testSetAndGetFamilyConnections() {
        DisasterVictim victim = new DisasterVictim("Random");
        HashSet<FamilyRelation> connections = new HashSet<>();

        DisasterVictim relative1 = new DisasterVictim("Test");
        DisasterVictim relative2 = new DisasterVictim("Name");
        FamilyRelation relation1 = new FamilyRelation(victim, relative1, RelationshipType.SIBLING);
        FamilyRelation relation2 = new FamilyRelation(victim, relative2, RelationshipType.PARENT_CHILD);
        connections.add(relation1);
        connections.add(relation2);

        victim.setFamilyConnections(connections);

        HashSet<FamilyRelation> retrievedConnections = victim.getFamilyConnections();
        assertEquals("Number of family connections should match", connections.size(), retrievedConnections.size());
        assertEquals("Family connections should match", connections, retrievedConnections);
    }

    @Test
    public void testSetAndGetMedicalRecords() {
        DisasterVictim victim = new DisasterVictim("Test");
        ArrayList<MedicalRecord> medicalRecords = new ArrayList<>();

        Location location1 = new Location("Hospital A", "123 Street");
        MedicalRecord record1 = new MedicalRecord(location1, "2024-04-01");
        MedicalRecord record2 = new MedicalRecord(location1, "2024-04-05");
        medicalRecords.add(record1);
        medicalRecords.add(record2);

        victim.setMedicalRecords(medicalRecords);

        ArrayList<MedicalRecord> retrievedRecords = victim.getMedicalRecords();
        assertEquals("Number of medical records should match", medicalRecords.size(), retrievedRecords.size());
        assertEquals("Medical records should match", medicalRecords, retrievedRecords);
    }

    @Test
    public void testSetAndGetPersonalBelongings() {
        DisasterVictim victim = new DisasterVictim("Test");
        ArrayList<Supply> personalBelongings = new ArrayList<>();

        Supply supply1 = new Supply("Water", 10);
        Supply supply2 = new Supply("Food", 20);
        personalBelongings.add(supply1);
        personalBelongings.add(supply2);

        victim.setPersonalBelongings(personalBelongings);

        ArrayList<Supply> retrievedBelongings = victim.getPersonalBelongings();
        assertEquals("Number of personal belongings should match", personalBelongings.size(), retrievedBelongings.size());
        assertEquals("Personal belongings should match", personalBelongings, retrievedBelongings);
    }

    @Test
    public void testGetEntryDate() {
        DisasterVictim victim = new DisasterVictim("Test", LocalDate.now());
        String expectedEntryDate = LocalDate.now().toString();

        assertEquals("Entry date should match", expectedEntryDate, victim.getEntryDate());
    }

    @Test
    public void testSetValidGender() {
        DisasterVictim victim = new DisasterVictim("Test");
        GenderOption genderOptions = new GenderOption("./src/edu/ucalgary/oop/GenderOptions.txt");

        try {
            ArrayList<String> options = genderOptions.getOptions();

            for (String gender : options) {
                victim.setGender(gender);
                assertEquals("Gender should match", gender, victim.getGender());
            }
        } catch (IllegalArgumentException e) {
            fail("Valid gender should not throw exceptions");
        } catch (IOException e) {
            fail("File Not Found");
        }

    }

    @Test
    public void testSetInvalidGender() {
        DisasterVictim victim = new DisasterVictim("Test");
        String invalidGender = "invalid";
        boolean correctValue = false;
        String failureReason = "no exception was thrown";

        try {
            victim.setGender(invalidGender);
        } catch (IOException e) {
            failureReason = "file not found";
        } catch (IllegalArgumentException e) {
            correctValue = true;
        } catch (Exception e) {
            failureReason = "wrong exception was thrown";
        }

        String message = "setGender() should throw an IllegalArgumentException if gender is not a valid option but " + failureReason;
        assertTrue(message, correctValue);
    }

    @Test
    public void testGetAndSetLocation() {
        Location expectedLocation = new Location("Hospital", "123 Main St");
        DisasterVictim victim = new DisasterVictim("Test");
        victim.setLocation(expectedLocation);
        assertEquals("Location should match", expectedLocation, victim.getLocation());
    }

    @Test
    public void testGetAndSetComments() {
        String expectedComments = "Patient in stable condition";
        DisasterVictim victim = new DisasterVictim("Test");
        victim.setComments(expectedComments);
        assertEquals("Comments should match", expectedComments, victim.getComments());
    }

    /**
     * Searches for a Supply object with the same type as the specified element within the personal belongings list.
     *
     * @param elementToFind the Supply object to search for
     * @return the first matching Supply object found, or null if no match is found
     */
    private boolean inSupplies(ArrayList<Supply> supplies, Supply elementToFind) {
        for (Supply element : supplies) {
            if (element.getType().equals(elementToFind.getType())) {
                return true;
            }
        }
        return false;
    }
}

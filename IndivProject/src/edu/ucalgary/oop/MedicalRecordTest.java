package edu.ucalgary.oop;

import org.junit.Test;

import static org.junit.Assert.*;

public class MedicalRecordTest {
    Location expectedLocation = new Location("ShelterA", "140 8 Ave NW ");
    private final String expectedTreatmentDetails = "Broken arm treated";
    private final String expectedDateOfTreatment = "2024-01-19";
    MedicalRecord testMedicalRecord = new MedicalRecord(expectedLocation, expectedTreatmentDetails, expectedDateOfTreatment);
    private final String validDateOfTreatment = "2024-02-04";
    private final String inValidDateOfTreatment = "2024/02/04";

    @Test
    public void testConstructorThreeArguments() {
        assertNotNull("Constructor should create a non-null Location object", testMedicalRecord);
        assertEquals("Constructor should set Location correctly", expectedLocation, testMedicalRecord.getLocation());
        assertEquals("Constructor should set the treatment details correctly", expectedTreatmentDetails, testMedicalRecord.getTreatmentDetails());
        assertEquals("Constructor should set the date correctly", expectedDateOfTreatment, testMedicalRecord.getDateOfTreatment());
    }

    @Test
    public void testConstructorInvalidDateThreeArguments() {
        boolean correctValue = false;
        String failureReason = "no exception was thrown";
        try {
            new MedicalRecord(expectedLocation, expectedTreatmentDetails, inValidDateOfTreatment);
        } catch (IllegalArgumentException e) {
            correctValue = true;
        } catch (Exception e) {
            failureReason = "the wrong type of exception was thrown";
        }
        String message = "Constructor should throw IllegalArgumentException when date is not in valid format of 'YYYY-MM-DD' but " + failureReason;
        assertTrue(message, correctValue);
    }

    @Test
    public void testConstructorTwoArguments() {
        MedicalRecord test = new MedicalRecord(expectedLocation, validDateOfTreatment);
        assertNotNull("Constructor should create a non-null Location object", test);
        assertEquals("Constructor should set Location correctly", expectedLocation, test.getLocation());
        assertEquals("Constructor should set the date correctly", validDateOfTreatment, test.getDateOfTreatment());
    }

    @Test
    public void testConstructorInvalidDateTwoArguments() {
        boolean correctValue = false;
        String failureReason = "no exception was thrown";
        try {
            new MedicalRecord(expectedLocation, inValidDateOfTreatment);
        } catch (IllegalArgumentException e) {
            correctValue = true;
        } catch (Exception e) {
            failureReason = "the wrong type of exception was thrown";
        }
        String message = "Constructor should throw IllegalArgumentException when date is not in valid format of 'YYYY-MM-DD' but " + failureReason;
        assertTrue(message, correctValue);
    }

    @Test
    public void testConstructorOneArgument() {
        MedicalRecord test = new MedicalRecord(expectedLocation);
        assertNotNull("Constructor should create a non-null Location object", test);
        assertEquals("Constructor should set Location correctly", expectedLocation, test.getLocation());
    }

    @Test
    public void testGetLocation() {
        assertEquals("getLocation should return the correct Location", expectedLocation, testMedicalRecord.getLocation());
    }

    @Test
    public void testSetLocation() {
        Location newExpectedLocation = new Location("Shelter B", "150 8 Ave NW ");
        testMedicalRecord.setLocation(newExpectedLocation);
        assertEquals("setLocation should update the Location", newExpectedLocation.getName(), testMedicalRecord.getLocation().getName());
    }

    @Test
    public void testGetTreatmentDetails() {
        assertEquals("getTreatmentDetails should return the correct treatment details", expectedTreatmentDetails, testMedicalRecord.getTreatmentDetails());
    }

    @Test
    public void testSetTreatmentDetails() {
        String newExpectedTreatment = "No surgery required";
        testMedicalRecord.setTreatmentDetails(newExpectedTreatment);
        assertEquals("setTreatmentDetails should update the treatment details", newExpectedTreatment, testMedicalRecord.getTreatmentDetails());
    }

    @Test
    public void testGetDateOfTreatment() {
        assertEquals("getDateOfTreatment should return the correct date of treatment", expectedDateOfTreatment, testMedicalRecord.getDateOfTreatment());
    }

    @Test
    public void testSetDateOfTreatment() {
        String newExpectedDateOfTreatment = "2024-02-05";
        testMedicalRecord.setDateOfTreatment(newExpectedDateOfTreatment);
        assertEquals("setDateOfTreatment should update date of treatment", newExpectedDateOfTreatment, testMedicalRecord.getDateOfTreatment());
    }

    @Test
    public void testSetDateOfTreatmentWithValidFormat() {

        testMedicalRecord.setDateOfTreatment(validDateOfTreatment); // Should not throw an exception
    }

    @Test
    public void testSetDateOfBirthWithInvalidFormat() {
        boolean correctValue = false;
        String failureReason = "no exception was thrown";

        try {
            testMedicalRecord.setDateOfTreatment(inValidDateOfTreatment);
        } catch (IllegalArgumentException e) {
            correctValue = true;
        } catch (Exception e) {
            failureReason = "the wrong type of exception was thrown";
        }

        String message = "setDateOfTreatment() should throw an IllegalArgumentException with invalid date format '" + inValidDateOfTreatment + "' but " + failureReason + ".";
        assertTrue(message, correctValue);
    }

    @Test
    public void testSetDateOfBirthWithNotADate() {
        boolean correctValue = false;
        String failureReason = "no exception was thrown";

        try {
            testMedicalRecord.setDateOfTreatment(expectedTreatmentDetails);
        } catch (IllegalArgumentException e) {
            correctValue = true;
        } catch (Exception e) {
            failureReason = "the wrong type of exception was thrown";
        }

        String message = "setDateOfTreatment() should throw an IllegalArgumentException with invalid non-date input '" + inValidDateOfTreatment + "' but " + failureReason + ".";
        assertTrue(message, correctValue);
    }
}

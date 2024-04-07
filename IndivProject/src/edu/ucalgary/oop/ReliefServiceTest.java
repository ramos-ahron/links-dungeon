package edu.ucalgary.oop;

import org.junit.Test;
import static org.junit.Assert.*;

public class ReliefServiceTest {
    ReliefService testReliefService = new ReliefService();

    @Test
    public void testObjectCreation() {
        assertNotNull(testReliefService);
    }

    @Test
    public void testAddShelter() {
        Location testLocation = new Location("Test", "Random Address");

        assertTrue("newly created object should have an empty shelters", testReliefService.getShelters().isEmpty());
        testReliefService.addShelter(testLocation);
        assertNotNull("addShelter() should update the contents of shelters", testReliefService.getShelters());
    }

    @Test
    public void testInvalidAddShelterNull() {
        boolean correctValueNull = false;
        String failureReasonNull = "no exception was thrown";

        try {
            testReliefService.addShelter(null);
        } catch (NullPointerException e) {
            correctValueNull = true;
        } catch (Exception e) {
            failureReasonNull = "the wrong type of exception was thrown";
        }

        String messageNull = "addShelter() should throw an NullPointerException if null is tried to be added to shelters but " + failureReasonNull;

        assertTrue(messageNull, correctValueNull);
    }

    @Test
    public void testInvalidAddOccupantInList() {
        Location testLocation = new Location("Test", "Random Address");

        boolean correctValueInList = false;
        String failureReasonInList = "no exception was thrown";

        try {
            testReliefService.addShelter(testLocation);
            testReliefService.addShelter(testLocation);
        } catch (IllegalArgumentException e) {
            correctValueInList = true;
        } catch (Exception e) {
            failureReasonInList = "the wrong type of exception was thrown";
        }

        String messageInList = "addShelter() should throw an IllegalArgumentException if location is already in shelters but " + failureReasonInList;

        assertTrue(messageInList, correctValueInList);
    }

    @Test
    public void testRemoveShelter() {
        Location testLocation1 = new Location("Test", "Random Address");
        Location testLocation2 = new Location("Test", "Random Address");

        testReliefService.getShelters().clear();

        testReliefService.addShelter(testLocation1);
        testReliefService.removeShelter(testLocation2);

        for (Location element : testReliefService.getShelters()) {
            System.out.println(element.getName());
        }

        assertTrue("removeShelter() should make shelters empty", testReliefService.getShelters().isEmpty());
    }
}

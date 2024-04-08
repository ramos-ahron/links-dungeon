package edu.ucalgary.oop;

import org.junit.Test;

import java.util.LinkedList;

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
        Location testLocation1 = new Location("Test", "Random Address");
        Location testLocation2 = new Location("Test", "Random Address");

        boolean correctValueInList = false;
        String failureReasonInList = "no exception was thrown";

        try {
            testReliefService.addShelter(testLocation1);
            testReliefService.addShelter(testLocation2);
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

    @Test
    public void testInvalidRemoveShelterNull() {
        boolean correctValueNull = false;
        String failureReasonNull = "no exception was thrown";

        try {
            testReliefService.removeShelter(null);
        } catch (NullPointerException e) {
            correctValueNull = true;
        } catch (Exception e) {
            failureReasonNull = "the wrong type of exception was thrown";
        }

        String messageNull = "removeShelter() should throw an NullPointerException if null is tried to be removed from shelters but " + failureReasonNull;

        assertTrue(messageNull, correctValueNull);
    }

    @Test
    public void testInvalidRemoveOccupantNotInList() {
        Location testLocation = new Location("Test", "Random Address");

        boolean correctValueNotInList = false;
        String failureReasonNotInList = "no exception was thrown";

        try {
            testReliefService.removeShelter(testLocation);
        } catch (IllegalArgumentException e) {
            correctValueNotInList = true;
        } catch (Exception e) {
            failureReasonNotInList = "the wrong type of exception was thrown";
        }

        String messageInList = "removeShelter() should throw an IllegalArgumentException if location is not in shelters but " + failureReasonNotInList;

        assertTrue(messageInList, correctValueNotInList);
    }

    @Test
    public void testAddMissingPerson() {
        DisasterVictim testVictim = new DisasterVictim("Random", "Name", "2024-01-10");

        assertTrue("newly created object should have an empty shelters", testReliefService.getMissingPeople().isEmpty());
        testReliefService.addMissingPerson(testVictim);
        assertNotNull("addShelter() should update the contents of shelters", testReliefService.getMissingPeople());
    }

    @Test
    public void testInvalidAddMissingPersonNull() {
        boolean correctValueNull = false;
        String failureReasonNull = "no exception was thrown";

        try {
            testReliefService.addMissingPerson(null);
        } catch (NullPointerException e) {
            correctValueNull = true;
        } catch (Exception e) {
            failureReasonNull = "the wrong type of exception was thrown";
        }

        String messageNull = "addMissingPerson() should throw an NullPointerException if null is tried to be added to missingPeople but " + failureReasonNull;

        assertTrue(messageNull, correctValueNull);
    }

    @Test
    public void testInvalidAddMissingPersonInList() {
        DisasterVictim testVictim1 = new DisasterVictim("Random", "Name", "2024-01-10");
        DisasterVictim testVictim2 = new DisasterVictim("Random", "Name", "2024-01-10");

        boolean correctValueInList = false;
        String failureReasonInList = "no exception was thrown";

        try {
            testReliefService.addMissingPerson(testVictim1);
            testReliefService.addMissingPerson(testVictim2);
        } catch (IllegalArgumentException e) {
            correctValueInList = true;
        } catch (Exception e) {
            failureReasonInList = "the wrong type of exception was thrown";
        }

        String messageInList = "addMissingPerson() should throw an IllegalArgumentException if victim is already in missingPeople but " + failureReasonInList;

        assertTrue(messageInList, correctValueInList);
    }

    @Test
    public void testRemoveMissingPerson() {
        DisasterVictim testVictim1 = new DisasterVictim("Random", "Name", "2024-01-10");
        DisasterVictim testVictim2 = new DisasterVictim("Random", "Name", "2024-01-10");

        testReliefService.getMissingPeople().clear();

        testReliefService.addMissingPerson(testVictim1);
        testReliefService.removeMissingPerson(testVictim2);

        assertTrue("removeMissingPerson() should make missingPeople empty", testReliefService.getMissingPeople().isEmpty());
    }

    @Test
    public void testInvalidRemoveMissingPersonNull() {
        boolean correctValueNull = false;
        String failureReasonNull = "no exception was thrown";

        try {
            testReliefService.removeMissingPerson(null);
        } catch (NullPointerException e) {
            correctValueNull = true;
        } catch (Exception e) {
            failureReasonNull = "the wrong type of exception was thrown";
        }

        String messageNull = "removeMissingPerson() should throw a NullPointerException if null is tried to be removed from missingPeople but " + failureReasonNull;

        assertTrue(messageNull, correctValueNull);
    }

    @Test
    public void testInvalidRemoveMissingPersonNotInList() {
        DisasterVictim testVictim = new DisasterVictim("Random", "Name", "2024-01-10");

        boolean correctValueNotInList = false;
        String failureReasonNotInList = "no exception was thrown";

        try {
            testReliefService.removeMissingPerson(testVictim);
        } catch (IllegalArgumentException e) {
            correctValueNotInList = true;
        } catch (Exception e) {
            failureReasonNotInList = "the wrong type of exception was thrown";
        }

        String messageInList = "removeMissingPerson() should throw an IllegalArgumentException if victim is not in missingPeople but " + failureReasonNotInList;

        assertTrue(messageInList, correctValueNotInList);
    }

    @Test
    public void testGetAndSetShelters() {
        LinkedList<Location> testLocationList = new LinkedList<>();
        testLocationList.add(new Location("Location1", "Address1"));
        testLocationList.add(new Location("Location2", "Address2"));
        testLocationList.add(new Location("Location3", "Address3"));
        testLocationList.add(new Location("Location4", "Address4"));

        testReliefService.setShelters(testLocationList);

        assertEquals("setShelters() should update the value of shelters", testLocationList, testReliefService.getShelters());
    }

    @Test
    public void testSetAndGetMissingPeople() {
        LinkedList<DisasterVictim> testVictimList = new LinkedList<>();

        testVictimList.add(new DisasterVictim("Victim1", "Random1", "2024-01-01"));
        testVictimList.add(new DisasterVictim("Victim2", "Random2", "2024-01-02"));
        testVictimList.add(new DisasterVictim("Victim3", "Random3", "2024-01-03"));

        testReliefService.setMissingPeople(testVictimList);

        assertEquals("setMissingPeople() should update the value of missingPeople", testVictimList, testReliefService.getMissingPeople());
    }

    @Test
    public void testGetWorkerID() {
        int counter = ReliefService.getWorkerIdCounter();
        int workerID = testReliefService.getWorkerId();

        assertEquals("getWorkerID() should return getWorkerIdCounter() - 1", counter, workerID + 1);
    }
}

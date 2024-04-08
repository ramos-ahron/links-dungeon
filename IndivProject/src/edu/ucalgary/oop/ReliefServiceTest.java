package edu.ucalgary.oop;

import org.junit.Test;

import java.util.LinkedList;

import static org.junit.Assert.*;

public class ReliefServiceTest {
    @Test
    public void testAddShelter() {
        Location testLocation = new Location("Test", "Random Address");
        ReliefService.getShelters().clear();
        ReliefService.addShelter(testLocation);
        assertTrue("addShelter() should update the contents of shelters", inListLocation(ReliefService.getShelters(), testLocation));
    }

    @Test
    public void testInvalidAddShelterNull() {
        boolean correctValueNull = false;
        String failureReasonNull = "no exception was thrown";

        try {
            ReliefService.addShelter(null);
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
            ReliefService.addShelter(testLocation1);
            ReliefService.addShelter(testLocation2);
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

        ReliefService.getShelters().clear();

        ReliefService.addShelter(testLocation1);
        ReliefService.removeShelter(testLocation2);

        for (Location element : ReliefService.getShelters()) {
            System.out.println(element.getName());
        }

        assertTrue("removeShelter() should make shelters empty", ReliefService.getShelters().isEmpty());
    }

    @Test
    public void testInvalidRemoveShelterNull() {
        boolean correctValueNull = false;
        String failureReasonNull = "no exception was thrown";

        try {
            ReliefService.removeShelter(null);
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

        ReliefService.getShelters().clear();

        try {
            ReliefService.removeShelter(testLocation);
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
        ReliefService.getMissingPeople().clear();
        ReliefService.addMissingPerson(testVictim);
        assertTrue("addMissingPerson() should update the contents of missingPeople", inListMissingPerson(ReliefService.getMissingPeople(), testVictim));
    }

    @Test
    public void testInvalidAddMissingPersonNull() {
        boolean correctValueNull = false;
        String failureReasonNull = "no exception was thrown";

        try {
            ReliefService.addMissingPerson(null);
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

        boolean correctValueInList = false;
        String failureReasonInList = "no exception was thrown";

        try {
            ReliefService.addMissingPerson(testVictim1);
            ReliefService.addMissingPerson(testVictim1);
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

        ReliefService.getMissingPeople().clear();

        ReliefService.addMissingPerson(testVictim1);
        ReliefService.removeMissingPerson(testVictim1);

        assertTrue("removeMissingPerson() should make missingPeople empty", ReliefService.getMissingPeople().isEmpty());
    }

    @Test
    public void testInvalidRemoveMissingPersonNull() {
        boolean correctValueNull = false;
        String failureReasonNull = "no exception was thrown";

        try {
            ReliefService.removeMissingPerson(null);
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

        ReliefService.getMissingPeople().clear();

        try {
            ReliefService.removeMissingPerson(testVictim);
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

        ReliefService.setShelters(testLocationList);

        assertEquals("setShelters() should update the value of shelters", testLocationList, ReliefService.getShelters());
    }

    @Test
    public void testSetAndGetMissingPeople() {
        LinkedList<DisasterVictim> testVictimList = new LinkedList<>();

        testVictimList.add(new DisasterVictim("Victim1", "Random1", "2024-01-01"));
        testVictimList.add(new DisasterVictim("Victim2", "Random2", "2024-01-02"));
        testVictimList.add(new DisasterVictim("Victim3", "Random3", "2024-01-03"));

        ReliefService.setMissingPeople(testVictimList);

        assertEquals("setMissingPeople() should update the value of missingPeople", testVictimList, ReliefService.getMissingPeople());
    }


    /**
     * Checks if the specified location is present in the list of shelters.
     *
     * @param shelters      The list of shelters to search.
     * @param elementToFind The location to search for.
     * @return true if the location is found in the list of shelters, false otherwise.
     */
    private boolean inListLocation(LinkedList<Location> shelters, Location elementToFind) {
        for (Location location : shelters) {
            if (location.getName().equals(elementToFind.getName()) && location.getAddress().equals(elementToFind.getAddress())) {
                return true;
            }
        }
        return false;
    }

    /**
     * Checks if the specified victim is present in the list of missingPeople.
     *
     * @param missingPeople The list of missing people to search.
     * @param elementToFind The victim to search for.
     * @return true if the victim is found in the list of missing people, false otherwise.
     */
    private boolean inListMissingPerson(LinkedList<DisasterVictim> missingPeople, DisasterVictim elementToFind) {
        for (DisasterVictim victim : missingPeople) {
            if (elementToFind.getAssignedSocialID() == victim.getAssignedSocialID()) {
                return true;
            }
        }
        return false;
    }
}

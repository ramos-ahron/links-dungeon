package edu.ucalgary.oop;

import org.junit.Test;

import java.util.LinkedList;

import static org.junit.Assert.*;

public class LocationTest {
    private final String expectedName = "Shelter A";
    private final String expectedAddress = "1234 Shelter Ave";
    private final Location location = new Location(expectedName, expectedAddress);

    @Test
    public void testConstructor() {
        assertNotNull("Constructor should create a non-null Location object", location);
        assertEquals("Constructor should set the name correctly", expectedName, location.getName());
        assertEquals("Constructor should set the address correctly", expectedAddress, location.getAddress());
    }

    @Test
    public void testGetAndSetName() {
        String newName = "Shelter B";
        location.setName(newName);
        assertEquals("setName() should update the name of the location", newName, location.getName());
    }

    @Test
    public void testGetAndSetAddress() {
        String newAddress = "4321 Shelter Blvd";
        location.setAddress(newAddress);
        assertEquals("setAddress() should update the address of the location", newAddress, location.getAddress());
    }

    @Test
    public void testGetAndSetSupplies() {
        Supply supply1 = new Supply("Type A", 3);
        Supply supply2 = new Supply("Type B", 5);
        LinkedList<Supply> newSupplies = new LinkedList<>();
        newSupplies.add(supply1);
        newSupplies.add(supply2);

        location.setSupplies(newSupplies);

        assertEquals("setSupplies() should change the value of supplies", newSupplies, location.getSupplies());
    }

    @Test
    public void testGetAndSetOccupants() {
        DisasterVictim personOne = new DisasterVictim("John", "Dalian", "2024-01-19");
        DisasterVictim personTwo = new DisasterVictim("Jane", "McEwan", "2024-02-20");
        LinkedList<DisasterVictim> newOccupants = new LinkedList<>();
        newOccupants.add(personOne);
        newOccupants.add(personTwo);

        location.setOccupants(newOccupants);

        assertEquals("setOccupants() should change the value of occupants", newOccupants, location.getOccupants());
    }

    @Test
    public void testAddAndRemoveOccupant() {
        DisasterVictim victim = new DisasterVictim("Emma", "Smith", "2024-01-01");
        location.addOccupant(victim);

        assertTrue("addOccupants() should update occupants list", inList(location.getOccupants(), victim));

        location.removeOccupant(victim);
        assertFalse("removeOccupant() should update occupants list", inList(location.getOccupants(), victim));
    }

    @Test
    public void testInvalidAddOccupant() {
        DisasterVictim victim = new DisasterVictim("Liam", "Johnson", "2020-05-11");

        boolean correctValueNull = false;
        String failureReasonNull = "no exception was thrown";

        boolean correctValueInList = false;
        String failureReasonInList = "no exception was thrown";

        try {
            location.addOccupant(null);
        } catch (NullPointerException e) {
            correctValueNull = true;
        } catch (Exception e) {
            failureReasonNull = "the wrong type of exception was thrown";
        }

        try {
            location.addOccupant(victim);
            location.addOccupant(victim);
        } catch (IllegalArgumentException e) {
            correctValueInList = true;
        } catch (Exception e) {
            failureReasonInList = "the wrong type of exception was thrown";
        }

        String messageNull = "addOccupant() should throw an NullPointerException if null is tried to be added to occupants but " + failureReasonNull;
        String messageInList = "addOccupant() should throw an IllegalArgumentException if occupant is already in location but " + failureReasonInList;

        assertTrue(messageNull, correctValueNull);
        assertTrue(messageInList, correctValueInList);
    }

    @Test
    public void testInvalidRemoveOccupant() {
        DisasterVictim victim = new DisasterVictim("Liam", "Johnson", "2020-05-11");

        boolean correctValueNull = false;
        String failureReasonNull = "no exception was thrown";

        boolean correctValueInList = false;
        String failureReasonInList = "no exception was thrown";

        try {
            location.removeOccupant(null);
        } catch (NullPointerException e) {
            correctValueNull = true;
        } catch (Exception e) {
            failureReasonNull = "the wrong type of exception was thrown";
        }

        try {
            location.removeOccupant(victim);
        } catch (IllegalArgumentException e) {
            correctValueInList = true;
        } catch (Exception e) {
            failureReasonInList = "the wrong type of exception was thrown";
        }

        String messageNull = "removeOccupant() should throw an NullPointerException if null is tried to be removed to occupants but " + failureReasonNull;
        String messageInList = "removeOccupant() should throw an IllegalArgumentException if occupant is not in location but " + failureReasonInList;

        assertTrue(messageNull, correctValueNull);
        assertTrue(messageInList, correctValueInList);
    }

    @Test
    public void testAddAndRemoveSupply() {
        Supply supply = new Supply("Papaya", 100);
        location.addSupply(supply);

        assertTrue("addSupply() should update supplies list", inList(location.getSupplies(), supply));

        location.removeSupply(supply);
        assertFalse("removeSupply() should update supplies list", inList(location.getSupplies(), supply));
    }

    @Test
    public void testInvalidAddSupply() {
        boolean correctValue = false;
        String failureReason = "no exception was thrown";
        try {
            location.addSupply(null);
        } catch (NullPointerException e) {
            correctValue = true;
        } catch (Exception e) {
            failureReason = "the wrong type of exception was thrown";
        }

        String message = "addSupply() should throw a NullPointerException if supply provided is null but " + failureReason;
        assertTrue(message, correctValue);
    }

    @Test
    public void testInvalidRemoveSupply() {
        Supply invalidSupply = new Supply("Random", 5);

        boolean correctValueNull = false;
        String failureReasonNull = "no exception was thrown";

        boolean correctValueInList = false;
        String failureReasonInList = "no exception was thrown";

        boolean correctValueNegative = false;
        String failureReasonNegative = "no exception was thrown";

        try {
            location.removeSupply(null);
        } catch (NullPointerException e) {
            correctValueNull = true;
        } catch (Exception e) {
            failureReasonNull = "the wrong type of exception was thrown";
        }

        try {
            location.removeSupply(invalidSupply);
        } catch (IllegalArgumentException e) {
            correctValueInList = true;
        } catch (Exception e) {
            failureReasonInList = "the wrong type of exception was thrown";
        }

        try {
            location.addSupply(invalidSupply);
            location.removeSupply(new Supply("Random", 20));
        } catch (IllegalArgumentException e) {
            correctValueNegative = true;
        } catch (Exception e) {
            failureReasonNegative = "the wrong type of exception was thrown";
        }

        String messageNull = "removeSupply() should throw an NullPointerException if null is tried to be removed from supplies but " + failureReasonNull;
        String messageInList = "removeSupply() should throw an IllegalArgumentException if supply is not in location but " + failureReasonInList;
        String messageNegative = "removeSupply() should throw an IllegalArgumentException if resulting supply will give a negative amount but " + failureReasonNegative;


        assertTrue(messageNull, correctValueNull);
        assertTrue(messageInList, correctValueInList);
        assertTrue(messageNegative, correctValueNegative);
    }

    /**
     * Checks if the specified element is present in the provided LinkedList.
     *
     * @param list          the LinkedList to search
     * @param elementToFind the element to search for
     * @param <T>           the type of elements in the LinkedList
     * @return true if the element is found in the LinkedList, otherwise false
     */
    private <T> boolean inList(LinkedList<T> list, T elementToFind) {
        for (T element : list) {
            if (element.equals(elementToFind)) {
                return true;
            }
        }
        return false;
    }
}

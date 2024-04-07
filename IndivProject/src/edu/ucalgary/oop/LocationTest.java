package edu.ucalgary.oop;

import org.junit.Test;

import java.util.LinkedList;

import static org.junit.Assert.*;

public class LocationTest {
    private final String expectedName = "Shelter A";
    private final String expectedAddress = "1234 Shelter Ave";
    private final Location testLocation = new Location(expectedName, expectedAddress);

    @Test
    public void testConstructor() {
        assertNotNull("Constructor should create a non-null Location object", testLocation);
        assertEquals("Constructor should set the name correctly", expectedName, testLocation.getName());
        assertEquals("Constructor should set the address correctly", expectedAddress, testLocation.getAddress());
    }

    @Test
    public void testGetAndSetName() {
        String newName = "Shelter B";
        testLocation.setName(newName);
        assertEquals("setName() should update the name of the location", newName, testLocation.getName());
    }

    @Test
    public void testGetAndSetAddress() {
        String newAddress = "4321 Shelter Blvd";
        testLocation.setAddress(newAddress);
        assertEquals("setAddress() should update the address of the location", newAddress, testLocation.getAddress());
    }

    @Test
    public void testGetAndSetSupplies() {
        Supply supply1 = new Supply("Type A", 3);
        Supply supply2 = new Supply("Type B", 5);
        LinkedList<Supply> newSupplies = new LinkedList<>();
        newSupplies.add(supply1);
        newSupplies.add(supply2);

        testLocation.setSupplies(newSupplies);

        assertEquals("setSupplies() should change the value of supplies", newSupplies, testLocation.getSupplies());
    }

    @Test
    public void testGetAndSetOccupants() {
        DisasterVictim personOne = new DisasterVictim("John", "Dalian", "2024-01-19");
        DisasterVictim personTwo = new DisasterVictim("Jane", "McEwan", "2024-02-20");
        LinkedList<DisasterVictim> newOccupants = new LinkedList<>();
        newOccupants.add(personOne);
        newOccupants.add(personTwo);

        testLocation.setOccupants(newOccupants);

        assertEquals("setOccupants() should change the value of occupants", newOccupants, testLocation.getOccupants());
    }

    @Test
    public void testAddAndRemoveOccupant() {
        DisasterVictim victim = new DisasterVictim("Emma", "Smith", "2024-01-01");
        testLocation.addOccupant(victim);

        assertTrue("addOccupants() should update occupants list", inListOccupants(victim));

        testLocation.removeOccupant(victim);
        assertFalse("removeOccupant() should update occupants list", inListOccupants(victim));
    }

    @Test
    public void testInvalidAddOccupantNull() {
        DisasterVictim victim = new DisasterVictim("Liam", "Johnson", "2020-05-11");

        boolean correctValueNull = false;
        String failureReasonNull = "no exception was thrown";

        try {
            testLocation.addOccupant(null);
        } catch (NullPointerException e) {
            correctValueNull = true;
        } catch (Exception e) {
            failureReasonNull = "the wrong type of exception was thrown";
        }

        String messageNull = "addOccupant() should throw an NullPointerException if null is tried to be added to occupants but " + failureReasonNull;

        assertTrue(messageNull, correctValueNull);
    }

    @Test
    public void testInvalidAddOccupantInList() {
        DisasterVictim victim = new DisasterVictim("Liam", "Johnson", "2020-05-11");

        boolean correctValueInList = false;
        String failureReasonInList = "no exception was thrown";

        try {
            testLocation.addOccupant(victim);
            testLocation.addOccupant(victim);
        } catch (IllegalArgumentException e) {
            correctValueInList = true;
        } catch (Exception e) {
            failureReasonInList = "the wrong type of exception was thrown";
        }

        String messageInList = "addOccupant() should throw an IllegalArgumentException if occupant is already in location but " + failureReasonInList;

        assertTrue(messageInList, correctValueInList);
    }

    @Test
    public void testInvalidRemoveOccupantNull() {
        DisasterVictim victim = new DisasterVictim("Liam", "Johnson", "2020-05-11");

        boolean correctValueNull = false;
        String failureReasonNull = "no exception was thrown";

        try {
            testLocation.removeOccupant(null);
        } catch (NullPointerException e) {
            correctValueNull = true;
        } catch (Exception e) {
            failureReasonNull = "the wrong type of exception was thrown";
        }

        String messageNull = "removeOccupant() should throw an NullPointerException if null is tried to be removed to occupants but " + failureReasonNull;

        assertTrue(messageNull, correctValueNull);
    }

    @Test
    public void testInvalidRemoveOccupantInList() {
        DisasterVictim victim = new DisasterVictim("Liam", "Johnson", "2020-05-11");

        boolean correctValueInList = false;
        String failureReasonInList = "no exception was thrown";

        try {
            testLocation.removeOccupant(victim);
        } catch (IllegalArgumentException e) {
            correctValueInList = true;
        } catch (Exception e) {
            failureReasonInList = "the wrong type of exception was thrown";
        }

        String messageInList = "removeOccupant() should throw an IllegalArgumentException if occupant is not in location but " + failureReasonInList;

        assertTrue(messageInList, correctValueInList);
    }

    @Test
    public void testAddAndRemoveSupply() {
        Supply supply = new Supply("Papaya", 100);
        testLocation.addSupply(supply);

        assertTrue("addSupply() should update supplies list", inListSupply(supply));

        testLocation.removeSupply(supply);
        assertFalse("removeSupply() should update supplies list", inListSupply(supply));
    }

    @Test
    public void testInvalidAddSupply() {
        boolean correctValue = false;
        String failureReason = "no exception was thrown";
        try {
            testLocation.addSupply(null);
        } catch (NullPointerException e) {
            correctValue = true;
        } catch (Exception e) {
            failureReason = "the wrong type of exception was thrown";
        }

        String message = "addSupply() should throw a NullPointerException if supply provided is null but " + failureReason;
        assertTrue(message, correctValue);
    }

    @Test
    public void testInvalidRemoveSupplyNull() {
        boolean correctValueNull = false;
        String failureReasonNull = "no exception was thrown";

        try {
            testLocation.removeSupply(null);
        } catch (NullPointerException e) {
            correctValueNull = true;
        } catch (Exception e) {
            failureReasonNull = "the wrong type of exception was thrown";
        }

        String messageNull = "removeSupply() should throw an NullPointerException if null is tried to be removed from supplies but " + failureReasonNull;

        assertTrue(messageNull, correctValueNull);
    }

    @Test
    public void testInvalidRemoveSupplyInList() {
        Supply invalidSupply = new Supply("Random", 5);

        boolean correctValueInList = false;
        String failureReasonInList = "no exception was thrown";

        try {
            testLocation.removeSupply(invalidSupply);
        } catch (IllegalArgumentException e) {
            correctValueInList = true;
        } catch (Exception e) {
            failureReasonInList = "the wrong type of exception was thrown";
        }

        String messageInList = "removeSupply() should throw an IllegalArgumentException if supply is not in location but " + failureReasonInList;

        assertTrue(messageInList, correctValueInList);
    }

    @Test
    public void testInvalidRemoveSupplyNegative() {
        Supply invalidSupply = new Supply("Random", 5);

        boolean correctValueNegative = false;
        String failureReasonNegative = "no exception was thrown";

        try {
            testLocation.addSupply(invalidSupply);
            testLocation.removeSupply(new Supply("Random", 20));
        } catch (IllegalArgumentException e) {
            correctValueNegative = true;
        } catch (Exception e) {
            failureReasonNegative = "the wrong type of exception was thrown";
        }

        String messageNegative = "removeSupply() should throw an IllegalArgumentException if resulting supply will give a negative amount but " + failureReasonNegative;

        assertTrue(messageNegative, correctValueNegative);
    }

    /**
     * Checks if the specified supply is present in the list of supplies.
     *
     * @param elementToFind The supply to search for.
     * @return true if the supply is found in the list, otherwise false.
     */
    private boolean inListSupply(Supply elementToFind) {
        for (Supply element : testLocation.getSupplies()) {
            // Check if both type and other attributes match
            if (element.equals(elementToFind)) {
                return true;
            }
        }
        return false;
    }

    /**
     * Checks if the specified occupant is present in the list of occupants.
     *
     * @param elementToFind The occupant to search for.
     * @return true if elementToFind is in occupants
     */
    private boolean inListOccupants(DisasterVictim elementToFind) {
        for (DisasterVictim element : testLocation.getOccupants()) {
            if (element.getAssignedSocialID() == elementToFind.getAssignedSocialID()) {
                return true;
            }
        }
        return false;
    }
}

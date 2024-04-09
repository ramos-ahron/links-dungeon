package edu.ucalgary.oop;

import org.junit.Test;

import java.util.LinkedList;

import static org.junit.Assert.*;

public class LocationReliefWorkerTest {
    private final LocationReliefWorker testLocationReliefWorker = new LocationReliefWorker();

    @Test
    public void testObjectCreation() {
        assertNotNull(testLocationReliefWorker);
    }

    @Test
    public void testAddDisasterVictim() {
        DisasterVictim victim = new DisasterVictim("Random1", "Name1", "2020-02-20");

        Location shelter = new Location("Test", "Location");

        ReliefService.getShelters().clear();
        ReliefService.addShelter(shelter);

        // should not be missing but in location
        testLocationReliefWorker.addDisasterVictim(victim, shelter);

        assertTrue("addDisasterVictim() should add " + victim + " to location", inListMissingPerson(shelter.getOccupants(), victim));
        assertFalse("addDisasterVictim() should not add " + victim + " to missingPeople since " + shelter + " is a valid location", inListMissingPerson(ReliefService.getMissingPeople(), victim));
    }

    @Test
    public void testAddDisasterVictimMissing() {
        DisasterVictim victim = new DisasterVictim("Random2", "Name2", "2020-02-20");

        Location location = new Location("Random", "Shelter");

        testLocationReliefWorker.addDisasterVictim(victim, location);

        assertTrue("addDisasterVictim() should add " + victim + " to location", inListMissingPerson(location.getOccupants(), victim));
        assertTrue("addDisasterVictim() should not add " + victim + " to missingPeople since " + location + " is a valid location", inListMissingPerson(ReliefService.getMissingPeople(), victim));
    }

    @Test
    public void testRemoveDisasterVictim() {
        DisasterVictim victim = new DisasterVictim("Random1", "Name1", "2020-02-20");

        Location shelter = new Location("Test", "Location");

        ReliefService.getShelters().clear();
        ReliefService.addShelter(shelter);

        testLocationReliefWorker.addDisasterVictim(victim, shelter);

        testLocationReliefWorker.removeDisasterVictim(victim);

        assertTrue("removeDisasterVictim() should remove victim from shelter", shelter.getOccupants().isEmpty());
    }

    @Test
    public void testRemoveDisasterVictimMissing() {
        DisasterVictim victim = new DisasterVictim("Random3", "Name3", "2020-02-20");

        Location location = new Location("Random1", "Shelter1");

        testLocationReliefWorker.addDisasterVictim(victim, location);

        testLocationReliefWorker.removeDisasterVictim(victim);

        assertTrue("removeDisasterVictim() should remove victim from location", location.getOccupants().isEmpty());
        assertFalse("removeDisasterVictim() should remove victim from missingPeople", inListMissingPerson(ReliefService.getMissingPeople(), victim));
    }

    @Test
    public void testGiveSupplies() {
        Location testLocation = new Location("test", "location");

        ReliefService.addShelter(testLocation);

        testLocation.addSupply(new Supply("water", 10));

        DisasterVictim testVictim = new DisasterVictim("test", "victim", "2020-01-10");

        testLocationReliefWorker.addDisasterVictim(testVictim, testLocation);

        testLocationReliefWorker.giveSupplies(testVictim, new Supply("water", 4));

        assertEquals("Location should have their supplies deducted", 6, testLocation.getSupplies().get(0).getQuantity());
        assertEquals("Victim should have their personal belongings increased", 4, testVictim.getPersonalBelongings().get(0).getQuantity());
    }

    @Test
    public void testUpdateDisasterVictimLocation() {
        Location testLocation1 = new Location("test1", "location1");
        Location testLocation2 = new Location("test2", "location2");


        DisasterVictim testVictim = new DisasterVictim("test", "victim", "2020-01-10");

        ReliefService.getShelters().clear();
        ReliefService.addShelter(testLocation1);

        testLocationReliefWorker.addDisasterVictim(testVictim, testLocation1);
        testLocationReliefWorker.updateDisasterVictimLocation(testVictim, testLocation2);

        assertFalse("updateDisasterVictimLocation() should update the original location's occupants list", inListMissingPerson(testLocation1.getOccupants(), testVictim));
        assertEquals("updateDisasterVictim() should update the victim's location", testVictim.getLocation(), testLocation2);
        assertTrue("updateDisasterVictimLocation() should update the new location's occupants list", inListMissingPerson(testLocation2.getOccupants(), testVictim));
    }

    @Test
    public void testUpdateDisasterVictimLocationMissing() {
        Location testLocation1 = new Location("test1", "location1");
        Location testLocation2 = new Location("test2", "location2");


        DisasterVictim testVictim = new DisasterVictim("test", "victim", "2020-01-10");

        ReliefService.getShelters().clear();
        ReliefService.getMissingPeople().clear();
        ReliefService.addShelter(testLocation1);

        // victim originally not missing
        testLocationReliefWorker.addDisasterVictim(testVictim, testLocation1);

        testLocationReliefWorker.updateDisasterVictimLocation(testVictim, testLocation2);

        assertTrue("updateDisasterVictimLocation() should consider victim as missing after changing its location to another location that is not considered a shelter", inListMissingPerson(ReliefService.getMissingPeople(), testVictim));
    }

    @Test
    public void testUpdateDisasterVictimNotMissing() {
        Location testLocation1 = new Location("test1", "location1");
        Location testLocation2 = new Location("test2", "location2");


        DisasterVictim testVictim = new DisasterVictim("test", "victim", "2020-01-10");

        ReliefService.getShelters().clear();
        ReliefService.getMissingPeople().clear();
        ReliefService.addShelter(testLocation1);

        // victim originally missing
        testLocationReliefWorker.addDisasterVictim(testVictim, testLocation2);

        testLocationReliefWorker.updateDisasterVictimLocation(testVictim, testLocation1);

        assertFalse("updateDisasterVictimLocation() should consider victim as not missing after changing its location to another location that is considered a shelter", inListMissingPerson(ReliefService.getMissingPeople(), testVictim));
    }

    @Test
    public void testInvalidUpdateDisasterVictimLocation() {
        Location testLocation1 = new Location("test1", "location1");
        Location testLocation2 = new Location("test1", "location1");


        DisasterVictim testVictim = new DisasterVictim("test", "victim", "2020-01-10");

        ReliefService.getShelters().clear();
        ReliefService.getMissingPeople().clear();
        ReliefService.addShelter(testLocation1);

        testLocationReliefWorker.addDisasterVictim(testVictim, testLocation1);

        boolean correctValue = false;
        String failureReason = "no exception was thrown";

        try {
            testLocationReliefWorker.updateDisasterVictimLocation(testVictim, testLocation2);
        } catch (IllegalArgumentException e) {
            correctValue = true;
        } catch (Exception e) {
            failureReason = "the wrong type of exception was thrown";
        }

        String message = "updateDisasterVictimLocation() should throw a IllegalArgumentException if location provided is the same as previous location but " + failureReason;
        assertTrue(message, correctValue);
    }

    @Test
    public void testAddDisasterVictimMedicalRecord() {
        MedicalRecord testMedicalRecord = new MedicalRecord(new Location("test", "address"));

        DisasterVictim testVictim = new DisasterVictim("Random", "Name", "2023-03-28");

        testLocationReliefWorker.addDisasterVictimMedicalRecord(testVictim, testMedicalRecord);

        assertEquals("addDisasterVictimMedicalRecord() should add medical record to victim's list of medical records", testVictim.getMedicalRecords().get(0), testMedicalRecord);
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

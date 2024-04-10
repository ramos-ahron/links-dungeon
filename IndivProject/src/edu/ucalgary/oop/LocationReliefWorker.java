package edu.ucalgary.oop;

public class LocationReliefWorker extends ReliefService {
    /**
     * Constructs a new LocationReliefWorker instance.
     */
    public LocationReliefWorker() {
    }


    /**
     * Adds the specified disaster victim to the provided location and updates relevant records.
     *
     * @param victim   The disaster victim to be added.
     * @param location The location where the victim will be placed.
     */
    public void addDisasterVictim(DisasterVictim victim, Location location) {
        location.addOccupant(victim);
        victim.setLocation(location);
        addPerson(victim);

        // If location is not in shelters, consider victim as missing
        if (inListShelter(location) == null) {
            addMissingPerson(victim);
        }

        if (inListLocation(location) == null) {
            addLocation(location);
        }
    }


    /**
     * Removes the specified disaster victim from their current location and updates relevant records.
     *
     * @param victim The disaster victim to be removed.
     */
    public void removeDisasterVictim(DisasterVictim victim) {
        victim.getLocation().removeOccupant(victim);
        removePerson(victim);
        for (FamilyRelation familyRelation : victim.getFamilyConnections()) {
            victim.removeFamilyRelationship(familyRelation.getPersonTwo(), familyRelation.getRelationshipType());
        }
        try {
            // Remove from missingPeople if missing
            removeMissingPerson(victim);
        } catch (IllegalArgumentException ignored) {

        }
        try {
            // Remove from missingPeople if missing
            removePerson(victim);
        } catch (IllegalArgumentException ignored) {

        }
    }


    /**
     * Gives supplies to the specified disaster victim, adding them to their personal belongings.
     *
     * @param victim The disaster victim to whom the supplies will be given.
     * @param supply The supply item to be given to the victim.
     * @throws IllegalArgumentException If the victim is not currently located in a valid shelter.
     */
    public void giveSupplies(DisasterVictim victim, Supply supply) throws IllegalArgumentException {
        if (inListLocation(victim.getLocation()) == null) {
            throw new IllegalArgumentException("Disaster victim is not in a valid shelter");
        }
        victim.getLocation().removeSupply(supply);
        victim.addPersonalBelonging(supply);
    }


    /**
     * Updates the location of the specified disaster victim to the new location provided.
     *
     * @param victim      The disaster victim whose location is being updated.
     * @param newLocation The new location to which the victim will be moved.
     * @throws IllegalArgumentException If the new location is the same as the current location of the victim.
     */
    public void updateDisasterVictimLocation(DisasterVictim victim, Location newLocation) throws IllegalArgumentException {
        if (victim.getLocation().getName().equals(newLocation.getName()) && victim.getLocation().getAddress().equals(newLocation.getAddress())) {
            throw new IllegalArgumentException("New location cannot be the same as old location");
        }

        victim.getLocation().removeOccupant(victim);
        victim.setLocation(newLocation);
        newLocation.addOccupant(victim);

        // If newLocation is not a shelter, consider as missing
        if (inListLocation(newLocation) == null) {
            try {
                addMissingPerson(victim);
            } catch (IllegalArgumentException ignored) {

            }
        } else {
            // If newLocation is shelter, consider as not missing
            try {
                removeMissingPerson(victim);
            } catch (IllegalArgumentException ignored) {

            }
        }
    }


    /**
     * Adds a medical record to the specified disaster victim.
     *
     * @param victim        The disaster victim to whom the medical record will be added.
     * @param medicalRecord The medical record to be added to the victim.
     */
    public void addDisasterVictimMedicalRecord(DisasterVictim victim, MedicalRecord medicalRecord) {
        victim.addMedicalRecord(medicalRecord);
    }
}

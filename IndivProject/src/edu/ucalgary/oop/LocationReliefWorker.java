package edu.ucalgary.oop;

public class LocationReliefWorker extends ReliefService {
    public LocationReliefWorker() {}

    public void addDisasterVictim(DisasterVictim victim, Location location) {
        location.addOccupant(victim);
        victim.setLocation(location);

        // If location is not in shelters, consider victim as missing
        if (inListLocation(location) == null) {
            addMissingPerson(victim);
        }

        /*
          TODO: Connect this to database
         */
    }

    public void removeDisasterVictim(DisasterVictim victim) {
        victim.getLocation().removeOccupant(victim);
        try {
            // remove from missingPeople if missing
            removeMissingPerson(victim);
        } catch (IllegalArgumentException ignored) {

        }
        /*
            TODO: Connect this to database
         */
    }

    public void giveSupplies(DisasterVictim victim, Supply supply) throws IllegalArgumentException {
        if (inListLocation(victim.getLocation()) == null) { // If missing, cannot give supplies
            throw new IllegalArgumentException("Disaster victim is not in a valid shelter");
        }
        victim.getLocation().removeSupply(supply);
        victim.addPersonalBelonging(supply);
        /*
            TODO: Connect this to database
         */
    }

    public void updateDisasterVictimLocation(DisasterVictim victim, Location newLocation) throws IllegalArgumentException {
        // Make sure that new location is not the same as old location
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
        /*
            TODO: Connect this to database
         */
    }

    public void addDisasterVictimMedicalRecord(DisasterVictim victim, MedicalRecord medicalRecord) {
        victim.addMedicalRecord(medicalRecord);
        /*
            TODO: Connect this to database
         */
    }
}

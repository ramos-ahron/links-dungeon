package edu.ucalgary.oop;

public class LocationReliefWorker extends ReliefService {
    public LocationReliefWorker() {
        super();
    }

    public void addMissingPerson(DisasterVictim missingPerson, Location lastKnownLocation) {
        /*
          TODO: Connect this to database
         */
    }

    public void addDisasterVictim(DisasterVictim victim, Location location) throws IllegalArgumentException {
        if (inList(location) != null) {
            location.addOccupant(victim);
            /*
              TODO: Connect this to database
             */
        } else {
            throw new IllegalArgumentException("Disaster victim is not in a valid shelter");
        }
    }

    public void removeDisasterVictim(DisasterVictim victim) {
        victim.getShelter().removeOccupant(victim);
    }

    public void giveSupplies(DisasterVictim victim, Supply supply) throws IllegalArgumentException {
        if (inList(victim.getShelter()) == null) { // If missing, cannot give supplies
            throw new IllegalArgumentException("Disaster victim is not in a valid shelter");
        }
        victim.getShelter().removeSupply(supply);
        victim.addPersonalBelonging(supply);
    }

    public void updateDisasterVictimLocation(DisasterVictim victim, Location newLocation) {
        victim.setShelter(newLocation);
    }

    public void addDisasterVictimMedicalRecord(DisasterVictim victim, MedicalRecord medicalRecord) {
        victim.addMedicalRecord(medicalRecord);
    }
}

package edu.ucalgary.oop;

import java.sql.*;

public class LocationReliefWorker extends ReliefService {
    /**
     * Constructs a new LocationReliefWorker instance.
     */
    public LocationReliefWorker() {}


    /**
     * Adds the specified disaster victim to the provided location and updates relevant records.
     *
     * @param victim The disaster victim to be added.
     * @param location The location where the victim will be placed.
     */
    public void addDisasterVictim(DisasterVictim victim, Location location) {
        location.addOccupant(victim);
        victim.setLocation(location);
        addPerson(victim);

        // If location is not in shelters, consider victim as missing
        if (inListLocation(location) == null) {
            addMissingPerson(victim);
        }

        int locationId = 0;
        DatabaseInitializer.createConnection();
        try {
            String query = "SELECT location_id \n" +
                    "FROM Location \n" +
                    "WHERE name = ? AND address = ?";
            PreparedStatement myStmt = DatabaseInitializer.dbConnect.prepareStatement(query);
            myStmt.setString(1, location.getName());
            myStmt.setString(2, location.getAddress());
            ResultSet resultSet = myStmt.executeQuery();

            if (resultSet.next()) {
                locationId = resultSet.getInt("location_id");
            }
            String insertQuery = "INSERT INTO DisasterVictim (id, first_name, last_name, entry_date, age, gender, comments, date_of_birth, location_id) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)";
            PreparedStatement insertStmt = DatabaseInitializer.dbConnect.prepareStatement(insertQuery);

            insertStmt.setInt(1, victim.getAssignedSocialID());
            insertStmt.setString(2, victim.getFirstName());
            insertStmt.setString(3, victim.getLastName());
            insertStmt.setString(4, victim.getEntryDate());
            insertStmt.setInt(5, victim.getAge());
            insertStmt.setString(6, victim.getGender());
            insertStmt.setString(7, victim.getComments());
            insertStmt.setString(8, victim.getDateOfBirth());
            insertStmt.setInt(9, locationId);

            insertStmt.executeUpdate();
        } catch (SQLException e) {
            e.printStackTrace();
        }
        DatabaseInitializer.close();
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
        DatabaseInitializer.createConnection();
        try {
            Statement myStmt = DatabaseInitializer.dbConnect.createStatement();
            String deleteQuery = "DELETE FROM DisasterVictim WHERE victim_id = ?";
            PreparedStatement deleteStmt = DatabaseInitializer.dbConnect.prepareStatement(deleteQuery);
            deleteStmt.setInt(1, victim.getAssignedSocialID());
            deleteStmt.executeUpdate();
        } catch (SQLException e) {
            e.printStackTrace();
        }
        DatabaseInitializer.close();
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
     * @param victim The disaster victim whose location is being updated.
     * @param newLocation The new location to which the victim will be moved.
     * @throws IllegalArgumentException If the new location is the same as the current location of the victim.
     */
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


    /**
     * Adds a medical record to the specified disaster victim.
     *
     * @param victim The disaster victim to whom the medical record will be added.
     * @param medicalRecord The medical record to be added to the victim.
     */
    public void addDisasterVictimMedicalRecord(DisasterVictim victim, MedicalRecord medicalRecord) {
        victim.addMedicalRecord(medicalRecord);
    /*
        TODO: Connect this to database
     */
    }
}

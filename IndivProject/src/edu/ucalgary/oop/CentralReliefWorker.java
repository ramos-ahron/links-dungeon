package edu.ucalgary.oop;

import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.ArrayList;

public class CentralReliefWorker extends ReliefService {
    private static final ArrayList<Inquirer> inquirers = new ArrayList<>();

    public CentralReliefWorker() {
        super();
    }

    public void addInquirer(Inquirer inquirer, Inquiry inquiry) {
        Inquirer inquirer2 = null;
        for (Inquirer inquirer1 : inquirers) {
            if (inquirer1.getFirstName().equals(inquirer.getFirstName()) && inquirer1.getPhoneNumber().equals(inquirer.getPhoneNumber())) {
                inquirer2 = inquirer1;
            }
        }
        if (inquirer2 == null) {
            inquirer2 = inquirer;
            inquirers.add(inquirer2);
        }
        try {
            inquirer2.getInquiries().addInquirer(inquiry);
        } catch (IllegalArgumentException ignored) {

        }
    }

    public String findDisasterVictim(String firstNamePattern, String lastNamePattern) {
        StringBuilder message = new StringBuilder();
        try {
            DatabaseInitializer.createConnection();

            String query = "SELECT * FROM DisasterVictim WHERE first_name LIKE ? OR last_name LIKE ?";
            PreparedStatement statement = DatabaseInitializer.dbConnect.prepareStatement(query);

            statement.setString(1, "%" + firstNamePattern + "%");
            statement.setString(2, "%" + lastNamePattern + "%");
            ResultSet resultSet = statement.executeQuery();

            while (resultSet.next()) {
                for (DisasterVictim victim : getPeople()) {
                    if (victim.getAssignedSocialID() == resultSet.getInt("victim_id")) {
                        message.append(victim.getInfo());
                    }
                }
            }

            if (message.length() == 0) {
                message.append("There are no victims with the given name pattern");
            }
            DatabaseInitializer.close();
        } catch (SQLException e) {
            e.printStackTrace();
        }
        return message.toString();
    }

    public String findDisasterVictim(String firstNamePattern) {
        StringBuilder message = new StringBuilder();
        try {
            DatabaseInitializer.createConnection();

            String query = "SELECT * FROM DisasterVictim WHERE first_name LIKE ?";
            PreparedStatement statement = DatabaseInitializer.dbConnect.prepareStatement(query);

            statement.setString(1, "%" + firstNamePattern + "%");
            ResultSet resultSet = statement.executeQuery();

            while (resultSet.next()) {
                for (DisasterVictim victim : getPeople()) {
                    if (victim.getAssignedSocialID() == resultSet.getInt("victim_id")) {
                        message.append(victim.getInfo());
                    }
                }
            }

            if (message.length() == 0) {
                message.append("There are no victims with the given name pattern");
            }
            DatabaseInitializer.close();
        } catch (SQLException e) {
            e.printStackTrace();
        }
        return message.toString();
    }

    public String getRelationships(DisasterVictim victim) {
        StringBuilder message = new StringBuilder();
        for (FamilyRelation relation : victim.getFamilyConnections()) {
            message.append(victim.getFirstName()).append(" ").append(relation.getRelationshipType()).append(" ").append(relation.getPersonTwo().getFirstName()).append("\n\n");
        }
        if (message.length() == 0) {
            message.append("Victim has no recorded relationships");
        }
        return message.toString();
    }
}

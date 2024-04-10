package edu.ucalgary.oop;

import java.sql.*;
import java.util.ArrayList;

public class DatabaseInitializer {
    public static Connection dbConnect;
    public static ResultSet results;

    public static void main(String[] args) {
    }

    /**
     * Retrieves information about all the inquirers stored in the database.
     * This method establishes a database connection, executes a SQL query to select
     * all records from the INQUIRER table, and retrieves the following information
     * for each inquirer: ID, first name, last name, and phone number.
     * The retrieved information is stored in an ArrayList of ArrayLists of Strings.
     * Each inner ArrayList represents the information for a single inquirer,
     * where the elements are arranged in the following order:
     * [ID, first name, last name, phone number].
     *
     * @return an ArrayList containing information about all the inquirers in the database,
     * where each inner ArrayList represents the information for a single inquirer
     * and contains the ID, first name, last name, and phone number of the inquirer
     */
    public static ArrayList<ArrayList<String>> getInquirerInfo() {
        ArrayList<ArrayList<String>> inquirerInfo = new ArrayList<>();
        createConnection();
        try {
            Statement stmt = dbConnect.createStatement();
            ResultSet results = stmt.executeQuery("SELECT * FROM INQUIRER");
            while (results.next()) {
                ArrayList<String> info = new ArrayList<>();
                info.add(results.getString("id"));
                info.add(results.getString("firstName"));
                info.add(results.getString("lastName"));
                info.add(results.getString("phoneNumber"));
                inquirerInfo.add(info);
            }
            stmt.close();
        } catch (SQLException e) {
            e.printStackTrace();
        }
        close();
        return inquirerInfo;
    }

    /**
     * Retrieves information about all the inquiries logged in the database.
     * This method establishes a database connection, executes a SQL query to select
     * all records from the INQUIRY_LOG table, and retrieves the following information
     * for each inquiry log entry: ID, inquirer ID, call date, and details.
     * The retrieved information is stored in an ArrayList of ArrayLists of Strings.
     * Each inner ArrayList represents the information for a single inquiry log entry,
     * where the elements are arranged in the following order:
     * [ID, inquirer ID, call date, details].
     *
     * @return an ArrayList containing information about all the inquiry log entries in the database,
     * where each inner ArrayList represents the information for a single inquiry log entry
     * and contains the ID, inquirer ID, call date, and details of the inquiry
     */
    public static ArrayList<ArrayList<String>> getInquiryLogInfo() {
        ArrayList<ArrayList<String>> inquiryLogInfo = new ArrayList<>();
        createConnection();
        try {
            Statement stmt = dbConnect.createStatement();
            ResultSet results = stmt.executeQuery("SELECT * FROM INQUIRY_LOG");
            while (results.next()) {
                ArrayList<String> info = new ArrayList<>();
                info.add(results.getString("id"));
                info.add(results.getString("inquirer"));
                info.add(results.getString("callDate"));
                info.add(results.getString("details"));
                inquiryLogInfo.add(info);
            }
            stmt.close();
        } catch (SQLException e) {
            e.printStackTrace();
        }
        close();
        return inquiryLogInfo;
    }

    /**
     * Retrieves information about dietary restrictions recorded in the database.
     * This method establishes a database connection, executes a SQL query to select
     * all records from the DietaryRestriction table, and retrieves the following information
     * for each dietary restriction entry: restriction name and victim ID.
     * The retrieved information is stored in an ArrayList of ArrayLists of Strings.
     * Each inner ArrayList represents the information for a single dietary restriction entry,
     * where the elements are arranged in the following order:
     * [restriction name, victim ID].
     *
     * @return an ArrayList containing information about all the dietary restriction entries in the database,
     * where each inner ArrayList represents the information for a single dietary restriction entry
     * and contains the restriction name and victim ID
     */
    public static ArrayList<ArrayList<String>> getDietaryRestrictionInfo() {
        ArrayList<ArrayList<String>> dietaryRestrictionInfo = new ArrayList<>();
        createConnection();
        try {
            Statement stmt = dbConnect.createStatement();
            results = stmt.executeQuery("SELECT * FROM DietaryRestriction");
            while (results.next()) {
                ArrayList<String> info = new ArrayList<>();
                info.add(results.getString("restriction_name"));
                info.add(results.getString("victim_id"));
                dietaryRestrictionInfo.add(info);
            }
            stmt.close();
        } catch (SQLException e) {
            e.printStackTrace();
        }
        close();
        return dietaryRestrictionInfo;
    }

    /**
     * Retrieves information about relationships recorded in the database.
     * This method establishes a database connection, executes a SQL query to select
     * all records from the Relationship table, and retrieves the following information
     * for each relationship entry: relationship type, victim1 ID, and victim2 ID.
     * The retrieved information is stored in an ArrayList of ArrayLists of Strings.
     * Each inner ArrayList represents the information for a single relationship entry,
     * where the elements are arranged in the following order:
     * [relationship type, victim1 ID, victim2 ID].
     *
     * @return an ArrayList containing information about all the relationship entries in the database,
     * where each inner ArrayList represents the information for a single relationship entry
     * and contains the relationship type, victim1 ID, and victim2 ID
     */
    public static ArrayList<ArrayList<String>> getRelationshipInfo() {
        ArrayList<ArrayList<String>> relationshipInfo = new ArrayList<>();
        createConnection();
        try {
            Statement stmt = dbConnect.createStatement();
            results = stmt.executeQuery("SELECT * FROM Relationship");
            while (results.next()) {
                ArrayList<String> info = new ArrayList<>();
                info.add(results.getString("relationship_type"));
                info.add(results.getString("victim1_id"));
                info.add(results.getString("victim2_id"));
                relationshipInfo.add(info);
            }
            stmt.close();
        } catch (SQLException e) {
            e.printStackTrace();
        }
        close();
        return relationshipInfo;
    }

    /**
     * Retrieves information about medical records recorded in the database.
     * This method establishes a database connection, executes a SQL query to select
     * medical records along with related information from the MedicalRecord table,
     * and retrieves the following information for each medical record entry: treatment details,
     * date of treatment, victim ID, location name, and location address.
     * The retrieved information is stored in an ArrayList of ArrayLists of Strings.
     * Each inner ArrayList represents the information for a single medical record entry,
     * where the elements are arranged in the following order:
     * [treatment details, date of treatment, victim ID, location name, location address].
     *
     * @return an ArrayList containing information about all the medical record entries in the database,
     * where each inner ArrayList represents the information for a single medical record entry
     * and contains the treatment details, date of treatment, victim ID, location name, and location address
     */
    public static ArrayList<ArrayList<String>> getMedicalRecordInfo() {
        ArrayList<ArrayList<String>> medicalRecordInfo = new ArrayList<>();
        createConnection();
        try {
            Statement stmt = dbConnect.createStatement();
            results = stmt.executeQuery("SELECT \n" +
                    "    mr.treatment_details,\n" +
                    "    mr.date_of_treatment,\n" +
                    "    dv.victim_id,\n" +
                    "    loc.name AS location_name,\n" +
                    "    loc.address AS location_address\n" +
                    "FROM \n" +
                    "    MedicalRecord mr\n" +
                    "JOIN \n" +
                    "    DisasterVictim dv ON mr.victim_id = dv.victim_id\n" +
                    "JOIN \n" +
                    "    Location loc ON mr.location_id = loc.location_id");
            while (results.next()) {
                ArrayList<String> info = new ArrayList<>();
                info.add(results.getString("treatment_details"));
                info.add(results.getString("date_of_treatment"));
                info.add(results.getString("victim_id"));
                info.add(results.getString("location_name"));
                info.add(results.getString("location_address"));
                medicalRecordInfo.add(info);
            }
            stmt.close();
        } catch (SQLException e) {
            e.printStackTrace();
        }
        close();
        return medicalRecordInfo;
    }

    /**
     * Retrieves information about locations recorded in the database.
     * This method establishes a database connection, executes a SQL query to select
     * names and addresses of locations from the Location table,
     * and retrieves the following information for each location entry: name and address.
     * The retrieved information is stored in an ArrayList of ArrayLists of Strings.
     * Each inner ArrayList represents the information for a single location entry,
     * where the elements are arranged in the following order: [name, address].
     *
     * @return an ArrayList containing information about all the location entries in the database,
     * where each inner ArrayList represents the information for a single location entry
     * and contains the name and address of the location
     */
    public static ArrayList<ArrayList<String>> getLocationInfo() {
        ArrayList<ArrayList<String>> locationInfo = new ArrayList<>();
        createConnection();
        try {
            Statement stmt = dbConnect.createStatement();
            results = stmt.executeQuery("SELECT * FROM Location");
            while (results.next()) {
                ArrayList<String> info = new ArrayList<>();
                info.add(results.getString("name"));
                info.add(results.getString("address"));
                info.add(results.getString("shelter"));
                locationInfo.add(info);
            }
            stmt.close();
        } catch (SQLException e) {
            e.printStackTrace();
        }
        close();
        return locationInfo;
    }

    /**
     * Retrieves information about disaster victims recorded in the database.
     * This method establishes a database connection, executes a SQL query to select
     * various details of disaster victims from the DisasterVictim table,
     * including victim ID, first name, last name, entry date, age, gender, comments, date of birth,
     * as well as the name and address of the location where the victim is located.
     * The retrieved information is stored in an ArrayList of ArrayLists of Strings.
     * Each inner ArrayList represents the information for a single victim entry,
     * where the elements are arranged in the following order:
     * [victim_id, first_name, last_name, entry_date, age, gender, comments, date_of_birth, location_name, location_address].
     *
     * @return an ArrayList containing information about all the disaster victim entries in the database,
     * where each inner ArrayList represents the information for a single victim entry
     * and contains various details about the victim and their location
     */
    public static ArrayList<ArrayList<String>> getDisasterVictimInfo() {
        createConnection();
        ArrayList<ArrayList<String>> victimInfo = new ArrayList<>();
        try {
            Statement stmt = dbConnect.createStatement();
            results = stmt.executeQuery("SELECT \n" +
                    "    dv.victim_id, \n" +
                    "    dv.first_name, \n" +
                    "    dv.last_name, \n" +
                    "    dv.entry_date, \n" +
                    "    dv.age, \n" +
                    "    dv.gender, \n" +
                    "    dv.comments, \n" +
                    "    dv.date_of_birth, \n" +
                    "    loc.name AS location_name, \n" +
                    "    loc.address AS location_address\n" +
                    "FROM \n" +
                    "    DisasterVictim dv\n" +
                    "JOIN \n" +
                    "    Location loc ON dv.location_id = loc.location_id");
            while (results.next()) {
                ArrayList<String> info = new ArrayList<>();
                info.add(results.getString("victim_id"));
                info.add(results.getString("first_name"));
                info.add(results.getString("last_name"));
                info.add(results.getString("entry_date"));
                info.add(results.getString("age"));
                info.add(results.getString("gender"));
                info.add(results.getString("comments"));
                info.add(results.getString("date_of_birth"));
                info.add(results.getString("location_name"));
                info.add(results.getString("location_address"));

                victimInfo.add(info);
            }
            stmt.close();
        } catch (SQLException e) {
            e.printStackTrace();
        }
        close();
        return victimInfo;
    }

    /**
     * Retrieves information about supplies recorded in the database.
     * This method establishes a database connection, executes a SQL query to select
     * details of supplies from the Supply table, including supply ID, type, quantity,
     * reference type (whether it is associated with a location or a victim),
     * the name and address of the location (if applicable), and the victim ID (if applicable).
     * The retrieved information is stored in an ArrayList of ArrayLists of Strings.
     * Each inner ArrayList represents the information for a single supply entry,
     * where the elements are arranged in the following order:
     * [supply_id, type, quantity, reference_type, location_name, location_address, victim_id].
     *
     * @return an ArrayList containing information about all the supply entries in the database,
     * where each inner ArrayList represents the information for a single supply entry
     * and contains various details about the supply and its associated location or victim
     */
    public static ArrayList<ArrayList<String>> getSupplyInfo() {
        createConnection();
        ArrayList<ArrayList<String>> supplyInfo = new ArrayList<>();

        try {
            Statement stmt = dbConnect.createStatement();
            results = stmt.executeQuery("SELECT s.supply_id, s.type, s.quantity, s.reference_type, \n" +
                    "       l.name AS location_name, l.address AS location_address,\n" +
                    "       dv.victim_id, dv.first_name AS victim_first_name\n" +
                    "FROM Supply s\n" +
                    "LEFT JOIN Location l ON s.reference_id = l.location_id AND s.reference_type = 'Location'\n" +
                    "LEFT JOIN DisasterVictim dv ON s.reference_id = dv.victim_id AND s.reference_type = 'Victim';\n");

            while (results.next()) {
                ArrayList<String> info = new ArrayList<>();
                info.add(results.getString("supply_id"));
                info.add(results.getString("type"));
                info.add(results.getString("quantity"));
                info.add(results.getString("reference_type"));
                info.add(results.getString("location_name"));
                info.add(results.getString("location_address"));
                info.add(results.getString("victim_id"));

                supplyInfo.add(info);
            }
            stmt.close();

        } catch (SQLException e) {
            e.printStackTrace();
        }

        close();
        return supplyInfo;
    }

    /**
     * Establishes a connection to the PostgreSQL database used for the project.
     * This method uses JDBC to connect to the specified database URL with the provided
     * username and password.
     */
    public static void createConnection() {
        try {
            dbConnect = DriverManager.getConnection("jdbc:postgresql://localhost/ensf380project", "oop", "ucalgary");
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }

    /**
     * Closes the database connection and any associated resources such as result sets.
     * This method is responsible for closing the database connection and the result set
     * if they are not null. It catches any SQL exceptions that might occur during the
     * closing process and prints their stack traces.
     */
    public static void close() {
        try {
            if (results != null) {
                results.close();
            }
            if (dbConnect != null) {
                dbConnect.close();
            }
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }
}

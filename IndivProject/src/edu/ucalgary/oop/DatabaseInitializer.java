package edu.ucalgary.oop;

import java.sql.*;
import java.util.ArrayList;

public class DatabaseInitializer {
    private static Connection dbConnect;
    private static ResultSet results;

    public static void main(String[] args) {
    }

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

    public static ArrayList<ArrayList<String>> getLocationInfo() {
        ArrayList<ArrayList<String>> locationInfo = new ArrayList<>();
        createConnection();
        try {
            Statement stmt = dbConnect.createStatement();
            results = stmt.executeQuery("SELECT name, address FROM Location");
            while (results.next()) {
                ArrayList<String> info = new ArrayList<>();
                info.add(results.getString("name"));
                info.add(results.getString("address"));
                locationInfo.add(info);
            }
            stmt.close();
        } catch (SQLException e) {
            e.printStackTrace();
        }
        close();
        return locationInfo;
    }

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

    public static void createConnection() {
        try {
            dbConnect = DriverManager.getConnection("jdbc:postgresql://localhost/ensf380project", "oop", "ucalgary");
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }

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

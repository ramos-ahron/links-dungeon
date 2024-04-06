package edu.ucalgary.oop;

import java.sql.*;
import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

public class DatabaseManager {
    private final SQLQueryRunner queryRunner;
    private Connection dbConnect;
    private ResultSet results;

    public DatabaseManager() {
        queryRunner = new SQLQueryRunner("ensf380project");
    }

    public static void main(String[] args) {
        DatabaseManager test = new DatabaseManager();
        test.createConnection();

        // Example usage
        System.out.println(test.selectInquirer());

        test.close();
    }


    /**
     * Executes a SQL query using the SQLQueryRunner.
     *
     * @param query The SQL query to execute.
     * @return The number of rows affected by the query, -1 if failed.
     */
    public int executeQuery(String query) {
        int rowCount = -1;
        try {
            PreparedStatement statement = dbConnect.prepareStatement(query);
            rowCount = queryRunner.executeQuery(statement);
        } catch (SQLException ex) {
            ex.printStackTrace();
        }
        return rowCount;
    }

    /**
     * Retrieves inquirer information from the database.
     *
     * @return A StringBuffer containing inquirer info
     */
    public StringBuffer selectInquirer() {
        StringBuffer nameAndPhone = new StringBuffer();

        try {
            Statement myStmt = dbConnect.createStatement();
            results = myStmt.executeQuery("SELECT firstName, lastName, phoneNumber FROM inquirer");

            while (results.next()) {
                String firstName = results.getString("firstName");
                String lastName = results.getString("lastName");
                String phoneNumber = results.getString("phoneNumber");

                nameAndPhone.append(firstName);
                if (lastName != null) {
                    nameAndPhone.append(" ").append(lastName);
                }
                nameAndPhone.append(", ").append(phoneNumber).append('\n');
            }
        } catch (SQLException ex) {
            ex.printStackTrace();
        }
        return nameAndPhone;
    }

    /**
     * Retrieves inquirer and inquiry log information from the database.
     *
     * @return A StringBuffer containing inquirer and inquiry log info
     */
    public StringBuffer selectInquiryLog() {
        StringBuffer info = new StringBuffer();

        try {
            Statement myStmt = dbConnect.createStatement();
            results = myStmt.executeQuery("SELECT i.firstName, i.phoneNumber, i.lastName, l.callDate, l.details " +
                    "FROM INQUIRER i " +
                    "JOIN INQUIRY_LOG l ON i.id = l.inquirer");

            while (results.next()) {
                String firstName = results.getString("firstName");
                String phoneNumber = results.getString("phoneNumber");
                String lastName = results.getString("lastName");
                String callDate = results.getString("callDate");
                String details = results.getString("details");

                info.append(firstName);
                if (lastName != null) {
                    info.append(" ").append(lastName);
                }
                info.append(", ").append(phoneNumber).append(", ").append(callDate).append(", ").append(details).append('\n');
            }
        } catch (SQLException ex) {
            ex.printStackTrace();
        }
        return info;
    }

    private void createConnection() {
        try {
            dbConnect = DriverManager.getConnection("jdbc:postgresql://localhost/ensf380project", "oop", "ucalgary");
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }

    /**
     * Closes the connection and result set.
     */
    public void close() {
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

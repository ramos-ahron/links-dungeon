package edu.ucalgary.oop;

import java.sql.*;

public class SQLQueryRunner {
    private Connection dbConnect;

    private String projectName;

    /**
     * Constructor
     *
     * @param projectName The name of the project
     */
    public SQLQueryRunner(String projectName) {
        this.projectName = projectName;
    }

    /**
     * Gets Project Name
     * @return The name of the project that jdbc is connected to
     */
    public String getProjectName() {
        return projectName;
    }

    /**
     * Sets Project Name
     * @param projectName The name oy the project
     */
    public void setProjectName(String projectName) {
        this.projectName = projectName;
    }

    /**
     * Evecutes the statement
     * @param statement The statement to be executed
     * @return The number of rows affected, -1 if failed to execute
     */
    public int executeQuery(PreparedStatement statement) {
        int rowCount = -1;
        try {
            createConnection();
            rowCount = statement.executeUpdate();
            statement.close();
        } catch (SQLException ex) {
            ex.printStackTrace();
        } finally {
            close();
        }
        return rowCount;
    }

    /**
     * Creates a connection with the database ensf380project.
     */
    private void createConnection() {
        try {
            dbConnect = DriverManager.getConnection("jdbc:postgresql://localhost/" + projectName, "oop", "ucalgary");
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }

    /**
     * Closes the connection and result set.
     */
    public void close() {
        try {
            if (dbConnect != null) {
                dbConnect.close();
            }
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }
}
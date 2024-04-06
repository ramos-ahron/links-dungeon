package edu.ucalgary.oop;

import java.io.*;
import java.util.ArrayList;

public class GenderOption {
    private static ArrayList<String> options = new ArrayList<>();
    private static String filePath;

    /**
     * Constructor
     *
     * @param filePath The path to the file path
     */
    public GenderOption(String filePath) {
        GenderOption.filePath = filePath;
    }

    public static void main(String[] args) {
    }

    /**
     * Reads the .txt file and puts its contents into an ArrayList
     *
     * @return The ArrayList of all the genders
     * @throws IOException Throws exception if file does not exist
     */
    private ArrayList<String> readGenderOptions() throws IOException {
        ArrayList<String> genderOptions = new ArrayList<>();

        BufferedReader br = new BufferedReader(new FileReader(filePath));
        String line;
        while ((line = br.readLine()) != null) {
            line = line.trim();
            if (!line.isEmpty()) {
                genderOptions.add(line);
            }
        }

        return genderOptions;
    }

    /**
     * Writes the options ArrayList into filePath
     *
     * @throws IOException Throws exception if file does not exist
     */
    private void writeGenderOptions() throws IOException {
        // Check if the file exists
        File file = new File(filePath);
        if (!file.exists()) {
            throw new IOException("File not found: " + filePath);
        }

        // Proceed with writing options to the file
        try (BufferedWriter bw = new BufferedWriter(new FileWriter(filePath))) {
            for (String option : options) {
                bw.write(option);
                bw.newLine();
            }
        }
    }

    /**
     * Returns if gender is in options
     *
     * @param gender The gender to find
     * @return True if gender is in options, otherwise False
     */
    public boolean containsGender(String gender) {
        return options.contains(gender);
    }

    /**
     * @return Returns a String ArrayList of all the Genders in the provided filePath
     * @throws IOException Throws exception if file does not exist
     */
    public ArrayList<String> getOptions() throws IOException {
        options = readGenderOptions();
        return options;
    }

    /**
     * Updates the .txt file if a new ArrayList of Genders is provided through this function
     *
     * @param options The new ArrayList of String of Genders
     * @throws IOException Throws exception if file does not exist
     */
    public void setOptions(ArrayList<String> options) throws IOException {
        GenderOption.options = options;
        writeGenderOptions();
    }

    /**
     * @return The filePath provided
     */
    public String getFilePath() {
        return filePath;
    }

    /**
     * @param filePath The new filePath
     */
    public void setFilePath(String filePath) {
        GenderOption.filePath = filePath;
    }
}

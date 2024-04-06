package edu.ucalgary.oop;

import java.io.*;
import java.util.ArrayList;

public class GenderOptions {
    private static ArrayList<String> options = new ArrayList<>();
    private static String filePath;

    /**
     * Constructor
     *
     * @param filePath The path to the file path
     */
    public GenderOptions(String filePath) {
        GenderOptions.filePath = filePath;
    }

    public static void main(String[] args) {

        String fileName = "C:\\Users\\ahron\\OneDrive\\Desktop\\Files\\University\\ENSF 380\\Assignments\\I3\\IA3\\IndivProject\\src\\edu\\ucalgary\\oop\\GenderOptions.txt";
        GenderOptions test = new GenderOptions(fileName);
        System.out.println(test.containsGender("man")); // Will print true if "man" exists in the options list
        System.out.println(test.containsGender("non-binary")); // Will print true if "non-binary" exists in the options list
        System.out.println(test.containsGender("woman")); // Will print true if "woman" exists in the options list
        System.out.println(test.containsGender("agender")); // Will print false if "agender" does not exist in the options list
    }

    /**
     * Reads the .txt file and puts its contents into an ArrayList
     *
     * @return The ArrayList of all the genders
     */
    private ArrayList<String> readGenderOptions() {
        ArrayList<String> genderOptions = new ArrayList<>();

        try (BufferedReader br = new BufferedReader(new FileReader(filePath))) {
            String line;
            while ((line = br.readLine()) != null) {
                line = line.trim();
                if (!line.isEmpty()) {
                    genderOptions.add(line);
                }
            }
        } catch (IOException e) {
            e.printStackTrace();
        }

        return genderOptions;
    }

    /**
     * Writes the options ArrayList into filePath
     *
     * @return 1 if successful, 0 if not
     */
    private int writeGenderOptions() {
        try (BufferedWriter bw = new BufferedWriter(new FileWriter(filePath))) {
            for (String option : options) {
                bw.write(option);
                bw.newLine(); // Add newline after each option
            }
            return 1;
        } catch (IOException e) {
            e.printStackTrace();
            return 0;
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
     */
    public ArrayList<String> getOptions() {
        options = readGenderOptions();
        return options;
    }

    /**
     * Updates the .txt file if a new ArrayList of Genders is provided through this function
     *
     * @param options The new ArrayList of String of Genders
     */
    public void setOptions(ArrayList<String> options) {
        GenderOptions.options = options;
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
        GenderOptions.filePath = filePath;
    }
}

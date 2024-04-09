package edu.ucalgary.oop;

import org.junit.Test;

import java.io.IOException;
import java.util.ArrayList;

import static org.junit.Assert.*;

public class GenderOptionTest {
    private final String path = "./src/edu/ucalgary/oop/GenderOptions.txt";
    private final GenderOption testGenderOptions = new GenderOption(path);

    @Test
    public void testObjectCreation() {
        assertNotNull(testGenderOptions);
    }

    @Test
    public void testConstructor() {
        assertNotNull("Constructor should create a non-null Location object", testGenderOptions);
        assertEquals("Constructor should set the path correctly", path, testGenderOptions.getFilePath());
    }

    @Test
    public void testSetAndGetOptions() {
        ArrayList<String> oldOptions = null;
        try {
            oldOptions = testGenderOptions.getOptions();
        } catch (IOException e) {
            e.printStackTrace();
            fail("Unexpected IOException occurred");
        }
        ArrayList<String> newOptions = new ArrayList<>();
        newOptions.add("element1");
        newOptions.add("element2");
        newOptions.add("element3");

        try {
            testGenderOptions.setOptions(newOptions);
            assertEquals("setOptions should update options", newOptions, testGenderOptions.getOptions());
            testGenderOptions.setOptions(oldOptions);
        } catch (IOException e) {
            e.printStackTrace();
            fail("Unexpected IOException occurred");
        }
    }

    @Test
    public void testSetAndGetFilePath() {
        String oldPath = testGenderOptions.getFilePath();
        String newPath = "random.txt";
        testGenderOptions.setFilePath(newPath);
        assertEquals("setFilePath should update filePath", newPath, testGenderOptions.getFilePath());
        testGenderOptions.setFilePath(oldPath);
    }

    @Test
    public void testContainsGender() {
        ArrayList<String> genderOptions = null;
        try {
            genderOptions = testGenderOptions.getOptions();
        } catch (IOException e) {
            e.printStackTrace();
            fail("Unexpected IOException occurred");
        }
        for (String gender : genderOptions) {
            assertTrue("containsGender should return True for all elements in options", testGenderOptions.containsGender(gender));
        }
        assertFalse("containsGender should return False for non-existent gender", testGenderOptions.containsGender("aoeuidhtns"));
    }

    @Test
    public void testInvalidFileSet() {
        String randomFilePath = "RandomFiles.txt";

        boolean correctValueSet = false;
        String failureReasonSet = "No Exception was Thrown";

        ArrayList<String> newOptions = new ArrayList<>();
        newOptions.add("element1");
        newOptions.add("element2");
        newOptions.add("element3");

        testGenderOptions.setFilePath(randomFilePath);
        try {
            testGenderOptions.setOptions(newOptions);
        } catch (IOException e) {
            correctValueSet = true;
        } catch (Exception e) {
            failureReasonSet = "the wrong type of exception was thrown";
        }

        String messageSet = "setOptions() should throw an IOException with invalid file path '" + randomFilePath + "' but " + failureReasonSet + ".";
        assertTrue(messageSet, correctValueSet);
    }

    @Test
    public void testInvalidFileGet() {
        String randomFilePath = "RandomFiles.txt";

        boolean correctValueGet = false;
        String failureReasonGet = "No Exception was Thrown";

        testGenderOptions.setFilePath(randomFilePath);
        try {
            testGenderOptions.getOptions();
        } catch (IOException e) {
            correctValueGet = true;
        } catch (Exception e) {
            failureReasonGet = "the wrong type of exception was thrown";
        }

        String messageGet = "getOptions() should throw an IOException with invalid file path '" + randomFilePath + "' but " + failureReasonGet + ".";
        assertTrue(messageGet, correctValueGet);
    }
}

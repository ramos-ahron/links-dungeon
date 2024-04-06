package edu.ucalgary.oop;

import org.junit.Test;

import java.io.IOException;
import java.util.ArrayList;

import static org.junit.Assert.*;

public class GenderOptionsTest {
    private final String path = "C:\\Users\\ahron\\OneDrive\\Desktop\\Files\\University\\ENSF 380\\Assignments\\I3\\IA3\\IndivProject\\src\\edu\\ucalgary\\oop\\GenderOptions.txt";
    private final GenderOptions testGenderOptions = new GenderOptions(path);

    @Test
    public void testObjectCreation() {
        assertNotNull(testGenderOptions);
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
    public void testInvalidFile() {
        String randomFilePath = "RandomFiles.txt";

        boolean correctValueSet = false;
        String failureReasonSet = "No Exception was Thrown";

        boolean correctValueGet = false;
        String failureReasonGet = "No Exception was Thrown";

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

        try {
            testGenderOptions.getOptions();
        } catch (IOException e) {
            correctValueGet = true;
        } catch (Exception e) {
            failureReasonGet = "the wrong type of exception was thrown";
        }

        String messageSet = "setOptions() should throw an IOException with invalid file path '" + randomFilePath + "' but " + failureReasonSet + ".";
        assertTrue(messageSet, correctValueSet);

        String messageGet = "getOptions() should throw an IOException with invalid file path '" + randomFilePath + "' but " + failureReasonGet + ".";
        assertTrue(messageGet, correctValueGet);
    }
}

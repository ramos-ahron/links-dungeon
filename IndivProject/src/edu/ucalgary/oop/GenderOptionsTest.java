package edu.ucalgary.oop;

import org.junit.Test;

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
        ArrayList<String> oldOptions = testGenderOptions.getOptions();
        ArrayList<String> newOptions = new ArrayList<>();
        newOptions.add("element1");
        newOptions.add("element2");
        newOptions.add("element3");
        testGenderOptions.setOptions(newOptions);
        assertEquals("setOptions should update options", newOptions, testGenderOptions.getOptions());
        testGenderOptions.setOptions(oldOptions);
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
        ArrayList<String> genderOptions = testGenderOptions.getOptions();
        for (String gender : genderOptions) {
            assertTrue("containsGender should return True for all elements in options", testGenderOptions.containsGender(gender));
        }
        assertFalse("containsGender should return False for non-existent gender", testGenderOptions.containsGender("aoeuidhtns"));
    }
}

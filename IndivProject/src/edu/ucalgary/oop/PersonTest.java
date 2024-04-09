package edu.ucalgary.oop;

import org.junit.Test;

import static org.junit.Assert.*;

public class PersonTest {
    Person testPerson1 = new Person("Ahron", "Ramos");
    Person testPerson2 = new Person("Ahron");

    @Test
    public void testObjectCreation() {
        assertNotNull(testPerson1);
        assertNotNull(testPerson2);
    }

    @Test
    public void testValidConstructorWithFirstAndLastName() {
        String firstName = "John";
        String lastName = "Doe";
        Person person = new Person(firstName, lastName);
        assertEquals("Constructor should properly assign firstName", firstName, person.getFirstName());
        assertEquals("Constructor should properly assign lastName", lastName, person.getLastName());
    }

    @Test
    public void testValidConstructorWithFirstNameOnly() {
        String firstName = "Jane";
        Person person = new Person(firstName);
        assertEquals("Constructor should properly assign firstName", firstName, person.getFirstName());
    }

    @Test
    public void testInvalidConstructorWithNullFirstName() {
        boolean correctValue = false;
        String failureReason = "no exception was thrown";

        try {
            new Person(null);
        } catch (NullPointerException e) {
            correctValue = true;
        } catch (Exception e) {
            failureReason = "the wrong exception was thrown";
        }

        String message = "Constructor should throw a NullPointerException if parameter is null but " + failureReason;
        assertTrue(message, correctValue);
    }

    @Test
    public void testInvalidConstructorWithEmptyFirstName() {
        boolean correctValue = false;
        String failureReason = "no exception was thrown";

        try {
            new Person("");
        } catch (NullPointerException e) {
            correctValue = true;
        } catch (Exception e) {
            failureReason = "the wrong exception was thrown";
        }

        String message = "Constructor should throw a NullPointerException if parameter is empty but " + failureReason;
        assertTrue(message, correctValue);
    }

    @Test
    public void testInvalidConstructorWithNullLastName() {
        boolean correctValue = false;
        String failureReason = "no exception was thrown";

        try {
            new Person("John", null);
        } catch (NullPointerException e) {
            correctValue = true;
        } catch (Exception e) {
            failureReason = "the wrong exception was thrown";
        }

        String message = "Constructor should throw a NullPointerException if parameter is null but " + failureReason;
        assertTrue(message, correctValue);
    }

    @Test
    public void testInvalidConstructorWithEmptyLastName() {
        boolean correctValue = false;
        String failureReason = "no exception was thrown";

        try {
            new Person("John", "");
        } catch (NullPointerException e) {
            correctValue = true;
        } catch (Exception e) {
            failureReason = "the wrong exception was thrown";
        }

        String message = "Constructor should throw a NullPointerException if parameter is null but " + failureReason;
        assertTrue(message, correctValue);
    }

    @Test
    public void testGetAndSetFirstName() {
        Person person = new Person("John", "Doe");

        assertEquals("John", person.getFirstName());

        String newFirstName = "Jane";
        person.setFirstName(newFirstName);
        assertEquals(newFirstName, person.getFirstName());
    }

    @Test
    public void testGetAndSetLastName() {
        // Create a Person instance
        Person person = new Person("John", "Doe");

        // Test getLastName method
        assertEquals("Doe", person.getLastName());

        // Test setLastName method
        String newLastName = "Smith";
        person.setLastName(newLastName);
        assertEquals(newLastName, person.getLastName());
    }
}

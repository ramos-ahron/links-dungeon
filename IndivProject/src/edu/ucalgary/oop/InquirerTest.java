package edu.ucalgary.oop;

import org.junit.Test;

import static org.junit.Assert.*;

public class InquirerTest {
    @Test
    public void testObjectCreation() {
        Inquirer test1 = new Inquirer("Random", "Name", "123-456-7890");
        Inquirer test2 = new Inquirer("Test", "Case", "098-765-4321", "some stuff");

        assertNotNull(test1);
        assertNotNull(test2);
    }

    @Test
    public void testValidPhoneNumberConstructor() {
        String firstName = "John";
        String lastName = "Doe";
        String validPhoneNumber = "123-456-7890";
        String info = "Additional information";

        Inquirer inquirer = new Inquirer(firstName, lastName, validPhoneNumber, info);

        assertEquals("Constructor should update inquirer firstName", firstName, inquirer.getFirstName());
        assertEquals("Constructor should update inquirer lastName", lastName, inquirer.getLastName());
        assertEquals("Constructor should update inquirer phoneNumber", validPhoneNumber, inquirer.getPhoneNumber());
        assertEquals("Constructor should update inquirer info", info, inquirer.getInfo());
    }

    @Test
    public void testInvalidPhoneNumberConstructor() {
        String firstName = "John";
        String lastName = "Doe";
        String invalidPhoneNumber = "123-456";
        String info = "Additional information";

        boolean correctValue = false;
        String failureReason = "no exception was thrown";

        try {
            new Inquirer(firstName, lastName, invalidPhoneNumber, info);
        } catch (IllegalArgumentException e) {
            correctValue = true;
        } catch (Exception e) {
            failureReason = "wrong exception was thrown";
        }

        String message = "Constructor should throw IllegalArgumentException if invalid phoneNumber was passed but " + failureReason;

        assertTrue(message, correctValue);
    }

    @Test
    public void testGetPhoneNumber() {
        Inquirer inquirer = new Inquirer("John", "Doe", "123-456-7890");

        String phoneNumber = inquirer.getPhoneNumber();

        assertEquals("getPhoneNumber() should return initialized phoneNumber", "123-456-7890", phoneNumber);
    }

    @Test
    public void testSetPhoneNumber() {
        Inquirer inquirer = new Inquirer("John", "Doe", "123-456-7890");

        inquirer.setPhoneNumber("987-654-3210");

        assertEquals("setPhoneNumber() should update phoneNumber", "987-654-3210", inquirer.getPhoneNumber());
    }

    @Test
    public void testGetInfo() {
        Inquirer inquirer = new Inquirer("John", "Doe", "123-456-7890", "Additional info");

        String info = inquirer.getInfo();

        assertEquals("getInfo() should return initialized phoneNumber", "Additional info", info);
    }

    @Test
    public void testSetInfo() {
        Inquirer inquirer = new Inquirer("John", "Doe", "123-456-7890", "Additional info");

        inquirer.setInfo("Updated info");

        assertEquals("setInfo() should update info", "Updated info", inquirer.getInfo());
    }
}

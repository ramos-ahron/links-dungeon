package edu.ucalgary.oop;

import org.junit.Test;

import static org.junit.Assert.*;

public class SupplyTest {
    private final String expectedType = "Blanket";
    private final int expectedQuantity = 5;
    private final Supply testSupply = new Supply(expectedType, expectedQuantity);

    @Test
    public void testConstructor() {
        assertNotNull("Constructor should create a non-null Location object", testSupply);
        assertEquals("Constructor should set the type correctly", expectedType, testSupply.getType());
        assertEquals("Constructor should set the quantity correctly", expectedQuantity, testSupply.getQuantity());

        Supply testSupplyW = new Supply("Water");
        assertEquals("Constructor should set the type correctly", "Water", testSupplyW.getType());
        assertEquals("Constructor should set the quantity correctly", 0, testSupplyW.getQuantity());
    }

    @Test
    public void testObjectCreation() {
        Supply testSupplyW = new Supply("Water");
        assertNotNull(testSupply);
        assertNotNull(testSupplyW);
    }

    @Test
    public void testInvalidObjectCreationTypeEmpty() {
        boolean correctValue = false;
        String failureReason = "no exception was thrown";
        try {
            new Supply("", 1);
        } catch (IllegalArgumentException e) {
            correctValue = true;
        } catch (Exception e) {
            failureReason = "the wrong type of exception was thrown";
        }

        String message = "Constructor should throw IllegalArgumentException when type is empty but " + failureReason;
        assertTrue(message, correctValue);
    }

    @Test
    public void testInvalidObjectCreationTypeNull() {
        boolean correctValue = false;
        String failureReason = "no exception was thrown";
        try {
            new Supply(null, 1);
        } catch (IllegalArgumentException e) {
            correctValue = true;
        } catch (Exception e) {
            failureReason = "the wrong type of exception was thrown";
        }

        String message = "Constructor should throw IllegalArgumentException when type is null but " + failureReason;
        assertTrue(message, correctValue);
    }

    @Test
    public void testInvalidObjectCreationQuantity() {
        boolean correctValue = false;
        String failureReason = "no exception was thrown";
        try {
            new Supply("Random", -4);
        } catch (IllegalArgumentException e) {
            correctValue = true;
        } catch (Exception e) {
            failureReason = "the wrong type of exception was thrown";
        }

        String message = "Constructor should throw IllegalArgumentException when quantity is negative but " + failureReason;
        assertTrue(message, correctValue);
    }

    @Test
    public void testSetAndGetType() {
        String oldType = testSupply.getType();
        String newType = "Tissue";

        testSupply.setType(newType);

        assertEquals("getType() should return expected supply type", oldType, expectedType);
        assertEquals("setType() should update supply type", newType, testSupply.getType());

        testSupply.setType(oldType);
    }

    @Test
    public void testSetAndGetQuantity() {
        int oldQuantity = testSupply.getQuantity();
        int newQuantity = 3;

        testSupply.setQuantity(newQuantity);

        assertEquals("getQuantity() should return expected supply quantity", oldQuantity, expectedQuantity);
        assertEquals("setQuantity() should update supply quantity", newQuantity, testSupply.getQuantity());

        testSupply.setQuantity(oldQuantity);
    }

    @Test
    public void testInvalidQuantity() {
        int invalidQuantity = -1;
        boolean correctValue = false;
        String failureReason = "no exception was thrown";

        try {
            testSupply.setQuantity(invalidQuantity);
        } catch (IllegalArgumentException e) {
            correctValue = true;
        } catch (Exception e) {
            failureReason = "the wrong type of exception was thrown";
        }
        String message = "setQuantity() should throw an IllegalArgumentException whenever quantity passed is negative but " + failureReason;
        assertTrue(message, correctValue);
    }

    @Test
    public void testAdd() {
        int quantity1 = testSupply.getQuantity();
        int amount1 = 3;
        int amount2 = -2;

        testSupply.add(amount1);
        int quantity2 = testSupply.getQuantity();

        testSupply.add(amount2);
        int quantity3 = testSupply.getQuantity();

        assertEquals("add() should update quantity amount with new amount", quantity2, quantity1 + amount1);
        assertEquals("add() should update quantity amount with new amount", quantity3, quantity2 + amount2);

        testSupply.setQuantity(quantity1);
    }

    @Test
    public void testInvalidAdd() {
        int quantity = testSupply.getQuantity();
        int invalidAmount = -(quantity + 1);

        boolean correctValue = false;
        String failureReason = "no exception was thrown";

        try {
            testSupply.add(invalidAmount);
        } catch (IllegalArgumentException e) {
            correctValue = true;
        } catch (Exception e) {
            failureReason = "the wrong type of exception was thrown";
        }

        String message = "add() should throw an IllegalArgumentException if the resulting quantity amount is negative but " + failureReason;
        assertTrue(message, correctValue);
    }
}

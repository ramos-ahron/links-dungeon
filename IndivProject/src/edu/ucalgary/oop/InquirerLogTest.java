package edu.ucalgary.oop;

import org.junit.Test;

import java.util.HashSet;

import static org.junit.Assert.*;

public class InquirerLogTest {
    @Test
    public void testAddInquirer_ValidInquirer() {
        Inquirer inquirer = new Inquirer("Jane", "Doe", "123-456-7890");
        InquirerLog.addInquirer(inquirer);

        assertTrue("addInquirer() should update inquirerList", InquirerLog.getInquirerList().contains(inquirer));
    }

    @Test
    public void testAddInquirerNullInquirer() {
        boolean correctValue = false;
        String failureReason = "no exception was thrown";

        try {
            InquirerLog.addInquirer(null);
        } catch (IllegalArgumentException e) {
            correctValue = true;
        } catch (Exception e) {
            failureReason = "wrong exception was thrown";
        }

        String message = "addInquirer() should throw IllegalArgumentException if null is used as parameter but " + failureReason;
        assertTrue(message, correctValue);
    }

    @Test
    public void testAddInquirerDuplicateInquirer() {
        Inquirer inquirer1 = new Inquirer("John", "Doe", "123-456-7890");
        Inquirer inquirer2 = new Inquirer("John", "Doe", "123-456-7890");

        boolean correctValue = false;
        String failureReason = "no exception was thrown";

        InquirerLog.getInquirerList().clear();
        InquirerLog.addInquirer(inquirer1);
        try {
            InquirerLog.addInquirer(inquirer2);
        } catch (IllegalArgumentException e) {
            correctValue = true;
        } catch (Exception e) {
            failureReason = "wrong exception was thrown";
        }

        String message = "addInquirer() should throw IllegalArgumentException if inquirer already in the set but " + failureReason;
        assertTrue(message, correctValue);
    }

    @Test
    public void testRemoveInquirerValidInquirer() {
        Inquirer inquirer = new Inquirer("Jane", "Doe", "123-456-7890");
        InquirerLog.addInquirer(inquirer);

        InquirerLog.removeInquirer(inquirer);

        assertFalse("removeInquirer() should update inquirerList", InquirerLog.getInquirerList().contains(inquirer));
    }

    @Test
    public void testRemoveInquirerNullInquirer() {
        boolean correctValue = false;
        String failureReason = "no exception was thrown";

        try {
            InquirerLog.removeInquirer(null);
        } catch (IllegalArgumentException e) {
            correctValue = true;
        } catch (Exception e) {
            failureReason = "wrong exception was thrown";
        }

        String message = "removeInquirer() should throw IllegalArgumentException if null is used as parameter but " + failureReason;
        assertTrue(message, correctValue);
    }

    @Test
    public void testRemoveInquirerNotInList() {
        Inquirer inquirer = new Inquirer("John", "Doe", "123-456-7890");
        boolean correctValue = false;
        String failureReason = "no exception was thrown";
        try {
            InquirerLog.removeInquirer(inquirer);
        } catch (IllegalArgumentException e) {
            correctValue = true;
        } catch (Exception e) {
            failureReason = "wrong exception was thrown";
        }
        String message = "removeInquirer() should throw IllegalArgumentException if inquirer is not in set but " + failureReason;
        assertTrue(message, correctValue);
    }

    @Test
    public void testSetAndGetInquirerList() {
        HashSet<Inquirer> newList = new HashSet<>();
        newList.add(new Inquirer("John", "Doe", "123-456-7890"));

        InquirerLog.setInquirerList(newList);

        assertEquals("setInquirerList() should update the values of inquirerList and getInquirerList() should return the updated value", newList, InquirerLog.getInquirerList());
    }
}

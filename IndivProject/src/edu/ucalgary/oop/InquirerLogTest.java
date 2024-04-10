package edu.ucalgary.oop;

import org.junit.Test;

import java.util.HashSet;

import static org.junit.Assert.*;

public class InquirerLogTest {
    @Test
    public void testAddInquirerValidInquiry() {
        InquirerLog inquirerLog = new InquirerLog();
        Inquiry inquiry = new Inquiry("123-456-7890");
        inquirerLog.addInquirer(inquiry);

        assertTrue("addInquirer() should update inquirerList", inquirerLog.getInquirerList().contains(inquiry));
    }

    @Test
    public void testAddInquirerNullInquiry() {
        InquirerLog inquirerLog = new InquirerLog();
        boolean correctValue = false;
        String failureReason = "no exception was thrown";

        try {
            inquirerLog.addInquirer(null);
        } catch (IllegalArgumentException e) {
            correctValue = true;
        } catch (Exception e) {
            failureReason = "wrong exception was thrown";
        }

        String message = "addInquirer() should throw IllegalArgumentException if null is used as parameter but " + failureReason;
        assertTrue(message, correctValue);
    }

    @Test
    public void testAddInquirerDuplicateInquiry() {
        InquirerLog inquirerLog = new InquirerLog();
        Inquiry inquiry1 = new Inquiry("123-456-7890");
        Inquiry inquiry2 = new Inquiry("123-456-7890");

        boolean correctValue = false;
        String failureReason = "no exception was thrown";

        inquirerLog.getInquirerList().clear();
        inquirerLog.addInquirer(inquiry1);
        try {
            inquirerLog.addInquirer(inquiry2);
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
        InquirerLog inquirerLog = new InquirerLog();
        Inquiry inquiry = new Inquiry("123-456-7890");
        inquirerLog.addInquirer(inquiry);

        inquirerLog.removeInquirer(inquiry);

        assertFalse("removeInquirer() should update inquirerList", inquirerLog.getInquirerList().contains(inquiry));
    }

    @Test
    public void testRemoveInquirerNullInquirer() {
        InquirerLog inquirerLog = new InquirerLog();
        boolean correctValue = false;
        String failureReason = "no exception was thrown";

        try {
            inquirerLog.removeInquirer(null);
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
        InquirerLog inquirerLog = new InquirerLog();
        Inquiry inquirer = new Inquiry("123-456-7890");
        boolean correctValue = false;
        String failureReason = "no exception was thrown";
        try {
            inquirerLog.removeInquirer(inquirer);
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
        InquirerLog inquirerLog = new InquirerLog();
        HashSet<Inquiry> newList = new HashSet<>();
        newList.add(new Inquiry("123-456-7890"));

        inquirerLog.setInquirerList(newList);

        assertEquals("setInquirerList() should update the values of inquirerList and getInquirerList() should return the updated value", newList, inquirerLog.getInquirerList());
    }
}

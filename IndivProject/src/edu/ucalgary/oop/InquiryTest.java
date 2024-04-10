package edu.ucalgary.oop;

import static org.junit.Assert.*;
import org.junit.Test;

import java.time.LocalDate;

public class InquiryTest {
    @Test
    public void testConstructorWithValidDate() {
        String date = "2022-04-08";
        String info = "Test inquiry";
        Inquiry inquiry = new Inquiry(date, info);
        assertEquals("Constructor should update date properly", date, inquiry.getDate());
        assertEquals("Constructor should update info properly", info, inquiry.getInfo());
    }

    @Test
    public void testConstructorWithInvalidDate() {
        String date = "2022-04-32";
        String info = "Test inquiry";

        boolean correctValue = false;
        String failureReason = "no exception was thrown";

        try {
            new Inquiry(date, info);
        } catch (IllegalArgumentException e) {
            correctValue = true;
        } catch (Exception e) {
            failureReason = "wrong exception was thrown";
        }

        String message = "Constructor should throw IllegalArgumentException when invalid date is used but " + failureReason;

        assertTrue(message, correctValue);
    }

    @Test
    public void testConstructorWithFutureDate() {
        String date = LocalDate.now().plusDays(1).toString(); // Future date
        String info = "Test inquiry";
        boolean correctValue = false;
        String failureReason = "no exception was thrown";

        try {
            new Inquiry(date, info);
        } catch (IllegalArgumentException e) {
            correctValue = true;
        } catch (Exception e) {
            failureReason = "wrong exception was thrown";
        }

        String message = "Constructor should throw IllegalArgumentException when invalid date is used but " + failureReason;

        assertTrue(message, correctValue);
    }

    @Test
    public void testGetDate() {
        String date = "2022-04-08";
        String info = "Test inquiry";
        Inquiry inquiry = new Inquiry(date, info);
        assertEquals("getDate() should return expected date", date, inquiry.getDate());
    }

    @Test
    public void testGetInfo() {
        String date = "2022-04-08";
        String info = "Test inquiry";
        Inquiry inquiry = new Inquiry(date, info);
        assertEquals("getInfo() should return expected info", info, inquiry.getInfo());
    }

    @Test
    public void testSetInfo() {
        String date = "2022-04-08";
        String info = "Test inquiry";
        Inquiry inquiry = new Inquiry(date, info);

        String newInfo = "Updated inquiry";
        inquiry.setInfo(newInfo);

        assertEquals("setInfo() should set info to the new expected info", newInfo, inquiry.getInfo());
    }
}

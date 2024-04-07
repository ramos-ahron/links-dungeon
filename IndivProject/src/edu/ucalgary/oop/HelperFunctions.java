package edu.ucalgary.oop;

import java.time.LocalDate;
import java.time.format.DateTimeFormatter;
import java.util.LinkedList;

abstract public class HelperFunctions {
    /**
     * Checks if the provided date string has an invalid format.
     *
     * @param date the date string to check
     * @return true if the date string has an invalid format, otherwise false
     */
    public static boolean invalidDateFormat(String date) {
        try {
            LocalDate.parse(date, DateTimeFormatter.ISO_DATE);
            return false;
        } catch (Exception e) {
            return true;
        }
    }

    /**
     * Checks if the specified element is present in the provided LinkedList.
     *
     * @param list          the LinkedList to search
     * @param elementToFind the element to search for
     * @param <T>           the type of elements in the LinkedList
     * @return true if the element is found in the LinkedList, otherwise false
     */
    public static <T> boolean inList(LinkedList<T> list, T elementToFind) {
        for (T element : list) {
            if (element.equals(elementToFind)) {
                return true;
            }
        }
        return false;
    }
}

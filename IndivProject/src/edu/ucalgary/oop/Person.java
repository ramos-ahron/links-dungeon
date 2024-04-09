package edu.ucalgary.oop;

public class Person {
    private String firstName;
    private String lastName;

    public Person(String firstName, String lastName) throws NullPointerException {
        this(firstName);
        if (lastName.isEmpty() || lastName == null) {
            throw new NullPointerException("Cannot have a last name that is empty or null");
        }
        this.lastName = lastName;
    }

    public Person(String firstName) throws NullPointerException {
        if (firstName.isEmpty() || firstName == null) {
            throw new NullPointerException("Cannot have a first name that is empty or null");
        }
        this.firstName = firstName;
    }

    public String getFirstName() {
        return firstName;
    }

    public void setFirstName(String firstName) {
        this.firstName = firstName;
    }

    public String getLastName() {
        return lastName;
    }

    public void setLastName(String lastName) {
        this.lastName = lastName;
    }
}

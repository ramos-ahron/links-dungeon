package edu.ucalgary.oop;

public class Person {
    private String firstName;
    private String lastName;

    /**
     * Constructs a Person object with the specified first name and last name.
     *
     * @param firstName the first name of the person
     * @param lastName  the last name of the person
     * @throws NullPointerException if the first name or last name is null or empty
     */
    public Person(String firstName, String lastName) throws NullPointerException {
        if (firstName == null || firstName.isEmpty()) {
            throw new NullPointerException("First name cannot be null or empty");
        }
        setNames(firstName, lastName);
    }

    /**
     * Constructs a Person object with the specified first name.
     *
     * @param firstName the first name of the person
     * @throws NullPointerException if the first name is null or empty
     */
    public Person(String firstName) throws NullPointerException {
        if (firstName == null || firstName.isEmpty()) {
            throw new NullPointerException("First name cannot be null or empty");
        }
        this.firstName = firstName;
    }

    /**
     * Sets the first name and last name of the individual.
     *
     * @param firstName the first name of the individual
     * @param lastName the last name of the individual, can be null or empty if not available
     */
    private void setNames(String firstName, String lastName) {
        this.firstName = firstName;
        if (lastName != null && !lastName.isEmpty()) {
            this.lastName = lastName;
        }
    }


    /**
     * Retrieves the first name of the person.
     *
     * @return the first name of the person
     */
    public String getFirstName() {
        return firstName;
    }


    /**
     * Sets the first name of the person.
     *
     * @param firstName the first name to set for the person
     */
    public void setFirstName(String firstName) {
        this.firstName = firstName;
    }


    /**
     * Retrieves the last name of the person.
     *
     * @return the last name of the person
     */
    public String getLastName() {
        return lastName;
    }


    /**
     * Sets the last name of the person.
     *
     * @param lastName the last name to set for the person
     */
    public void setLastName(String lastName) {
        this.lastName = lastName;
    }
}

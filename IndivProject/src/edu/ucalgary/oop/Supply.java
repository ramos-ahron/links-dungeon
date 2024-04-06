package edu.ucalgary.oop;

public class Supply {
    private String type;
    private int quantity;

    /**
     * Constructor, sets quantity to 0 if not provided
     *
     * @param type The type of supply
     */
    public Supply(String type) {
        this.type = type;
        this.quantity = 0;
    }

    /**
     * Constructor
     *
     * @param type     The type of supply
     * @param quantity The number of supplies
     * @throws IllegalArgumentException Gets thrown if quantity is negative
     */
    public Supply(String type, int quantity) throws IllegalArgumentException {
        this.type = type;

        if (invalidQuantity(quantity)) {
            throw new IllegalArgumentException("Cannot initialize supply with negative quantity");
        }

        this.quantity = quantity;
    }

    public static void main(String[] args) {
        Supply supply = new Supply("Type A", 100);
        System.out.println("Type: " + supply.getType());
        System.out.println("Quantity: " + supply.getQuantity());

        supply.setType("Type B");
        supply.setQuantity(200);
        System.out.println("Updated Type: " + supply.getType());
        System.out.println("Updated Quantity: " + supply.getQuantity());
    }

    /**
     * Checks if quantity provided is valid
     *
     * @param quantity The quantity provided
     * @return true if valid, otherwise false
     */
    private boolean invalidQuantity(int quantity) {
        return quantity < 0;
    }

    /**
     * Adds amount to quantity
     *
     * @param amount The amount of supplies to be added
     * @throws IllegalArgumentException Gets thrown if amount makes quantity negative
     */
    public void add(int amount) throws IllegalArgumentException {
        if (this.quantity + amount < 0) {
            throw new IllegalArgumentException("This amount makes the number of supplies negative");
        }
        this.quantity += amount;
    }

    /**
     * @return The type of supply
     */
    public String getType() {
        return type;
    }

    /**
     * Sets the type of quantity
     *
     * @param type The new type of quantity
     */
    public void setType(String type) {
        this.type = type;
    }

    /**
     * @return The number of supplies
     */
    public int getQuantity() {
        return quantity;
    }

    /**
     * Sets the new amount of quantity
     *
     * @param quantity The new amount of quantity
     * @throws IllegalArgumentException Gets thrown if quantity is negative
     */
    public void setQuantity(int quantity) throws IllegalArgumentException {
        if (invalidQuantity(quantity)) {
            throw new IllegalArgumentException("Cannot initialize supply with negative quantity");
        }
        this.quantity = quantity;
    }
}

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
     */
    public Supply(String type, int quantity) {
        this.type = type;
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
     * Adds amount to quantity
     *
     * @param amount The amount of supplies to be added
     */
    public void add(int amount) {
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
     */
    public void setQuantity(int quantity) {
        this.quantity = quantity;
    }
}

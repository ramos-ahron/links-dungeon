package edu.ucalgary.oop;

public class Supply {
    private String type;
    private int quantity;

    public Supply(String type, int quantity) {
        this.type = type;
        this.quantity = quantity;
    }

    public void setType(String type) {
        this.type = type;
    }

    public void setQuantity(int quantity) {
        this.quantity = quantity;
    }

    public String getType() {
        return type;
    }

    public int getQuantity() {
        return quantity;
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
}

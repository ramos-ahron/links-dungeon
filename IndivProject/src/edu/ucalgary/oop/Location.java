package edu.ucalgary.oop;

import java.util.LinkedList;

public class Location {
    private String name;
    private String address;
    private LinkedList<DisasterVictim> occupants;
    private LinkedList<Supply> supplies;
    private static DatabaseManager database;

    public Location(String name, String address) {
        this.name = name;
        this.address = address;
        this.occupants = new LinkedList<>();
        this.supplies = new LinkedList<>();
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }

    public LinkedList<DisasterVictim> getOccupants() {
        return occupants;
    }

    public void setOccupants(LinkedList<DisasterVictim> occupants) {
        this.occupants.clear();
        for (DisasterVictim occupant : occupants) {
            this.occupants.add(occupant);
        }
    }

    public LinkedList<Supply> getSupplies() {
        return supplies;
    }

    public void setSupplies(LinkedList<Supply> supplies) {
        this.supplies.clear();
        this.supplies.addAll(supplies);
    }

    public void addOccupant(DisasterVictim occupant) {
        this.occupants.add(occupant);
    }

    public void removeOccupant(DisasterVictim occupant) {
        this.occupants.remove(occupant);
    }

    public void addSupply(Supply supply) {

    }

    public void addSupply(Supply supply, int num) {
        for (int i = 0; i < num; i++) {
            this.supplies.add(supply);
        }
    }

    public void removeSupply(Supply supply) {

    }

    public void removeSupply(Supply supply, int num) {
        for (int i = 0; i < num; i++) {
            this.supplies.remove(supply);
        }
    }
}


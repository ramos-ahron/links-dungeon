package edu.ucalgary.oop;

import java.util.LinkedList;

public class Location extends HelperFunctions {
    private final LinkedList<DisasterVictim> occupants;
    private final LinkedList<Supply> supplies;
    private String name;
    private String address;
//    private static DatabaseManager database;

    /**
     * Constructs a new location with the specified name and address.
     * Initializes the list of occupants and supplies to empty LinkedLists.
     *
     * @param name    the name of the location
     * @param address the address of the location
     */
    public Location(String name, String address) {
        this.name = name;
        this.address = address;
        this.occupants = new LinkedList<>();
        this.supplies = new LinkedList<>();
    }

    /**
     * Returns the name of the location.
     *
     * @return the name of the location
     */
    public String getName() {
        return name;
    }

    /**
     * Sets the name of the location.
     *
     * @param name the name to set
     */
    public void setName(String name) {
        this.name = name;
    }

    /**
     * Returns the address of the location.
     *
     * @return the address of the location
     */
    public String getAddress() {
        return address;
    }

    /**
     * Sets the address of the location.
     *
     * @param address the address to set
     */
    public void setAddress(String address) {
        this.address = address;
    }

    /**
     * Returns the list of occupants at the location.
     *
     * @return the list of occupants
     */
    public LinkedList<DisasterVictim> getOccupants() {
        return occupants;
    }

    /**
     * Sets the list of occupants at the location.
     *
     * @param occupants the list of occupants to set
     */
    public void setOccupants(LinkedList<DisasterVictim> occupants) {
        this.occupants.clear();
        this.occupants.addAll(occupants);
    }

    /**
     * Returns the list of supplies at the location.
     *
     * @return the list of supplies
     */
    public LinkedList<Supply> getSupplies() {
        return supplies;
    }

    /**
     * Sets the list of supplies at the location.
     *
     * @param supplies the list of supplies to set
     */
    public void setSupplies(LinkedList<Supply> supplies) {
        this.supplies.clear();
        this.supplies.addAll(supplies);
    }


    /**
     * Adds the specified occupant to the list of occupants.
     *
     * @param occupant the occupant to be added
     * @throws NullPointerException     if the provided occupant is null
     * @throws IllegalArgumentException if the provided occupant is already in the list of occupants
     */
    public void addOccupant(DisasterVictim occupant) throws NullPointerException, IllegalArgumentException {
        if (occupant == null) {
            throw new NullPointerException("The occupant provided cannot be null");
        }
        if (inList(occupants, occupant)) {
            throw new IllegalArgumentException("The occupant is already in the location");
        } else {
            this.occupants.add(occupant);
        }
    }

    /**
     * Removes the specified occupant from the list of occupants.
     *
     * @param occupant the occupant to be removed
     * @throws NullPointerException     if the provided occupant is null
     * @throws IllegalArgumentException if the provided occupant is not found in the list of occupants
     */
    public void removeOccupant(DisasterVictim occupant) throws NullPointerException, IllegalArgumentException {
        if (occupant == null) {
            throw new NullPointerException("The occupant provided cannot be null");
        }
        if (inList(occupants, occupant)) {
            this.occupants.remove(occupant);
        } else {
            throw new IllegalArgumentException("The occupant is not found in the location");
        }
    }


    /**
     * Adds the specified supply to the inventory.
     *
     * @param supply the supply to be added
     * @throws NullPointerException if the provided supply is null
     */
    public void addSupply(Supply supply) throws NullPointerException {
        if (supply == null) {
            throw new NullPointerException("The supply provided cannot be null");
        }
        if (inList(supplies, supply)) {
            int amount = supply.getQuantity();
            for (Supply existingSupply : supplies) {
                if (existingSupply.getType().equals(supply.getType())) {
                    existingSupply.add(amount);
                    refreshSupplies(supplies);
                    return;
                }
            }
        } else {
            supplies.add(supply);
        }
    }


    /**
     * Removes the specified supply from the inventory.
     *
     * @param supply the supply to be removed
     * @throws NullPointerException     if the provided supply is null
     * @throws IllegalArgumentException if the provided supply is not found in the inventory
     */
    public void removeSupply(Supply supply) throws NullPointerException, IllegalArgumentException {
        if (supply == null) {
            throw new NullPointerException("The supply provided cannot be null");
        }
        if (inList(supplies, supply)) {
            int amount = -supply.getQuantity();
            for (Supply existingSupply : supplies) {
                if (existingSupply.getType().equals(supply.getType())) {
                    existingSupply.add(amount);
                    refreshSupplies(supplies);
                    return;
                }
            }
        } else {
            throw new IllegalArgumentException("The supply provided is not found in the inventory");
        }
    }

    /**
     * Removes supplies from the provided list that have a quantity of zero.
     *
     * @param list the LinkedList of supplies to refresh
     */
    private void refreshSupplies(LinkedList<Supply> list) {
        list.removeIf(supply -> supply.getQuantity() == 0);
    }
}


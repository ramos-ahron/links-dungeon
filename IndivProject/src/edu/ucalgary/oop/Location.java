package edu.ucalgary.oop;

import java.util.LinkedList;

public class Location {
    private final LinkedList<DisasterVictim> occupants = new LinkedList<>();
    private final LinkedList<Supply> supplies = new LinkedList<>();
    private String name;
    private String address;

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

        if (inListOccupants(occupant) != null) {
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
        DisasterVictim occupantToRemove = inListOccupants(occupant);

        if (occupantToRemove != null) {
            this.occupants.remove(occupantToRemove);
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
        if (inListSupply(supply)) {
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
        if (inListSupply(supply)) {
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

    /**
     * Checks if the specified supply is present in the list of supplies.
     *
     * @param elementToFind The supply to search for.
     * @return true if the supply is found in the list, otherwise false.
     */
    private boolean inListSupply(Supply elementToFind) {
        for (Supply element : supplies) {
            // Check if both type and other attributes match
            if (element.getType().equals(elementToFind.getType())) {
                return true;
            }
        }
        return false;
    }

    /**
     * Checks if the specified occupant is present in the list of occupants.
     *
     * @param elementToFind The occupant to search for.
     * @return The first found occupant with the same assignedSocialID as the specified elementToFind,
     * or null if no such occupant is found.
     */
    private DisasterVictim inListOccupants(DisasterVictim elementToFind) {
        for (DisasterVictim element : occupants) {
            if (element.getAssignedSocialID() == elementToFind.getAssignedSocialID()) {
                return element;
            }
        }
        return null;
    }
}


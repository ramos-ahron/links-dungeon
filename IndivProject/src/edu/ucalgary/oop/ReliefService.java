package edu.ucalgary.oop;

import java.util.LinkedList;


abstract public class ReliefService {
    private static final LinkedList<Location> shelters = new LinkedList<>();
    private static final LinkedList<Location> locations = new LinkedList<Location>();
    private static final LinkedList<DisasterVictim> missingPeople = new LinkedList<>();
    private static final LinkedList<DisasterVictim> people = new LinkedList<>();


    /**
     * Adds a shelter to the list of shelters.
     *
     * @param location The location representing the shelter to be added.
     * @throws NullPointerException     If the provided location is null.
     * @throws IllegalArgumentException If the location is already a shelter in the list.
     */
    public static void addShelter(Location location) throws NullPointerException, IllegalArgumentException {
        if (location == null) {
            throw new NullPointerException("The location provided cannot be null");
        }

        if (inListLocation(location) != null) {
            throw new IllegalArgumentException("The location is already a shelter");
        } else {
            shelters.add(location);
        }
    }


    /**
     * Removes a shelter from the list of shelters.
     *
     * @param location The location representing the shelter to be removed.
     * @throws NullPointerException     If the provided shelter location is null.
     * @throws IllegalArgumentException If the location is not found in the list of shelters.
     */
    public static void removeShelter(Location location) throws NullPointerException, IllegalArgumentException {
        if (location == null) {
            throw new NullPointerException("The shelter provided cannot be null");
        }

        Location locationToRemove = inListLocation(location);

        if (locationToRemove != null) {
            shelters.remove(locationToRemove);
        } else {
            throw new IllegalArgumentException("The location is not a shelter");
        }
    }

    /**
     * Adds a shelter to the list of locations.
     *
     * @param location The location representing the shelter to be added.
     * @throws NullPointerException     If the provided location is null.
     * @throws IllegalArgumentException If the location is already a locations in the list.
     */
    public static void addLocation(Location location) throws NullPointerException, IllegalArgumentException {
        if (location == null) {
            throw new NullPointerException("The location provided cannot be null");
        }

        if (inListLocation(location) != null) {
            throw new IllegalArgumentException("The location is already a shelter");
        } else {
            locations.add(location);
        }
    }


    /**
     * Removes a shelter from the list of locations.
     *
     * @param location The location representing the location to be removed.
     * @throws NullPointerException     If the provided location is null.
     * @throws IllegalArgumentException If the location is not found in the list of locations.
     */
    public static void removeLocation(Location location) throws NullPointerException, IllegalArgumentException {
        if (location == null) {
            throw new NullPointerException("The shelter provided cannot be null");
        }

        Location locationToRemove = inListLocation(location);

        if (locationToRemove != null) {
            locations.remove(locationToRemove);
        } else {
            throw new IllegalArgumentException("The location is not a shelter");
        }
    }

    /**
     * Adds a missing person to the list of missing people.
     *
     * @param victim The victim to be added to the list.
     * @throws NullPointerException     If the provided victim is null.
     * @throws IllegalArgumentException If the victim is already in the list of missing people.
     */
    public static void addMissingPerson(DisasterVictim victim) throws NullPointerException, IllegalArgumentException {
        if (victim == null) {
            throw new NullPointerException("The victim provided cannot be null");
        }

        if (inListMissingPerson(victim) != null) {
            throw new IllegalArgumentException("The victim is already in the list");
        } else {
            missingPeople.add(victim);
        }
    }

    /**
     * Removes a missing person from the list of missing people.
     *
     * @param victim The victim to be removed from the list.
     * @throws NullPointerException     If the provided victim is null.
     * @throws IllegalArgumentException If the victim is not found in the list of missing people.
     */
    public static void removeMissingPerson(DisasterVictim victim) throws NullPointerException, IllegalArgumentException {
        if (victim == null) {
            throw new NullPointerException("The victim provided cannot be null");
        }

        DisasterVictim personToRemove = inListMissingPerson(victim);

        if (personToRemove != null) {
            missingPeople.remove(personToRemove);
        } else {
            throw new IllegalArgumentException("The victim is not found in the list");
        }
    }

    /**
     * Adds a missing person to the list of people.
     *
     * @param victim The victim to be added to the list.
     * @throws NullPointerException     If the provided victim is null.
     * @throws IllegalArgumentException If the victim is already in the list of people.
     */
    public static void addPerson(DisasterVictim victim) throws NullPointerException, IllegalArgumentException {
        if (victim == null) {
            throw new NullPointerException("The victim provided cannot be null");
        }

        if (inListMissingPerson(victim) != null) {
            throw new IllegalArgumentException("The victim is already in the list");
        } else {
            people.add(victim);
        }
    }

    /**
     * Removes a missing person from the list of people.
     *
     * @param victim The victim to be removed from the list.
     * @throws NullPointerException     If the provided victim is null.
     * @throws IllegalArgumentException If the victim is not found in the list of people.
     */
    public static void removePerson(DisasterVictim victim) throws NullPointerException, IllegalArgumentException {
        if (victim == null) {
            throw new NullPointerException("The victim provided cannot be null");
        }

        DisasterVictim personToRemove = inListPeople(victim);

        if (personToRemove != null) {
            people.remove(personToRemove);
        } else {
            throw new IllegalArgumentException("The victim is not found in the list");
        }
    }


    /**
     * Retrieves the list of shelters.
     *
     * @return The list of shelters.
     */
    public static LinkedList<Location> getShelters() {
        return shelters;
    }


    /**
     * Sets the list of shelters.
     *
     * @param shelters The new list of shelters to set.
     */
    public static void setShelters(LinkedList<Location> shelters) {
        ReliefService.shelters.clear();
        ReliefService.shelters.addAll(shelters);
    }

    /**
     * Retrieves the list of shellocationsters.
     *
     * @return The list of locations.
     */
    public static LinkedList<Location> getLocations() {
        return locations;
    }


    /**
     * Sets the list of locations.
     *
     * @param locations The new list of locations to set.
     */
    public static void setLocations(LinkedList<Location> locations) {
        ReliefService.locations.clear();
        ReliefService.locations.addAll(locations);
    }

    /**
     * Retrieves the list of missing people.
     *
     * @return The list of missing people.
     */
    public static LinkedList<DisasterVictim> getMissingPeople() {
        return missingPeople;
    }

    /**
     * Sets the list of missing people.
     *
     * @param missingPeople The new list of missing people to set.
     */
    public static void setMissingPeople(LinkedList<DisasterVictim> missingPeople) {
        ReliefService.missingPeople.clear();
        ReliefService.missingPeople.addAll(missingPeople);
    }

    /**
     * Retrieves the list of people.
     *
     * @return The list of people.
     */
    public static LinkedList<DisasterVictim> getPeople() {
        return people;
    }

    /**
     * Sets the list of people.
     *
     * @param people The new list of people to set.
     */
    public static void setPeople(LinkedList<DisasterVictim> people) {
        ReliefService.people.clear();
        ReliefService.people.addAll(people);
    }


    /**
     * Checks if the specified location is present in the list of shelters.
     *
     * @param elementToFind The location to search for.
     * @return The first found location with the same name and address as the specified elementToFind,
     *         or null if no such location is found.
     */
    public static Location inListLocation(Location elementToFind) {
        for (Location location : shelters) {
            if (location.getName().equals(elementToFind.getName()) && location.getAddress().equals(elementToFind.getAddress())) {
                return location;
            }
        }
        return null;
    }

    /**
     * Checks if the specified victim is present in the list of missingPeople.
     *
     * @param elementToFind The victim to search for.
     * @return The first found victim with the same social id as the specified elementToFind,
     *         or null if no such victim is found.
     */
    public static DisasterVictim inListMissingPerson(DisasterVictim elementToFind) {
        for (DisasterVictim victim : missingPeople) {
            if (elementToFind.getAssignedSocialID() == victim.getAssignedSocialID()) {
                return victim;
            }
        }
        return null;
    }

    /**
     * Checks if the specified victim is present in the list of people.
     *
     * @param elementToFind The victim to search for.
     * @return The first found victim with the same social id as the specified elementToFind,
     *         or null if no such victim is found.
     */
    public static DisasterVictim inListPeople(DisasterVictim elementToFind) {
        for (DisasterVictim victim : people) {
            if (elementToFind.getAssignedSocialID() == victim.getAssignedSocialID()) {
                return victim;
            }
        }
        return null;
    }
}

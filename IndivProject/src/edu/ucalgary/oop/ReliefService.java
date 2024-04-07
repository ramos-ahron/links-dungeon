package edu.ucalgary.oop;

import java.util.LinkedList;

public class ReliefService {
    private static int WORKER_ID_COUNTER = 1;
    private final int workerId;

    private final LinkedList<Location> shelters = new LinkedList<>();

    /**
     * Initializes a new ReliefService instance.
     *
     * <p>
     * This constructor assigns a unique worker ID to the ReliefService instance based on the current value of the WORKER_ID_COUNTER.
     * </p>
     */
    public ReliefService() {
        workerId = WORKER_ID_COUNTER++;
    }

    /**
     * Adds a shelter to the list of shelters.
     *
     * @param location The location representing the shelter to be added.
     * @throws NullPointerException     If the provided location is null.
     * @throws IllegalArgumentException If the location is already a shelter in the list.
     */
    public void addShelter(Location location) throws NullPointerException, IllegalArgumentException {
        if (location == null) {
            throw new NullPointerException("The location provided cannot be null");
        }

        if (inList(location) != null) {
            throw new IllegalArgumentException("The location is already a shelter");
        } else {
            this.shelters.add(location);
        }
    }


    /**
     * Removes a shelter from the list of shelters.
     *
     * @param location The location representing the shelter to be removed.
     * @throws NullPointerException     If the provided shelter location is null.
     * @throws IllegalArgumentException If the location is not found in the list of shelters.
     */
    public void removeShelter(Location location) throws NullPointerException, IllegalArgumentException {
        if (location == null) {
            throw new NullPointerException("The shelter provided cannot be null");
        }

        Location locationToRemove = inList(location);

        if (locationToRemove != null) {
            this.shelters.remove(locationToRemove);
        } else {
            throw new IllegalArgumentException("The location is not a shelter");
        }
    }


    /**
     * Retrieves the list of shelters.
     *
     * @return The list of shelters.
     */
    public LinkedList<Location> getShelters() {
        return shelters;
    }


    /**
     * Sets the list of shelters.
     *
     * @param shelters The new list of shelters to set.
     */
    public void setShelters(LinkedList<Location> shelters) {
        this.shelters.clear();
        this.shelters.addAll(shelters);
    }


    /**
     * Retrieves the worker ID associated with this ReliefService instance.
     *
     * @return The worker ID.
     */
    public int getWorkerId() {
        return workerId;
    }


    /**
     * Retrieves the current value of the worker ID counter.
     *
     * @return The current value of the worker ID counter.
     */
    public static int getWorkerIdCounter() {
        return WORKER_ID_COUNTER;
    }


    /**
     * Checks if the specified location is present in the list of shelters.
     *
     * @param elementToFind The location to search for.
     * @return The first found location with the same name and address as the specified elementToFind,
     *         or null if no such location is found.
     */
    public Location inList(Location elementToFind) {
        for (Location location : shelters) {
            if (location.getName().equals(elementToFind.getName()) && location.getAddress().equals(elementToFind.getAddress())) {
                return location;
            }
        }
        return null;
    }

}

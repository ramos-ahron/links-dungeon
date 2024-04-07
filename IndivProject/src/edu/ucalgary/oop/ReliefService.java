package edu.ucalgary.oop;

import java.util.LinkedList;

public class ReliefService {
    private static int WORKER_ID_COUNTER = 1;
    private final int workerId;

    private final LinkedList<Location> shelters = new LinkedList<>();

    public ReliefService() {
        workerId = WORKER_ID_COUNTER ++;
    }

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

    public LinkedList<Location> getShelters() {
        return shelters;
    }

    public void setShelters(LinkedList<Location> shelters) {
        this.shelters.clear();
        this.shelters.addAll(shelters);
    }

    public int getWorkerId() {
        return workerId;
    }

    public Location inList(Location elementToFind) {
        for (Location location : shelters) {
            if (location.getName().equals(elementToFind.getName()) && location.getAddress().equals(elementToFind.getAddress())) {
                return location;
            }
        }
        return null;
    }

}

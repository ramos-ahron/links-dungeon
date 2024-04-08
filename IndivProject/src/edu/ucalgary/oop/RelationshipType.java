package edu.ucalgary.oop;

public enum RelationshipType {
    GUARDIAN_WARD("Guardian-Ward"),
    PARENT_CHILD("Parent-Child"),
    SIBLING("Sibling"),
    FRIEND("Friend");

    private final String displayName;

    RelationshipType(String displayName) {
        this.displayName = displayName;
    }

    @Override
    public String toString() {
        return displayName;
    }
}

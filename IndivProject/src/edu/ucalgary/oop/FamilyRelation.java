package edu.ucalgary.oop;

import java.util.HashSet;

public class FamilyRelation {
    private DisasterVictim personOne;
    private String relationshipTo;
    private DisasterVictim personTwo;

    private HashSet<FamilyRelation> currentRelations = new HashSet<>();

    public FamilyRelation(DisasterVictim personOne, String relationshipTo, DisasterVictim personTwo) {
        this.personOne = personOne;
        this.relationshipTo = relationshipTo;
        this.personTwo = personTwo;
    }

    public DisasterVictim getPersonOne() {
        return personOne;
    }

    public void setPersonOne(DisasterVictim personOne) {
        this.personOne = personOne;
    }

    public String getRelationshipTo() {
        return relationshipTo;
    }

    public void setRelationshipTo(String relationshipTo) {
        this.relationshipTo = relationshipTo;
    }

    public DisasterVictim getPersonTwo() {
        return personTwo;
    }

    public void setPersonTwo(DisasterVictim personTwo) {
        this.personTwo = personTwo;
    }

    public HashSet<FamilyRelation> getCurrentRelations() {
        return currentRelations;
    }

    public void setCurrentRelations(HashSet<FamilyRelation> currentRelations) {
        this.currentRelations = currentRelations;
    }

    public boolean isEqualTo(FamilyRelation relationOne, FamilyRelation relationTwo) {
        // Compare two FamilyRelation objects and return true if they are equal, otherwise return false
        // Implement your logic here
        return true;
    }
}

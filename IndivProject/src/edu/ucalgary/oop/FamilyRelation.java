package edu.ucalgary.oop;

import java.util.HashSet;

public class FamilyRelation {
    private DisasterVictim personOne;
    private RelationshipType relationshipType;
    private DisasterVictim personTwo;

    private HashSet<FamilyRelation> currentRelations = new HashSet<>();

    public FamilyRelation(DisasterVictim personOne, DisasterVictim personTwo, RelationshipType relationshipType) {
        this.personOne = personOne;
        this.personTwo = personTwo;
        this.relationshipType = relationshipType;
    }

    public DisasterVictim getPersonOne() {
        return personOne;
    }

    public void setPersonOne(DisasterVictim personOne) {
        this.personOne = personOne;
    }

    public RelationshipType getRelationshipType() {
        return relationshipType;
    }

    public void setRelationshipType(RelationshipType relationshipType) {
        this.relationshipType = relationshipType;
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

    @Override
    public boolean equals(Object obj) {
        if (this == obj) {
            return true;
        }
        if (obj == null) {
            return false;
        }
        if (getClass() != obj.getClass()) {
            return false;
        }
        FamilyRelation other = (FamilyRelation) obj;
        return this.personOne.getAssignedSocialID() == other.personOne.getAssignedSocialID() &&
                this.personTwo.getAssignedSocialID() == other.personTwo.getAssignedSocialID() &&
                this.relationshipType == other.relationshipType;
    }
}

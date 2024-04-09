package edu.ucalgary.oop;

import java.util.HashSet;

public class FamilyRelation {
    private DisasterVictim personOne;
    private RelationshipType relationshipType;
    private DisasterVictim personTwo;

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

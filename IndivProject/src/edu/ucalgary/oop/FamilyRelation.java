package edu.ucalgary.oop;

import java.util.HashSet;

public class FamilyRelation {
    private DisasterVictim personOne;
    private RelationshipType relationshipType;
    private DisasterVictim personTwo;

    /**
     * Constructs a FamilyRelation object representing the relationship between two DisasterVictim objects.
     *
     * @param personOne        the first DisasterVictim involved in the relationship
     * @param personTwo        the second DisasterVictim involved in the relationship
     * @param relationshipType the type of relationship between the two victims
     */
    public FamilyRelation(DisasterVictim personOne, DisasterVictim personTwo, RelationshipType relationshipType) {
        this.personOne = personOne;
        this.personTwo = personTwo;
        this.relationshipType = relationshipType;
    }

    /**
     * Retrieves the first DisasterVictim involved in the relationship.
     *
     * @return the first DisasterVictim involved in the relationship
     */
    public DisasterVictim getPersonOne() {
        return personOne;
    }


    /**
     * Sets the first DisasterVictim involved in the relationship.
     *
     * @param personOne the first DisasterVictim to set in the relationship
     */
    public void setPersonOne(DisasterVictim personOne) {
        this.personOne = personOne;
    }


    /**
     * Retrieves the type of relationship between two disaster victims.
     *
     * @return the RelationshipType representing the type of relationship
     */
    public RelationshipType getRelationshipType() {
        return relationshipType;
    }


    /**
     * Sets the type of relationship between two disaster victims.
     *
     * @param relationshipType the RelationshipType to set for the relationship
     */
    public void setRelationshipType(RelationshipType relationshipType) {
        this.relationshipType = relationshipType;
    }


    /**
     * Retrieves the second disaster victim involved in the family relationship.
     *
     * @return the second disaster victim involved in the relationship
     */
    public DisasterVictim getPersonTwo() {
        return personTwo;
    }


    /**
     * Sets the second disaster victim involved in the family relationship.
     *
     * @param personTwo the second disaster victim to set in the relationship
     */
    public void setPersonTwo(DisasterVictim personTwo) {
        this.personTwo = personTwo;
    }


    /**
     * Indicates whether some other object is "equal to" this one.
     *
     * @param obj the reference object with which to compare
     * @return true if this object is the same as the obj argument; false otherwise
     */
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

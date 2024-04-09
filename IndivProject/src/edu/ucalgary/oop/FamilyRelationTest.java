package edu.ucalgary.oop;

import org.junit.Test;
import static org.junit.Assert.*;

public class FamilyRelationTest {
    FamilyRelation testRelation = new FamilyRelation(new DisasterVictim("Ahron", "Ramos"), new DisasterVictim("Derick", "White"), RelationshipType.SIBLING);

    @Test
    public void testObjectCreation() {
        assertNotNull(testRelation);
    }

    @Test
    public void testGetPersonOne() {
        DisasterVictim personOne = new DisasterVictim("John");
        DisasterVictim personTwo = new DisasterVictim("Cena");
        FamilyRelation familyRelation = new FamilyRelation(personOne, personTwo, RelationshipType.SIBLING);

        assertEquals("getPersonOne() should return the first DisasterVictim involved in the relationship", personOne, familyRelation.getPersonOne());
    }

    @Test
    public void testSetPersonOne() {
        DisasterVictim personOne = new DisasterVictim("John");
        DisasterVictim personTwo = new DisasterVictim("Cena");
        FamilyRelation familyRelation = new FamilyRelation(personOne, personTwo, RelationshipType.SIBLING);

        DisasterVictim newPersonOne = new DisasterVictim("Taylor");

        familyRelation.setPersonOne(newPersonOne);

        assertEquals("setPersonOne() should set the first DisasterVictim involved in the relationship", newPersonOne, familyRelation.getPersonOne());
    }

    @Test
    public void testGetRelationshipType() {
        DisasterVictim personOne = new DisasterVictim("John");
        DisasterVictim personTwo = new DisasterVictim("Cena");
        RelationshipType relationshipType = RelationshipType.SIBLING;
        FamilyRelation familyRelation = new FamilyRelation(personOne, personTwo, relationshipType);

        assertEquals("getRelationshipType() should return the type of relationship", relationshipType, familyRelation.getRelationshipType());
    }

    @Test
    public void testSetRelationshipType() {
        DisasterVictim personOne = new DisasterVictim("John");
        DisasterVictim personTwo = new DisasterVictim("Cena");
        RelationshipType initialRelationshipType = RelationshipType.SIBLING;
        RelationshipType newRelationshipType = RelationshipType.PARENT_CHILD;
        FamilyRelation familyRelation = new FamilyRelation(personOne, personTwo, initialRelationshipType);

        familyRelation.setRelationshipType(newRelationshipType);

        assertEquals("setRelationshipType() should set the type of relationship", newRelationshipType, familyRelation.getRelationshipType());
    }

    @Test
    public void testGetPersonTwo() {
        DisasterVictim personOne = new DisasterVictim("John");
        DisasterVictim personTwo = new DisasterVictim("Cena");
        RelationshipType relationshipType = RelationshipType.SIBLING;
        FamilyRelation familyRelation = new FamilyRelation(personOne, personTwo, relationshipType);

        assertEquals("getPersonTwo() should return the second DisasterVictim involved in the relationship", personTwo, familyRelation.getPersonTwo());
    }

    @Test
    public void testSetPersonTwo() {
        DisasterVictim personOne = new DisasterVictim("John");
        DisasterVictim personTwo = new DisasterVictim("Cena");
        RelationshipType relationshipType = RelationshipType.SIBLING;
        FamilyRelation familyRelation = new FamilyRelation(personOne, personTwo, relationshipType);

        DisasterVictim newPersonTwo = new DisasterVictim("Taylor");

        familyRelation.setPersonTwo(newPersonTwo);

        assertEquals("setPersonTwo() should set the second DisasterVictim involved in the relationship", newPersonTwo, familyRelation.getPersonTwo());
    }

    @Test
    public void testEquals() {
        DisasterVictim personOne = new DisasterVictim("John");
        DisasterVictim personTwo = new DisasterVictim("Cena");
        RelationshipType relationshipType = RelationshipType.SIBLING;

        FamilyRelation relation1 = new FamilyRelation(personOne, personTwo, relationshipType);
        FamilyRelation relation2 = new FamilyRelation(personOne, personTwo, relationshipType);

        assertEquals("equals() should return true for two FamilyRelation objects with the same parameters", relation1, relation2);
    }
}

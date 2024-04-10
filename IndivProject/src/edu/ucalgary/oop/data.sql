CREATE TABLE Location (
    location_id 			SERIAL PRIMARY KEY,
    name 							VARCHAR(255) NOT NULL,
    address 					VARCHAR(255) NOT NULL,
		shelter 					BOOLEAN NOT NULL
);


CREATE TABLE DisasterVictim (
    victim_id 				SERIAL PRIMARY KEY,
    first_name				VARCHAR(255) NOT NULL,
		last_name					VARCHAR(255),
		entry_date 				DATE,
		gender 						VARCHAR(20),
    comments 					TEXT,
    date_of_birth 		DATE,
    location_id 			INT NOT NULL,
    FOREIGN KEY (location_id) REFERENCES Location(location_id) ON DELETE CASCADE
);


CREATE TABLE Supply (
    supply_id 				SERIAL PRIMARY KEY,
    type 							VARCHAR(255) NOT NULL,
    quantity 					INT NOT NULL,
    reference_type 		VARCHAR(20) NOT NULL,
    reference_id 			INT NOT NULL,
    FOREIGN KEY (reference_id) REFERENCES Location(location_id) ON DELETE CASCADE,
    FOREIGN KEY (reference_id) REFERENCES DisasterVictim(victim_id) ON DELETE CASCADE
);


CREATE TABLE MedicalRecord (
    record_id SERIAL PRIMARY KEY,
    treatment_details	TEXT,
    victim_id 				INT,
    location_id 			INT,
    date_of_treatment	DATE,
    FOREIGN KEY (victim_id) REFERENCES DisasterVictim(victim_id) ON DELETE CASCADE,
    FOREIGN KEY (location_id) REFERENCES Location(location_id) ON DELETE CASCADE
);


CREATE TABLE Relationship (
    relationship_id 	SERIAL PRIMARY KEY,
    relationship_type VARCHAR(255) NOT NULL,
    victim1_id 				INT NOT NULL,
    victim2_id 				INT NOT NULL,
    FOREIGN KEY (victim1_id) REFERENCES DisasterVictim(victim_id) ON DELETE CASCADE,
    FOREIGN KEY (victim2_id) REFERENCES DisasterVictim(victim_id) ON DELETE CASCADE
);


CREATE TABLE DietaryRestriction (
		restriction_id		SERIAL PRIMARY KEY,
		restriction_name	VARCHAR(50) NOT NULL,
		victim_id					INT,
		FOREIGN KEY (victim_id) REFERENCES DisasterVictim(victim_id) ON DELETE CASCADE
);


INSERT INTO Location (name, address, shelter) VALUES
    ('Maple Grove Hospital', '123 Main St', true),
    ('UrgentCare Emergency Center', '456 Elm Street', true),
    ('Meadowview Retirement Village', '789 Oak Street', false);


INSERT INTO DisasterVictim (first_name, last_name, entry_date, comments, date_of_birth, location_id) VALUES
		('John', 'Doe', '2024-04-01', 'Injured leg', '1994-01-01', 1),
		('Jane', 'Doe', '2024-04-03', 'Needs medication', '1999-05-15', 2),
    ('Alice', 'Smith', '2024-04-05', 'Fractured arm', '1984-03-10', 2),
    ('Bob', 'Johnson', '2024-04-07', 'Severe cough', '1989-08-20', 3);


INSERT INTO Supply (type, quantity, reference_type, reference_id) VALUES
    ('Splints', 50, 'Location', 1),       
    ('Bottled Water', 30, 'Location', 1),     
    ('Canned Food', 20, 'Location', 1), 
		
    ('Blankets', 20, 'Location', 2),         
    ('Bottled Water', 30, 'Location', 2),     
    ('Canned Food', 20, 'Location', 2),
		
		('Splints', 3, 'Victim', 2), 
		('Disinfectants', 1, 'Victim', 3),
		('Burn Cream', 2, 'Victim', 1);


INSERT INTO MedicalRecord (treatment_details, victim_id, location_id, date_of_treatment) VALUES
		('Applied bandage to leg', 1, 1, '2024-04-02'),
		('Prescribed medication', 2, 2, '2024-04-04'),
		('Applied a cast to the fractured arm', 3, 2, '2024-04-05'),
		('Administered cough syrup for symptom relief', 4, 1, '2024-04-07');


INSERT INTO Relationship (relationship_type, victim1_id, victim2_id) VALUES
		('Couple', 1, 2),
		('Friend', 1, 3),
		('Friend', 3, 4);


INSERT INTO DietaryRestriction (restriction_name, victim_id) VALUES
		('Asian vegetarian meal', 1),
		('Diabetic meal', 2),
    ('Gluten intolerant meal', 3),
    ('Kosher meal', 4);
		
CREATE USER oop password 'ucalgary';
ALTER DATABASE ensf380project OWNER TO oop;

GRANT ALL PRIVILEGES ON TABLE inquirer TO oop;
GRANT ALL PRIVILEGES ON TABLE inquiry_log TO oop;
GRANT ALL PRIVILEGES ON TABLE dietaryrestriction TO oop;
GRANT ALL PRIVILEGES ON TABLE disastervictim TO oop;
GRANT ALL PRIVILEGES ON TABLE disastervictimdietaryrestriction TO oop;
GRANT ALL PRIVILEGES ON TABLE location TO oop;
GRANT ALL PRIVILEGES ON TABLE medicalrecord TO oop;
GRANT ALL PRIVILEGES ON TABLE relationship TO oop;
GRANT ALL PRIVILEGES ON TABLE supply TO oop;

GRANT ALL PRIVILEGES ON SEQUENCE inquirer_id_seq TO oop;
GRANT ALL PRIVILEGES ON SEQUENCE inquiry_log_id_seq TO oop;
GRANT ALL PRIVILEGES ON SEQUENCE location_location_id_seq TO oop;
GRANT ALL PRIVILEGES ON SEQUENCE disastervictim_victim_id_seq TO oop;
GRANT ALL PRIVILEGES ON SEQUENCE supply_supply_id_seq TO oop;
GRANT ALL PRIVILEGES ON SEQUENCE medicalrecord_record_id_seq TO oop;
GRANT ALL PRIVILEGES ON SEQUENCE relationship_relationship_id_seq TO oop;
GRANT ALL PRIVILEGES ON SEQUENCE dietaryrestriction_restriction_id_seq TO oop;

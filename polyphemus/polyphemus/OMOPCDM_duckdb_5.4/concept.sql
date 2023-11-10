CREATE TABLE @cdmDatabaseSchema.concept (
			concept_id integer NOT NULL PRIMARY KEY,
			concept_name varchar(255) NOT NULL,
			domain_id varchar(20) NOT NULL,
			vocabulary_id varchar(20) NOT NULL,
			concept_class_id varchar(20) NOT NULL,
			standard_concept varchar(1) NULL,
			concept_code varchar(50) NOT NULL,
			valid_start_date date NOT NULL,
			valid_end_date date NOT NULL,
			invalid_reason varchar(1),
    
            FOREIGN KEY (domain_id) REFERENCES @cdmDatabaseSchema.DOMAIN (DOMAIN_ID),
            FOREIGN KEY (vocabulary_id) REFERENCES @cdmDatabaseSchema.VOCABULARY (VOCABULARY_ID),
            FOREIGN KEY (concept_class_id) REFERENCES @cdmDatabaseSchema.CONCEPT_CLASS (CONCEPT_CLASS_ID)
            );
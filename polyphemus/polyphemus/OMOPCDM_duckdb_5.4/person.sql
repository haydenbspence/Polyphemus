CREATE TABLE @cdmDatabaseSchema.person (
			person_id integer NOT NULL PRIMARY KEY,
			gender_concept_id integer NOT NULL,
			year_of_birth integer NOT NULL,
			month_of_birth integer NULL,
			day_of_birth integer NULL,
			birth_datetime TIMESTAMP NULL,
			race_concept_id integer NOT NULL,
			ethnicity_concept_id integer NOT NULL,
			location_id integer NULL,
			provider_id integer NULL,
			care_site_id integer NULL,
			person_source_value varchar(50) NULL,
			gender_source_value varchar(50) NULL,
			gender_source_concept_id integer NULL,
			race_source_value varchar(50) NULL,
			race_source_concept_id integer NULL,
			ethnicity_source_value varchar(50) NULL,
			ethnicity_source_concept_id integer NULL,
			
			FOREIGN KEY (gender_concept_id) REFERENCES @cdmDatabaseSchema.concept (concept_id),
			FOREIGN KEY (race_concept_id) REFERENCES @cdmDatabaseSchema.concept (concept_id),
			FOREIGN KEY (ethnicity_concept_id) REFERENCES @cdmDatabaseSchema.concept (concept_id)
			);
import os
import toml
import ibis

# Load the TOML file
with open('config.toml', 'r') as f:
    config = toml.load(f)

# Set the environment variables
for key, value in config.items():
    os.environ[key] = str(value)

from models import Person

def insert_person(person: Person):

    conn = ibis.duckdb.connect('md:Eunomia')

    conn.execute("INSERT INTO person VALUES (?, ?, ?, ?, ?, ?)",
                 [person.person_id, person.gender_concept_id, person.year_of_birth,
                  person.race_concept_id, person.ethnicity_concept_id, person.person_source_value])

def get_person(person_id: int):

    conn = ibis.duckdb.connect('md:Eunomia')

    result = conn.execute("SELECT * FROM person WHERE person_id = ?", [person_id]).fetchone()
    
    if result:
        return {
            "person_id": result[0],
            "gender_concept_id": result[1],
            "year_of_birth": result[2],
            "race_concept_id": result[3],
            "ethnicity_concept_id": result[4],
            "person_source_value": result[5]
        }
    else:
        return
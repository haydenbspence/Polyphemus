import duckdb
from models import Person

conn = duckdb.connect(database='omop54.db', read_only=False)

def execute_ddl_file(file_path, schema_name):

    with open(file_path, 'r') as file:
        sql_commands = file.read()

    sql_commands = sql_commands.replace('@cdmDatabaseSchema', schema_name)

    conn = duckdb.connect()

    conn.execute(f'CREATE SCHEMA {schema_name}')
    conn.execute(sql_commands)

def execute_primary_keys_file(file_path, schema_name):

    with open(file_path, 'r') as file:
        sql_commands = file.read()

    sql_commands = sql_commands.replace('@cdmDatabaseSchema', schema_name)

    conn = duckdb.connect()

    conn.execute(sql_commands)

def init_db(schema_name):
    execute_ddl_file('./ddl/OMOPCDM_duckdb_5.4_ddl.sql', schema_name)
        

def insert_person(person: Person):
    conn.execute("INSERT INTO person VALUES (?, ?, ?, ?, ?, ?)",
                 [person.person_id, person.gender_concept_id, person.year_of_birth,
                  person.race_concept_id, person.ethnicity_concept_id, person.person_source_value])


def get_person(person_id: int):
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
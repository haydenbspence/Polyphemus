from fastapi import FastAPI
from models import Person
import database

app = FastAPI()
schema_name = 'cdm'

@app.get("/tables/")
async def tables():
    table_list = database.list_tables()
    return table_list

@app.post("/person/")
async def create_person(person: Person):
    database.insert_person(person)
    return {"message": "Person added successfully"}

@app.get("/person/{person_id}")
async def get_person(person_id: int):
    person = database.get_person(person_id)
    if person:
        return person
    else:
        return {"message": "Person not found"}

def run():
    import uvicorn
    uvicorn.run("polyphemus.main:app", host="0.0.0.0", port=8000)

if __name__ == "__main__":
    run()

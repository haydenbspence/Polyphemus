import requests

# URL of the FastAPI server
url = 'http://127.0.0.1:8000/person/'

# List of people data
people_data = [
    {
        "person_id": 12345,
        "gender_concept_id": 1,
        "year_of_birth": 1980,
        "race_concept_id": 2,
        "ethnicity_concept_id": 3,
        "person_source_value": "example_source_value_1"
    },
    {
        "person_id": 12346,
        "gender_concept_id": 2,
        "year_of_birth": 1985,
        "race_concept_id": 3,
        "ethnicity_concept_id": 4,
        "person_source_value": "example_source_value_2"
    },
    {
        "person_id": 12347,
        "gender_concept_id": 1,
        "year_of_birth": 1990,
        "race_concept_id": 4,
        "ethnicity_concept_id": 5,
        "person_source_value": "example_source_value_3"
    }
]

for person_data in people_data:
    try:
        response = requests.post(url, json=person_data)
        if response.status_code == 200:
            print('Person ID:', person_data['person_id'])
            print('Status Code:', response.status_code)
            print('Response:', response.json())
        else:
            print('Error with Person ID:', person_data['person_id'])
            print('Status Code:', response.status_code)
            print('Response:', response.json())

    except requests.exceptions.RequestException as e:
        # Handle any requests-related errors here
        print('Request failed for Person ID:', person_data['person_id'])
        print(e)

    print('-----------------------')

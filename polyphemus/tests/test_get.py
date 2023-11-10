import requests

# URL of the FastAPI server
base_url = 'http://127.0.0.1:8000/person/'

# List of person_ids to retrieve
person_ids = [12345, 12346, 12347]  # Add the person_ids you want to retrieve

for person_id in person_ids:
    # Constructing the full URL for each GET request
    get_url = f"{base_url}{person_id}"

    response = requests.get(get_url)

    print('Fetching data for Person ID:', person_id)
    print('Status Code:', response.status_code)
    
    if response.status_code == 200:
        print('Response:', response.json())
    else:
        print('Error occurred:', response.text)

    print('-----------------------')

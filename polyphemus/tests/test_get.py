import requests

# URL of the FastAPI server
base_url = 'https://api.haydenspence.com/list_table/'

response = requests.get(base_url)

print('Status Code:', response.status_code)

if response.status_code == 200:
    print('Response:', response.json())
else:
    print('Error occurred:', response.text)

print('-----------------------')

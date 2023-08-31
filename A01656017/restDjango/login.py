import requests
api_url = 'http://127.0.0.1:8000/users/'
response = requests.get(api_url, auth=('A01656017','password'))
response.json
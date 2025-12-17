import requests
from time import sleep
import json

peso_id = 4
estatura_id = 20

url = f'http://127.0.0.1:8000/calcula_imc_id/{peso_id}/{estatura_id}'

response = requests.get(url)

print(response.json())


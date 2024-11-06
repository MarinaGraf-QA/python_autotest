import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '0c6859b3132699f2221c11addd3f7dd1'
HEADER = {'Content-Type': 'application/json', 'trainer_token':TOKEN}
body_creation = {
    "name": "FurFurFur",
    "photo_id": 73
}

body_change = {
    "pokemon_id": "125197",
    "name": "Forbs",
    "photo_id": 73
}

body_pokeball = {
    "pokemon_id": "125197"
}

response = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_creation)
print(response.text)

response = requests.put(url = f'{URL}/pokemons', headers = HEADER, json =  body_change)
print(response.text)

response = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json =  body_pokeball)
print(response.text)
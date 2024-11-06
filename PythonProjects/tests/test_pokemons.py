import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '0c6859b3132699f2221c11addd3f7dd1'
HEADER = {'Content-Type': 'application/json', 'trainer_token':TOKEN}
TRAINER_ID = '8292'

def test_status_code():
    response = requests.get(url = f'{URL}/trainers', params = {'level': '3'})
    assert response.status_code == 200

def test_name_trainer():
        response_get = requests.get(url = f'{URL}/trainers', params = {'trainer_id': TRAINER_ID})
        assert response_get.json() ["data"][0]["trainer_name"] == 'CrazyMev'


@pytest.mark.parametrize('key,value',[("trainer_name", "CrazyMev"),("id", TRAINER_ID)])
def test_parametrize(key, value):
      response_parametrize = requests.get(url = f'{URL}/trainers', params = {'trainer_id': TRAINER_ID})
      assert response_parametrize.json()["data"][0][key] == value
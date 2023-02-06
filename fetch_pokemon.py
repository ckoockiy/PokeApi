
import requests
from PIL import Image
from io import BytesIO


def getPokemon(number):
    pokemon = []

    data = requests.get(f"https://pokeapi.co/api/v2/pokemon/{number}")

    nombre = data.json()['forms'][0]['name']
    imagen = data.json()['sprites']['front_default']
    hp = data.json()['stats'][0]['base_stat']
    attack = data.json()['stats'][1]['base_stat']
    defense = data.json()['stats'][2]['base_stat']
    special_attack = data.json()['stats'][3]['base_stat']
    special_defense = data.json()['stats'][4]['base_stat']
    speed = data.json()['stats'][5]['base_stat']

    response = requests.get(imagen).content
    
    pokemon.append([nombre, response, hp, attack, defense,
                    special_attack, special_defense, speed])
    
    return pokemon

"""
def getPokemon_opc_two(number):
    data = requests.get(f"https://pokeapi.co/api/v2/pokemon/{number}")
    pokemon_data = data.json()
    
    pokemon = [
        pokemon_data['forms'][0]['name'],
        requests.get(pokemon_data['sprites']['front_default']).content,
        *[stat['base_stat'] for stat in pokemon_data['stats']]
    ]
    
    return [pokemon]
"""
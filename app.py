from flask import Flask
import redis
import os
from dotenv import load_dotenv
from enum import Enum
import json

app = Flask(__name__)
load_dotenv()

# Redis
redis_host = os.getenv("REDIS_HOST")
redis_port = os.getenv("REDIS_PORT")
redis_password = os.getenv("REDIS_PASSWORD")

class DataTypes(Enum):
    ITEMS = 1
    POKEMON = 2
    MOVES = 3
    ABILITIES = 4
    LOCATIONS = 5

redis_pokemon_client = redis.StrictRedis(host=redis_host, port=redis_port, password=redis_password, decode_responses=True, db=DataTypes.POKEMON.value)
redis_items_client = redis.StrictRedis(host=redis_host, port=redis_port, password=redis_password, decode_responses=True, db=DataTypes.ITEMS.value)
redis_moves_client = redis.StrictRedis(host=redis_host, port=redis_port, password=redis_password, decode_responses=True, db=DataTypes.MOVES.value)
redis_abilities_client = redis.StrictRedis(host=redis_host, port=redis_port, password=redis_password, decode_responses=True, db=DataTypes.ABILITIES.value)
redis_locations_client = redis.StrictRedis(host=redis_host, port=redis_port, password=redis_password, decode_responses=True, db=DataTypes.LOCATIONS.value)

def get_pokemon(dex):
    print('Get Pokemon #' + str(dex))
    return redis_pokemon_client.get(dex)

def get_item(id):
    print('Get Item #' + str(id))
    return redis_items_client.get(id)

def get_move(id):
    print('Get Move #' + str(id))
    return redis_moves_client.get(id)

def get_ability(id):
    print('Get Ability #' + str(id))
    return redis_abilities_client.get(id)

def get_location(name):
    print('Get Location #' + name)
    return redis_locations_client.get(name)

@app.route('/')
def hello():
    return "Hello, World!"

@app.route('/celina')
def celina():
    return "I love you Celina!!"

@app.route('/api/pokemmo/pokemon/<int:dex>')
def pokemon(dex):
    return get_pokemon(dex)

@app.route('/api/pokemmo/item/<int:id>')
def item(id):
    return get_item(id)

@app.route('/api/pokemmo/move/<int:id>')
def move(id):
    return get_move(id)

@app.route('/api/pokemmo/ability/<int:id>')
def ability(id):
    return get_ability(id)

@app.route('/api/pokemmo/location/<string:name>')
def location(name):
    return get_location(name)

@app.route('/api/pokemmo/locations')
def locations():
    locations = []
    for key in redis_locations_client.keys():
        locationData = redis_locations_client.get(key)
        locationJson = json.loads(locationData)
        locations.append(locationJson)
    return locations

@app.route('/api/pokemmo/pokemons')
def pokemons():
    pokemons = []
    for key in redis_pokemon_client.keys():
        pokemonData = redis_pokemon_client.get(key)
        pokemonJson = json.loads(pokemonData)
        pokemons.append(pokemonJson)
    return pokemons

@app.route('/api/pokemmo/items')
def items():
    items = []
    for key in redis_items_client.keys():
        itemsData = redis_items_client.get(key)
        itemsJson = json.loads(itemsData)
        items.append(itemsJson)
    return items

@app.route('/api/pokemmo/moves')
def moves():
    moves = []
    for key in redis_moves_client.keys():
        movesData = redis_moves_client.get(key)
        movesJson = json.loads(movesData)
        moves.append(movesJson)
    return moves

@app.route('/api/pokemmo/abilities')
def abilities():
    abilities = []
    for key in redis_abilities_client.keys():
        abilitiesData = redis_abilities_client.get(key)
        abilitiesJson = json.loads(abilitiesData)
        abilities.append(abilitiesJson)
    return abilities
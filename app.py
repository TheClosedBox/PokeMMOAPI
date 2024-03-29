from flask import Flask
import redis
import os
from dotenv import load_dotenv
from enum import Enum

app = Flask(__name__)
load_dotenv()

# Redis
redis_host = os.getenv("REDIS_HOST")
redis_port = os.getenv("REDIS_PORT")
redis_password = os.getenv("REDIS_PASSWORD")

class DataTypes(Enum):
    ITEMS = 1
    POKEMON = 2
    MOVES = 3,
    ABILITIES = 4,
    LOCATIONS = 5

pokemon_client = redis.Redis(host=redis_host, port=redis_port, password=redis_password, db=DataTypes.POKEMON.value)
item_client = redis.Redis(host=redis_host, port=redis_port, password=redis_password, db=DataTypes.ITEMS.value)
move_client = redis.Redis(host=redis_host, port=redis_port, password=redis_password, db=DataTypes.MOVES.value)
ability_client = redis.Redis(host=redis_host, port=redis_port, password=redis_password, db=DataTypes.ABILITIES.value)
location_client = redis.Redis(host=redis_host, port=redis_port, password=redis_password, db=DataTypes.LOCATIONS.value)

def get_pokemon(dex):
    print('Get Pokemon #' + str(dex))
    print(pokemon_client)
    return pokemon_client.get(dex)

def get_item(id):
    print('Get Item #' + str(id))
    print(item_client)
    return item_client.get(id)

def get_move(id):
    print('Get Move #' + str(id))
    print(move_client)
    return move_client.get(id)

def get_ability(id):
    print('Get Ability #' + str(id))
    print(ability_client)
    return ability_client.get(id)

def get_location(name):
    print('Get Location #' + str(name))
    print(location_client)
    return location_client.get(name)

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
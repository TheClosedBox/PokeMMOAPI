from flask import Flask
import redis
import os
from dotenv import load_dotenv

app = Flask(__name__)
load_dotenv()

# Redis
redis_host = os.getenv("REDIS_HOST")
redis_port = os.getenv("REDIS_PORT")
redis_password = os.getenv("REDIS_PASSWORD")
pokemon_db = os.getenv("POKEMON_DB")
item_db = os.getenv("ITEM_DB")
move_db = os.getenv("MOVE_DB")
pokemon_client = redis.Redis(host=redis_host, port=redis_port, password=redis_password, db=pokemon_db)
item_client = redis.Redis(host=redis_host, port=redis_port, password=redis_password, db=item_db)
move_client = redis.Redis(host=redis_host, port=redis_port, password=redis_password, db=move_db)

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
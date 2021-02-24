from flask import Flask , jsonify
import json
import random


app = Flask(__name__)

@app.route('/')
def comomasteguste():
    return "loquetedelagana"  

@app.route('/users/<user_name>')
def users_phrase(user_name):
    with open('bd.json') as file:
        data = json.load(file)
        return str(data[user_name])
    
@app.route('/users/<user_name>/random')
def random_phrase(user_name):
    with open('bd.json') as file:
        data = json.load(file)
        return str(data[user_name][random.randrange( 0, len(data[user_name]), 1)])
    
@app.route('/users/<user_name>/<id>')
def id_phrase(user_name,id):
    with open('bd.json') as file:
        data = json.load(file)
        return str(data[user_name][int(id)])

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8080, debug=True)

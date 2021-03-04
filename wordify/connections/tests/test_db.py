from wordify.connections.db import Connection
import json

def test_read_db():
    with open('resources/db.json', 'r') as file:
        data = json.load(file)       
        expected_return = data

    connect = Connection()
    function_return = connect.read_db()

    assert function_return == expected_return

def test_write_json():
    connect = Connection()
    function_return = connect.write_json({"paco": [{"id":'0', "data":'palo'}]})

    assert function_return == True

def test_write_db():
    connect = Connection()
    function_return = connect.write_db('elena', "tu opinion")

    assert function_return == True
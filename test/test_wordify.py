
from wordify import *
import json


def test_comomasteguste():
    expected_return = "loquetedelagana"
    sisoy = comomasteguste()
    assert sisoy == expected_return
 
def test_users_phrase():
    with open('../bd.json') as file:
        data = json.load(file)       
        expected_return = str(data["elena"])

    function_return = users_phrase("elena")

    assert function_return == expected_return

def test_random_phrase():
    with open('../bd.json') as file:
        data = json.load(file)       
        expected_return = str(data["elena"])

    function_return = random_phrase("elena")

    assert function_return in expected_return

def test_id_phrase():
    with open('../bd.json') as file:
        data = json.load(file)       
        expected_return = str(data["elena"][0])

    function_return = id_phrase("elena", 0)

    assert function_return == expected_return
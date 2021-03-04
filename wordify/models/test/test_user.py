from unittest import TestCase
from wordify.models.user import User


def values(): 
    name = "Amumu"
    phrases = [{"id":0,"data":"Dejame abrazarte"}, {"id":1,"data":"Seremos amigos para siempre"}]
    amumu = User(name, phrases)
    return amumu

def test_get_name():
    character = values()
    expected_return = "Amumu"
    
    value = character.get_name()
    assert value == expected_return

def test_get_phrases():
    character = values()
    expected_return = [{"id":0,"data":"Dejame abrazarte"}, {"id":1,"data":"Seremos amigos para siempre"}]
    
    value = character.get_phrases()
    assert value == expected_return

def test_get_id_phrase():
    character = values()
    expected_return = {"id":0,"data":"Dejame abrazarte"}

    value = character.get_id_phrase(0)
    assert value == expected_return

def test_set_name():
    character = values()
    expected_return = "Lux"

    character.set_name("Lux")
    value = character.get_name()
    assert value == expected_return

def test_add_phrase():
    character = values()
    expected_value = {"id":2,"data":"Vamos a buscar amigos"}

    add_value = "Vamos a buscar amigos"
    character.add_phrase(add_value)

    expected_values = character.get_phrases()
    assert expected_value in expected_values



    
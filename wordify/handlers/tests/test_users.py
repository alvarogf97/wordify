from unittest import mock
from wordify.handlers.users import phrases_random



def retrieve_by_id(id):
    pass

def user_serializer(user):
    pass

def test_random_phrase():
    id = 0
    serializer_return = [
        {
            "id" : 0,
            "phrase": "Soy una frase"
        },
        {
            "id" : 1,
            "phrase": "Soy una frase bis"
        }
        ]
    with mock.create_autospec(retrieve_by_id, return_value='object_user') as mock_retrieve:
        with mock.create_autospec(user_serializer, return_value=serializer_return) as mock_serializer:
            assert phrases_random(id) in serializer_return
            mock_retrieve.assert_called()
            mock_serializer_assert_called()

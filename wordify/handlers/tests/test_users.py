
from unittest import TestCase
from unittest import mock
from wordify.wsgi import make_app



class TestUserHandler(TestCase):
    
    @property
    def app(self):
        return make_app()
    
    @mock.patch('wordify.handlers.users.serializer')
    @mock.patch('wordify.handlers.users.userservice')
    def test_get_users_phrases_success(self, mock_userservice, mock_serializer):
        expected_id = 8
        expected_user = 'Juanma' 
        expected_result = {'Okay': ' '}

        mock_userservice.return_value = expected_user
        mock_serializer.return_value = expected_result

        with self.app.test_client() as c:
            response = c.get(f'/users/{expected_id}/phrases')
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.json, expected_result)
        mock_userservice.assert_called_once_with(expected_id)
        mock_serializer.assert_called_once_with(expected_user)

    @mock.patch('wordify.handlers.users.userservice')
    def test_get_users_phrases_user_not_found(self, mock_userservice):
        expected_id = 8
        expected_error = Exception('no found')
        expected_result = {'error': str(expected_error)}

        mock_userservice.side_effect = expected_error
        with self.app.test_client() as c:
            response = c.get(f'/users/{expected_id}/phrases')
            self.assertEqual(response.status_code, 404)
            self.assertEqual(response.json, expected_result)


    
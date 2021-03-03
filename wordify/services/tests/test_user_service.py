from unittest import mock
from unittest import TestCase
from wordify.services.user_service import errors
from wordify.services.user_service.factory import get_user_service
from wordify.services.user_service.backends.json import JsonUserService


class TestUserService(TestCase):

    def test_user_service_factory_json(self):
        backend = get_user_service()
        self.assertIsInstance(backend, JsonUserService)

    @mock.patch('os.getenv')
    def test_user_service_factory_backend_error(self, get_env_mock):
        get_env_mock.return_value = 'PALOMO'
        self.assertRaises(errors.UserServiceBackendError, get_user_service)

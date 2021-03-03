import os
from wordify.services.user_service import errors
from wordify.services.user_service.backends.json import JsonUserService


backends = {
    'JSON': JsonUserService
}


def get_user_service():
    backend = os.getenv('DB_TYPE', 'JSON')
    try:
        return backends[backend]()
    except KeyError:
        raise errors.UserServiceBackendError(f'backend not found: {backend}')

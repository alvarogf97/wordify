import abc


class UserService(abc.ABC):

    @abc.abstractmethod
    def get_user_by_id(self, identifier):
        pass

    @abc.abstractmethod
    def create_user(self, name, phrases=None):
        pass

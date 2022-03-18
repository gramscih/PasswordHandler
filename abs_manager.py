from abc import ABC, abstractmethod


class AbsManager(ABC):
    @staticmethod
    @abstractmethod
    def get_instance():
        pass
    @abstractmethod
    def write(self, data):
        pass

    @abstractmethod
    def read(self, app_name, id=None):
        pass

    @abstractmethod
    def update(self, app_name, new_pwd):
        pass

    @abstractmethod
    def delete(self, id):
        pass
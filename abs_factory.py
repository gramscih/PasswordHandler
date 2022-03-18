from abs_manager import AbsManager
from db_manager import DBManager
from file_manager import FileManager

# MANAGER_NAME = "DBManager"
MANAGER_NAME = "FileManager"

def get_manager_instance():
    types = AbsManager.__subclasses__()
    store_mgr = [t for t in types if t.__name__ == MANAGER_NAME][0]
    return store_mgr.get_instance()


# inst = get_manager_instance()
# print(inst)
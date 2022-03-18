from abs_manager import AbsManager

FILE_NAME = "pwd_db.txt"

class FileManager(AbsManager):
    __instance = None

    def __init__(self):
        FileManager.__instance = self

    @staticmethod
    def get_instance():
        if FileManager.__instance == None:
            FileManager()
        return FileManager.__instance

    def write(self, data):
        with open(FILE_NAME, "a") as file:
            file.write("{}: {}\n".format(data["app_name"], data["app_pwd"]))

    def read(self, app_name, id=None):
        with open(FILE_NAME, "r") as file:
            lines = file.read().split('\n')
            return [(line.split(':')[0], line.split(':')[1]) for line in lines if line.split(':')[0] == app_name][0]

    def update(self, app_name, new_pwd):
        pass

    def delete(self, id):
        pass

# file_manager = FileManager()
obj1 = FileManager.get_instance()
obj2 = FileManager()

print(obj1)
print(obj2)
# file_manager.write({"app_name": "Google", "app_pwd":"123qwerASD"})
# app = file_manager.read("Google")
# print(app)

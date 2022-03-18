import sqlite3

from abs_manager import AbsManager

class DBManager(AbsManager):
    __instance = None
    def __init__(self):
        DBManager.__instance = self
        self.db_connection = sqlite3.connect('AppPassword.db')
        self.cursor = self.db_connection.cursor()

    @staticmethod
    def get_instance():
        if DBManager.__instance == None:
            DBManager()
        return DBManager.__instance

    def write(self, data):
        script = "INSERT INTO app_pwd (app_name, app_pwd) VALUES ('{}', '{}')".format(
            data.get("app_name"), data.get("app_pwd"))
        self.cursor.execute(script)
        self.db_connection.commit()

    def read(self, app_name, id=None):
        script = "SELECT * FROM app_pwd WHERE app_name='{}'%s".format(app_name)
        script = script % "" if not id else script % " and id={}".format(id)
        rows = self.cursor.execute(script).fetchall()
        result = None

        for row in rows:
            result = (row[1], row[2])

        return result

    def update(self, app_name, new_pwd):
        script = f"UPDATE app_pwd SET app_pwd='{new_pwd}' WHERE app_name='{app_name}'"
        self.cursor.execute(script)
        self.db_connection.commit()

    def delete(self, id):
        pass

# db_manager = DBManager()
# # db_manager.write({"app_name": "Google", "app_pwd":"123qwerASD"})
# print(db_manager.read("google"))
# db_manager.get_instance()
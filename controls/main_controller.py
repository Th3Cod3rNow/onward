import data_base
from pathlib import Path
import sys

class Controller:
    def __init__(self):
        path = str(Path(__file__).resolve().parent.parent)
        sys.path.insert(0, path)
        self.BD = data_base.DataBase(way=path + "/DATABASES/users")

        self.base_user_params = {"task_list": list, "telegram_id": int, "alice_id": str}

    def log_in(self, user_name: str, password: str, telegram_id=None, alice_id=None):
        user = self.BD.get_user_by_user_name(user_name)
        if user:
            if user[2] == password:
                if telegram_id:
                    update = self.BD.update_user_by_user_name(user_name, {"telegram_id": telegram_id})
                    if update:
                        return True
                    return False
                if alice_id:
                    update = self.BD.update_user_by_user_name(user_name, {"alice_id": alice_id})
                    if update:
                        return True
                    return False
                return True

            return False
        return False

    def create_user(self, user_name: str, password: str):
        self.BD.insert_user(user_name, password)

    def update_user_base_params(self, user_id, params):
        if params in self.base_user_params and user_id:
            self.BD.update_user(user_id, params)
            return True
        else:
            return False

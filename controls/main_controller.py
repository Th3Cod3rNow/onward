import data_base
from pathlib import Path
import sys


class Controller:
    def __init__(self):
        path = str(Path(__file__).resolve().parent.parent)
        sys.path.insert(0, path)
        self.BD = data_base.DataBase(way=path + "/DATABASES/users")

        self.base_user_params = {
            "task_list",
            "telegram_id",
            "alice_id"
        }
        self.base_task_params = {
            "description",
            "task_name",
            "performer_id",
            "completed"
        }

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
        if user_name and password:
            self.BD.insert_user(user_name, password)
            return True
        return False

    def get_user_by_alice_id(self, alice_id):
        if alice_id:
            a_id = self.BD.get_user_by_alice_id(alice_id)
            return a_id
        return False

    def get_user_by_telegram_id(self, telegram_id):
        if telegram_id:
            t_id = self.BD.get_user_by_telegram_id(telegram_id)
            return t_id
        return False

    def update_user_base_params(self, user_id, params):
        updating_params = set(params.keys()) & self.base_user_params
        if len(updating_params) > 0 and user_id:
            update = self.BD.update_user_by_user_id(user_id, updating_params)
            if update:
                return True
            return False
        else:
            return False

    def create_task(self, author_id, name):
        if author_id and name:
            insertion = self.BD.insert_task(name, author_id)
            if insertion:
                return insertion
            return False
        return False

    def update_task(self, task_id, params):
        print(set(params.keys()) in self.base_task_params, set(params.keys()), self.base_task_params)
        updating_params = set(params.keys()) & self.base_task_params
        if len(updating_params) > 0 and task_id:
            update = self.BD.update_task_by_task_id(task_id, updating_params)
            if update:
                return True
            return False
        return False

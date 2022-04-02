import sqlite3

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
            "alice_id",
            "group_id"
        }
        self.base_task_params = {
            "description",
            "task_name",
            "performer_id",
            "completed",
            "group_id"
        }
        self.base_group_params = {
            "task_list",
            "user_list"
        }

    def log_in(self, user_name: str, password: str, telegram_id=None, alice_id=None):
        user = self.BD.get_user_by("user_name",user_name)
        if user:
            if user[2] == password:
                if telegram_id:
                    update = self.BD.update_user_by_user_name(user_name, {"telegram_id": telegram_id})
                    if update:
                        return user
                    return False
                elif alice_id:
                    update = self.BD.update_user_by_user_name(user_name, {"alice_id": alice_id})
                    if update:
                        return user
                    return False
                else:
                    return user

            return False
        return False

    def create_user(self, user_name: str, password: str):
        if user_name and password:
            user = self.BD.insert_user(user_name, password)
            return user
        return False

    def update_user_base_params(self, user_id, params):
        updating_params = set(params.keys()) & self.base_user_params
        print(updating_params, set(params.keys()), user_id)
        if updating_params == set(params.keys()) and user_id:
            update = self.BD.update_user_by_user_id(user_id, params)
            if update:
                return True
            return False
        else:
            return False

    def get_user_by(self, parameter, value):
        if parameter and value:
            user = self.BD.get_user_by(parameter,value)
            return user
    def create_task(self, author_id, name):
        if author_id and name:
            try:
                insertion = self.BD.insert_task(name, int(author_id))
                if insertion:
                    return insertion
                return False
            except sqlite3.IntegrityError:
                return False
        return False
    def get_tasks_by(self, parameter, value):
        tasks = self.BD.get_tasks_by(parameter, value)
        return tasks
    def update_task(self, task_id, params):
        updating_params = set(params.keys()) & self.base_task_params
        if updating_params == set(params.keys()) and task_id:
            update = self.BD.update_task_by_task_id(task_id, params)
            if update:
                return True
            return False
        return False

    def update_group(self, group_id, params):
        updating_params = set(params.keys()) & self.base_group_params
        if updating_params == set(params.keys()) and group_id:
            update = self.BD.update_group_by_group_id(group_id, params)
            if update:
                return True
            return False
        return False

    def create_group(self, group_name):
        if group_name:
            try:
                insertion = self.BD.insert_group(group_name)
                if insertion:
                    return insertion
                return False
            except sqlite3.IntegrityError:
                return False
        return False

    def get_groups(self):
        groups = self.BD.get_groups()
        return groups

    def get_task_by(self, parameter, value):
        if parameter and value:
            task = self.BD.get_task_by(parameter,value)
            return task
        return False

    def get_group_by(self, parameter, value):
        if parameter and value:
            group = self.BD.get_group_by(parameter, value)
            if group:
                return group
            return False
        return False
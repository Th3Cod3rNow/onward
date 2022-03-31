import sqlite3


def sqlite_lower(val: str):
    return val.lower()


def sqlite_upper(val: str):
    return val.upper()


def ignore_case_collation(val1: str, val2: str):
    if val1.lower() == val2.lower():
        return 0
    elif val1.lower() < val2.lower():
        return -1
    return 1


class DataBase:
    def __init__(self, way=None):
        self.connection=None
        if isinstance(way, str):
            try:
                connection = sqlite3.connect(way, check_same_thread=False)
                self.connection = connection
                self.connection.create_collation("NOCASE", ignore_case_collation)
                self.connection.create_function("LOWER", 1, sqlite_lower)
                self.connection.create_function("UPPER", 1, sqlite_upper)
            except FileNotFoundError:
                raise FileNotFoundError("Data base with way:", way, "- didn't found")
        else:
            raise TypeError("Way must be string")

    def insert_user(self, user_name, password):
        cursor = self.connection.cursor()
        cursor.execute(
            '''
            INSERT INTO video (user_name, password)
            VALUES (?,?)
            ''',
            (user_name, password,),
        )

        new_id = self.get_last_user()[0]
        cursor.close()
        self.connection.commit()  # save changes
        return new_id

    def get_last_user(self) -> list:
        """
        Returns last video in table
        :return last:
        """
        cursor = self.connection.cursor()
        cursor.execute(
            '''
            SELECT MAX(user_id) FROM users
            ''')
        last = cursor.fetchone()
        cursor.close()
        return last

    def insert_task(self, task_name, description, author_id, performer_id, completed=False):
        cursor = self.connection.cursor()
        cursor.execute(
            '''
            INSERT INTO tasks (task_name, description, author_id, performer_id, completed)
            VALUES (?,?,?,?,?)
            ''',
            (task_name, description, author_id, performer_id, completed,),
        )
        cursor.execute(
            '''
            UPDATE 
            ''')

        new_id = self.get_last_task()[0]
        cursor.close()
        self.connection.commit()  # save changes
        return new_id

    def get_last_task(self) -> list:
        """
        Returns last video in table
        :return last:
        """
        cursor = self.connection.cursor()
        cursor.execute(
            '''
            SELECT MAX(taks_id) FROM tasks
            ''')
        last = cursor.fetchone()
        cursor.close()
        return last

    def get_user_by_user_name(self, user_name:str) -> list:
        if user_name:
            cursor = self.connection.cursor()
            cursor.execute(
                '''
                SELECT * FROM users
                WHERE user_name = ?
                ''',
                (user_name,))
            user = cursor.fetchone()
            cursor.close()
            return user
        return list()
    def update_user_by_user_id(self, user_id, params):
        if params and user_id:
            values = params.values()
            items = [item for item in params.items()]

            cursor = self.connection.cursor()
            for item in params:
                cursor.execute(
                    "UPDATE users set "+item+" = ? WHERE user_id=?", (params[item],user_id,))
            self.connection.commit()
            cursor.close()
            return True
        else:
            return False
    def update_user_by_user_name(self, user_name, params):
        if params and user_name:
            values = params.values()
            items = [item for item in params.items()]

            cursor = self.connection.cursor()
            for item in params:
                query = ("UPDATE users set "+item+" = ? WHERE user_id=?", (params[item],user_name,))
                cursor.execute(
                    "UPDATE users SET "+item+" = ? WHERE user_name= ? ", (params[item],user_name,))
            self.connection.commit()
            cursor.close()
            return True
        else:
            return False
    def __del__(self):
        if self.connection:
            self.connection.close()
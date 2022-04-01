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
            INSERT INTO users (user_name, password)
            VALUES (?,?)
            ''',
            (user_name, password,),
        )

        new_id = self.get_last_user()[0]
        cursor.close()
        self.connection.commit()  # save changes
        return new_id

    def get_last_user(self) -> list:
        cursor = self.connection.cursor()
        cursor.execute(
            '''
            SELECT MAX(user_id) FROM users
            ''')
        last = cursor.fetchone()
        cursor.close()
        return last

    def insert_task(self, task_name, author_id):
        cursor = self.connection.cursor()
        cursor.execute(
            '''
            INSERT INTO tasks (task_name,author_id)
            VALUES (?,?)
            ''',
            (task_name, author_id,),
        )
        new_id = self.get_last_task()[0]
        cursor.close()
        self.connection.commit()  # save changes
        return new_id

    def get_last_task(self) -> list:
        cursor = self.connection.cursor()
        cursor.execute(
            '''
            SELECT MAX(task_id) FROM tasks
            ''')
        last = cursor.fetchone()
        cursor.close()
        return last

    def get_user_by_telegram_id(self, telegram_id):
        if telegram_id:
            cursor = self.connection.cursor()
            cursor.execute(
                '''
                SELECT * FROM users WHERE telegram_id = ?
                ''',
                (telegram_id,))
            user = cursor.fetchone()
            cursor.close()
            return user
        return False

    def get_user_by_alice_id(self, alice_id):
        if alice_id:
            cursor = self.connection.cursor()
            cursor.execute(
                '''
                SELECT * FROM users WHERE alice_id = ?
                ''',
                (alice_id,))
            user = cursor.fetchone()
            cursor.close()
            return user
        return False

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
        return False
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
            cursor = self.connection.cursor()
            for item in params:
                cursor.execute(
                    "UPDATE users SET "+item+" = ? WHERE user_name= ? ", (params[item],user_name,))
            self.connection.commit()
            cursor.close()
            return True
        else:
            return False

    def update_task_by_task_id(self, task_id, params):
        if params and task_id:
            cursor = self.connection.cursor()
            for item in params:
                print(item, params[item])
                cursor.execute(
                    "UPDATE tasks SET " + item + " = ? WHERE task_id= ? ", (params[item], task_id,))
            self.connection.commit()
            cursor.close()
            return True
        else:
            return False


    def __del__(self):
        if self.connection:
            self.connection.close()
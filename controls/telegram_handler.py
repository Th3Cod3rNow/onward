from main_controller import Controller


class Handler:
    def __init__(self, DataBase=None):
        self.commands = {
            "/start": self.start,
            "LOGIN": self.log_in,  # <username> \n <password>
            "CREATE": self.create_user  # <username> \n <password>
        }

        self.controller = Controller()

    def processing(self, message):
        body = message["text"]
        user_tg_id = message["from_user"]["id"]
        self.user = self.controller.get_user_by_telegram_id(user_tg_id)
        if not self.user and len(body.split('\n')) > 0 and body.split('\n')[0] != 'LOGIN':
            answer = self.user_doesnt_logged_in(body, user_tg_id)
            return answer
        if body.split('\n')[0] in self.commands:
            answer = self.commands[body.split('\n')[0]](body, user_tg_id)
            return answer

    def user_doesnt_logged_in(self, body, user_tg_id):
        answer = "Вы не вошли в аккаунт. Чтобы войти в аккаунт введите:\nLOGIN\n<username>\n<password>"
        return (int(user_tg_id), answer)

    def log_in(self, body, user_tg_id):
        splitted = body.split('\n')
        if len(splitted) == 3:
            if self.user and self.user[4]:
                answer = "У вас уже есть аккаунт"
            else:
                LOGIN = self.controller.log_in(splitted[1], splitted[2], int(user_tg_id))
                if LOGIN:
                    answer = "Вход произошел успешно"
                else:
                    answer = "Неверные логин или пароль"
        else:
            answer = "Неверный формат ввода"
        return (int(user_tg_id), answer)

    def start(self, body, user_tg_id):
        answer = "Для входа в систему введите логин и пароль, которые Вам выдали в следующем формате:\nLOGIN\n<user_name>\n<password>"
        return (int(user_tg_id), answer)

    def create_user(self, body, user_tg_id):
        splitted = body.split()
        if len(splitted) == 3:
            CREATE = self.controller.create_user(splitted[1], splitted[2])
            if CREATE:
                answer = "Профиль успешно создан"
            else:
                answer = "Ошибка ввода. Убедитесь, что ввели сообщение в следующем формате:\nCREATE\n<username>\n<password>"
        else:
            answer = "Неверный формат ввода. Убедитесь, что ввели сообщение в следующем формате:\nCREATE\n<username>\n<password>"

        return (int(user_tg_id), answer)

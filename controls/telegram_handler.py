from main_controller import Controller

class Handler:
    def __init__(self, DataBase=None):
        self.commands = {
            "/start": self.start,
            "LOGIN": self.log_in
        }

        self.controller = Controller()

    def processing(self, message):
        body = message["text"]
        user_tg_id = message["from_user"]["id"]
        if body.split('\n')[0] in self.commands:
            answer = self.commands[body.split('\n')[0]](body, user_tg_id)
            return answer

    def log_in(self, body, user_tg_id):
        splitted = body.split('\n')
        if len(splitted) == 3:
            LOGIN=self.controller.log_in(splitted[1], splitted[2], int(user_tg_id))
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
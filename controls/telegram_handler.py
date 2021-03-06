from main_controller import Controller


class Handler:
    def __init__(self, DataBase=None):
        self.commands = {
            # "/start": self.start,
            # "LOGIN": self.log_in,  # <username> \n <password>
            # "CREATE": self.create_user,  # <username> \n <password>
            # "/newtask": self.new_task,
            # "task_name": self.create_task,
            # "task_description": self.task_description,
            # "/newgroup": self.create_group,
            # "/task": self.get_task
        }
        self.buttons = {
            # "change_description_group":self.button_change_task_desctiption
        }

        self.controller = Controller()

    def processing(self, update):
        return 0

    # def processing(self, message, context=None, button_command=None):
    #     print(message, button_command)
    #     if button_command:
    #         body = button_command
    #     else:
    #         body = message["text"]
    #     user_tg_id = message["from_user"]["id"]
    #     self.user = self.controller.get_user_by_telegram_id(user_tg_id)
    #     if not self.user and len(body.split('\n')) > 0 and body.split('\n')[0] != 'LOGIN':
    #         answer = self.user_doesnt_logged_in(body, user_tg_id)
    #         return answer
    #     if button_command:
    #         body = button_command.split()[0]
    #         params = button_command.split()[1:]
    #         answer = self.buttons[button_command](body, user_tg_id, params)
    #         return answer
    #     if body.split('\n')[0].split()[0] in self.commands:
    #         answer = self.commands[body.split('\n')[0].split()[0]](body, user_tg_id)
    #         return answer
    #     if context == "task_name":
    #         answer = self.commands[context](body, user_tg_id)
    #         return answer
    #     if context.startswith("task_description"):
    #         answer = self.commands["task_description"](body, user_tg_id, int(context.split()[1]))
    #         return answer
    #     if context.startswith("change_description"):
    #         answer = self.commands["task_description"](body,user_tg_id, int(context.split()[1]))
    #
    # def user_doesnt_logged_in(self, body, user_tg_id):
    #     answer = "Вы не вошли в аккаунт. Чтобы войти в аккаунт введите:\nLOGIN\n<username>\n<password>"
    #     return (int(user_tg_id), answer)
    #
    # def log_in(self, body, user_tg_id):
    #     splitted = body.split('\n')
    #     if len(splitted) == 3:
    #         if self.user and self.user[4]:
    #             answer = "У вас уже есть аккаунт"
    #         else:
    #             LOGIN = self.controller.log_in(splitted[1], splitted[2], telegram_id=(user_tg_id))
    #             if LOGIN:
    #                 answer = "Вход произошел успешно"
    #             else:
    #                 answer = "Неверные логин или пароль"
    #     else:
    #         answer = "Неверный формат ввода"
    #     return (int(user_tg_id), answer)
    #
    # def start(self, body, user_tg_id):
    #     answer = "Для входа в систему введите логин и пароль, которые Вам выдали в следующем формате:\nLOGIN\n<user_name>\n<password>"
    #     return (int(user_tg_id), answer)
    #
    # def create_user(self, body, user_tg_id):
    #     splitted = body.split()
    #     if len(splitted) == 3:
    #         CREATE = self.controller.create_user(splitted[1], splitted[2])
    #         if CREATE:
    #             answer = "Профиль успешно создан"
    #         else:
    #             answer = "Ошибка ввода. Убедитесь, что ввели сообщение в следующем формате:\nCREATE\n<username>\n<password>"
    #     else:
    #         answer = "Неверный формат ввода. Убедитесь, что ввели сообщение в следующем формате:\nCREATE\n<username>\n<password>"
    #     return (int(user_tg_id), answer)
    #
    # def new_task(self, body, user_tg_id):
    #     answer = "Введите название задания"
    #     return (int(user_tg_id), answer, "task_name")
    #
    # def create_group(self, body, user_tg_id):
    #     group_name = ' '.join(body.split()[1:])
    #     try:
    #         creation = self.controller.create_group(group_name)
    #     except Exception:
    #         creation = False
    #     if creation:
    #         answer = "Группа создана"
    #     else:
    #         answer = "Ошибка создания группы"
    #     return (int(user_tg_id), answer)
    #
    # def create_task(self, body, user_tg_id):
    #     task_id = self.controller.create_task(self.controller.get_user_by_telegram_id(user_tg_id)[0], body)
    #     answer = "Введите описание задания"
    #     return (int(user_tg_id), answer, "task_description " + str(task_id))
    #
    # def task_description(self, body, user_tg_id, task_id):
    #     params = {"description": body}
    #     self.controller.update_task(task_id, params)
    #     answer = "Задание создано. Номер задания: " + str(task_id)
    #     return (int(user_tg_id), answer)
    #
    # def get_task(self, body, user_tg_id):
    #     answer = "Ошибка"
    #     if len(body.split()) == 2:
    #         task_id = body.split()[1]
    #         if task_id.isdigit():
    #             task_id = int(task_id)
    #             task = self.controller.get_task_by_task_id(task_id)
    #             if task:
    #                 answer = "Вот информация о задании\nНазвание:\n" + task[1] + "\nОписание:\n" + task[
    #                     2] + "\nГруппа задания: " + str(task[6]) + "\nГотовность:" + str(task[5])
    #                 return (int(user_tg_id), answer, "task_keyboard", task_id)
    #             else:
    #                 answer = "Задание не найдено"
    #
    #     return (int(user_tg_id), answer)
    #
    # def button_change_task_desctiption(self, body, user_tg_id, task_id):
    #     answer = "Введите описание задания"
    #     return (int(user_tg_id), answer, "change_discription " + str(task_id))

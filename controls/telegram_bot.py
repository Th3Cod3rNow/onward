from telegram.ext import Updater, MessageHandler, Filters, CommandHandler, CallbackQueryHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
import json
from uuid import uuid4
from telegram_handler import Handler
import main_controller

import logging  # Logging

logging.basicConfig(level=20,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

config_file = open("config.json", mode="r")
config = json.load(config_file)
config_file.close()

token_file = open(config["main"]["token-file"], mode='r')
token = token_file.read()
token_file.close()

handler = Handler()
STATE = None

controller = main_controller.Controller()

ready = {
    1: "+",
    0: "-"
}

def chatting(update, context):
    global STATE
    data = {"entering", "enter_group_name", "enter_in_group", "exit_group", "task_name", "description_task",
            "group_task", "task_deadline", "take_task", "task_info", "complete_task"}
    for i in data:
        if i not in context.user_data:
            context.user_data[i] = False
    if context.user_data["entering"]:
        login(update, context)
        context.user_data["entering"] = False
    elif context.user_data["enter_group_name"]:
        create_group(update, context)
        context.user_data["enter_group_name"] = False
    elif context.user_data["enter_in_group"]:
        enter_in_group(update, context)
        context.user_data["enter_in_group"] = False
    elif context.user_data["exit_group"]:
        exit_group(update, context)
        context.user_data["exit_group"] = False
    elif context.user_data["task_name"]:
        create_task(update, context)
        context.user_data["task_name"] = False
    elif context.user_data["description_task"]:
        task_add_description(update, context, context.user_data["description_task"])
        context.user_data["description_task"] = False
    elif context.user_data["group_task"]:
        task_add_group(update, context, context.user_data["group_task"])
        context.user_data["group_task"] = False
    elif context.user_data["take_task"]:
        context.user_data["take_task"] = False
        take_task(update, context)
    elif context.user_data["task_info"]:
        task_info(update, context)
        context.user_data["task_info"] = False
    elif context.user_data["complete_task"]:
        complete_task(update, context)
        context.user_data["complete_task"] = False

    else:
        update.message.reply_text("Не понял вас")

    for i in data:
        if i not in context.user_data:
            context.user_data[i] = False

def complete_task(update, context):
    task_id = update.message["text"]
    if task_id.isdigit():
        task_id = int(task_id)
        task = controller.get_task_by("task_id", task_id)
        if task:
            controller.update_task(task_id, {"completed": True})
            text = "Готово"
        else:
            text = "Задания не существует"
    else:
        text = "Неверный формат ввода"
    update.message.reply_text(text)
def task_info(update, context):
    task_id = update.message["text"]
    if task_id.isdigit():
        task_id = int(task_id)
        task = controller.get_task_by("task_id", task_id)
        if task:
            text = ""
            text += str(task_id)
            text += ". "
            text += task[1]
            text += '\n\nОписание:\n'
            text += task[2]
            text += '\n\nИсполнитель:\n'
            text += str(task[4]) + '. '
            text += controller.get_user_by("user_id", int(task[4]))[1]
            text += '\n\nГотовность: '
            text += str(task[5])
        else:
            text = "Задания не существует"
    else:
        text = "Неверный формат выполненным"
    update.message.reply_text(text)

def take_task(update, context):
    task_id = update.message["text"]
    text = "Что-то пошло не так"
    user = controller.get_user_by("telegram_id", update.message["from_user"]["id"])
    if task_id.isdigit():
        task_id = int(task_id)
        task = controller.get_task_by("task_id", task_id)
        if task:
            if task[4]:
                text = "Это задание уже кто-то делает"
            else:
                user_tasks = user[3].split()
                user_tasks.append(str(task[0]))

                controller.update_user_base_params(user[0], {"task_list": ' '.join(list(set(user_tasks)))})
                controller.update_task(task[0], {"performer_id":user[0]})
                text = "Готово"
        else:
            text = 'Такого задания не существует'
    else:
        text = "Неверный формат ввода"

    update.message.reply_text(text)

def task_add_group(update, context, task_id):
    group_id = update["message"]["text"]

    if group_id.isdigit():
        group_id = int(group_id)
        upd_task = controller.update_task(int(task_id), {"group_id": group_id})
        group = controller.get_group_by("group_id", int(group_id))
        print(group, "task_add_group", upd_task)
        if group is not None and upd_task:
            new_tasks = list(set(group[1].split()))
            new_tasks.append(str(task_id))
            upd_group = controller.update_group(group_id, params={"task_list": ' '.join(list(set(new_tasks)))})
            if upd_group:
                context.user_data["task_deadline"] = task_id
                update.message.reply_text("Группа создана")

        elif group is None:
            upd_task = controller.update_task(task_id, {"group_id": 0})
            update.message.reply_text("Такой группы не существует")


def task_add_description(update, context, task_id):
    desc = update["message"]["text"]
    if desc:
        controller.update_task(task_id, {"description": desc})
        context.user_data["group_task"] = task_id
        update.message.reply_text("Введите номер группы задания")


def create_task(update, context):
    name = update['message']['text']
    task = controller.create_task(controller.get_user_by("telegram_id", int(update['message']['chat']['id']))[0], name)
    if task:
        context.user_data["description_task"] = task
        update.message.reply_text("Введите описание задания")
    else:
        update.message.reply_text("Что-то пошло не так")


def enter_in_group(update, context):
    user = controller.get_user_by("telegram_id", update["message"]["from_user"]["id"])
    if user:
        if update["message"]["text"].isdigit():

            group = controller.get_group_by("group_id", int(update["message"]["text"]))
            if group:
                if not group[2]:
                    new_users = []
                else:
                    new_users = group[2].split()
                # controller.update_user_base_params(user[0], {"group_id": int(update["message"]["text"])})
                new_groups = list(set(user[6].split()))
                new_groups.append(update["message"]["text"])
                controller.update_user_base_params(user[0], {"group_id": ' '.join(list(set(new_groups)))})
                new_users.append(str(user[0]))
                new_users = ' '.join(list(set(new_users)))
                controller.update_group(int(update["message"]["text"]), {"user_list": new_users})
                update.message.reply_text("Вы вошли в группу")
            else:
                update.message.reply_text("Такой группы не существует")
        else:
            update.message.reply_text("Неверный формат ввода")
    else:
        update.message.reply_text("Что-то пошло не так")


def create_group(update, context):
    group = controller.create_group(update["message"]["text"])
    if group:
        update.message.reply_text("Группа создана")
    else:
        update.message.reply_text("Ошибка. Возможно группа с таким названием уже существует")


def login(update, context):
    body = update["message"]["text"].split('\n')
    if len(body) == 2:
        user = controller.log_in(body[0], body[1], telegram_id=update["message"]["from_user"]["id"])
        if user:
            update.message.reply_text("Вход выполнен")
        else:
            update.message.reply_text("Проверьте ещё раз логин, пароль")
    else:
        update.message.reply_text("Проверьте формат ввода")


def buttons(update, context):
    query = update.callback_query
    query.answer()
    choice = query.data
    if choice.startswith("login"):
        login_info(update, context)
    if choice == "task_list":
        task_list(update, context)
    if choice == 'create_group':
        create_group_info(update, context)
    if choice == 'group_list':
        group_list(update, context)
    if choice == 'enter_in_group':
        group_enter_info(update, context)
    elif choice == 'exit_group':
        exit_group_info(update, context)
    elif choice == 'my_tasks':
        my_task_list(update, context)
    elif choice == "create_task":
        create_task_info(update, context)
    elif choice == 'take_task':
        take_task_info(update, context)
    elif choice == 'task_info':
        task_info_info(update, context)
    elif choice == 'complete_task':
        complete_task_info(update, context)

def complete_task_info(update, context):
    context.user_data['complete_task'] = True
    update.callback_query.message.reply_text("Введите ID задания")

def task_info_info(update, context):
    context.user_data["task_info"] = True
    update.callback_query.message.reply_text("Введите ID задания")


def take_task_info(update, context):
    context.user_data["take_task"] = True
    update.callback_query.message.reply_text("Введите ID задания, которое хотите взять")

def my_task_list(update, context):
    user = controller.get_user_by("telegram_id", int(update["callback_query"]["message"]["chat"]["id"]))
    print(user)
    if user[6]:
        tasks = user[3].split()
        print(tasks)
        text = "Вот ваш список заданий:\n"
        for task in tasks:
            addition = ""
            addition += str(task)
            addition += '. '
            addition += controller.get_task_by("task_id", int(task))[1]
            addition += " (" + ready[controller.get_task_by("task_id", int(task))[5]] +")"
            text += addition
            text += '\n'
        update.callback_query.message.reply_text(text)
    else:
        update.callback_query.message.reply_text("Чтобы увидеть список заданий сначала войдите в одну из групп")

def create_task_info(update, context):
    context.user_data["task_name"] = True
    update.callback_query.message.reply_text("Введите название задания")


def exit_group_info(update, context):
    context.user_data["exit_group"] = True
    update.callback_query.message.reply_text("Введите ID группы, из которой хотите выйти")


def exit_group(update, context):
    # print(update["callback_query"]["message"]["chat"])
    user = controller.get_user_by("telegram_id", int(update["message"]["chat"]["id"]))
    group_id = update["message"]["text"]
    if not group_id.isdigit():
        update.message.reply_text("Неверный формат ввода")
    elif user:
        group_id = int(group_id)
        if user[6]:
            new_groups = list(set(user[6].split()) - set(str(group_id)))
            new_groups = ' '.join(list(set(new_groups)))
            controller.update_user_base_params(user[0], {"group_id": new_groups})
            group = controller.get_group_by("group_id", int(group_id))
            new_users = list(set(group[2].split()) - set(str(user[0])))
            new_users = ' '.join(list(set(new_users)))
            controller.update_group(group_id, {"user_list": new_users})
            update.message.reply_text("Вы вышли из группы")
        else:
            update.message.reply_text("Вы не состоите ни в одной группе")
    else:
        update.message.reply_text("Что-то пошло не так")


def group_enter_info(update, context):
    context.user_data["enter_in_group"] = True
    text = "Введите ID группы, в которую хотите войти"
    update.callback_query.message.reply_text(text)


def create_group_info(update, context):
    context.user_data["enter_group_name"] = True
    text = "Введите название группы"
    update.callback_query.message.reply_text(text)


def task_list(update, context):
    user = controller.get_user_by("telegram_id", int(update["callback_query"]["message"]["chat"]["id"]))
    print(user)
    if user[6]:
        groups = user[6].split()
        text = "Вот список заданий ваших групп:\n"
        print(groups)
        for group in groups:
            text += "Группа №" + str(group) + "(" + controller.get_group_by("group_id", int(group))[3] + "):\n"
            tasks = controller.get_tasks_by("group_id", group)
            for task in tasks:
                addition = ""
                addition += str(task[0])
                addition += '. '
                addition += str(task[1])
                addition += " (" + ready[task[5]] + ")"
                text += addition
                text += '\n'
            text += '\n'
        update.callback_query.message.reply_text(text)
    else:
        update.callback_query.message.reply_text("Чтобы увидеть список заданий сначала войдите в одну из групп")


def group_list(update, context):
    groups = controller.get_groups()
    text = 'Вот список групп\n'
    print(groups)
    if groups:
        for group in groups:
            addition = ''
            addition += str(group[0])
            addition += '. '
            addition += group[3]
            text += addition
            text += '\n'
        update.callback_query.message.reply_text(text)
    else:
        update.callback_query.message.reply_text("Кажется групп ещё нет")


def start(update, context):
    tg_id = int(update["message"]["from_user"]["id"])
    user = controller.get_user_by(parameter="telegram_id", value=tg_id)
    if user:
        update.message.reply_text("Вы уже вошли в аккаунт")
    else:
        keyboard = [[InlineKeyboardButton("Войти", callback_data="login")]]
        kb = InlineKeyboardMarkup(keyboard)
        text = "Войдите в аккаунт с помощью логина и пароля, который вам выдали"
        update.message.reply_text(text, reply_markup=kb)


def login_info(update, context):
    text = "Введите в две строки логин и пароль. Пример:\nuser\npassword"
    context.user_data["entering"] = True
    update.callback_query.message.reply_text(text)


def help_info(update, context):
    if update["message"]:
        user = controller.get_user_by("telegram_id", update["message"]["from_user"]["id"])
        if user:
            keyboard = [
                [
                    InlineKeyboardButton("Задания групп", callback_data="task_list"),
                    InlineKeyboardButton("Мои задания", callback_data="my_tasks")
                ],
                [
                    InlineKeyboardButton("Взять задание", callback_data="take_task"),
                    InlineKeyboardButton("Пометить выполненным", callback_data="complete_task")
                ],
                [
                    InlineKeyboardButton("Создать задание", callback_data="create_task"),
                    InlineKeyboardButton("Узнать о задании", callback_data="task_info")
                ],
                [
                    InlineKeyboardButton("Список групп", callback_data="group_list"),
                    InlineKeyboardButton("Создать группу", callback_data="create_group")

                ],
                [
                    InlineKeyboardButton("Войти в группу", callback_data="enter_in_group"),
                    InlineKeyboardButton("Выйти из группы", callback_data="exit_group")
                ]
            ]
            kb = InlineKeyboardMarkup(keyboard)
            update.message.reply_text("Вот все достпуные команды", reply_markup=kb)


def main():
    updater = Updater(token, use_context=True)

    dp = updater.dispatcher

    text_handler = MessageHandler(Filters.text, chatting)
    command_start = CommandHandler("start", start)
    command_help = CommandHandler("help", help_info)

    dp.add_handler(CallbackQueryHandler(buttons))
    dp.add_handler(command_start)
    dp.add_handler(command_help)
    dp.add_handler(text_handler)
    logging.info("Bot has started!")
    updater.start_polling(poll_interval=1)
    updater.idle()


if __name__ == '__main__':
    main()

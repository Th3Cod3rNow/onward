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


def chatting(update, context):
    global STATE
    answer = handler.processing(update)
    data = {"entering", "enter_group_name", "enter_in_group", "exit_group"}
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
    else:
        update.message.reply_text("Не понял вас")
    context.user_data["entering"] = False
    context.user_data["enter_group_name"] = False
    context.user_data["exit_group"] = False

def enter_in_group(update, context):
    user = controller.get_user_by("telegram_id", update["message"]["from_user"]["id"])
    if user:
        if update["message"]["text"].isdigit():

            controller.update_user_base_params(user[0], {"group_id": int(update["message"]["text"])})
            group = controller.get_group_by("group_id", int(update["message"]["text"]))
            if group:
                if not group[2]:
                    new_users = []
                else:
                    new_users = group[2].split()

                new_users.append(str(user[0]))
                new_users = ' '.join(list(set(new_users)))
                controller.update_group(int(update["message"]["text"]), {"user_list": new_users})
                update.message.reply_text("Вы вошли в групу")
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

def exit_group_info(update,context):
    context.user_data["exit_group"] = True
    update.callback_query.message.reply_text("Введите ID группы, из которой хотите выйти")


def exit_group(update, context):
    # print(update["callback_query"]["message"]["chat"])
    user = controller.get_user_by("telegram_id", int(update["message"]["chat"]["id"]))
    group_id = update["message"]["text"]
    if not group_id.isdigit():
        update.message.reply_text("Неверный формат ввода")
    elif user:
        group_id=int(group_id)
        if user[6]:
            new_groups = list(set(user[6].split()) - set(str(group_id)))
            new_groups = ' '.join(new_groups)
            controller.update_user_base_params(user[0], {"group_id":new_groups})
            group = controller.get_group_by("group_id", int(group_id))
            print(user[0], group[2])
            new_users = list(set(group[2].split()) - set(str(user[0])))
            new_users = ' '.join(new_users)
            print(new_users)
            controller.update_group(group_id, {"user_list":new_users})
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
    if user[6]:
        tasks = controller.get_tasks_by("group_id", user[6])
        text = "Вот список заданий вашей группы:\n"
        for task in tasks:
            addition = ""
            addition+= str(task[0])
            addition+='. '
            addition+=task[3]
            text += addition
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
                    InlineKeyboardButton("Задания группы", callback_data="task_list"),
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

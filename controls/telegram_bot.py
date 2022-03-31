from telegram.ext import Updater, MessageHandler, Filters
import data_base
import telegram_handler
import random
import threading
import time
import sys
import json
import requests
from telegram_handler import Handler
import telegram_sender as sender

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

def chatting(update, bot, get_ans = False, ready_message = None):
    answer = handler.processing(update["message"])
    print(answer)
    if answer:
        if isinstance(answer[0], int) and isinstance(answer[1], str):
            sender.send_text(bot.bot, *answer)
        else:
            sender.send_text(bot.bot, update["message"]["from_user"]["id"], "Не понял вас")

def main():
    updater = Updater(token, use_context=True)

    dp = updater.dispatcher

    text_handler = MessageHandler(Filters.text, chatting)

    # adding handler
    dp.add_handler(text_handler)
    logging.info("Bot has started!")
    updater.start_polling(poll_interval=1)
    updater.idle()

if __name__ == '__main__':
    main()
from telegram.ext import Updater, MessageHandler, Filters, CommandHandler
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
STATE = None

def chatting(update, context):
    global STATE

    answer = handler.processing(update["message"], context=STATE)
    if answer and update:
        if len(answer) == 3:
            STATE = answer[2]
            sender.send_text(update.message, *answer[:2])
        else:
            STATE = None
            if isinstance(answer[0], int) and isinstance(answer[1], str):
                sender.send_text(update.message, *answer[:2])
            else:
                sender.send_text(update.message, update["message"]["from_user"]["id"], "Не понял вас")



def main():
    updater = Updater(token, use_context=True)

    dp = updater.dispatcher

    text_handler = MessageHandler(Filters.text, chatting)
    # context_handler = MessageHandler(Filters.text, context_chatting)
    #
    # dp.add_handler(CommandHandler("start", chatting))
    # dp.add_handler(CommandHandler("newtask", chatting))

    dp.add_handler(text_handler)
    logging.info("Bot has started!")
    updater.start_polling(poll_interval=1)
    updater.idle()

if __name__ == '__main__':
    main()
def send_text(bot, user_tg_id, msg):
    bot.send_message(user_tg_id, text=msg)
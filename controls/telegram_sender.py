def send_text(message, user_tg_id, msg):
    message.reply_text(msg)

def send_keyboard(message, user_tg_id, msg, keyboard):
    message.reply_text(msg, reply_markup=keyboard)
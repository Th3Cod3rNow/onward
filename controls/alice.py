from flask import Flask, request
import main_controller

app = Flask(__name__)
controller = main_controller.Controller()


@app.route('/', methods=["POST"])
def index():

    if request.json["session"]["new"] is True:
        response_text = "Здравствуйте!"
    else:
        response_text = "Извините, я не поняла."

    user_id = request.json.get("session", {}).get("user_id")

    if controller.get_user_by_alice_id(user_id):
        text = request.json.get("request", {}).get("command")

        if ("цели" in text) or ("задания" in text) or ("кейсы" in text):
            response_text = f"Ваши цели:\n1. aaaaa\n2. bbbbb\n3. ccccc"

        response_text = handle_message(request.json.get("request", {}).get("original_utterance"), user_id)

    else:
        response_text = handle_message(request.json.get("request", {}).get("original_utterance"), user_id)

    response = {
        "version": "1.0",
        "response": {
            "text": response_text,
            "end_session": False
        }
    }

    return response


def handle_message(text, user_alice_id):
    user = controller.get_user_by_alice_id(user_alice_id)
    splited = text.split()
    if len(splited) == 3:
        if splited[0] == "login" and user is None:
            login = controller.log_in(splited[1], splited[2], alice_id=user_alice_id)
            if login:
                return "Вы успешно прошли аутентификацию!"
            else:
                return "Пожалуйста, проверьте логин и пароль еще раз."
        elif splited[0] == "create":
            create = controller.create_user(splited[1], splited[2])
            if create and user:
                return "Вы успешно создали аккаунт для нового пользователя!"
            else:
                return "Вы не можете создавать новых пользователей!"


app.run(host="0.0.0.0", port=5000, debug=True)

from flask import Flask, request

app = Flask(__name__)


@app.route('/', methods=["POST"])
def index():

    text = request.json.get("request", {}).get("command")
    response_text = "Извините, я не поняла!"

    if ("цели" in text) or ("задания" in text) or ("кейсы" in text):
        response_text = f"Ваши цели:\n1. aaaaa\n2. bbbbb\n3. ccccc"

    response = {
        "version": "1.0",
        "session": {
            "user": {
                "user_id": "6C91DA5198D1758C6A9F63A7C5CDDF09359F683B13A18A151FBF4C8B092BB0C2",
                "access_token": "AgAAAAAB4vpbAAApoR1oaCd5yR6eiXSHqOGT8dT"
            }
        },
        "response": {
            "text": response_text,
            "end_session": False
        }
    }

    return response


app.run(host="0.0.0.0", port=5000, debug=True)

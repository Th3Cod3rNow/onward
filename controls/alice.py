from flask import Flask, request
import main_controller

app = Flask(__name__)
controller = main_controller.Controller()


@app.route('/', methods=["POST"])
def index():
    user_id = request.json.get("session", {}).get("user_id")

    if controller.get_user_by("alice_id", user_id):
        response_text = handle_message(request.json.get("request", {}).get("command"), user_id)
    else:
        response_text = "Войдите в аккаунт. (Никнейм Пароль)"
        text = request.json.get("request", {}).get("original_utterance")
        if "новый аккаунт" in text:
            response_text = new_account(text.split())
        elif len(text.split()) > 1:
            response_text = auth(text.split()[0], text.split()[1], user_id)

    response = {
        "version": "1.0",
        "response": {
            "text": response_text,
            "end_session": False
        }
    }

    return response


def new_account(login_text):
    user_login = login_text[2]
    user_password = login_text[3]

    if controller.create_user(user_login, user_password):
        return "Вы успешно создали аккаунт!"

    return "Вы не смогли создать аккаунт. Попробуйте еще раз."


def auth(username, user_password, alice_user_id):
    if controller.log_in(username, user_password, alice_id=alice_user_id):
        return "Вы успешно авторизовались!"
    return "Вы не смогли войти. Проверьте введенные данные еще раз."


def handle_message(text, user_alice_id):
    if "новая группа" in text:
        user_for_group = controller.get_user_by("alice_id", user_alice_id)
        group_id = controller.create_group(text.split()[2])

        if group_id:
            all_groups = user_for_group[-1] + " " + str(group_id)

            controller.update_group(group_id, {"user_list": user_for_group[0]})
            controller.update_user_base_params(user_for_group[0], {"group_id": all_groups})

            return f"Группа \"{text.split()[2]}\" успешно создана!"

        return "Группа с таким названием уже существует!"

    elif "добавить задание" in text:
        id_for_task = controller.get_user_by("alice_id", user_alice_id)[0]
        task_name = text[17:text.index("описание") - 1]
        task_description = text[text.index("описание") + 9:text.index("группа") - 1]
        task_group = controller.get_group_by("name", text[text.index("группа") + 7:])

        if task_group:
            task_id = controller.create_task(id_for_task, task_name)

            controller.update_task(task_id, {"description": task_description, "group_id": task_group[0]})
            controller.update_group(task_group[0], {"task_list": task_group[1] + str(task_id) + " "})

            return f"Задание \"{task_name}\" успешно создано!"

        return "Такой группы не существует!"

    elif "вступить в" in text:
        id_for_join = controller.get_user_by("alice_id", user_alice_id)
        enter = text[11:]
        taken_group = controller.get_group_by("name", enter)

        if taken_group:
            if str(taken_group[0]) not in id_for_join[-1]:
                all_groups = id_for_join[-1] + " " + str(taken_group[0])
                all_users = taken_group[2] + " " + str(id_for_join[0])

                controller.update_user_base_params(id_for_join[0], {"group_id": all_groups})
                controller.update_group(taken_group[0], {"user_list": all_users})

                return f"Вы вступили в группу \"{enter}\"."

            return "Вы уже состоите в этой группе."

        return "Такой группы не существует!"

    elif "все задания" in text:
        out_text = ""
        all_groups = controller.get_user_by("alice_id", user_alice_id)[-1].split()

        if all_groups:
            for i in all_groups:
                all_tasks = controller.get_group_by("group_id", int(i))
                if all_tasks:
                    for j in all_tasks[1].split():
                        out_text += str(controller.get_task_by("task_id", int(j))[0]) + " - Тема: " + \
                                    controller.get_task_by("task_id", int(j))[1] + " - Описание: " + \
                                    controller.get_task_by("task_id", int(j))[2] + "\n"

        if out_text:
            return out_text

        return "Заданий нет."

    elif "взять задание" in text:
        task_name = text.split()

        if controller.get_task_by("task_id", task_name[2]):
            all_user_tasks = controller.get_user_by("alice_id", user_alice_id)

            controller.update_user_base_params(all_user_tasks[0], {"task_list": all_user_tasks[3] + " " + task_name[2]})
            controller.update_task(task_name[2], {"performer_id": all_user_tasks[0]})

            return f"Задание {task_name[2]} добавлено в \"Ваши задания\"."

        return "Такого задания не существует."

    elif "мои задания" in text:
        out_text = ""
        my_tasks = controller.get_user_by("alice_id", user_alice_id)

        if my_tasks[3]:
            for i in my_tasks[3].split():
                out_text += i + " - Тема: " + controller.get_task_by("task_id", int(i))[1] +\
                            " - Описание: " + controller.get_task_by("task_id", int(i))[2] + "\n"

            return out_text

        return "У Вас нет активных заданий."

    else:
        if request.json["session"]["new"] is True:
            return "Здравствуйте!"

        return "Извините, я не поняла Вас!"


app.run(host="0.0.0.0", port=5000, debug=True)

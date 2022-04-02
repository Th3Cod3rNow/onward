from http.server import HTTPServer, SimpleHTTPRequestHandler
import html
import main_controller
from flask import Flask, app
from flask import jsonify
from flask import *
import os
import ast
from flask import Flask
from flask import Flask, request, jsonify, make_response

PORT = 8888
controller = main_controller.Controller()
Handler = SimpleHTTPRequestHandler
httpd = HTTPServer(("", PORT), Handler)

GROUPS = [
    {
        "id": ID,
        "name": controller.get_group_by('group_id', value=str(ID))[3],
        "tasks": controller.get_tasks_by('task_id', value=controller.get_group_by('group_id', value=ID)[1]),
        "users": controller.get_user_by("user_id", value=controller.get_group_by('group_id', value=ID)[2])
    }
    for ID in controller.log_in(user_name='user', password='user')[6].split()

]

print(GROUPS)
app = Flask(__name__)


def _build_cors_preflight_response():
    response = make_response()
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add('Access-Control-Allow-Headers', "*")
    response.headers.add('Access-Control-Allow-Methods', "*")
    return response


def corsify_actual_response(response):
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response


# app.config['SET_SECRET_KEY'] = 'key'

@app.route('/Groups', methods=['GET', 'OPTIONS'])
def all_books():
    if request.method == 'GET':
        return corsify_actual_response(jsonify(
            {
                'status': 'success',
                'groups': GROUPS
            }

        ))
    elif request.method == 'OPTIONS':
        print(123)
        data = request.get_json()
        username = data["username"]
        password = data["password"]
        print(username, password)
        user = controller.log_in(username, password)
        if user:
            return corsify_actual_response(jsonify({
                "status": "success",
                "groups": GROUPS
            }))


# Создание пользователя
@app.route('/createUser/Username=<string:username>&Password=<string:password>', methods=['GET'])
def create_user(username: str, password: str):
    if request.method == "GET":
        if username and password:
            user = controller.create_user(username, password)
            if user:
                return corsify_actual_response(jsonify({
                    "status": "success"
                }))
            else
                return corsify_actual_response(jsonify({
                    "status": "user_already_exists"
                }))
# Создание задания
@app.route('---', methods=['GET'])
def create_task(name, description, performer, group, author_id = 0):
    if request.method == 'GET':
        task_id = controller.create_task(author_id, name)
        controller.update_task(int(task_id), {"description": description,
                                              "performer_id": controller.get_user_by("user_name", performer)[0],
                                              "group_id": controller.get_group_by("group_name", group)})
        return corsify_actual_response(jsonify({
            "status": "success"
        }))

# Создаиние группы
@app.route('---', methods=["GET"])
def create_group(name):
    if request.method == 'GET':
        group_id = controller.create_group(name)
        return corsify_actual_response(jsonify({
            "status": "success"
        }))



app.run(port=8888, host='127.0.0.1')

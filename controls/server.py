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


def GROUPS(username, password):
    groups = list()
    user = controller.log_in(username, password)
    if user:
        for ID in user[6].split():
            group = controller.get_group_by("group_id", str(ID))
            groups.append({
                "id": ID,
                "name": group[3],
                "tasks": [controller.get_task_by("task_id", int(task)) for task in group[1].split()],
                "users": group[2].split()
            })
    return groups


def USER(user):
    user_dict = {
        "id": user[0],
        "name": user[1],
        "password": user[2],
        "task_list": user[3].split(),
        "group_id": user[6].split(),
        "groups": GROUPS(user[1], user[2])
    }
    return user_dict


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

@app.route('/login/Username=<string:username>&Password=<string:password>', methods=['GET'])
def all_books(username, password):
    if request.method == 'GET':
        user = controller.get_user_by("user_name", username)
        if user:
            return corsify_actual_response(jsonify(
                {
                    'status': 'success',
                    'groups': GROUPS(username, password)
                }

            ))
        else:
            return corsify_actual_response(jsonify(
                {
                    'status': 'user_doesnt_exist'
                }

            ))


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
            return corsify_actual_response(jsonify({
                "status": "user_already_exists"
            }))


# Создание задания
@app.route(
    '/addTask/Username=<string:author_name>&Taskname=<string:name>&Body=<string:description>&idGroup=<int:group_id>',
    methods=['GET'])
def add_task(author_name, name, description, group_id):
    if request.method == 'GET':
        author = controller.get_user_by("user_name", author_name)
        author_id = author[0]
        task_id = controller.create_task(author_id, name)
        task = controller.update_task(int(task_id), {"description": description,
                                                     "group_id": group_id})
        if task:
            group = controller.get_group_by("group_id", group_id)
            if group:
                group_tasks = group[1].split()
                group_tasks.append(str(task_id))
                new_tasks = ' '.join(list(set(group_tasks)))
                controller.update_group(int(group_id), {"task_list": new_tasks})
                return corsify_actual_response(jsonify({
                    "status": "success",
                    "groups": GROUPS(author[1], author[2]),
                    "group": {"group_id": group_id,
                                 "name": group[3],
                                 "tasks": [controller.get_task_by("task_id", int(task)) for task in new_tasks],
                                 "users": group[2].split()
                                 }
                }))
            else:
                return corsify_actual_response(jsonify({
                    "status": "group_doesnt_exist"
                }))
        else:
            return corsify_actual_response(jsonify({
                "status": "error"
            }))


@app.route('/addGroup/name=<string:name>&author_id=<int:author_id>', methods=["GET"])
def add_group(self, name, author_id):
    if request.method == 'GET':
        user = controller.get_user_by("user_id", author_id)
        group_id = controller.create_group(name)
        if group_id and user:
            group = controller.get_group_by("group_id", int(group_id))
            user_groups = user[6].split()
            user_groups.append(str(group_id))
            new_groups = ' '.join(list(set(user_groups)))
            controller.update_task(int(group_id), {"group_id": new_groups})
            return corsify_actual_response(jsonify({
                "status": "success",
                "groups": GROUPS(user[1], user[2]),
                                 "group": {"group_id": group_id,
                                 "name": group[3],
                                 "tasks": [controller.get_task_by("task_id", int(task)) for task in group[1].split()],
                                 "users": group[2].split()
                                 }
            }))
        else:
            "group_already_exist"


'''
# Создаиние группы
@app.route('---', methods=["GET"])
def create_group(name):
    if request.method == 'GET':
        group_id = controller.create_group(name)
        return corsify_actual_response(jsonify({
            "status": "success"
        }))



'''
app.run(port=8888, host='127.0.0.1')

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
        "name": controller.get_group_by('group_id', value=ID)[3],
        "tasks": controller.get_tasks_by('task_id', value=controller.get_group_by('group_id', value=ID)[1]),
        "users": controller.get_user_by("user_id", value=controller.get_group_by('group_id', value=ID)[2])
    }
    for ID in controller.log_in(user_name='Nikita', password='123456')[6]

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

@app.route('/Groups', methods=['GET'])
def all_books():
    print(request.method)

    return corsify_actual_response(jsonify(
        {
            'status': 'success',
            'groups': GROUPS
        }

    ))


app.run(port=8888, host='127.0.0.1')

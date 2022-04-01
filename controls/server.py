from http.server import HTTPServer, SimpleHTTPRequestHandler
import html
import main_controller

PORT = 8888
controller = main_controller.Controller()
Handler = SimpleHTTPRequestHandler
httpd = HTTPServer(("", PORT), Handler)

GROUPS = [
    {
        "id": ID,
        "name": controller.get_group_by_group_id(ID)[3],
        "tasks": controller.get_group_by_group_id(ID)[1],
        "performers": controller.get_group_by_group_id(ID)[2]
    }
    for ID in controller.log_in(user_name=user_name, password=password)[6]
]

while True:
    requests_raw, client_adress = httpd.get_request()
    print(1,requests_raw)

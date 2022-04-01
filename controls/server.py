from http.server import HTTPServer, SimpleHTTPRequestHandler
import html

PORT = 8888

Handler = SimpleHTTPRequestHandler
httpd = HTTPServer(("", PORT), Handler)

while True:
    requests_raw, client_adress = httpd.get_request()
    print(1,requests_raw)

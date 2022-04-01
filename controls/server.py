from http.server import HTTPServer, SimpleHTTPRequestHandler
import html
import requests

PORT = 8888

Handler = SimpleHTTPRequestHandler
httpd = HTTPServer(("", PORT), Handler)

print("Serving at port", PORT)
while True:
    requests_raw, client_address = httpd.get_request()
    req = requests.request("GET", "127.0.0.1:8080")
    print(req)
    print(requests_raw, 123)

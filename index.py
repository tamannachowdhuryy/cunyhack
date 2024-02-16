import http.server
import socketserver
from http import HTTPStatus
import json

class Handler(http.server.SimpleHTTPRequestHandler):

    preferences = {}

    def do_POST(self): 
        # Set the required headers for the POST request.
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()

        # Read the body of the request. This is the "body" we set in the JavaScript code.
        content_length = int(self.headers["Content-Length"])
        body = self.rfile.read(content_length)
        body_message = json.loads(body)

        # Do some processing logic. This is the "meat and potatoes" of your app.
        print("Received Request: ")
        print(body_message)



# Run the server
port_num = 8000
httpd = socketserver.TCPServer(("", port_num), Handler)
print("Starting Up on Port " + str(port_num))
httpd.serve_forever()

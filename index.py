import http.server
import socketserver
from http import HTTPStatus
import json

class Handler(http.server.SimpleHTTPRequestHandler):

    user_data = []

    def do_GET(self):
        # Set the required headers for the GET request.
        self.send_response(HTTPStatus.OK)

        if self.path == '/':
            # Serve the HTML file
            self.send_header("Content-type", "text/html")
            self.end_headers()

            with open("index.html", "rb") as file:
                self.wfile.write(file.read())
        else:
            # Serve other files (CSS, JS, etc.) using the default handler
            super().do_GET()

    def do_POST(self):
        # Set the required headers for the POST request.
        self.send_response(HTTPStatus.OK)
        self.send_header("Content-type", "application/json")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()

        # Read the body of the request. This is the "body" we set in the JavaScript code.
        content_length = int(self.headers["Content-Length"])
        body = self.rfile.read(content_length)
        body_message = json.loads(body)

        # Do some processing logic. This is the "meat and potatoes" of your app.
        print("Received Request:")
        print(body_message)

        # Extract user information from the request and update preferences
        user_info = {
            "cs_course": body_message.get("cs_course"),
            "math_course": body_message.get("math_course"),
            "hunter_courses": body_message.get("hunter_courses")
        }

        # Store the user information in the list
        self.user_data.append(user_info)

        # Send a response indicating successful storage
        response_data = {"status": "success", "message": "User information stored successfully"}
        self.wfile.write(json.dumps(response_data).encode("utf-8"))

    def do_OPTIONS(self):
        # Set the required headers for the preflight request.
        self.send_response(HTTPStatus.OK)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "POST, GET, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.send_header("Access-Control-Max-Age", "86400")
        self.end_headers()

# Run the server
port_num = 8000
httpd = socketserver.TCPServer(("", port_num), Handler)
print("Starting Up on Port " + str(port_num))
httpd.serve_forever()
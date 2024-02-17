import http.server
import socketserver
from http import HTTPStatus
import json
import csv
import random

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
       
            super().do_GET()

    def do_POST(self):
        # Set the required headers for the POST request.
        self.send_response(HTTPStatus.OK)
        self.send_header("Content-type", "application/json")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()

        content_length = int(self.headers["Content-Length"])
        body = self.rfile.read(content_length)
        body_message = json.loads(body)

        print("Received Request:")
        print(body_message)

        # Extract user information from the request and update preferences
        user_info = {
            "cs_course": body_message.get("cs_course"),
            "math_course": body_message.get("math_course"),
            "hunter_courses": body_message.get("hunter_courses")
        }

        self.user_data.append(user_info)


        response_data = {"status": "success", "message": "User information stored successfully"}
        self.wfile.write(json.dumps(response_data).encode("utf-8"))

    def do_OPTIONS(self):
      
        self.send_response(HTTPStatus.OK)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "POST, GET, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.send_header("Access-Control-Max-Age", "86400")
        self.end_headers()

    def generate_calendar(self, user_info):
        with open('requirements.csv', 'r') as f:
            reader = csv.DictReader(f)
            data = list(reader)

        # Filter events for the given user preferences
        filtered_courses = [course for course in data if course['Course'] == user_info['cs_course']]

        # Initialize calendar_info_list as a list
        calendar_info_list = []

        for course in filtered_courses:
            if user_info['cs_course'] == 'csci 127':
                # Customize calendar_info for 'csci 127'
                calendar_info = {
                    "event_date": "2022-02-21",  # Example date
                    "event_title": f"Event for {course['Course']}",
                    "event_time": f"Event for {course['Course']} students"
                }
                calendar_info_list.append(calendar_info)

     


        return calendar_info_list


# Run the server
port_num = 8000
httpd = socketserver.TCPServer(("", port_num), Handler)
print("Starting Up on Port " + str(port_num))
httpd.serve_forever()

#!/usr/bin/python3
"""Simple API using Python with the 'http.server' module"""

import http.server
import json


class Server(http.server.BaseHTTPRequestHandler):
    """Subclass of http.server.BaseHTTPRequestHandler"""

    def do_GET(self):
        """Handles GET requests"""

        if self.path == "/":
            self.send_response(200)
            self.end_headers()

            self.wfile.write(b"Hello, this is a simple API!")
        elif self.path == "/data":
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()

            dataset = {"name": "John", "age": 30, "city": "New York"}
            json_data = json.dumps(dataset)
            self.wfile.write(bytes(json_data, 'utf-8'))
        elif self.path == "/status":
            self.send_response(200)
            self.end_headers()

            self.wfile.write(b"OK")
        elif self.path == "/info":
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()

            info = {"version": "1.0", "description": "A simple API built with http.server"}
            json_data = json.dumps(info)
            self.wfile.write(bytes(json_data, 'utf-8'))
        else:
            self.send_response(404)
            self.end_headers()

            self.wfile.write(b"Endpoint not found")


def run(server_class=http.server.HTTPServer, handler_class=Server):
    server_address = ('', 5000)
    print(f"Server running on port {server_address[1]} ...")
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()


if __name__ == "__main__":
    run()

#!/usr/bin/python3
"""Develop a simple API using Python with the `http.server` module
"""
from http.server import BaseHTTPRequestHandler, HTTPServer
import json


class SimpleAPIHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/data':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            data = {"name": "john", "age": 30, "city": "New York"}
            self.wfile.write(json.dumps(data).encode())
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b"Endpoint not found")


if __name__ == "__main__":
    server = HTTPServer(('localhost', 8000), SimpleAPIHandler)
    print("Starting server on http://localhost:8000")
    server.serve_forever()

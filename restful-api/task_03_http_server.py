#!usr/bin/python3
"""Develop a simple API using Python with the `http.server` modulea
"""
from http.server import BaseHTTPRequestHandler, HTTPServer
import json


class SimpleAPIHandler(BaseHTTPRequestHandler):
    def send_text(self, data, status=200):
        self.send_response(status)
        self.send_header("Content-type", "text/json")
        self.end_headers()
        self.wfile.write(data.encode("utf-8"))

    def send_json(self, data, status=200):
        """send"""
        self.send_response(status)
        self.send_header("content-type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(data).encode("utf-8"))

    def do_GET(self):
        """get"""
        if self.path == '/':
            self.send_text("Hello, this is a simple API!")
        elif self.path == '/data':
            self.send_json({"name": "john", "age": 30, "city": "New York"})
        elif self.path == '/status':
            self.send_text("OK")
        elif self.path == '/info':
            self.send_json({
                  "version": "1.0",
                  "description": "A simple API built with http.server"
            })
        else:
            self.send_text("Endpoint not found", 404)

    def run_server(host="localhost", port=8000):
        """Starts the HTTP server"""
        server = HTTPServer((host, port), SimpleAPIHandler)
        print(f"Server started at http://{host}:{port}")

        try:
            server.serve_forever()

        except KeyboardInterrupt:
            print("\nShutting down server...")
            server.server_close()

    if __name__ == "__main__":
        run_server()

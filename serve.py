#!/usr/bin/env python3
import os
import socketserver
import http.server

SERVE_DIR = os.path.dirname(os.path.abspath(__file__))
PORT = 3000

os.chdir(SERVE_DIR)

Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Serving {SERVE_DIR} at http://localhost:{PORT}")
    httpd.serve_forever()

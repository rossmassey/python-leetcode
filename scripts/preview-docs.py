#!/usr/local/bin/python3

import os
import http.server
import socketserver
import subprocess
import threading

PORT = 8000
DIRECTORY = "docs/build/html"

def run_server():
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print(f"Serving at port http://localhost:{PORT}")
        httpd.serve_forever()

def build_docs():
    # Find the absolute path to the script's directory
    script_dir = os.path.dirname(os.path.realpath(__file__))

    # Determine the correct path to the docs directory
    docs_path = os.path.join(script_dir, "../docs")

    # Ensure the path is absolute
    docs_path = os.path.abspath(docs_path)

    subprocess.run(["make", "html"], cwd=docs_path)

# Initial build
build_docs()

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

# Start the server in a separate thread
server_thread = threading.Thread(target=run_server)
server_thread.daemon = True
server_thread.start()

# Main loop for user input
try:
    while True:
        command = input("Enter 'r' to rebuild docs, or 'q' to quit: ")
        if command.lower() == 'r':
            build_docs()
            print(f"Rebuilt the documentation at http://localhost:{PORT}")
        elif command.lower() == 'q':
            break
except KeyboardInterrupt:
    pass

print("\nExiting...")

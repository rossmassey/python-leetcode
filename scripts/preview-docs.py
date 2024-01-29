#!/usr/bin/python3

import os
import http.server
import socketserver
import subprocess
import threading

PORT = 8000
DIRECTORY = "../docs/build/html"


def run_server():
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        httpd.serve_forever()


def get_abs_path():
    script_dir = os.path.dirname(os.path.realpath(__file__))
    docs_path = os.path.join(script_dir, "../docs")
    return os.path.abspath(docs_path)


def build_docs():
    abs_path = get_abs_path()

    subprocess.run(["make", "clean"], cwd=abs_path, shell=True)
    return subprocess.run(["make", "html"], cwd=abs_path, shell=True)


def test_docs():
    abs_path = get_abs_path()

    return subprocess.run(["make", "doctest"], cwd=abs_path, shell=True)


class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)


if __name__ == "__main__":
    # Initial build
    build_docs()

    # Start the server in a separate thread
    server_thread = threading.Thread(target=run_server)
    server_thread.daemon = True
    server_thread.start()

    # Main loop for user input
    try:
        while True:
            test_docs()
            print(f"\nHosting at http://localhost:{PORT}\n")
            command = input("Enter 'r' to rebuild docs, or 'q' to quit: ")
            if command.lower() == 'r':
                build_docs()
                print(f"Rebuilt the documentation at http://localhost:{PORT}")
            elif command.lower() == 'q':
                break
    except KeyboardInterrupt:
        pass

    print("\nExiting...")

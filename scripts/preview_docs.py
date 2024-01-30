#!/usr/bin/python3
"""
This script is used to preview the documentation locally

Runs on port ``8000`` by default

Enter ``r`` to reload, and ``q`` to quit
"""
import os
import http.server
import socketserver
import subprocess
import threading

PORT = 8000
DIRECTORY = "docs/build/html"

IS_WIN = os.name == 'nt'  # check if windows os (new technology)


def run_server():
    """
    Run the server forever
    """
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        httpd.serve_forever()


def _get_abs_path() -> str:
    """
    Get the absolute path to the docs directory

    Returns:
        str: Absolute path to docs directory
    """
    script_dir = os.path.dirname(os.path.realpath(__file__))
    docs_path = os.path.join(script_dir, "../docs")
    return os.path.abspath(docs_path)


def build_docs() -> subprocess.CompletedProcess:
    """
    Build the documentation

    Returns:
        subprocess.CompletedProcess: The result of the build
    """
    abs_path = _get_abs_path()

    subprocess.run(["make", "clean"], cwd=abs_path, shell=IS_WIN)
    return subprocess.run(["make", "html"], cwd=abs_path, shell=IS_WIN)


def test_docs() -> subprocess.CompletedProcess:
    """
    Test the documentation

    Returns:
        subprocess.CompletedProcess: The result of the test
    """
    abs_path = _get_abs_path()

    return subprocess.run(["make", "doctest"], cwd=abs_path, shell=IS_WIN)


class Handler(http.server.SimpleHTTPRequestHandler):
    """
    Handler for the HTTP server
    """

    def __init__(self, *args, **kwargs):
        """
        Initialize the handler

        Args:
            directory (str): The directory to serve
        """
        super().__init__(*args, directory=DIRECTORY, **kwargs)


def main():
    """
    Main function for the script
    """
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


if __name__ == "__main__":
    main()

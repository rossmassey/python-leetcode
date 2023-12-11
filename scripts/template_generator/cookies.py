import os


def read_cookies() -> dict:
    """
    reads and parses the cookies from 'cookies.txt',
    located in the same directory as this script

    Returns:
        dict: each key-value pair corresponds to a cookie.
    """
    script_dir = os.path.dirname(os.path.abspath(__file__))
    cookies_file_path = os.path.join(script_dir, 'cookies.txt')

    cookies = {}
    with open(cookies_file_path, 'r') as file:
        for line in file:
            # Skip standard comment lines
            if line.startswith('#') and not line.startswith('#HttpOnly_'):
                continue

            # Handle HttpOnly cookies
            if line.startswith('#HttpOnly_'):
                line = line[len('#HttpOnly_'):]

            parts = line.strip().split('\t')
            if len(parts) == 7:
                # Extract the cookie name and value
                name, value = parts[5], parts[6]
                cookies[name] = value
    return cookies

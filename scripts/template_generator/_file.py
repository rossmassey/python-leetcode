"""
File utilities
"""
from pathlib import Path


def get_absolute_path(relative_path: str):
    """
    Get absolute path from relative path

    Args:
        relative_path: relative path from repo root

    Returns:
        str: absolute path
    """
    # go up three levels (../../../)
    repo_root = Path(__file__).parents[2]
    absolute_path = repo_root / relative_path

    return str(absolute_path.resolve())


def read_from_repo(relative_path: str) -> str:
    """
    Read file from repo

    Args:
        relative_path: relative path from repo root

    Returns:
        str: file contents
    """
    with open(get_absolute_path(relative_path), 'r', encoding='utf-8') as file:
        return file.read()


def write_to_repo(relative_path: str, content: str):
    """
    Write file to repo

    Args:
        relative_path: relative path from repo root
        content: content to write
    """
    with open(get_absolute_path(relative_path), 'w', encoding='utf-8') as file:
        file.write(content)


def fill_template(template_name: str, fields: dict):
    """
    Fill template with fields

    Args:
        template_name: name under templates/ folder
        fields: fields to fill template with
    """
    template_path = f"scripts/template_generator/templates/{template_name}"
    template = read_from_repo(template_path)

    return template.format(**fields)


def append_line(relative_path: str, line: str):
    """
    Append line to file
    Args:
        relative_path: relative path from repo root
        line: line to append
    """
    with open(get_absolute_path(relative_path), 'a', encoding='utf-8') as file:
        file.write(line + '\n')


def replace_line(relative_path: str, pattern: str, replacement: str):
    """
    Replace pattern in lines of file

    Args:
        relative_path: relative path from repo root
        pattern: pattern to search for
        replacement: replacement string
    """
    absolute_path = get_absolute_path(relative_path)
    with open(absolute_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    with open(absolute_path, 'w', encoding='utf-8') as file:
        for line in lines:
            if pattern in line:
                file.write(line.replace(pattern, replacement))
            else:
                file.write(line)

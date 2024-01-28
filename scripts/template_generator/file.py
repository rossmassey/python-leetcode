from pathlib import Path


def get_absolute_path(relative_path: str):
    # go up three levels (../../../)
    repo_root = Path(__file__).parents[2]
    absolute_path = repo_root / relative_path

    return str(absolute_path.resolve())


def read_from_repo(relative_path: str):
    with open(get_absolute_path(relative_path), 'r') as file:
        return file.read()


def write_to_repo(relative_path: str, content: str):
    with open(get_absolute_path(relative_path), 'w') as file:
        file.write(content)


def fill_template(template_name: str, fields: dict):
    template_path = f"scripts/template_generator/templates/{template_name}"
    template = read_from_repo(template_path)

    return template.format(**fields)


def append_line(relative_path: str, line: str):
    with open(get_absolute_path(relative_path), 'a') as file:
        file.write(line + '\n')


def replace_line(relative_path: str, line: str, replacement: str):
    absolute_path = get_absolute_path(relative_path)
    with open(absolute_path, 'r') as file:
        lines = file.readlines()

    with open(absolute_path, 'w') as file:
        for line in lines:
            if line.strip("\n") == line:
                file.write(replacement + '\n')
            else:
                file.write(line)

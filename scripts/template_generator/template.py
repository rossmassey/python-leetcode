import os
import re
import textwrap


def read_template(name: str) -> str:
    script_dir = os.path.dirname(__file__)
    template_path = os.path.join(script_dir, "templates/" + name)
    return read_file_contents(template_path)


def fill_template(template: str, fields: dict) -> str:
    fields["constraints_section"] = textwrap.indent(
        fields["constraints_section"],
        '\t' * 2
    )
    fields["intro_section"] = textwrap.indent(
        fields["intro_section"],
        '\t'
    )
    fields["examples_section"] = textwrap.indent(
        fields["examples_section"],
        '\t'
    )
    fields["params_section"] = textwrap.indent(
        fields["params_section"],
        '\t' * 3
    )

    # remove class/func from synced code
    indent_match = r'^(?! {8}).*(\n|$)'
    fixed_code = re.sub(indent_match, '', fields['code_section'], flags=re.MULTILINE)
    fields['code_section'] = fixed_code

    return template.format_map(fields)


def generate_solution(fields: dict) -> None:
    script_dir = os.path.dirname(__file__)

    solution_file_name = f"q_{fields['num_padded']}_{fields['title_slug_underscore']}.py"
    solution_path = os.path.join(script_dir, "../../src/leetcode/", solution_file_name)

    solution_template = read_template("question_template.txt")
    filled_solution_template = fill_template(solution_template, fields)

    write_file_contents(solution_path, filled_solution_template)


def read_file_contents(file_path: str) -> str:
    with open(file_path, 'r') as file:
        return file.read()


def write_file_contents(file_path: str, content: str) -> None:
    with open(file_path, 'w') as file:
        file.write(content)

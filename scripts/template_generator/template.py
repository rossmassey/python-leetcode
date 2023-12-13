import os
import re
import textwrap

SCRIPT_DIR = os.path.dirname(__file__)


def read_template(name: str) -> str:
    template_path = os.path.join(SCRIPT_DIR, "templates/" + name)
    return read_file_contents(template_path)


def fill_solution_template(template: str, fields: dict) -> str:
    tab = ' ' * 4  # 4 spaces instead of \t

    fields["constraints_section"] = textwrap.indent(
        fields["constraints_section"],
        tab * 2
    )
    fields["intro_section"] = textwrap.indent(
        fields["intro_section"],
        tab
    )
    fields["examples_section"] = textwrap.indent(
        fields["examples_section"],
        tab
    )
    fields["params_section"] = textwrap.indent(
        fields["params_section"],
        tab * 3
    )

    # remove class/func from synced code
    indent_match = r'^(?! {8}).*(\n|$)'
    fixed_code = re.sub(indent_match, '', fields['code_section'], flags=re.MULTILINE)
    fields['code_section'] = fixed_code

    return template.format_map(fields)


def generate_solution(fields: dict) -> None:
    # create solution template
    solution_file_name = f"q_{fields['num_padded']}_{fields['title_slug_underscore']}.py"
    solution_path = os.path.join(SCRIPT_DIR, "../../src/leetcode/", solution_file_name)

    solution_template = read_template("question_template.txt")
    filled_solution_template = fill_solution_template(solution_template, fields)

    write_file_contents(solution_path, filled_solution_template)

    # add to leetcode package
    leetcode_init_path = os.path.join(SCRIPT_DIR, "../../src/leetcode/", "__init__.py")
    import_statement = f"from .{solution_file_name[:-3]} import Solution{fields['num_padded']}\n"
    append_to_file(leetcode_init_path, import_statement)



def generate_doc(fields: dict) -> None:
    formatted_name = f"{fields['num_padded']}_{fields['title_slug_underscore']}"

    # automodule file
    doc_file_name = f"{formatted_name}.rst"
    doc_path = os.path.join(SCRIPT_DIR, "../../docs/source/leetcode", doc_file_name)

    doc_template = read_template("doc_template.txt")
    fields["doc_title_underline"] = '-' * len(f"0000 - {fields['title']}")
    filled_doc_template = doc_template.format_map(fields)

    write_file_contents(doc_path, filled_doc_template)

    # add to index import list
    index_path = os.path.join(SCRIPT_DIR, "../../docs/source", "neetcode.rst")
    append_to_file(index_path, f"   leetcode/{formatted_name}\n")

    # update ref link in neetcode index
    index_text = read_file_contents(index_path)
    human_text = f"{fields['num_padded']} - {fields['title']}"
    ref_text = f":ref:`{fields['num_padded']}_{fields['title_slug_underscore']}`"
    index_text = index_text.replace(human_text, ref_text)

    write_file_contents(index_path, index_text)


def read_file_contents(file_path: str) -> str:
    with open(file_path, 'r') as file:
        return file.read()


def write_file_contents(file_path: str, content: str) -> None:
    with open(file_path, 'w') as file:
        file.write(content)


def append_to_file(file_path: str, text: str) -> None:
    with open(file_path, 'a') as file:
        file.write(text)

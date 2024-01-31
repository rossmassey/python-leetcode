"""
This module contains the logic for processing the template files and references
"""
from ._formatter import format_fields
from ._file import fill_template, write_to_repo, append_line, replace_line

# sphinx rst use 3 space
DOC_TAB = ' ' * 3


def process_templates(fields: dict):
    """
    Process templates and writes files / updates references

    Args:
        fields (dict): problem info
    """

    fields = format_fields(fields)
    fields = _add_template_fields(fields)

    # write solution template
    solution_template = fill_template("question_template.txt", fields)
    solution_file_name = f'q_{fields["num_padded"]}_{fields["title_slug_underscore"]}'
    solution_path = f'src/leetcode/{solution_file_name}.py'
    write_to_repo(solution_path, solution_template)

    # add src/leetcode/__init__ import
    package_init = f'src/leetcode/__init__.py'
    import_stmt = f'from .{solution_file_name} import Solution{fields["num_padded"]}'
    append_line(package_init, import_stmt)

    # create doc automodule file
    doc_template = fill_template("doc_template.txt", fields)
    doc_file_name = f'{fields["num_padded"]}_{fields["title_slug_underscore"]}'
    doc_path = f'docs/source/leetcode/{doc_file_name}.rst'
    write_to_repo(doc_path, doc_template)

    # add to sphinx table of contents
    toc_location = f'docs/source/neetcode.rst'
    toc_entry = f'{DOC_TAB}leetcode/{doc_file_name}'
    append_line(toc_location, toc_entry)

    # update neetcode reference
    entry = f'{fields["num_padded"]} - {fields["title"]}'
    doc_ref = f':ref:`{fields["num_padded"]}_{fields["title_slug_underscore"]}`'
    replace_line(toc_location, entry, doc_ref)


def _add_template_fields(fields: dict) -> dict:
    """
    Add supplementary fields required for templates

    Args:
        fields (dict): base problem info

    Returns:
        dict: fields with supplementary fields added
    """
    num_padded = f'{int(fields["num"]):04}'
    title_slug_underscore = fields['slug'].replace('-', '_')

    title_name = f"`{fields['difficulty']} "
    title_url = f"<https://leetcode.com/problems/{fields['slug']}/>`_"
    title_header = title_name + title_url

    doc_title = f"{num_padded} - {fields['title']}"

    params = zip(fields['func']['params'], fields['func']['param_types'])
    func_name = fields['func']['name']

    combined_params = []
    for param, param_type in params:
        if param == 'self':
            continue
        combined_params.append(f'{param}: {param_type}')

    rtype = fields['func']['rtype']

    func_signature = f"{func_name}({', '.join(combined_params)}) -> {rtype}"

    return {
        **fields,
        'num_padded':             num_padded,
        'title_slug_underscore':  title_slug_underscore,
        'title_header':           title_header,
        'title_header_underline': '-' * len(title_header),
        'doc_title':              doc_title,
        'doc_title_underline':    '-' * len(doc_title),
        'func_signature':         func_signature,
    }

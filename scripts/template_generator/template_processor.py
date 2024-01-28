import formatter
import file


def process_templates(fields: dict):
    fields = formatter.format_fields(fields)
    fields = add_template_fields(fields)

    # process solution
    solution_template = file.fill_template("question_template.txt", fields)
    solution_file = f'q_{fields['num_padded']}_{fields['title_slug_underscore']}.py'
    solution_path = f'src/leetcode/{solution_file}'
    file.write_to_repo(solution_path, solution_template)

    # TODO add to leetcode __init__

    # process doc
    doc_template = file.fill_template("doc_template.txt", fields)
    doc_file = f'{fields['num_padded']}_{fields['title_slug_underscore']}.rst'
    doc_path = f'docs/source/leetcode/{doc_file}'
    file.write_to_repo(doc_path, doc_template)

    # TODO add to sphinx toc
    # TODO update neetcode link


def add_template_fields(fields: dict) -> dict:
    num_padded = f'{int(fields["num"]):04}'
    title_slug_underscore = fields['slug'].replace('-', '_')

    title_name = f"`#{fields['num']} - {fields['difficulty']} "
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
        'num_padded': num_padded,
        'title_slug_underscore': title_slug_underscore,
        'title_header': title_header,
        'title_header_underline': '-' * len(title_header),
        'doc_title': doc_title,
        'doc_title_underline': '-' * len(doc_title),
        'func_signature': func_signature,
        'code_section': 'tee hee'
    }



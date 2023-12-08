import json
import re

import network


def get_identifier_for(problem_num: int) -> list:
    """
    retrieve the identifier and slug for a given leetcode problem

    Parameters:
        problem_num (int): frontend question ID of leetcode problem

    Returns:
        list: containing internal question id (int) and title slug (str)
    """
    leetcode_data = json.loads(network.fetch_problems())
    problems = leetcode_data["stat_status_pairs"]

    for problem in problems:
        if problem["stat"]["frontend_question_id"] == problem_num:
            slug = problem["stat"]["question__title_slug"]
            question_id = problem["stat"]["question_id"]

            return [int(question_id), slug]

    return [-1, "not found"]


def parse_python_snippet(code: str) -> dict:
    """
    parses python code snippet for function signature and information

    Parameters:
        code (str): raw text containing leetcode code snippet

    Returns:
        dict: dictionary containing extracted function signature and information
    """
    # Remove lines starting with #
    code_lines = code.split('\n')
    code = '\n'.join(
        line for line in code_lines if not line.strip().startswith('#'))

    # Function signature
    func_signature_match = re.search(r'def (.+):', code)
    if not func_signature_match:
        raise ValueError("Function signature not found")

    func_signature = func_signature_match.group(1)

    # Function name
    func_name_match = re.match(r'(\w+)', func_signature)
    if not func_name_match:
        raise ValueError("Function name not found")

    func_name = func_name_match.group(1)

    # Parameters and parameter types
    params_match = re.search(r'\((.*?)\)', func_signature)
    if not params_match:
        raise ValueError("Parameters not found")

    params_with_types = params_match.group(1).split(',')
    params = []
    param_types = []

    for param in params_with_types:
        param = param.strip()
        if param != 'self':
            if ':' in param:
                p_name, p_type = param.split(':')
                params.append(p_name.strip())
                param_types.append(p_type.strip())
            else:
                params.append(param)
                param_types.append(None)

    # Return type
    rtype_match = re.search(r'-> (.*)', func_signature)
    rtype = rtype_match.group(1).strip() if rtype_match else None

    return {
        'func_signature': func_signature,
        'func_name': func_name,
        'params': params,
        'param_types': param_types,
        'rtype': rtype
    }


def clean_html(text: str) -> str:
    """
    cleans up leetcode problem content

    Parameters:
        text (str): HTML formatted problem text

    Returns:
        str: human readable problem text
    """
    # Replace <code>xx</code> with ``xx``, handling multiline and spaces
    text = re.sub(r'<code>([\s\S]*?)</code>', r'``\1``', text)

    # Replace <sup>xx</sup> with ^xx
    text = re.sub(r'<sup>(.*?)</sup>', r'^\1', text)

    # Replace <strong ... >xx</strong> with **xx**
    text = re.sub(r'<strong(?: [^>]*)?>(.*?)</strong>', r'**\1**', text)

    # Just get rid of italics (remove <em> tags)
    text = re.sub(r'<em>(.*?)</em>', r'\1', text)

    # Replace &nbsp; with space
    text = re.sub(r'&nbsp;', ' ', text)

    # Replace &quot; with "
    text = re.sub(r'&quot;', '"', text)

    # Remove <font> tags (including attributes and contents)
    text = re.sub(r'<font[^>]*>.*?</font>', '', text)

    # Remove other HTML tags
    text = re.sub(r'<[^>]+>', '', text)

    # Replace &lt; with <
    text = re.sub(r'&lt;', '<', text)

    # Replace &gt; with >
    text = re.sub(r'&gt;', '>', text)

    return text


def get_template_fields(slug: str) -> dict:
    """
    collects fields that will be used in template files

    Parameters:
        slug (str): leetcode title slug

    Returns:
        dict: fields like difficulty and func_name for template
    """
    lang = "python3"
    fields = {}
    problem_data = json.loads(network.fetch_graphql(
        network.query_problem(slug))
    )["data"]["question"]

    for snippet in problem_data["codeSnippets"]:
        if snippet["langSlug"] == lang:
            code = snippet["code"]
            fields = parse_python_snippet(code)

    fields["num"] = problem_data["questionFrontendId"]
    fields["difficulty"] = problem_data["difficulty"]
    fields["title"] = problem_data["title"]
    fields["title_slug"] = slug
    fields["content"] = clean_html(problem_data["content"])

    return fields


def get_synced_code(question_id: int) -> str:
    """
    gets last synced/saved user code for leetcode problem

    requires user to sign in and save cookies to cookies.txt

    Parameters:
        question_id (str): internal leetcode question id

    Returns:
        str: last synced user code
    """
    #  see: query languageList {  languageList {    id    name  }}
    python_id = 11

    synced_code = json.loads(network.fetch_graphql(
        network.query_synced_code(question_id, python_id))
    )["data"]["syncedCode"]

    if synced_code is None:
        return "No synced code found"
    else:
        return synced_code["code"]

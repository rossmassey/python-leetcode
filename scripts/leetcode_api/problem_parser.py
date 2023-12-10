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


def clean_html(text: str) -> str:
    """
    cleans up leetcode problem content

    Parameters:
        text (str): HTML formatted problem text

    Returns:
        str: human readable problem text
    """
    code_pattern = r'<code>([\s\S]*?)</code>'
    superscript_pattern = r'<sup>(.*?)</sup>'
    bold_pattern = r'<strong(?: [^>]*)?>(.*?)</strong>'
    italics_pattern = r'<em>(.*?)</em>'
    nbsp_pattern = r'&nbsp;'
    quote_pattern = r'&quot;'
    font_tag_pattern = r'<font[^>]*>.*?</font>'
    img_pattern = r'<img alt="" src="(.*?)" style=".*?" />'
    html_junk_pattern = r'<[^>]+>'
    less_than_pattern = r'&lt;'
    greater_than_pattern = r'&gt;'

    text = re.sub(code_pattern, r'``\1``', text)
    text = re.sub(superscript_pattern, r'^\1', text)
    text = re.sub(bold_pattern, r'**\1**', text)
    text = re.sub(italics_pattern, r'\1', text)  # remove italics
    text = re.sub(nbsp_pattern, ' ', text)
    text = re.sub(quote_pattern, '"', text)
    text = re.sub(font_tag_pattern, '', text)
    text = re.sub(img_pattern, ".. image:: \\1\n", text)  # rst format
    text = re.sub(html_junk_pattern, '', text)
    text = re.sub(less_than_pattern, '<', text)
    text = re.sub(greater_than_pattern, '>', text)

    return text


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


def parse_leetcode_content(text: str) -> dict:
    """
    parses leetcode content

    Parameters:
        text (str): leetcode content field

    Returns:
        dict: parsed content with intro, examples, constraints, and follow up
    """

    # clean and split text
    def clean_and_split(text: str) -> list:
        return [item.strip() for item in text.split('\n') if item.strip()]

    # clean and join text into a single string
    def clean_and_join(text: str) -> str:
        return ' '.join(clean_and_split(text))

    # re patterns for different sections
    example_pattern = r"\*\*Example (\d+):\*\*(.*?)(?:\.\. image:: (.*?))?\*\*Input:\*\*(.*?)\*\*Output:\*\*(.*?)(?:\*\*Explanation:\*\*(.*?))?(?=\*\*Example|\*\*Constraints|\*\*Follow up|$)"
    constraints_pattern = r"\*\*Constraints:\*\*(.*?)(?=\*\*|$)"
    follow_up_pattern = r"\*\*Follow up:\*\*(.*)"

    # intro
    intro = text.split("**Example 1:**")[0].strip()

    #  examples
    examples = []
    for match in re.finditer(example_pattern, text, re.DOTALL):
        example_number, _, image_url, input_text, output_text, explanation = match.groups()
        example = {
            "img": image_url.strip() if image_url else None,
            "inputs": clean_and_split(input_text),
            "output": clean_and_join(output_text),
            "explanation": clean_and_join(explanation) if explanation else None
        }
        examples.append(example)

    # constraints
    constraints_match = re.search(constraints_pattern, text, re.DOTALL)
    constraints = clean_and_split(constraints_match.group(1)) if constraints_match else []

    # follow up
    follow_up_match = re.search(follow_up_pattern, text, re.DOTALL)
    follow_up = follow_up_match.group(1).strip() if follow_up_match else None

    return {
        "intro": intro,
        "examples": examples,
        "constraints": constraints,
        "follow_up": follow_up
    }


def parse_python_snippet(code: str) -> dict:
    """
    parses python code snippet for function signature and information

    Parameters:
        code (str): raw text containing leetcode code snippet

    Returns:
        dict: dictionary containing extracted function signature and information
    """
    # remove comments
    code_lines = code.split('\n')
    code = '\n'.join(
        line for line in code_lines if not line.strip().startswith('#'))

    # function signature
    func_signature_match = re.search(r'def (.+):', code)
    if not func_signature_match:
        raise ValueError("Function signature not found")

    func_signature = func_signature_match.group(1)

    # function name
    func_name_match = re.match(r'(\w+)', func_signature)
    if not func_name_match:
        raise ValueError("Function name not found")

    func_name = func_name_match.group(1)

    # parameters
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

    # return
    rtype_match = re.search(r'-> (.*)', func_signature)
    rtype = rtype_match.group(1).strip() if rtype_match else None

    return {
        'func_signature': func_signature,
        'func_name': func_name,
        'params': params,
        'param_types': param_types,
        'rtype': rtype
    }


def expand_field_arrays(fields: dict) -> dict:
    """
    converts arrays of fields like examples into text with newlines

    Parameters:
        fields (dict): current parsed leetcode fields

    Returns:
        dict: sections fields added
    """

    # constraints array
    constraints_section = ""
    for constraint in fields["constraints"]:
        constraints_section += f"* {constraint}\n"
    fields["constraints_section"] = constraints_section

    # examples array
    examples_section = ""
    for (i, example) in enumerate(fields["examples"], 1):
        examples_section += f":Example {i}:\n\n"
        examples_section += f">>> Solution{fields['num_padded']}."
        examples_section += f"{fields['func_name']}({example['inputs'][0]})\n"
        examples_section += f"{example['output']}\n\n"

        if example["img"] is not None:
            examples_section += f"..image:: {example['img']}\n\n"

        if example["explanation"] is not None:
            examples_section += f"{example['explanation']}\n\n"
    fields["examples_section"] = examples_section

    # params array
    params_section = ""
    for param, param_type in zip(fields["params"], fields["param_types"]):
        params_section += f"{param} ({param_type}): TODO \n"
    fields["params_section"] = params_section

    return fields


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

    # graphql request to get problem data
    problem_data = json.loads(network.fetch_graphql(
        network.query_problem(slug))
    )["data"]["question"]

    # grab code snippet for python
    for snippet in problem_data["codeSnippets"]:
        if snippet["langSlug"] == lang:
            fields = parse_python_snippet(snippet["code"])

    # remove html and extract content sections
    clean_content = clean_html(problem_data["content"])
    content_fields = parse_leetcode_content(clean_content)

    fields["num"] = problem_data["questionFrontendId"]
    fields["num_padded"] = fields["num"].zfill(4)
    fields["difficulty"] = problem_data["difficulty"]
    fields["title"] = problem_data["title"]
    fields["title_slug"] = slug
    fields["intro"] = content_fields["intro"]
    fields["constraints"] = content_fields["constraints"]
    fields["follow_up"] = content_fields["follow_up"]
    fields["examples"] = content_fields["examples"]

    fields = expand_field_arrays(fields)
    return fields

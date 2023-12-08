#!/usr/bin/python3

import requests
import os
import json
import re

GRAPHQL_URL = "https://leetcode.com/graphql"
PROBLEM_API_URL = "https://leetcode.com/api/problems/all/"

def fetch_graphql(payload):
    # copy from leetcode.com -> Network tab -> File: /graphql/ -> Cookies
    # cookies = {
    #     "_dd_s": "...",
    #     "csrftoken": "...",
    #     "LEETCODE_SESSION": "..."
    # }

    # or use extension to export cookies.txt from leetcode.com
    cookies = read_cookies()  # TODO: add try, ask for cookies to be pasted?

    response = requests.post(GRAPHQL_URL, json=payload, cookies=cookies)
    return response.text


def fetch_problems():
    response = requests.get(PROBLEM_API_URL)
    return response.text  # TODO cache problem list


# requires leetcode cookies to sync, otherwise will return null
def query_synced_code(question_id, language):
    return {
        "query": """
        query SyncedCode($questionId: Int!, $lang: Int!) {
          syncedCode(questionId: $questionId, lang: $lang) {
            code
          }
        }
        """,
        "variables": {
            "questionId": question_id,
            "lang": language
        }
    }


def query_problem(title_slug):
    return {
        "query": """
        query questionCustom($titleSlug: String!) {
            question(titleSlug: $titleSlug) {
                questionId
                questionFrontendId
                title
                difficulty
                content
                codeSnippets {
                    lang
                    langSlug
                    code
                }
            }
        }
        """,
        "variables": {
            "titleSlug": title_slug
        }
    }


def read_cookies():
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


def get_identifier_for(problem_num):
    leetcode_data = json.loads(fetch_problems())
    problems = leetcode_data["stat_status_pairs"]

    for problem in problems:
        if problem["stat"]["frontend_question_id"] == int(problem_num):
            slug = problem["stat"]["question__title_slug"]
            question_id = problem["stat"]["question_id"]

            return [int(question_id), slug]

    return [-1, "not found"]


def process_code_snippet(code):
    # Remove lines starting with #
    code_lines = code.split('\n')
    code = '\n'.join(line for line in code_lines if not line.strip().startswith('#'))

    # Function signature
    func_signature_match = re.search(r'def (.+):', code)
    if not func_signature_match:
        return "Function signature not found"

    func_signature = func_signature_match.group(1)

    # Function name
    func_name_match = re.match(r'(\w+)', func_signature)
    if not func_name_match:
        return "Function name not found"

    func_name = func_name_match.group(1)

    # Parameters and parameter types
    params_match = re.search(r'\((.*?)\)', func_signature)
    if not params_match:
        return "Parameters not found"

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


def scrape_html(text):
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

def get_template_fields(slug):
    lang = "python3"
    fields = {}
    problem_data = json.loads(fetch_graphql(query_problem(slug)))["data"]["question"]

    for snippet in problem_data["codeSnippets"]:
        if snippet["langSlug"] == lang:
            code = snippet["code"]
            fields = process_code_snippet(code)

    fields["num"] = problem_data["questionFrontendId"]
    fields["difficulty"] = problem_data["difficulty"]
    fields["title"] = problem_data["title"]
    fields["title_slug"] = slug
    fields["content"] = scrape_html(problem_data["content"])

    return fields


def get_synced_code(question_id):
    #  query languageList {  languageList {    id    name  }}
    python_id = 11
    synced_code = json.loads(fetch_graphql(query_synced_code(question_id, python_id)))["data"]["syncedCode"]

    if synced_code is None:
        return "No synced code found"
    else:
        return synced_code["code"]



# MAIN
def main():
    num = int(input("Enter problem number: "))

    (question_id, slug) = get_identifier_for(num)

    template = get_template_fields(slug)
    synced_code = get_synced_code(question_id)

    print("\nTemplate fields:")
    for field, value in template.items():
        print(f"{field}: {value}")

    print("\nSynced code:")
    print(synced_code)


main()
import requests
from cookies import read_cookies

GRAPHQL_URL = "https://leetcode.com/graphql"
PROBLEM_API_URL = "https://leetcode.com/api/problems/all/"


def fetch_graphql(payload: dict) -> str:
    """
    sends a request to leetcode's graphql endpoint

    Parameters:
        payload (dict): graphql query or mutation along with variables

    Returns:
        str: JSON format text response
    """
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


def fetch_problems() -> str:
    """
    sends a request to leetcode's all problem listing

    Returns:
        str: JSON format text response with all leetcode problems

    """
    response = requests.get(PROBLEM_API_URL)
    return response.text  # TODO cache problem list


def query_synced_code(question_id: int, language: int) -> dict:
    """
    graphql query payload for latest synced user written code

    requires cookies.txt to be recent

    Parameters:
        question_id (int): internal question id (doesn't match problem num)
        language (int): leetcode programming language code

    Returns:
        dict: a dictionary containing the graphql query string and variables
    """
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


def query_problem(title_slug: str) -> dict:
    """
    graphql query payload for general problem info and default provided code

    Parameters:
        title_slug (str): leetcode title slug

    Returns:
        dict: a dictionary containing the graphql query string and variables
    """
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

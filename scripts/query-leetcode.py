import requests

def fetch_data(url, payload, cookies):
    response = requests.post(url, json=payload, cookies=cookies)
    return response.text

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

def query_code(title_slug):
    return {
        "query": """
        query questionCustom($titleSlug: String!) {
            question(titleSlug: $titleSlug) {
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


def query_question_content(title_slug):
    return {
        "query": """
        query questionCustom($titleSlug: String!) {
            question(titleSlug: $titleSlug) {
                questionFrontendId
                title
                difficulty
                content
            }
        }
        """,
        "variables": {
            "titleSlug": title_slug
        }
    }

def read_cookies_to_json(file_path):
    cookies = {}
    with open(file_path, 'r') as file:
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


def query():
    url = "https://leetcode.com/graphql"
    
    question_id = 1
    language = 11
    title_slug = "two-sum"
    
    # payload = query_synced_code(question_id, language)
    payload = query_code(title_slug)
    # payload = query_question_content(title_slug)

    # copy from leetcode.com -> Network tab -> File: /graphql/ -> Cookies
    # cookies = {
    #     "_dd_s": "...",
    #     "csrftoken": "...",
    #     "LEETCODE_SESSION": "..."
    # }

    # or use extension to export cookies.txt from leetcode.com 
    cookies = read_cookies_to_json("cookies.txt")

    print(fetch_data(url, payload, cookies))

query()
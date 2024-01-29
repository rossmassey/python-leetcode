#!/usr/bin/python3
"""
Interactive script to get problem info from leetcode for given ``num``

This script will:

- create ``src/leetcode/q_num_title.py``
    - adds LeetCode problem name, difficulty, description, constraints
    - generate doctest from examples
    - generate docstring from code snippet
    - sync user code from LeetCode if available

- create ``docs/source/leetcode/num_title.rst``
    - generates Sphinx documentation

- updates ``docs/source/neetcode.rst``
    - update problem reference

This expects ``cookies.txt`` to be in same directory

See `rossmassey.fetch-leetcode-problem <https://pypi.org/project/rossmassey.fetch-leetcode-problem/>`_
for usage on ``cookies.txt`` and updating problem listing
"""
import os
import fetch_leetcode_problem

from ._template_processor import process_templates


def main():
    """
    Main entry point
    """
    # cookies token for synced user code
    script_dir = os.path.dirname(__file__)
    cookie_path = os.path.join(script_dir, 'cookies.txt')

    try:
        fetch_leetcode_problem.load_cookie(cookie_path)
    except Exception as error:
        print(f'{type(error)}: {error}')
        print('No synced code will be available')


    # local db acts as lookup table for problem num -> title slug/question id
    if fetch_leetcode_problem.count_problems() == 0:
        update = input("No problems in database ... update problems? (y/n) ")

        if update.lower() == 'y':
            fetch_leetcode_problem.update_problem_listing()
        else:
            exit(0)

    # ask user for problem number
    try:
        num = int(input("Enter problem number: "))
    except ValueError:
        print("Invalid number")
        exit(1)

    print("Fetching problem info...")
    fields = fetch_leetcode_problem.get_problem(num)
    if not fields:
        print("Problem not found")
        exit(1)
    else:
        print(f"Found {fields['title']}")

    print("Writing templates...")
    process_templates(fields)
    print("Done")


if __name__ == "__main__":
    main()

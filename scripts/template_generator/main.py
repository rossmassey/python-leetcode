#!/usr/bin/python3

import template
import fetch_leetcode_problem


def main():
    """
    interactive script to get problem info from leetcode
    """
    count = fetch_leetcode_problem.count_problems()
    if count == 0:
        update = input("No problems in database ... update problems? (y/n) ")
        if update.lower() == 'y':
            fetch_leetcode_problem.update_problem_listing()
        else:
            exit(0)

    try:
        num = int(input("Enter problem number: "))
    except ValueError:
        print("Invalid number")
        exit(1)

    try:
        fields = fetch_leetcode_problem.get_problem(num)
    except AttributeError:
        print("ERROR: Known bug - param type/rtype too nested")
        print("https://github.com/rossmassey/fetch-leetcode-problem/issues/1")
        exit(1)

    if not fields:
        print("Problem not found")
        exit(0)

    print(fields)
    fields['num_padded'] = 'TODO'
    fields['title_slug_underscore'] = 'TODO'
    fields['constraints_section'] = 'TODO'
    fields['intro_section'] = 'TODO'
    fields['examples_section'] = 'TODO'
    fields['params_section'] = 'TODO'
    fields['code_section'] = 'TODO'
    fields['title_slug'] = 'TODO'
    fields['title_underline'] = 'TODO'
    fields['func_signature'] = 'TODO'
    fields['rtype'] = 'TODO'


    print(f"Writing solution template...")
    template.generate_solution(fields)

    print(f"Writing doc template...")
    template.generate_doc(fields)


if __name__ == "__main__":
    main()

#!/usr/bin/python3

import fetch_leetcode_problem

import template
import formatter

from pprint import pprint


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

    fields = fetch_leetcode_problem.get_problem(num)

    if not fields:
        print("Problem not found")
        exit(0)

    template_fields = formatter.format_fields(fields)

    pprint(template_fields)

    print(f"Writing solution template...")
    # template.generate_solution(template_fields)

    print(f"Writing doc template...")
    # template.generate_doc(template_fields)


if __name__ == "__main__":
    main()

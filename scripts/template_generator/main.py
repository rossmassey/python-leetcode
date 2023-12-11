#!/usr/bin/python3

import problem_parser
import template


def main():
    """
    interactive script to get problem info from leetcode
    """
    num = int(input("Enter problem number: "))

    print(f"Finding {num}...")
    (question_id, slug) = problem_parser.get_identifier_for(num)

    print(f"Getting content for '{slug}'...")
    fields = problem_parser.get_template_fields(question_id, slug)

    print(f"Writing solution template...")
    template.generate_solution(fields)

    print(f"Writing doc template...")
    template.generate_doc(fields)


if __name__ == "__main__":
    main()

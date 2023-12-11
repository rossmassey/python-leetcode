#!/usr/bin/python3

import problem_parser
import template


def main():
    """
    interactive script to get problem info from leetcode
    """
    num = int(input("Enter problem number: "))

    (question_id, slug) = problem_parser.get_identifier_for(num)

    fields = problem_parser.get_template_fields(question_id, slug)
    title = fields["title"]

    print(f"Writing templates for '{title}'")
    template.generate_solution(fields)


if __name__ == "__main__":
    main()

#!/usr/bin/python3

import fetch_leetcode_problem

import template_processor


def main():
    """
    interactive script to get problem info from leetcode
    """
    if fetch_leetcode_problem.count_problems() == 0:
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

    print("Fetching problem info...")
    fields = fetch_leetcode_problem.get_problem(num)
    if not fields:
        print("Problem not found")
        exit(1)
    else:
        print(f"Found {fields['title']}")

    print("Writing templates...")
    template_processor.process_templates(fields)
    print("Done")

if __name__ == "__main__":
    main()

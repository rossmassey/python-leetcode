import problem_parser


def main():
    """
    interactive script to get problem info from leetcode

    TODO: generate solution file template
    """
    num = int(input("Enter problem number: "))

    (question_id, slug) = problem_parser.get_identifier_for(num)

    template = problem_parser.get_template_fields(slug)
    synced_code = problem_parser.get_synced_code(question_id)

    print("\nTemplate fields:")
    for field, value in template.items():
        print(f"{field}: {value}")

    print("\nSynced code:")
    print(synced_code)


if __name__ == "__main__":
    main()
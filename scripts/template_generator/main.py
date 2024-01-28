#!/usr/bin/python3

import fetch_leetcode_problem

import template_processor


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
        exit(1)

    template_processor.process_templates(fields)



    # fields['num_padded']              # create
    # fields['title_slug_underscore']   # create
    # fields['constraints_section']     #
    # fields['intro_section']           # description_section
    # fields['examples_section']        #
    # fields['params_section']          #
    # fields['code_section']            # hmm
    # fields['title_slug']              # slug
    # fields['title_underline']         # create
    # fields['func_signature']          # create
    # fields['rtype'] =                 # func.rtype

    print(f"Writing solution template...")
    # template.generate_solution(template_fields)

    print(f"Writing doc template...")
    # template.generate_doc(template_fields)




if __name__ == "__main__":
    main()

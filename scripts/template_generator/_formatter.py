"""
This module contains functions for formatting the template fields
"""
import textwrap

# 4 space tab
TAB = 4 * ' '


def format_fields(fields: dict) -> dict:
    """
    Expand list fields into paragraphs and indent content to align with
    associated docstring sections

    Args:
        fields (dict): fields containing problem info to format

    Returns:
        dict: formatted fields
    """
    description = fields['description']
    examples = _format_examples(fields)
    constraints = _format_constraints(fields['constraints'])
    params = _format_params(fields['func'])

    if fields['code']:
        synced_code = _format_code(fields['code'])

    formatted_fields = {
        # content
        'description_section': _indent(description, 1),
        'examples_section':    _indent(examples, 1),
        'constraints_section': _indent(constraints, 2),

        # doc string
        'params_section':      _indent(params, 3),

        # synced code
        'synced_code':         synced_code or ''  # already indented
    }

    return {**fields, **formatted_fields}


def _indent(text: str, level: int) -> str:
    """
    Indent text by level

    Args:
        text (str): text to indent
        level (int): how many levels to indent

    Returns:
        str: indented text
    """
    return textwrap.indent(text, TAB * level)


def _format_examples(fields: dict) -> str:
    """
    Goes through each example dict and formats it for docstring

    Create doctest from example input and output

    Includes image and explanation if available

    Args:
        fields (dict): fields containing problem info to format

    Returns:
        str: formatted examples
    """
    formatted_examples = []

    number = f'{int(fields['num']):04}'
    class_name = f'Solution{number}'
    func_name = f'>>> {class_name}.{fields['func']['name']}'

    for i, example in enumerate(fields['examples'], 1):
        formatted_example = f':Example {i}:\n\n'
        formatted_example += f'{func_name}({example['input']})\n'
        formatted_example += f'{example['output']}\n\n'

        if example['img']:
            formatted_example += f'{example['img']}\n\n'

        if example['explanation']:
            formatted_example += f'{example['explanation'].lstrip()}\n'

        formatted_examples.append(formatted_example)

    return '\n'.join(formatted_examples)


def _format_constraints(constraints: list) -> str:
    """
    Format constraints for docstring, as a rst list

    Args:
        constraints (list): list of constraints

    Returns:
        str: formatted constraints
    """
    return '\n'.join(f'* {constraint}' for constraint in constraints)


def _format_params(func: dict) -> str:
    """
    Format params for function docstring, google style guide format

    Args:
        func (dict): function info

    Returns:
        str: formatted params
    """
    formatted_params = []

    for param, param_type in zip(func['params'], func['param_types']):
        if param == 'self':
            continue

        formatted_params.append(f'{param}({param_type}): TODO')

    return '\n'.join(formatted_params)


def _format_code(code: str) -> str:
    """
    Removes class/func signature

    Assume only implementing a single function

    Args:
        code (str): synced user code

    Returns:
        str: user code without signatures (indented)
    """
    code_body = []
    for line in code.split('\n'):
        if 'def' in line or 'class' in line:
            continue
        code_body.append(line)

    return '\n'.join(code_body)

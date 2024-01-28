import textwrap

# 4 space tab
TAB = 4 * ' '


def format_fields(fields: dict) -> dict:
    description = fields['description']
    examples = _format_examples(fields)
    constraints = _format_constraints(fields['constraints'])
    params = _format_params(fields['func'])

    formatted_fields = {
        'description_section': _indent(description, 1),
        'examples_section':    _indent(examples, 1),
        'constraints_section': _indent(constraints, 2),
        'params_section':      _indent(params, 3)
    }

    return {**fields, **formatted_fields}


def _indent(text: str, level: int) -> str:
    return textwrap.indent(text, TAB * level)


def _format_examples(fields: dict) -> str:
    formatted_examples = []

    number = f'{int(fields['num']):04}'
    class_name = f'Solution{number}'
    func_name = f'>>> {class_name}.{fields['func']['name']}'

    for i, example in enumerate(fields['examples'], 1):
        formatted_example = f'Example {i}:\n'
        formatted_example += f'{func_name}({example['input']})\n'
        formatted_example += f'{example['output']}\n\n'

        if example['img']:
            formatted_example += f'{example['img']}\n\n'

        if example['explanation']:
            formatted_example += f'{example['explanation'].lstrip()}\n'

        formatted_examples.append(formatted_example)

    return '\n'.join(formatted_examples)


def _format_constraints(constraints: list) -> str:
    return '\n'.join(f'* {constraint}' for constraint in constraints)


def _format_params(func: dict) -> str:
    formatted_params = []

    for param, param_type in zip(func['params'], func['param_types']):
        if param == 'self':
            continue

        formatted_params.append(f'{param}({param_type}): TODO')

    return '\n'.join(formatted_params)

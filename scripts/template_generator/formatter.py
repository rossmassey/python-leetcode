import textwrap

# 4 space tab
TAB = 4 * ' '


def format_fields(fields: dict) -> dict:
    description = _indent(fields['description'], 1)

    examples = _format_examples(fields)
    examples = _indent(examples, 1)

    constraints = '\n'.join(fields['constraints'])
    constraints = _indent(constraints, 2)

    params = _format_params(fields['func'])
    params = _indent(params, 3)

    formatted_fields = {
        'description_section': description,
        'examples_section':    examples,
        'constraints_section': constraints,
        'params_section':      params
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
            formatted_example += f'{example['explanation']}\n'

        formatted_examples.append(formatted_example)

    return '\n'.join(formatted_examples)


def _format_params(func: dict) -> str:
    formatted_params = []

    for param, param_type in zip(func['params'], func['param_types']):
        if param == 'self':
            continue

        formatted_params.append(f'{param}({param_type}): TODO')

    return '\n'.join(formatted_params)

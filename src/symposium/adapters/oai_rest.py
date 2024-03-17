# -*- coding: utf-8 -*-
# Python

"""Copyright (c) Alexander Fedotov.
This source code is licensed under the license found in the
LICENSE file in the root directory of this source tree.
"""


def prepared_oai_messages(input):
    """
    :input_format
        messages = [
            {"role": "world",   "name": "openai",   "content": "Be an Abstract Intellect."},
            {"role": "human",   "name": "alex",     "content": "Can we discuss this?"},
            {"role": "machine", "name": "chatgpt",  "content": "Yes."}
            {"role": "human",   "name": "alex",     "content": "Then let's do it."}
        ]
    :outputformat
        messages = [
            {"role": "system",      "content": "Be an Abstract Intellect."}
            {"role": "user",        "content": "Can we discuss this?"}
            {"role": "assistant",   "content": "Yes."}
            {"role": "user",        "content": "Then let's do it."}
        ]
    """
    output_messages = []
    for message in input:
        output_message = {}
        if message['role'] == 'human':
            output_message['role'] = 'user'
        elif message['role'] == 'machine':
            output_message['role'] = 'assistant'
        elif message['role'] == 'world':
            output_message['role'] = 'system'
        output_message['content'] = message['content']
        output_messages.append(output_message)
    return input, output_messages


def formatted_oai_message(output_message):
    """
    :input_format
        messages = [
            {"role": "assistant",   "content": "I will lay it out later"}
        ]
    :outputformat
        messages = [
            {"role": "machine", "name": "chatgpt",   "content": "I will lay it out later"}
        ]
    """
    formatted_output = {}
    if output_message['role'] == 'assistant':
        formatted_output['role'] = 'machine'
        formatted_output['name'] = 'chatgpt'
        formatted_output['content'] = output_message['content']
    else:
        print('The role is not assistant')
    return formatted_output


def format_oai_output(output):
    """
    :list of choices
    :return: formatted_output, other
    """
    solo_candidate = output['choices'].pop(0)
    formatted_output = formatted_oai_message(solo_candidate['message'])
    if len(output['choices']) > 0:
        other = []
        for choice in output['choices']:
            other.append(formatted_oai_message(choice))
    else:
        other = None
    return formatted_output, other

# -*- coding: utf-8 -*-
# Python

"""Copyright (c) Alexander Fedotov.
This source code is licensed under the license found in the
LICENSE file in the root directory of this source tree.
"""


def prepared_ant_messages(input):
    """
    :input_format
        messages = [
            {"role": "human",   "name": "alex",     "content": "Can we discuss this?"},
            {"role": "machine", "name": "claude",   "content": "Yes."}
            {"role": "human",   "name": "alex",     "content": "Then let's do it."}
        ]
    :outputformat
        messages = [
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
        output_message['content'] = message['content']
        output_messages.append(output_message)
    return input, output_messages


def formatted_ant_output(output):
    """
    :input_format
        messages = [
            {"role": "assistant",   "content": "I will lay it out later"}
        ]
    :outputformat
        messages = [
            {"role": "machine", "name": "claude",   "content": "I will lay it out later"}
        ]
    """
    formatted_output = {}
    if output['role'] == 'assistant':
        formatted_output['role'] = 'machine'
        formatted_output['name'] = 'claude'
        formatted_output['content'] = output['content'][0]['text']
    else:
        print('The role is not assistant')
    return formatted_output

# -*- coding: utf-8 -*-
# Python

"""Copyright (c) Alexander Fedotov.
This source code is licensed under the license found in the
LICENSE file in the root directory of this source tree.
"""


def prepared_gem_messages(input):
    """
    :input_format
        messages = [
            {"role":"user","content": "Hello"}
        ]
    :outputformat
        messages = [
            {"role":"user", "parts":[{"text": "Hello!"}]}
        ]
    """
    output = []
    for message in input:
        output.append(
            {'role': message['role'],'parts': [{'text': message['content']}]}
        )
    return output



def formatted_gem_output(output):
    """
    :param output a dictionary returned from gemini_rest
    :return: formatted_output
    """
    solo_candidate = output['candidates'][0]['content']
    text = ''
    for part in solo_candidate['parts']:
        text += part['text'] + ' '
    formatted_output = {
        'role': solo_candidate['role'],
        'content': text
    }
    return formatted_output

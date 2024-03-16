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
            {"role":"user","content": "Hello"}
        ]
    :outputformat
        messages = [
            {"role":"user","content": "Hello"}
        ]
    """
    return input

def formatted_ant_output(output):
    """
    :param output a dictionary returned from gemini_rest
    :return: formatted_output
    """
    formatted_output = {'role': output['role'],
            'content': output['content'][0]['text']}
    return formatted_output

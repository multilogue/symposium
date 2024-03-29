# -*- coding: utf-8 -*-
# Python

"""Copyright (c) Alexander Fedotov.
This source code is licensed under the license found in the
LICENSE file in the root directory of this source tree.
"""
import os
from symposium.connectors.anthropic_rest import claud_complete, claud_message
from grammateus.entities import Grammateus


grammateus = Grammateus(origin='anthropic', location='convers.log')

# messages = [
#     {'role': 'human', 'name': 'alex', 'content': 'Put your name between the <name></name> tags.'},
# ]
# kwargs = {
#     "system": "be an Abstract Intellect.",
#     "max_tokens": 256
# }
# message = claud_message(
#     messages=messages,
#     recorder=grammateus,
#     **kwargs
# )
# if message is not None:
#     response=message['content']
kwargs = {
    "max_tokens": 256
}

messages = [
    {'role': 'human', 'name': 'alex', 'content': 'Put your name between the <name></name> tags.'}
]

message = claud_complete(
    messages,
    grammateus,
    **kwargs
)
if message is not None:
    response = message

print('ok')


if __name__ == '__main__':
    print('ok')
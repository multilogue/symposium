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

messages = [
    {'role': 'human', 'name': 'alex', 'content': 'Hello'}
]
message = claud_message(
    messages=messages,
    recorder=grammateus
)
response=message['content']

prompt = 'Hello'
completion = claud_complete(
    prompt,
    recorder=grammateus
)
response=completion['completion']

print('ok')


if __name__ == '__main__':
    print('ok')
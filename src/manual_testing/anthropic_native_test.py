# -*- coding: utf-8 -*-
# Python

"""Copyright (c) Alexander Fedotov.
This source code is licensed under the license found in the
LICENSE file in the root directory of this source tree.
"""
import os
from symposium.connectors.anthropic_native import get_claud_client, claud_complete, claud_message
from grammateus.entities import Grammateus

grammateus = Grammateus(origin='anthropic', location='convers.log')
ant = get_claud_client()

messages = [
    {'role': 'user','content': 'Hello'}
]
anthropic_message = claud_message(
    client=ant,
    messages=messages,
    recorder=grammateus
)
response=anthropic_message['content']

prompt = 'Hello'
anthropic_complete = claud_complete(
    ant,
    prompt,
    recorder=grammateus
)
completion = anthropic_complete['completion']

if __name__ == '__main__':
    print('ok')
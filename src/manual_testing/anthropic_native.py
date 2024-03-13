# -*- coding: utf-8 -*-
# Python

"""Copyright (c) Alexander Fedotov.
This source code is licensed under the license found in the
LICENSE file in the root directory of this source tree.
"""
import os
from symposium.connectors.anthropic import get_claud_client, claud_complete, claud_message
from grammateus.entities import Grammateus

grammateus = Grammateus(location='anthropic/conversation.log')
anthropic = get_claud_client()
messages = [
    {'role': 'user','content': 'Hello'}
]
anthropic_message = claud_message(
    client=anthropic,
    messages=messages,
    recorder=grammateus
)
prompt = 'Hello'
anthropic_complete = claud_complete(
    anthropic,
    prompt,
    recorder=grammateus
)
print('ok')


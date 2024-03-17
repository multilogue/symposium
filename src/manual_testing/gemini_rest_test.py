# -*- coding: utf-8 -*-
# Python

"""Copyright (c) Alexander Fedotov.
This source code is licensed under the license found in the
LICENSE file in the root directory of this source tree.
"""
from symposium.connectors.gemini_rest import gemini_message
from grammateus.entities import Grammateus


grammateus = Grammateus(origin='gemini', location='convers.log')

messages = [
        {"role":"human", "name":"alex", "content":"Hello"},
        {"role":"machine", "name":"gemini", "content":"Hi there"},
        {"role":"human", "name":"alex", "content":"How are you?"},
]
message = gemini_message(
    messages=messages,
    recorder=grammateus
)
response=message
print('ok')
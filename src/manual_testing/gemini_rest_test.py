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
        {"role":"user", "content":"Hello"}
]
message = gemini_message(
    messages=messages,
    recorder=grammateus
)
response=message['candidates'][0]['content']['parts'][0]['text']
print('ok')
# -*- coding: utf-8 -*-
# Python

"""Copyright (c) Alexander Fedotov.
This source code is licensed under the license found in the
LICENSE file in the root directory of this source tree.
"""

from os import environ
import dotenv
dotenv.load_dotenv()
from symposium.connectors import anthropic_rest as ant


def test_claud_message(self):
        messages = [
            {"role": "user", "content": "I am Alex"}
        ]
        kwa = {
            # "model": "claude-3-opus-20240229",
            "temperature": 0.5,
            "max_tokens": 5,
        }
        msgs = ant.claud_message(messages, **kwa)
        assert len(msgs) > 0


def test_claud_complete():
    assert False

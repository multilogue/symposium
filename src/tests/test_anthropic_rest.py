# -*- coding: utf-8 -*-
# Python

"""Copyright (c) Alexander Fedotov.
This source code is licensed under the license found in the
LICENSE file in the root directory of this source tree.
"""

from os import environ
from symposium.connectors import anthropic_rest as ant


class TestAnthropicRest:
    def test_claud_message(self):
        api_key = environ.get("ANTHROPIC_API_KEY")
        headers = {
            "x-api-key": api_key,
            "anthropic-version": "2023-06-01",
            "content-type": "application/json"
        }
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

# -*- coding: utf-8 -*-
# Python

"""Copyright (c) Alexander Fedotov.
This source code is licensed under the license found in the
LICENSE file in the root directory of this source tree.
"""

from os import environ
from symposium.connectors import anthropic_rest as ant


api_key             = environ.get("ANTHROPIC_API_KEY")
organization        = environ.get("ANTHROPIC_ORGANIZATION", "")
api_base            = environ.get("ANTHROPIC_API_BASE", "https://api.anthropic.com/v1")
api_type            = environ.get("ANTHROPIC_VERSION", "2023-06-01")
default_model       = environ.get("ANTHROPIC_DEFAULT_MODEL", "claude-instant-1.2")
completion_model    = environ.get("ANTHROPIC_COMPLETION_MODEL",'claude-instant-1.2')
message_model       = environ.get("ANTHROPIC_MESSAGE_MODEL",'claude-2.0')

HUMAN_PREFIX        = "\n\nHuman:"
MACHINE_PREFIX      = "\n\nAssistant:"

headers = {
    "x-api-key": api_key,
    "anthropic-version": "2023-06-01",
    "content-type": "application/json"
}


class TestAnthropicRest:
    def test_claud_message(self):
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

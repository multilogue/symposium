# -*- coding: utf-8 -*-
# Python

"""Copyright (c) Alexander Fedotov.
This source code is licensed under the license found in the
LICENSE file in the root directory of this source tree.
"""
from symposium.connectors.together_native import get_together_client, together_message
from grammateus.entities import Grammateus
from yaml import safe_load as yl


# mod = together_models()
grammateus = Grammateus(origin='together', location='conversation_test.log')

client_kwargs = f"""    # this is a yaml text
    timeout:      120.0
    max_retries:  4  # default is 3
"""

client = get_together_client(**yl(client_kwargs))

messages = """
    - role: human
      name: alex
      content: Put your name between the <name></name> tags.
"""
kwargs = """
    max_tokens: 100
    n: 1
"""

message = together_message(
    client=client,
    messages=yl(messages),
    recorder=grammateus,
    **yl(kwargs)
)
response=message


if __name__ == "__main__":
    print("You launched main.")



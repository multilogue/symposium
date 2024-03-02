# -*- coding: utf-8 -*-
# Python

"""Copyright (c) Alexander Fedotov.
This source code is licensed under the license found in the
LICENSE file in the root directory of this source tree.
"""


def get_client():
    client = None
    try:
        from google.ai import generativelanguage as glm
        client = glm.DiscussServiceClient(
            # defaults to os.environ.get("OPENAI_API_KEY")
            # client_options={"api_key": "my_api_key"},
        )
    except ImportError:
        print("openai package is not installed")

    return client


def message(client, **kwargs):
    """ All parameters should be in kwargs, but they are optional
    """
    request = client.GenerateMessageRequest(
        model='models/chat-bison-001',
        prompt = client.MessagePrompt(
            messages=[client.Message(content='I am Alex')]
        )
    )
    msg = None
    try:
        msg = client.generate_message(request)
    except Exception as e:
        print(e)
    return msg


if __name__ == "__main__":
    client = get_client()
    msg = message(client)
    print("ok")
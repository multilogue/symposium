# -*- coding: utf-8 -*-
# Python

"""Copyright (c) Alexander Fedotov.
This source code is licensed under the license found in the
LICENSE file in the root directory of this source tree.
"""
from os import environ
import requests

api_key             = environ.get("ANTHROPIC_API_KEY")
organization        = environ.get("ANTHROPIC_ORGANIZATION", "")
api_base            = environ.get("ANTHROPIC_API_BASE", "https://api.anthropic.com/v1")
api_type            = environ.get("ANTHROPIC_VERSION", "2023-06-01")
default_model       = environ.get("ANTHROPIC_DEFAULT_MODEL", "claude-instant-1.2")
completion_model    = environ.get("ANTHROPIC_COMPLETION_MODEL",'claude-instant-1.2')
message_model       = environ.get("ANTHROPIC_MESSAGE_MODEL",'claude-3-sonnet-20240229')
# claude-3-opus-20240229, claude-3-sonnet-20240229

HUMAN_PREFIX        = "\n\nHuman:"
MACHINE_PREFIX      = "\n\nAssistant:"

headers = {
    "x-api-key": api_key,
    "anthropic-version": "2023-06-01",
    "content-type": "application/json"
}


def claud_complete(prompt=None, recorder=None, **kwargs):
    """ All parameters should be in kwargs, but they are optional
    """
    json_data = {
        "model":                kwargs.get("model", completion_model),
        "max_tokens_to_sample": kwargs.get("max_tokens", 1),
        "prompt":               kwargs.get("prompt", f"{HUMAN_PREFIX}{prompt}{MACHINE_PREFIX}"),
        "stop_sequences":       kwargs.get("stop_sequences",[HUMAN_PREFIX]),
        "temperature":          kwargs.get("temperature", 0.5),
        "top_k":                kwargs.get("top_k", 250),
        "top_p":                kwargs.get("top_p", 0.5),
        "metadata":             kwargs.get("metadata", None)
    }
    responses = []
    try:
        response = requests.post(
            f"{api_base}/complete",
            headers=headers,
            json=json_data,
        )
        if response.status_code == requests.codes.ok:
            completion_dump = response.json()
            if recorder:
                log_message = {"query": json_data, "response": {"message": completion_dump}}
                recorder.log_event(log_message)
        else:
            print(f"Request status code: {response.status_code}")
            completion_dump = None
        if recorder:
            rec = {"prompt": json_data["prompt"], "completion": completion_dump['completion']}
            recorder.record(rec)
        return completion_dump
    except Exception as e:
        print("Unable to generate Completions response")
        print(f"Exception: {e}")
        return None


def claud_message(messages=None, recorder=None, **kwargs):
    """ All parameters should be in kwargs, but they are optional
    """
    json_data = {
        "model":                kwargs.get("model", message_model),
        "system":               kwargs.get("system", "answer concisely"),
        "messages":             kwargs.get("messages", messages),
        "max_tokens":           kwargs.get("max_tokens", 1),
        "stop_sequences":       kwargs.get("stop_sequences",['stop', HUMAN_PREFIX]),
        "stream":               kwargs.get("stream", False),
        "temperature":          kwargs.get("temperature", 0.5),
        "top_k":                kwargs.get("top_k", 250),
        "top_p":                kwargs.get("top_p", 0.5),
        "metadata":             kwargs.get("metadata", None)
    }
    try:
        response = requests.post(
            f"{api_base}/messages",
            headers=headers,
            json=json_data,
        )
        if response.status_code == requests.codes.ok:
            msg_dump = response.json()
            if recorder:
                log_message = {"query": json_data, "response": {"message": msg_dump}}
                recorder.log_event(log_message)
        else:
            print(f"Request status code: {response.status_code}")
            return None
        if recorder:
            rec = {"messages": json_data['messages'], "response": msg_dump['content']}
            recorder.record(rec)
        return msg_dump

    except Exception as e:
        print("Unable to generate Message response")
        print(f"Exception: {e}")
        return None


if __name__ == "__main__":
    print("you launched main.")
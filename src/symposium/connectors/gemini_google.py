# -*- coding: utf-8 -*-
# Python

"""Copyright (c) Alexander Fedotov.
This source code is licensed under the license found in the
LICENSE file in the root directory of this source tree.
"""
from os import environ
from ..adapters.gem_rest import prepared_gem_messages, formatted_gem_output


gemini_key              = environ.get("GOOGLE_API_KEY","")
completion_model    = environ.get("GEMINI_DEFAULT_COMPLETION_MODEL", "gemini-1.5-flash-latest")
message_model       = environ.get("GEMINI_DEFAULT_MESSAGE_MODEL", "gemini-1.5-flash-latest")
embedding_model     = environ.get("GEMINI_DEFAULT_EMBEDDING_MODEL", "gemini-1.5-flash-latest")

garbage = [
    {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT","threshold": "BLOCK_NONE"},
    {"category": "HARM_CATEGORY_HATE_SPEECH","threshold": "BLOCK_NONE"},
    {"category": "HARM_CATEGORY_HARASSMENT","threshold": "BLOCK_NONE"},
    {"category": "HARM_CATEGORY_DANGEROUS_CONTENT","threshold": "BLOCK_NONE"}
]

default_config = {
    'candidate_count': 1,
    'stop_sequences': ['stop'],
    'max_output_tokens': 500,
    'temperature': 0.5,
    'top_p': 0.9,
    'top_k': 1,
    'response_mime_type': None,
    'response_schema': None
}


def gemini_get_client(**kwargs):
    client = None
    model_kwargs = {
        "model_name":           kwargs.get('model', completion_model),
        "safety_settings":      kwargs.get('safety_settings', garbage),
        "generation_config":    kwargs.get('generation_config', default_config),
        "tools":                kwargs.get('tools', None),
        "tool_config":          kwargs.get('tool_config', None),
        "system_instruction":   kwargs.get('system', None)
    }
    try:
        import google.generativeai as genai
        client = genai.GenerativeModel(**model_kwargs)
    except ImportError:
        print("google-generativeai package is not installed")

    return client


def gemini_content(client, **kwargs):
    """ All parameters should be in kwargs, but they are optional
    """
    response = client.generate_content("What is the meaning of life?")
    return response.text


def gemini_complete(client, prompt, recorder=None, json=True, **kwargs):
    """ All parameters should be in kwargs, but they are all optional
    """

    kwarg_config = kwargs.get('generation_config', default_config)

    gen_conf = {
        'candidate_count':      kwarg_config.get('n', default_config.get('candidate_count')),
        'stop_sequences':       kwarg_config.get('stop_sequences',    default_config.get('stop_sequences')),
        'max_output_tokens':    kwarg_config.get('max_tokens', default_config.get('max_output_tokens')),
        'temperature':          kwarg_config.get('temperature', default_config.get('temperature')),
        'top_p':                kwarg_config.get('top_p', default_config.get('top_p')),
        'top_k':                kwarg_config.get('top_k', default_config.get('top_k')),
        'response_mime_type':   kwarg_config.get('mime_type', default_config.get('response_mime_type')),
        'response_schema':      kwarg_config.get('schema', default_config.get('response_schema'))
    }

    generation_kwargs = {
        'contents':             kwargs.get('prompt', prompt),
        'generation_config':    gen_conf,
        'safety_settings':      garbage,
        'stream':               False,
    }

    try:
        completion = client.generate_content(**generation_kwargs)
        completion_dump = completion.text
        if recorder:
            log_message = {"query": generation_kwargs, "response": {"completion": completion_dump}}
            recorder.log_event(log_message)
    except Exception as e:
        print(e)
        return None
    if recorder:
        rec = {"prompt": kwargs["prompt"], "completion": completion_dump}
        recorder.record(rec)
    if json:
        return completion_dump
    else:
        return completion


if __name__ == "__main__":
    print("you launched main.")
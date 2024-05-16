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


def gemini_get_client(**kwargs):
    client = None
    try:
        import google.generativeai as genai
        # generation_config = genai.GenerationConfig(
        #     max_output_tokens=kwargs.get('max_tokens_to_sample', 5),
        #     temperature=kwargs.get('temperature', 0.5),
        #     top_k=kwargs.get('top_k', 1),
        #     top_p=kwargs.get('top_p', 0.9),
        # )
        client = genai.GenerativeModel(model_name= kwargs.get('model_name', 'gemini-1.5-flash-latest'),
                                       safety_settings=garbage,
                                       system_instruction=kwargs.get('system_instruction', None))
    except ImportError:
        print("google-generativeai package is not installed")

    return client


def gemini_content(client, **kwargs):
    """ All parameters should be in kwargs, but they are optional
    """
    response = client.generate_content("What is the meaning of life?")
    return response.text


def gemini_complete(client, prompt, recorder=None, json=True, **kwargs):
    """ All parameters should be in kwargs, but they are optional
    """
    kwoo = {
        "model":            kwargs.get("model", completion_model),
        "max_tokens":       kwargs.get("max_tokens_to_sample", 5),
        "prompt":           kwargs.get("prompt", prompt),
        "suffix":           kwargs.get("suffix", None),
        "stop":             kwargs.get("stop_sequences", ["stop"]),
        "n":                kwargs.get("n", 1),
        "best_of":          kwargs.get("best_of", 1),
        "seed":             kwargs.get("seed", None),
        "frequency_penalty":kwargs.get("frequency_penalty", None),
        "presence_penalty": kwargs.get("presence_penalty", None),
        "logit_bias":       kwargs.get("logit_bias", {}),
        "logprobs":         kwargs.get("logprobs", None),
        "temperature":      kwargs.get("temperature", 0.5),
        "top_p":            kwargs.get("top_p", 0.5),
        # "user":             kwargs.get("user", None)
    }
    """
        generate_content(
        contents: content_types.ContentsType,
        *,
        generation_config: (generation_types.GenerationConfigType | None) = None,
        safety_settings: (safety_types.SafetySettingOptions | None) = None,
        stream: bool = False,
        tools: (content_types.FunctionLibraryType | None) = None,
        tool_config: (content_types.ToolConfigType | None) = None,
        request_options: (dict[str, Any] | None) = None
    ) -> generation_types.GenerateContentResponse
    """
    gen_conf = {
        "candidate_count": 1,
        "stop_sequences": [],
        "max_output_tokens": kwargs.get("max_tokens_to_sample", 1000),
        "temperature": kwargs.get("temperature", 0.5),
        "top_p":  kwargs.get("top_p", 0.5),
        "top_k": kwargs.get("top_k", 1),
        "response_mime_type": "text/plain",
        "response_schema":  None
    }
    kwa = {
        # "contents": kwargs.get("prompt", prompt),
        # "generation_config": gen_conf,
        "safety_settings": garbage,
        "stream": False,
          }
    try:
        completion = client.generate_content(prompt,generation_config=gen_conf, **kwa)
        completion_dump = completion.text
        if recorder:
            log_message = {"query": kwa, "response": {"completion": completion_dump}}
            recorder.log_event(log_message)
    except Exception as e:
        print(e)
        return None
    if recorder:
        rec = {"prompt": kwa["prompt"], "completion": completion_dump['choices']}
        recorder.record(rec)
    if json:
        return completion_dump
    else:
        return completion


if __name__ == "__main__":
    print("you launched main.")
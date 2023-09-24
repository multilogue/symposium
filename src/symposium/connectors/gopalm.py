# -*- coding: utf-8 -*-
# Python

"""Copyright (c) Alexander Fedotov.
This source code is licensed under the license found in the
LICENSE file in the root directory of this source tree.
"""
from os import environ
from typing import List
import requests


palm_key                = environ.get("PALM_KEY", "")
palm_api_base           = "https://generativelanguage.googleapis.com/v1beta3"
palm_completion_model   = environ.get("PALM_DEFAULT_TEXT_MODEL", "models/text-bison-001")
palm_chat_model         = environ.get("PALM_DEFAULT_CHAT_MODEL", "models/chat-bison-001")


def continuations(text_before,
                  model=palm_completion_model,
                  **kwargs) -> List:

    """A completions endpoint call through requests.
        kwargs:
            temperature     = 0 to 1.0
            top_p           = 0.0 to 1.0
            top_k           = The maximum number of tokens to consider when sampling.
            n               = 1 to 8 # number of candidates
            max_tokens      = number of tokens
            stop            = ["stop"]  array of up to 4 sequences
    """
    garbage = [{"category": 0, "threshold": 4}, {"category": 1, "threshold": 4},
               {"category": 2, "threshold": 4}, {"category": 3, "threshold": 4},
               {"category": 4, "threshold": 4}, {"category": 5, "threshold": 4}]

    responses = []
    json_data = {"prompt": {"text": text_before},
                 "temperature":     kwargs.get("temperature", 0.5),
                 "candidateCount":  kwargs.get("n", 1),
                 "safetySettings":  garbage,
                 "maxOutputTokens": kwargs.get("max_tokens", 100),
                 "topP":            kwargs.get("top_p", 0.1),
                 "topK":            kwargs.get("top_k", None)}
    try:
        response = requests.post(
            f"{palm_api_base}/{model}:generateText",
            params=f"key={palm_key}",
            json=json_data,
        )
        if response.status_code == requests.codes.ok:
            for count, candidate in enumerate(response.json()['candidates']):
                item = {"index": count, "text": candidate['output']}
                responses.append(item)
        else:
            print(f"Request status code: {response.status_code}")
        return responses
    except Exception as e:
        print("Unable to generate Completions response")
        print(f"Exception: {e}")
        return responses


# class HarmCategory(Enum):
#     r"""The category of a rating.
#
#     These categories cover various kinds of harms that developers
#     may wish to adjust.
#
#     Values:
#         HARM_CATEGORY_UNSPECIFIED (0):
#             Category is unspecified.
#         HARM_CATEGORY_DEROGATORY (1):
#             Negative or harmful comments targeting
#             identity and/or protected attribute.
#         HARM_CATEGORY_TOXICITY (2):
#             Content that is rude, disrepspectful, or
#             profane.
#         HARM_CATEGORY_VIOLENCE (3):
#             Describes scenarios depictng violence against
#             an individual or group, or general descriptions
#             of gore.
#         HARM_CATEGORY_SEXUAL (4):
#             Contains references to sexual acts or other
#             lewd content.
#         HARM_CATEGORY_MEDICAL (5):
#             Promotes unchecked medical advice.
#         HARM_CATEGORY_DANGEROUS (6):
#             Dangerous content that promotes, facilitates,
#             or encourages harmful acts.
#     """
#     HARM_CATEGORY_UNSPECIFIED = 0
#     HARM_CATEGORY_DEROGATORY = 1
#     HARM_CATEGORY_TOXICITY = 2
#     HARM_CATEGORY_VIOLENCE = 3
#     HARM_CATEGORY_SEXUAL = 4
#     HARM_CATEGORY_MEDICAL = 5
#     HARM_CATEGORY_DANGEROUS = 6
#
#
# safety_settings = {
#     "category": 0,
#     "threshold": 4
# }
#
#
# # easy = safety_types.
# permissive_safety_settings = safety_types.SafetySettingOptions(
#
# )


# def generate_text_request(
#     *,
#     model: model_types.AnyModelNameOptions = DEFAULT_TEXT_MODEL,
#     prompt: str | None = None,
#     temperature: float | None = None,
#     candidate_count: int | None = None,
#     max_output_tokens: int | None = None,
#     top_p: int | None = None,
#     top_k: int | None = None,
#     safety_settings: safety_types.SafetySettingOptions | None = None,
#     stop_sequences: str | Iterable[str] | None = None,
# ) -> glm.GenerateTextRequest:
#     """
#     Creates a `glm.GenerateTextRequest` object based on the provided parameters.
#
#     This function generates a `glm.GenerateTextRequest` object with the specified
#     parameters. It prepares the input parameters and creates a request that can be
#     used for generating text using the chosen model.
#
#     Args:
#         model: The model to use for text generation.
#         prompt: The prompt for text generation. Defaults to None.
#         temperature: The temperature for randomness in generation. Defaults to None.
#         candidate_count: The number of candidates to consider. Defaults to None.
#         max_output_tokens: The maximum number of output tokens. Defaults to None.
#         top_p: The nucleus sampling probability threshold. Defaults to None.
#         top_k: The top-k sampling parameter. Defaults to None.
#         safety_settings: Safety settings for generated text. Defaults to None.
#         stop_sequences: Stop sequences to halt text generation. Can be a string
#              or iterable of strings. Defaults to None.
#
#     Returns:
#         `glm.GenerateTextRequest`: A `GenerateTextRequest` object configured with the specified parameters.
#     """
#     model = model_types.make_model_name(model)
#     safety_settings = safety_types.normalize_safety_settings(safety_settings)
#     if isinstance(stop_sequences, str):
#         stop_sequences = [stop_sequences]
#     if stop_sequences:
#         stop_sequences = list(stop_sequences)
#
#     return glm.GenerateTextRequest(
#         model=model,
#         prompt=prompt,
#         temperature=temperature,
#         candidate_count=candidate_count,
#         max_output_tokens=max_output_tokens,
#         top_p=top_p,
#         top_k=top_k,
#         safety_settings=safety_settings,
#         stop_sequences=stop_sequences,
#     )


if __name__ == '__main__':
    kwa = {
        "n": 3,
        "top_k": 100
    }
    a = continuations(text_before="Can you distinguish an idiot from a human?", **kwa)
    print('ok')


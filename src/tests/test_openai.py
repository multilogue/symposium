# -*- coding: utf-8 -*-
# Python

"""Copyright (c) Alexander Fedotov.
This source code is licensed under the license found in the
LICENSE file in the root directory of this source tree.
"""
import symposium.connectors.openai as openai


def test_get_openai_client():
    client = openai.get_openai_client()
    assert False

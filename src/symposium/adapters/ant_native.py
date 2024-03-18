# -*- coding: utf-8 -*-
# Python

"""Copyright (c) Alexander Fedotov.
This source code is licensed under the license found in the
LICENSE file in the root directory of this source tree.
"""
from copy import deepcopy
import xml.etree.ElementTree as ElementTree


def extract_xml_tagged_content(text):
    """
    :input_format
        <message>
            This is some text with <tag_one>XML-tagged content</tag_one>.
            Another <tag_two>XML-tagged</tag_two> portion is here.
        </message>
    :outputformat
        This is some text with {{tag}} content. Another {{tag}} portion is here.
        [ {'tag_one': 'XML-tagged content'}, {'tag_two': 'XML-tagged'} ]

    BEWARE MULTI-LEVELED TAGS!!!
    """
    root = ElementTree.fromstring(text)
    # Extract all the tags
    txt = ' '.join(root.itertext()); tags = []
    tag_iter = root.iter(); next(tag_iter)
    for item in tag_iter:
        tag = item.tag
        text = item.text
        txt = txt.replace(text, f"({tag})")
        tags.append({tag: text})
    return txt, tags


def prepared_ant_messages(input):
    """
    :input_format
        messages = [
            {"role":"user","content": "Hello"}
        ]
    :outputformat
        messages = [
            {"role":"user","content": "Hello"}
        ]
    """
    return input


# Tagged content extraction






def main():
    # Example plain text with XML tags
    string = """
    This is some text with <tag_one>XML-tagged content</tag_one>. Another <tag_two>XML-tagged</tag_two> portion is here.
    """
    message = f'<message>{string}</message>'
    # Extract tagged content and replace with placeholders
    modified_text, tags = extract_xml_tagged_content(message)

    # Print modified text
    print("Modified Text:")
    print(modified_text)



if __name__ == "__main__":
    main()
    print("ok")

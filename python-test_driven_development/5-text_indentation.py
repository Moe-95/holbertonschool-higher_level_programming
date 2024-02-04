#!/usr/bin/python3
"""
This module contains a function that prints a text with 2 new lines after each of these characters: ., ? and :
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these characters: ., ? and :

    Args:
        text (str): The input text.

    Raises:
        TypeError: If text is not a string.

    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    text = text.strip()

    punctuation = ['.', '?', ':']
    for char in text:
        print(char, end='')
        if char in punctuation:
            print('\n')
            print()

# -*- coding: utf-8 -*-


"""
Description: File format determination library
Author: Mykyta Paliienko
License: MIT
"""


import os
import json


with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "data.json")) as data_file:
    data = json.loads(data_file.read())["data"]


class Info:
    """
    Does:
        Generates object with given arguments

    Takes:
        type_ -> list of file types
        extension -> list of file extensions
        mime -> list of file MIME types

    Returns:
        Object
    """

    def __init__(self, type_, extension, mime):
        self.type = type_
        self.extension = extension
        self.mime = mime

    def type_matches(self, type_):
        """ Checks if file type matches with given type """
        return type_ in self.type

    def extension_matches(self, extension):
        """ Checks if file extension matches with given extension """
        return extension in self.extension

    def mime_matches(self, mime):
        """ Checks if file MIME type matches with given MIME type """
        return mime in self.mime


def get(obj):
    """
    Does:
        Determines file format and picks suitable file types, extensions and MIME types

    Takes:
        obj -> byte sequence (128 bytes are enough)

    Returns:
        Instance of class Info
    """

    if not isinstance(obj, bytes):
        raise TypeError("object type must be bytes")

    info = {
        "type": dict(),
        "extension": dict(),
        "mime": dict()
    }

    stream = " ".join(['{:02X}'.format(byte) for byte in obj])

    for element in data:
        for signature in element["signature"]:
            offset = element["offset"] * 2 + element["offset"]
            if signature == stream[offset:len(signature) + offset]:
                for key in ["type", "extension", "mime"]:
                    info[key][element[key]] = len(signature)

    for key in ["type", "extension", "mime"]:
        info[key] = [element for element in sorted(info[key], key=info[key].get, reverse=True)]

    return Info(info["type"], info["extension"], info["mime"])

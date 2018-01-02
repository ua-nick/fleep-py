#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
Description: File format determination library
Author: Mykyta Paliienko
License: MIT
"""


import os
import json


class ArgumentError(Exception):
    """ Exception is thrown when function argument is missed """
    pass


with open(os.path.join(os.path.dirname(__file__), "data.json")) as data_file:
    data = json.loads(data_file.read())["data"]


def get(**kwargs):
    """
    Does:
        Main function that determines file format

    Takes:
        input -> data to be processed: path to the file or array of bytes
        output (optional) -> format of output values: extension (by default) or MIME type

    Returns:
        List of output values
    """

    if "input" not in kwargs:
        raise ArgumentError("missing argument 'input'")

    input_data = kwargs["input"]
    output_type = kwargs["output"] if "output" in kwargs else "extension"

    if isinstance(input_data, bytes):
        stream = " ".join(['{:02X}'.format(byte) for byte in input_data])
    elif isinstance(input_data, str):
        with open(input_data, "rb") as file:
            stream = " ".join(['{:02X}'.format(byte) for byte in file.read(32)])
    else:
        raise ValueError("'input' argument type must be string or bytes")

    if output_type not in ["extension", "mime"]:
        raise ValueError("'output' argument value must be 'extension' or 'mime'")

    output_data = []

    for element in data:
        for signature in element["signature"]:
            offset = element["offset"] * 2 + element["offset"]
            if signature == stream[offset:len(signature) + offset]:
                if output_type == "extension":
                    output_data.append(element["extension"])
                elif output_type == "mime":
                    output_data.append(element["mime"])

    return list(set(output_data))

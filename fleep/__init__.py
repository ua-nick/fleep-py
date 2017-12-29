#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
Description: File format identification library
Author: Mykyta Paliienko
License: MIT
"""


import os
import json


class ArgumentError(Exception):
    pass


abspath = os.path.abspath(os.path.dirname(__file__))
data = json.loads(open(os.path.join(abspath, "data.json"), "r", encoding="utf-8").read())["data"]


def get(**kwargs):

    if "input" not in kwargs:
        raise ArgumentError("missing argument 'input'")
    if "output" not in kwargs:
        raise ArgumentError("missing argument 'output'")

    input_data = kwargs["input"]
    output_type = kwargs["output"]

    if type(input_data) == bytes:
        stream = " ".join(['{:02X}'.format(byte) for byte in input_data])
    elif type(input_data) == str:
        file = open(input_data, "rb").read(32)
        stream = " ".join(['{:02X}'.format(byte) for byte in file])
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

#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
Description: File format identification library
Author: Mykyta Paliienko
License: MIT
"""


import os
import json


abspath = os.path.abspath(os.path.dirname(__file__))
data = json.loads(open(os.path.join(abspath, "data.json"), "r", encoding="utf-8").read())["data"]


def get(path):

    file = open(path, "rb").read(32)
    hex_bytes = " ".join(['{:02X}'.format(byte) for byte in file])

    out = []

    for element in data:
        for signature in element["signature"]:
            offset = element["offset"]*2+element["offset"]
            if signature == hex_bytes[offset:len(signature)+offset].upper():
                out.append(element["format"])

    return out

# -*- coding: utf-8 -*-
"""
    flag.registry
    ~~~~~~~~~~~~~
"""

flags = []


def add(flag):
    flags.append(flag)


def iter():
    return flags

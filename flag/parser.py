# -*- coding: utf-8 -*-
"""
    flag.parser
    ~~~~~~~~~~~
"""
import argparse

from . import registry


def parse():
    parser = argparse.ArgumentParser()

    for flag in registry.iter():
        flag.add_to_parser(parser)

    args = vars(parser.parse_args())

    for flag in registry.iter():
        flag.update(args[flag.name])

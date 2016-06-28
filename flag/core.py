# -*- coding: utf-8 -*-
"""
    flag.core
    ~~~~~~~~~
"""
from .utils import text_type
from . import registry


class Flag(object):
    type = None

    def __init__(self, name, default=None, help=None, required=False):
        self.parsed = False
        self.name = name
        self.default = default
        self.help = help
        self.value = None
        self.required = required

    def val(self):
        if not self.parsed:
            raise Exception("Cannot read flag before parsing")

        if self.value is not None:
            return self.value
        else:
            return self.default

    def update(self, val):
        self.parsed = True
        self.value = val

    def add_to_parser(self, parser):
        name = "--" + self.name

        parser.add_argument(
            name, default=self.default, help=self.help,
            type=self.type, required=self.required)


class BaseMethods(object):
    def __getattr__(self, attr):
        val = self.type(self.val())
        if hasattr(val, attr):
            return getattr(val, attr)
        raise AttributeError(attr)

    def __hash__(self):
        return self.val().__hash__()


class ComparisonOperators(object):
    def __lt__(self, other):
        return self.type(self) < other

    def __le__(self, other):
        return self.type(self) <= other

    def __eq__(self, other):
        return self.type(self) == other

    def __ne__(self, other):
        return self.type(self) != other

    def __gt__(self, other):
        return self.type(self) > other

    def __ge__(self, other):
        return self.type(self) >= other


class ArithmeticOperators(object):
    def __add__(self, other):
        return self.type(self) + other

    def __radd__(self, other):
        return other + self.type(self)

    def __mul__(self, other):
        return self.type(self) * other

    def __rmul__(self, other):
        return other * self.type(self)


class IntFlag(Flag, ComparisonOperators, ArithmeticOperators, BaseMethods):
    """ IntFlag is a flag that tries to behave like an int"""
    type = int

    def __str__(self):
        return self.val().__str__()


class StringFlag(Flag, ComparisonOperators, ArithmeticOperators, BaseMethods):
    """ StringFlag is a flag that tries to behave like a string"""

    def __str__(self):
        return self.val()

    def __len__(self):
        return len(self.type(self))

    def __getitem__(self, key):
        return self.type(self)[key]

    def __iter__(self):
        return iter(self.type(self))

    def __contains__(self, item):
        return item in self.type(self)

    @property
    def type(self):
        return text_type


def int(name, *args, **kwargs):
    flag = IntFlag(name, *args, **kwargs)
    registry.add(flag)
    return flag


def string(name, *args, **kwargs):
    flag = StringFlag(name, *args, **kwargs)
    registry.add(flag)
    return flag

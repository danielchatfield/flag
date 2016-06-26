# -*- coding: utf-8 -*-
"""
    flag.core
    ~~~~~~~~~
"""
from .utils import text_type
from . import registry


class Flag(object):
    type = None

    def __init__(self, name, default, help):
        self.parsed = False
        self.name = name
        self.default = default
        self.help = help
        self.value = None
        self.required = False

    def val(self):
        if not self.parsed:
            raise Exception("Cannot read flag before parsing")

        if self.value:
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


class IntFlag(Flag, ComparisonOperators, ArithmeticOperators):
    """ IntFlag is a flag that tries to behave like an int"""
    type = int

    def __str__(self):
        return self.val().__str__()

    def __init__(self, *args, **kwargs):
        Flag.__init__(self, *args, **kwargs)

    def __getattr__(self, attr):
        """
        Forwards any non-magic methods to the resulting int's class.
        """
        val = self.type(self.val())
        if hasattr(val, attr):
            return getattr(val, attr)
        raise AttributeError(attr)


class StringFlag(Flag, ComparisonOperators, ArithmeticOperators):
    """ StringFlag is a flag that tries to behave like a string"""

    def __str__(self):
        return self.val()

    def __getattr__(self, attr):
        """
        Forwards any non-magic methods to the resulting string's class. This
        allows support for string methods like `upper()`, `lower()`, etc.
        """
        string = self.type(self)
        if hasattr(string, attr):
            return getattr(string, attr)
        raise AttributeError(attr)

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


def int(name, default, help):
    flag = IntFlag(name, default, help)
    registry.add(flag)
    return flag


def string(name, default, help):
    flag = StringFlag(name, default, help)
    registry.add(flag)
    return flag

# -*- coding: utf-8 -*-
"""
   valuedispatch
   ~~~~~~~~~~~~~

   :mod:`valuedispatch`-like API but dispatches value instead of type.

   :copyright: (c) 2015-2016 by What! Studio
   :license: BSD, see LICENSE for more details.
"""
from functools import update_wrapper

from collections import UserDict


class MappingProxyType(UserDict):
    def __init__(self, data):
        UserDict.__init__(self)
        self.data = data


def valuedispatch(func):
    registry = {}

    def dispatch(value):
        return registry.get(value, func)

    def register(value, func=None):
        if func is None:
            return lambda f: register(value, f)

        registry[value] = func
        return func

    def wrapper(*args, **kwargs):
        return dispatch(args[0])(*args, **kwargs)

    wrapper.register = register
    wrapper.dispatch = dispatch
    wrapper.registry = MappingProxyType(registry)
    update_wrapper(wrapper, func)
    return wrapper

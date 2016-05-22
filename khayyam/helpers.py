# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import sys
import warnings
__author__ = 'vahid'


def force_encoded_string_output(func):  # pragma: no cover
    if sys.version_info.major < 3:
        def _func(*args, **kwargs):
            return func(*args, **kwargs).encode('utf-8')
        return _func
    else:
        return func


def deprecated(func):  # pragma: no cover
    """This is a decorator which can be used to mark functions
    as deprecated. It will result in a warning being emitted
    when the function is used."""
    def new_func(*args, **kwargs):
        warnings.warn("Call to deprecated function %s." % func.__name__,
                      category=DeprecationWarning)
        return func(*args, **kwargs)
    new_func.__name__ = func.__name__
    new_func.__doc__ = func.__doc__
    new_func.__dict__.update(func.__dict__)
    return new_func



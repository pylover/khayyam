# -*- coding: utf-8 -*-
import re
from .compat import get_unicode
import warnings
__author__ = 'vahid'


def deprecated(func):
    """This is a decorator which can be used to mark functions
    as deprecated. It will result in a warning being emmitted
    when the function is used."""
    def new_func(*args, **kwargs):
        warnings.warn("Call to deprecated function %s." % func.__name__,
                      category=DeprecationWarning)
        return func(*args, **kwargs)
    new_func.__name__ = func.__name__
    new_func.__doc__ = func.__doc__
    new_func.__dict__.update(func.__dict__)
    return new_func


@deprecated
def replace_if_match(data, pattern, new):
    if re.search(pattern, data):
        if hasattr(new, '__call__'):
            new = new()
        return data.replace(pattern, get_unicode(new))
    return data
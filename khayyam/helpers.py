# -*- coding: utf-8 -*-

import re
from .compat import get_unicode

__author__ = 'vahid'


def replace_if_match(data, pattern, new):
    if re.search(pattern, data):
        if hasattr(new, '__call__'):
            new = new()
        return data.replace(pattern, get_unicode(new))
    return data
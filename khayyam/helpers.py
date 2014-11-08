# -*- coding: utf-8 -*-

import re

__author__ = 'vahid'


def replace_if_match(data, pattern, new):
    if re.search(pattern, data):
        if callable(new):
            new = new()
        if not isinstance(new, basestring):
            new = unicode(new)
        return data.replace(pattern, new)
    return data
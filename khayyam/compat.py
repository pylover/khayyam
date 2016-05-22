# -*- coding: utf-8 -*-
import sys
__author__ = 'vahid'
_py3 = sys.version_info.major == 3

if _py3:
    # noinspection PyUnresolvedReferences
    # noinspection PyCompatibility
    from builtins import range as xrange_compat
else:
    # noinspection PyUnboundLocalVariable
    xrange_compat = xrange


# noinspection PyShadowingBuiltins
xrange = xrange_compat


def get_unicode(s):
    if _py3:
        return str(s)
    else:
        # noinspection PyCompatibility
        return unicode(s)

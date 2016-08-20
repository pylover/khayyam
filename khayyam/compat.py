# -*- coding: utf-8 -*-
import sys
__author__ = 'vahid'
_py3 = sys.version_info.major == 3

if _py3:  # pragma: no cover
    # noinspection PyUnresolvedReferences
    # noinspection PyCompatibility
    from builtins import range as xrange_compat
else:  # pragma: no cover
    # noinspection PyUnboundLocalVariable
    xrange_compat = xrange


# noinspection PyShadowingBuiltins
xrange = xrange_compat


def get_unicode(s):
    if _py3:  # pragma: no cover
        return str(s)
    else:  # pragma: no cover
        # noinspection PyCompatibility
        return unicode(s)

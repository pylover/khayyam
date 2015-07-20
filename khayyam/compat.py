# -*- coding: utf-8 -*-
import sys
__author__ = 'vahid'
_py3 = sys.version_info.major == 3
if _py3:
    from builtins import range as xrange_compat
else:
    # noinspection PyUnboundLocalVariable
    xrange_compat = xrange

xrange = xrange_compat

def get_unicode(s):
    if _py3:
        return str(s)
    else:
        return unicode(s)

# def xrange(*args, **kw):
#     return xrange_compat(*args, **kw)


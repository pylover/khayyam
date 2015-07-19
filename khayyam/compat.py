# -*- coding: utf-8 -*-
import sys
__author__ = 'vahid'


if sys.version_info.major == 3:

    def get_unicode(s):
        return str(s)

    xrange = range

elif sys.version_info.major == 2:

    def get_unicode(s):
        return unicode(s)

    xrange = xrange

else:
    raise Exception('invalid interpreter: %s' % str(sys.version_info))

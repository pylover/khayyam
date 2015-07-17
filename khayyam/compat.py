# -*- coding: utf-8 -*-
__author__ = 'vahid'

import sys

if sys.version_info.major == 3:

    def get_unicode(s):
        return str(s)

elif sys.version_info.major == 2:

    def get_unicode(s):
        return unicode(s)


else:
    raise Exception('invalid interpreter: %s' % sys.version_info)

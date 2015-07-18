# -*- coding: utf-8 -*-
from .directive import Directive
import khayyam.constants as consts
from khayyam.compat import get_unicode
__author__ = 'vahid'

class AmPmDirective(Directive):
    def __init__(self):
        super(AmPmDirective, self).__init__(
            'p',
            'ampm',
            consts.AM_PM_REGEX,
            get_unicode)

    def format(self, d):
        return '%s' % d.ampm()

    def post_parser(self, ctx, formatter):
        hour12 = ctx['hour12']
        if hour12 < 12:
            ctx['hour'] = hour12 + (12 if ctx['ampm'] == consts.AM_PM[1] else 0)
        else:
            ctx['hour'] = hour12


class AmPmASCIIDirective(Directive):
    def __init__(self):
        super(AmPmASCIIDirective, self).__init__(
            't',
            'ampm_ascii',
            consts.AM_PM_ASCII_REGEX,
            get_unicode)

    def format(self, d):
        return '%s' % d.ampmascii()

    def post_parser(self, ctx, formatter):
        hour12 = ctx['hour12']
        if hour12 < 12:
            ctx['hour'] = hour12 + (12 if ctx['ampm_ascii'] == consts.AM_PM_ASCII[1] else 0)
        else:
            ctx['hour'] = hour12


# -*- coding: utf-8 -*-
from .directive import Directive
from khayyam.formatting import constants as consts
from khayyam.compat import get_unicode
__author__ = 'vahid'


class BaseAmPmDirective(Directive):
    def __init__(self, key, name, regex):
        super(BaseAmPmDirective, self).__init__(key, name, regex, get_unicode)

    def format(self, d):
        return getattr(d, self.name)()

    def is_am(self, ctx):
        raise NotImplementedError()

    def post_parser(self, ctx, formatter):
        hour12 = ctx['hour12']

        if self.is_am(ctx): # AM
            hour = 0 if hour12 == 12 else hour12
        else: # PM
            hour = hour12 + (12 if hour12 < 12 else 0)

        ctx['hour'] = hour


class AmPmDirective(BaseAmPmDirective):

    def is_am(self, ctx):
        return ctx['ampm'] == consts.AM_PM[0]


class AmPmASCIIDirective(BaseAmPmDirective):

    def is_am(self, ctx):
        return ctx[self.name] == consts.AM_PM_ASCII[0]


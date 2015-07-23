# -*- coding: utf-8 -*-
from .persian import PersianNumberDirective
from khayyam.formatting import constants as consts
__author__ = 'vahid'

class PersianDayDirective(PersianNumberDirective):
    def __init__(self, key='D', name='persianday', regex=consts.PERSIAN_DAY_REGEX, zero_padding=False):
        self.zero_padding = zero_padding
        super(PersianDayDirective, self).__init__(key, name, regex)

    def format(self, d):
        fmt = '%%%sd' % ('.2' if self.zero_padding else '')
        return super(PersianDayDirective, self).format(fmt % d.day)

    def post_parser(self, ctx, formatter):
        super(PersianDayDirective, self).post_parser(ctx, formatter)
        if self.name in ctx and ctx[self.name]:
            ctx['day'] = ctx[self.name]

# -*- coding: utf-8 -*-
from .persian import PersianNumberDirective
from khayyam.formatting import constants as consts
__author__ = 'vahid'

class PersianMonthDirective(PersianNumberDirective):
    def __init__(self, key='R', name='persianmonth', regex=consts.PERSIAN_MONTH_REGEX, zero_padding=False):
        self.zero_padding = zero_padding
        super(PersianMonthDirective, self).__init__(key, name, regex)

    def format(self, d):
        fmt = '%%%sd' % ('.2' if self.zero_padding else '')
        return super(PersianMonthDirective, self).format(fmt % d.month)

    def post_parser(self, ctx, formatter):
        super(PersianMonthDirective, self).post_parser(ctx, formatter)
        if self.name in ctx and ctx[self.name]:
            ctx['month'] = ctx[self.name]

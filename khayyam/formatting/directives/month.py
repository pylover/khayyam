# -*- coding: utf-8 -*-
from .persian import PersianNumberDirective
from khayyam.formatting import constants as consts
__author__ = 'vahid'

class PersianMonthDirective(PersianNumberDirective):
    def __init__(self):
        super(PersianMonthDirective, self).__init__(
            'R', 'persianmonth', consts.PERSIAN_MONTH_REGEX)

    def format(self, d):
        return super(PersianMonthDirective, self).format('%.2d' % d.month)

    def post_parser(self, ctx, formatter):
        super(PersianMonthDirective, self).post_parser(ctx, formatter)
        if self.name in ctx and ctx[self.name]:
            ctx['month'] = ctx[self.name]

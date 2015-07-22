# -*- coding: utf-8 -*-
from .persian import PersianNumberDirective
from khayyam.formatting import constants as consts
__author__ = 'vahid'

class PersianDayDirective(PersianNumberDirective):
    def __init__(self):
        super(PersianDayDirective, self).__init__(
            'D', 'persianday', consts.PERSIAN_DAY_REGEX)

    def format(self, d):
        return super(PersianDayDirective, self).format('%.2d' % d.day)

    def post_parser(self, ctx, formatter):
        super(PersianDayDirective, self).post_parser(ctx, formatter)
        if self.name in ctx and ctx[self.name]:
            ctx['day'] = ctx[self.name]

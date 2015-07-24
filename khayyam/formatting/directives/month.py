# -*- coding: utf-8 -*-
from .persian import PersianNumberDirective
__author__ = 'vahid'


class PersianMonthDirective(PersianNumberDirective):

    def format(self, d):
        return super(PersianMonthDirective, self).format(d.month)

    def post_parser(self, ctx, formatter):
        super(PersianMonthDirective, self).post_parser(ctx, formatter)
        if self.name in ctx and ctx[self.name]:
            ctx['month'] = ctx[self.name]

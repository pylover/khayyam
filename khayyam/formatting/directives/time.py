# -*- coding: utf-8 -*-
from .persian import PersianNumberDirective
__author__ = 'vahid'


class PersianHour24Directive(PersianNumberDirective):

    def format(self, d):
        return super(PersianHour24Directive, self).format(d.hour)

    def post_parser(self, ctx, formatter):
        super(PersianHour24Directive, self).post_parser(ctx, formatter)
        if self.name in ctx and ctx[self.name]:
            ctx['hour'] = ctx[self.name]


class PersianHour12Directive(PersianNumberDirective):

    def format(self, d):
        return super(PersianHour12Directive, self).format(d.hour12())

    def post_parser(self, ctx, formatter):
        super(PersianHour12Directive, self).post_parser(ctx, formatter)
        if self.name in ctx and ctx[self.name]:
            ctx['hour12'] = ctx[self.name]


class PersianMinuteDirective(PersianNumberDirective):

    def format(self, d):
        return super(PersianMinuteDirective, self).format(d.minute)

    def post_parser(self, ctx, formatter):
        super(PersianMinuteDirective, self).post_parser(ctx, formatter)
        if self.name in ctx and ctx[self.name]:
            ctx['minute'] = ctx[self.name]


class PersianSecondDirective(PersianNumberDirective):

    def format(self, d):
        return super(PersianSecondDirective, self).format(d.second)

    def post_parser(self, ctx, formatter):
        super(PersianSecondDirective, self).post_parser(ctx, formatter)
        if self.name in ctx and ctx[self.name]:
            ctx['second'] = ctx[self.name]


class PersianMicrosecondDirective(PersianNumberDirective):

    def format(self, d):
        return super(PersianMicrosecondDirective, self).format('%.6d' % d.microsecond)

    def post_parser(self, ctx, formatter):
        super(PersianMicrosecondDirective, self).post_parser(ctx, formatter)
        if self.name in ctx and ctx[self.name]:
            ctx['microsecond'] = ctx[self.name]


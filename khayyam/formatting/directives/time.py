# -*- coding: utf-8 -*-
from .persian import PersianNumberDirective
from khayyam.formatting import constants as consts
__author__ = 'vahid'

class PersianMicrosecondDirective(PersianNumberDirective):
    def __init__(self):
        super(PersianMicrosecondDirective, self).__init__(
            'F', 'persianmicrosecond', consts.PERSIAN_MICROSECOND_REGEX)

    def format(self, d):
        return super(PersianMicrosecondDirective, self).format('%.6d' % d.microsecond)

    def post_parser(self, ctx, formatter):
        super(PersianMicrosecondDirective, self).post_parser(ctx, formatter)
        if self.name in ctx and ctx[self.name]:
            ctx['microsecond'] = ctx[self.name]


class PersianHour24Directive(PersianNumberDirective):
    def __init__(self):
        super(PersianHour24Directive, self).__init__(
            'h', 'persianhour24', consts.PERSIAN_HOUR24_REGEX)

    def format(self, d):
        return super(PersianHour24Directive, self).format('%.2d' % d.hour)

    def post_parser(self, ctx, formatter):
        super(PersianHour24Directive, self).post_parser(ctx, formatter)
        if self.name in ctx and ctx[self.name]:
            ctx['hour'] = ctx[self.name]


class PersianHour12Directive(PersianNumberDirective):
    def __init__(self):
        super(PersianHour12Directive, self).__init__(
            'i', 'persianhour12', consts.PERSIAN_HOUR12_REGEX)

    def format(self, d):
        return super(PersianHour12Directive, self).format('%.2d' % d.hour12())

    def post_parser(self, ctx, formatter):
        super(PersianHour12Directive, self).post_parser(ctx, formatter)
        if self.name in ctx and ctx[self.name]:
            ctx['hour12'] = ctx[self.name]


class PersianMinuteDirective(PersianNumberDirective):
    def __init__(self):
        super(PersianMinuteDirective, self).__init__(
            'r', 'persianminute', consts.PERSIAN_MINUTE_REGEX)

    def format(self, d):
        return super(PersianMinuteDirective, self).format('%.2d' % d.minute)

    def post_parser(self, ctx, formatter):
        super(PersianMinuteDirective, self).post_parser(ctx, formatter)
        if self.name in ctx and ctx[self.name]:
            ctx['minute'] = ctx[self.name]


class PersianSecondDirective(PersianNumberDirective):
    def __init__(self):
        super(PersianSecondDirective, self).__init__(
            's', 'persiansecond', consts.PERSIAN_SECOND_REGEX)

    def format(self, d):
        return super(PersianSecondDirective, self).format('%.2d' % d.second)

    def post_parser(self, ctx, formatter):
        super(PersianSecondDirective, self).post_parser(ctx, formatter)
        if self.name in ctx and ctx[self.name]:
            ctx['second'] = ctx[self.name]
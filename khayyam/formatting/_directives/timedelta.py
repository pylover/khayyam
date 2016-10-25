# -*- coding: utf-8 -*-
from .base import Directive
from .persian import PersianNumberDirective
from khayyam.formatting import constants as consts


class TotalHoursDirective(Directive):
    """
    Representing total hours in a timedelta.
    """

    def __init__(self, key, name):
        super(TotalHoursDirective, self).__init__(key, name, consts.UNLIMITED_INT_REGEX, int)

    def format(self, d):
        return str(int(d.total_hours))

    def post_parser(self, ctx, formatter):
        super(TotalHoursDirective, self).post_parser(ctx, formatter)
        if self.name in ctx and ctx[self.name]:
            ctx['hours'] = ctx[self.name]


class PersianTotalHoursDirective(PersianNumberDirective):
    """
    Representing total hours in persian form.
    """

    def __init__(self, key, name):
        super(PersianTotalHoursDirective, self).__init__(key, name, consts.PERSIAN_UNLIMITED_INT_REGEX, int)

    def format(self, d):
        return super(PersianTotalHoursDirective, self).format(int(d.total_hours))

    def post_parser(self, ctx, formatter):
        super(PersianTotalHoursDirective, self).post_parser(ctx, formatter)
        if self.name in ctx and ctx[self.name]:
            ctx['hours'] = ctx[self.name]


class PersianHoursDirective(PersianNumberDirective):
    """
    Representing Hour24 format in persian form.
    """

    def __init__(self, key, name):
        super(PersianHoursDirective, self).__init__(key, name, consts.PERSIAN_HOUR24_ZERO_PADDED_REGEX, int)

    def format(self, d):
        return super(PersianHoursDirective, self).format(int(d.hours))

    def post_parser(self, ctx, formatter):
        super(PersianHoursDirective, self).post_parser(ctx, formatter)
        if self.name in ctx and ctx[self.name]:
            ctx['hours'] = ctx[self.name]


class TotalMinutesDirective(Directive):
    """
    Representing total minutes in a timedelta.
    """

    def format(self, d):
        return super(TotalMinutesDirective, self).format(d.total_minutes)

    def post_parser(self, ctx, formatter):
        super(TotalMinutesDirective, self).post_parser(ctx, formatter)
        if self.name in ctx and ctx[self.name]:
            ctx['minutes'] = ctx[self.name]

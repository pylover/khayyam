# -*- coding: utf-8 -*-
from .directive import Directive
from khayyam.formatting import constants as consts
from khayyam.algorithms import days_in_year
from datetime import timedelta
from .persian import PersianNumberDirective
__author__ = 'vahid'


class ShortYearDirective(Directive):
    def __init__(self):
        super(ShortYearDirective, self).__init__(
            'y', 'shortyear', consts.SHORT_YEAR_REGEX, int)

    def format(self, d):
        return '%.2d' % (d.year % 100)

    def post_parser(self, ctx, formatter):
        from khayyam import JalaliDate
        ctx['year'] = int(JalaliDate.today().year / 100) * 100 + ctx['shortyear']


class DayOfYearDirective(Directive):
    def __init__(self):
        super(DayOfYearDirective, self).__init__(
            'j', 'dayofyear', consts.DAY_OF_YEAR_REGEX, int)

    def format(self, d):
        return '%.3d' % d.dayofyear()

    def post_parser(self, ctx, formatter):
        _dayofyear = ctx['dayofyear']
        if 'year' not in ctx:
            ctx['year'] = 1
        if 'month' in ctx:
            del ctx['month']
        if 'day' in ctx:
            del ctx['day']

        max_days = days_in_year(ctx['year'])
        if _dayofyear > max_days:
            raise ValueError(
                'Invalid dayofyear: %.3d for year %.4d. Valid values are: 1-%s' \
                 % (_dayofyear, ctx['year'], max_days))
        from khayyam import JalaliDate
        d = JalaliDate(year=ctx['year']) + timedelta(days=_dayofyear-1)
        ctx.update(dict(
            month=d.month,
            day=d.day
        ))


class PersianDayOfYearDirective(PersianNumberDirective):

    def __init__(self, key='J', name='persiandayofyear',
                 regex=consts.PERSIAN_DAY_OF_YEAR_REGEX, zero_padding=False):
        self.zero_padding = zero_padding
        super(PersianDayOfYearDirective, self).__init__(key, name, regex)

    def format(self, d):
        fmt = '%%%sd' % ('.3' if self.zero_padding else '')
        return super(PersianDayOfYearDirective, self).format(fmt % d.dayofyear())

    def post_parser(self, ctx, formatter):
        super(PersianDayOfYearDirective, self).post_parser(ctx, formatter)
        if self.name in ctx and ctx[self.name]:
            ctx['dayofyear'] = ctx[self.name]



class PersianYearDirective(PersianNumberDirective):
    def __init__(self, key='N', name='persianyear', regex=consts.PERSIAN_YEAR_REGEX, zero_padding=False):
        self.zero_padding = zero_padding
        super(PersianYearDirective, self).__init__(key, name, regex)

    def format(self, d):
        fmt = '%%%sd' % ('.4' if self.zero_padding else '')
        return super(PersianYearDirective, self).format(fmt % d.year)

    def post_parser(self, ctx, formatter):
        super(PersianYearDirective, self).post_parser(ctx, formatter)
        if self.name in ctx and ctx[self.name]:
            ctx['year'] = ctx[self.name]


class PersianShortYearDirective(PersianNumberDirective):
    def __init__(self, key='n', name='persianshortyear',
                 regex=consts.PERSIAN_SHORT_YEAR_REGEX, zero_padding=False):
        self.zero_padding = zero_padding
        super(PersianShortYearDirective, self).__init__(key, name, regex)

    def format(self, d):
        fmt = '%%%sd' % ('.2' if self.zero_padding else '')
        return super(PersianShortYearDirective, self).format(fmt % (d.year % 100))

    def post_parser(self, ctx, formatter):
        super(PersianShortYearDirective, self).post_parser(ctx, formatter)
        if self.name in ctx and ctx[self.name]:
            ctx['shortyear'] = ctx[self.name]

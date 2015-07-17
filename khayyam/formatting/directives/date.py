# -*- coding: utf-8 -*-
import re
from .directive import Directive
from datetime import timedelta
import khayyam.constants as consts
from khayyam.compat import get_unicode
from khayyam.algorithms import days_in_year
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
        # TODO: Add this behavior to the documents
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


class LocalFormatDirective(Directive):
    def __init__(self):
        super(LocalFormatDirective, self).__init__(
            'x', 'localformat', consts.LOCAL_FORMAT_REGEX, get_unicode)

    def format(self, d):
        return d.localformat()

    def post_parser(self, ctx, formatter):
        # TODO: Add this behavior to the documents
        regex = ' '.join([
            '(?P<weekdayname>%s)' % consts.PERSIAN_WEEKDAY_NAMES_REGEX,
            '(?P<day>%s)' % consts.DAY_REGEX,
            '(?P<monthname>%s)' % consts.PERSIAN_MONTH_NAMES_REGEX,
            '(?P<year>%s)' % consts.YEAR_REGEX
        ])

        match = re.match(regex, ctx['localformat'])
        d = match.groupdict()
        ctx.update(dict(
            weekdayname = formatter.directives_by_key['A'].type_(d['weekdayname']),
            day = formatter.directives_by_key['d'].type_(d['day']),
            monthname = formatter.directives_by_key['B'].type_(d['monthname']),
            year = formatter.directives_by_key['Y'].type_(d['year'])
        ))

# TODO: _first_day_of_week = SATURDAY
DATE_FORMAT_DIRECTIVES = [
    ShortYearDirective(),
    DayOfYearDirective(),
    LocalFormatDirective(),
    Directive(
        'Y',
        'year',
        consts.YEAR_REGEX,
        int,
        lambda d: '%.4d' % d.year,
    ),
    Directive(
        'm',
        'month',
        consts.MONTH_REGEX,
        int,
        lambda d: '%.2d' % d.month,
    ),
    Directive(
        'b',
        'monthabbr',
        consts.PERSIAN_MONTH_ABBRS_REGEX,
        get_unicode,
        lambda d: d.monthabbr(),
        lambda ctx, f: ctx.update({'month': [(k, v) for k, v in consts.PERSIAN_MONTH_ABBRS.items() if v == ctx['monthabbr']][0][0]})
    ),
    Directive(
        'B',
        'monthname',
        consts.PERSIAN_MONTH_NAMES_REGEX,
        get_unicode,
        lambda d: d.monthname(),
        lambda ctx, f: ctx.update({'month': [(k, v) for k, v in consts.PERSIAN_MONTH_NAMES.items() if v == ctx['monthname']][0][0]})
    ),
    Directive(
        'g',
        'monthabbr_ascii',
        consts.PERSIAN_MONTH_ABBRS_ASCII_REGEX,
        get_unicode,
        lambda d: d.monthabbr_ascii(),
        lambda ctx, f: ctx.update({'month': [(k, v) for k, v in consts.PERSIAN_MONTH_ABBRS_ASCII.items() if v == ctx['monthabbr_ascii']][0][0]})
    ),
    Directive(
        'G',
        'monthname_ascii',
        consts.PERSIAN_MONTH_NAMES_ASCII_REGEX,
        get_unicode,
        lambda d: d.monthname_ascii(),
        lambda ctx, f: ctx.update({'month': [(k, v) for k, v in consts.PERSIAN_MONTH_NAMES_ASCII.items() if v == ctx['monthname_ascii']][0][0]})
    ),
    Directive(
        'w',
        'weekday',
        consts.WEEKDAY_REGEX,
        int,
        lambda d: '%d' % d.weekday(),
    ),
    Directive(
        'W',
        'weekofyear',
        consts.WEEK_OF_YEAR_REGEX,
        int,
        lambda d: '%.2d' % d.weekofyear(consts.SATURDAY),
    ),
    Directive(
        'U',
        'weekofyear',
        consts.WEEK_OF_YEAR_REGEX,
        int,
        lambda d: '%.2d' % d.weekofyear(consts.MONDAY),
    ),
    Directive(
        'a',
        'weekdayabbr',
        consts.PERSIAN_WEEKDAY_ABBRS_REGEX,
        get_unicode,
        lambda d: d.weekdayabbr(),
    ),
    Directive(
        'A',
        'weekdayname',
        consts.PERSIAN_WEEKDAY_NAMES_REGEX,
        get_unicode,
        lambda d: d.weekdayname(),
    ),
    Directive(
        'e',
        'weekdayabbr_ascii',
        consts.PERSIAN_WEEKDAY_ABBRS_ASCII_REGEX,
        get_unicode,
        lambda d: d.weekdayabbr_ascii(),
    ),
    Directive(
        'E',
        'weekdayname_ascii',
        consts.PERSIAN_WEEKDAY_NAMES_ASCII_REGEX,
        get_unicode,
        lambda d: d.weekdayname_ascii(),
    ),
    Directive(
        'd',
        'day',
        consts.DAY_REGEX,
        int,
        lambda d: '%.2d' % d.day,
    ),
    # Directive(
    #     'x',
    #     'localformat',
    #     consts.LOCAL_FORMAT_REGEX,
    #     get_unicode,
    #     lambda d: d.localformat(),
    # ),
    Directive(
        '%',
        'percent',
        '%',
        None,
        lambda d: '%',
    ),
]
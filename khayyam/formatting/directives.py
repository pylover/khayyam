# -*- coding: utf-8 -*-
from khayyam.compat import get_unicode
import khayyam.constants as consts
__author__ = 'vahid'

class Directive(object):
    def __init__(self, key, name, regex, formatter, type_, post_parser=None):
        self.key = key
        self.name = name
        self.regex = regex
        self.type_ = type_
        self.formatter = formatter
        if post_parser:
            self.post_parser = post_parser

    def __repr__(self):
        return '%' + self.key

    def post_parser(self, ctx):
        return ctx


# TODO: _first_day_of_week = SATURDAY
DATE_FORMAT_DIRECTIVES = [
    Directive(
        'Y',
        'year',
        consts.YEAR_REGEX,
        lambda d: '%.4d' % d.year,
        int
    ),
    Directive(
        'y',
        'shortyear',
        consts.SHORT_YEAR_REGEX,
        lambda d: '%.2d' % (d.year % 100),
        int
    ),
    Directive(
        'm',
        'month',
        consts.MONTH_REGEX,
        lambda d: '%.2d' % d.month,
        int
    ),
    Directive(
        'b',
        'monthabbr',
        consts.PERSIAN_MONTH_ABBRS_REGEX,
        lambda d: d.monthabbr(),
        get_unicode,
        lambda ctx: {'month': [(k, v) for k, v in consts.PERSIAN_MONTH_ABBRS.items() if v == ctx['monthabbr']][0][0]}
    ),
    Directive(
        'B',
        'monthname',
        consts.PERSIAN_MONTH_NAMES_REGEX,
        lambda d: d.monthname(),
        get_unicode
    ),
    Directive(
        'g',
        'monthabbr_ascii',
        consts.PERSIAN_MONTH_ABBRS_ASCII_REGEX,
        lambda d: d.monthabbr_ascii(),
        get_unicode),
    Directive(
        'G',
        'monthname_ascii',
        consts.PERSIAN_MONTH_NAMES_ASCII_REGEX,
        lambda d: d.monthname_ascii(),
        get_unicode),
    Directive(
        'w',
        'weekday',
        consts.WEEKDAY_REGEX,
        lambda d: '%d' % d.weekday(),
        int
    ),
    Directive(
        'W',
        'weekofyear',
        consts.WEEK_OF_YEAR_REGEX,
        lambda d: '%.2d' % d.weekofyear(consts.SATURDAY),
        int
    ),
    Directive(
        'a',
        'weekdayabbr',
        consts.PERSIAN_WEEKDAY_ABBRS_REGEX,
        lambda d: d.weekdayabbr(),
        get_unicode
    ),
    Directive(
        'A',
        'weekdayname',
        consts.PERSIAN_WEEKDAY_NAMES_REGEX,
        lambda d: d.weekdayname(),
        get_unicode
    ),
    Directive(
        'e',
        'weekdayabbr_ascii',
        consts.PERSIAN_WEEKDAY_ABBRS_ASCII_REGEX,
        lambda d: d.weekdayabbr_ascii(),
        get_unicode
    ),
    Directive(
        'E',
        'weekdayname_ascii',
        consts.PERSIAN_WEEKDAY_NAMES_ASCII_REGEX,
        lambda d: d.weekdayname_ascii(),
        get_unicode
    ),
    Directive(
        'd',
        'day',
        consts.DAY_REGEX,
        lambda d: '%.2d' % d.day,
        int
    ),
    Directive(
        'j',
        'dayofyear',
        consts.DAY_OF_YEAR_REGEX,
        lambda d: '%.3d' % d.dayofyear(),
        int
    ),
    Directive(
        'x',
        'localformat',
        consts.LOCAL_FORMAT_REGEX,
        lambda d: d.localformat(),
        get_unicode),
    Directive(
        '%',
        'percent',
        '%',
        lambda d: '%',
        None
    ),
    # --------SUPPORTED--------
]
# -*- coding: utf-8 -*-
import re

import khayyam
from khayyam.compat import get_unicode
from khayyam.constants import SATURDAY, MONDAY
from khayyam.formatting import constants as consts
from khayyam.formatting.directives import Directive, DayOfYearDirective, persian, latin_digit, \
    PersianDayOfYearDirective, CompositeDirective, Hour12Directive, UTCOffsetDirective, PersianUTCOffsetDirective, \
    TimezoneNameDirective


__author__ = 'vahid'


class Formattable(object):
    pass


class BaseFormatter(object):
    _directives = [
        Directive('%', '%', formatter=lambda d: '%'),
    ]

    def __init__(self):
        self._directives_by_key = {}
        self._post_parsers = []
        for d in self._directives:
            self._directives_by_key[d.key] = d
            if d.require_post_parsing:
                self._post_parsers.append(d)

    def _create_parser_regex(self, format_string):
        regex = u'^'
        index = 0
        for m in re.finditer(consts.FORMAT_DIRECTIVE_REGEX, format_string):
            directive_key = m.group()[1:]
            if directive_key not in self._directives_by_key:
                continue
            directive = self._directives_by_key[directive_key]
            if index < m.start():
                regex += format_string[index:m.start()]
            index = m.end()
            if directive.key == u'%':
                regex += u'%'
                continue
            regex += u'(?P<%(group_name)s>%(regexp)s)' % dict(
                group_name=directive.key,
                regexp=directive.regex
            )
        regex += format_string[index:]
        regex += u'$'
        return regex

    def iter_format_directives(self, format_string):
        for m in re.finditer(consts.FORMAT_DIRECTIVE_REGEX, format_string):
            key = m.group()[1:]
            if key in self._directives_by_key:
                yield m, self._directives_by_key[key]

    def format(self, format_string, formattable):
        assert isinstance(formattable, Formattable)
        result = ''
        index = 0
        for match, directive in self.iter_format_directives(format_string):
            if index < match.start():
                result += format_string[index:match.start()]
            result += directive.format(formattable)
            index = match.end()
        result += format_string[index:]
        return result

    @staticmethod
    def filter_persian_digit(s):
        # FIXME: Rename it to normalize_digits
        # FIXME: A better algorithm is needed.
        for p, e in consts.PERSIAN_DIGIT_MAPPING:
            s = s.replace(p[1], p[0])
        return s

    def _parse(self, format_string, date_string):
        parser_regex = self._create_parser_regex(format_string)

        m = re.match(parser_regex, self.filter_persian_digit(date_string))
        if not m:
            raise ValueError(u"time data '%s' does not match format '%s' with generated regex: '%s'" % (
                date_string, format_string, parser_regex))
        result = {}
        for directive_key, v in m.groupdict().items():
            directive = self._directives_by_key[directive_key]
            if hasattr(directive, 'pre_parser'):
                v = directive.pre_parser(v)
            directive.parse(result, v)
        return result

    def _parse_post_processor(self, parse_result):
        for directive in self._post_parsers:
            if directive.target_name in parse_result.keys():
                directive.post_parser(parse_result, self)

    def parse(self, format_string, date_string):
        result = self._parse(format_string, date_string)
        self._parse_post_processor(result)
        return result


class JalaliDateFormatter(BaseFormatter):
    """
    Responsible to parse and formatting of a :py:class:`khayyam.JalaliDate` instance.

    """

    _directives = BaseFormatter._directives + [

        # YEAR

        Directive(
            'Y',
            consts.YEAR_REGEX,
            name='year',
            type_=int,
            formatter=lambda d: '%.4d' % d.year
        ),
        Directive(
            'y',
            consts.SHORT_YEAR_REGEX,
            type_=int,
            formatter=lambda d: '%.2d' % (d.year % 100),
            post_parser=lambda ctx, f: ctx.update(year=int(khayyam.JalaliDate.today().year / 100) * 100 + ctx['y'])
        ),
        Directive(
            'n',
            consts.PERSIAN_SHORT_YEAR_REGEX,
            type_=int,
            formatter=lambda d: persian('%d' % (d.year % 100)),
            post_parser=lambda ctx, f: ctx.update(year=int(khayyam.JalaliDate.today().year / 100) * 100 + ctx['n'])
        ),
        Directive(
            'u',
            consts.PERSIAN_SHORT_YEAR_ZERO_PADDED_REGEX,
            type_=int,
            formatter=lambda d: persian('%.2d' % (d.year % 100)),
            post_parser=lambda ctx, f: ctx.update(year=int(khayyam.JalaliDate.today().year / 100) * 100 + ctx['u'])
        ),
        Directive(
            'N',
            consts.PERSIAN_YEAR_REGEX,
            name='year',
            type_=int,
            formatter=lambda d: persian('%d' % d.year),
        ),
        Directive(
            'O',
            consts.PERSIAN_YEAR_ZERO_PADDED_REGEX,
            name='year',
            type_=int,
            formatter=lambda d: persian('%.4d' % d.year),
        ),

        # MONTH
        Directive(
            'm',
            consts.MONTH_REGEX,
            name='month',
            type_=int,
            formatter=lambda d: '%.2d' % d.month,
        ),
        Directive(
            'R',
            consts.PERSIAN_MONTH_REGEX,
            name='month',
            type_=int,
            formatter=lambda d: persian(d.month),
        ),
        Directive(
            'P',
            consts.PERSIAN_MONTH_ZERO_PADDED_REGEX,
            name='month',
            type_=int,
            formatter=lambda d: persian('%.2d' % d.month),
        ),
        Directive(
            'b',
            consts.PERSIAN_MONTH_ABBRS_REGEX,
            type_=get_unicode,
            formatter=lambda d: d.monthabbr(),
            post_parser=lambda ctx, f: ctx.update(
                month=next(k for k, v in consts.PERSIAN_MONTH_ABBRS.items() if v == ctx['b'])
            )
        ),
        Directive(
            'B',
            consts.PERSIAN_MONTH_NAMES_REGEX,
            type_=get_unicode,
            formatter=lambda d: d.monthname(),
            post_parser=lambda ctx, f: ctx.update(
                month=next(k for k, v in consts.PERSIAN_MONTH_NAMES.items() if v == ctx['B'])
            )
        ),
        Directive(
            'g',
            consts.PERSIAN_MONTH_ABBRS_ASCII_REGEX,
            type_=get_unicode,
            formatter=lambda d: d.monthabbr_ascii(),
            post_parser=lambda ctx, f: ctx.update(
                month=next(k for k, v in consts.PERSIAN_MONTH_ABBRS_ASCII.items() if v == ctx['g'])
            )
        ),
        Directive(
            'G',
            consts.PERSIAN_MONTH_NAMES_ASCII_REGEX,
            type_=get_unicode,
            formatter=lambda d: d.monthnameascii(),
            post_parser=lambda ctx, f: ctx.update(
                month=next(k for k, v in consts.PERSIAN_MONTH_NAMES_ASCII.items() if v == ctx['G'])
            )
        ),

        # WEEK
        Directive(
            'a',
            consts.PERSIAN_WEEKDAY_ABBRS_REGEX,
            type_=get_unicode,
            formatter=lambda d: d.weekdayabbr()
        ),
        Directive(
            'A',
            consts.PERSIAN_WEEKDAY_NAMES_REGEX,
            type_=get_unicode,
            formatter=lambda d: d.weekdayname()
        ),
        Directive(
            'e',
            consts.PERSIAN_WEEKDAY_ABBRS_ASCII_REGEX,
            type_=get_unicode,
            formatter=lambda d: d.weekdayabbrascii(),
        ),
        Directive(
            'E',
            consts.PERSIAN_WEEKDAY_NAMES_ASCII_REGEX,
            type_=get_unicode,
            formatter=lambda d: d.weekdaynameascii(),
        ),
        Directive(
            'T',
            consts.ENGLISH_WEEKDAY_NAMES_ASCII_REGEX,
            type_=get_unicode,
            formatter=lambda d: d.englishweekdaynameascii(),
        ),
        Directive(
            'w',
            consts.WEEKDAY_REGEX,
            type_=int,
            formatter=lambda d: '%d' % d.weekday(),
        ),
        Directive(
            'W',
            consts.WEEK_OF_YEAR_REGEX,
            type_=int,
            formatter=lambda d: '%.2d' % d.weekofyear(SATURDAY),
        ),
        Directive(
            'U',
            consts.WEEK_OF_YEAR_REGEX,
            type_=int,
            formatter=lambda d: '%.2d' % d.weekofyear(MONDAY),
        ),

        # DAY
        Directive(
            'd',
            consts.DAY_REGEX,
            name='day',
            type_=int,
            formatter=lambda d: '%.2d' % d.day
        ),
        Directive(
            'D',
            consts.PERSIAN_DAY_REGEX,
            name='day',
            type_=int,
            formatter=lambda d: persian(d.day),
        ),
        Directive(
            'K',
            consts.PERSIAN_DAY_ZERO_PADDED_REGEX,
            name='day',
            type_=int,
            formatter=lambda d: persian('%.2d' % d.day),
        ),
        DayOfYearDirective('j'),
        PersianDayOfYearDirective('J'),
        PersianDayOfYearDirective('V', regex=consts.PERSIAN_DAY_OF_YEAR_ZERO_PADDED_REGEX, zero_padded=True),

        # COMPOSITE
        CompositeDirective(
            'x',
            ' '.join((
                consts.PERSIAN_WEEKDAY_NAMES_REGEX,
                consts.PERSIAN_DAY_REGEX,
                consts.PERSIAN_MONTH_NAMES_REGEX,
                consts.PERSIAN_YEAR_REGEX)),
            "%A %D %B %N"
        ),
    ]


class JalaliDatetimeFormatter(JalaliDateFormatter):
    """
    Responsible to parse and formatting of a :py:class:`khayyam.JalaliDatetime` instance.

    """
    _directives = JalaliDateFormatter._directives + [

        # AM/PM
        Directive(
            't',
            consts.AM_PM_ASCII_REGEX,
            formatter=lambda d: d.ampmascii(),
        ),
        Directive(
            'p',
            consts.AM_PM_REGEX,
            formatter=lambda d: d.ampm(),
        ),

        # HOUR
        Directive(
            'H',
            consts.HOUR24_REGEX,
            name='hour',
            type_=int,
            formatter=lambda d: '%.2d' % d.hour
        ),
        Directive(
            'k',
            consts.PERSIAN_HOUR24_REGEX,
            name='hour',
            type_=int,
            formatter=lambda d: persian(d.hour),
        ),
        Directive(
            'h',
            consts.PERSIAN_HOUR24_ZERO_PADDED_REGEX,
            name='hour',
            type_=int,
            formatter=lambda d: persian('%.2d' % d.hour),
        ),
        Hour12Directive('I'),
        Hour12Directive(
            'l',
            consts.PERSIAN_HOUR12_REGEX,
            formatter=lambda d: persian(d.hour12()),
        ),
        Hour12Directive(
            'i',
            consts.PERSIAN_HOUR12_ZERO_PADDED_REGEX,
            formatter=lambda d: persian('%.2d' % d.hour12()),
        ),

        # MINUTE
        Directive(
            'M',
            consts.MINUTE_REGEX,
            name='minute',
            type_=int,
            formatter=lambda d: '%.2d' % d.minute
        ),
        Directive(
            'v',
            consts.PERSIAN_MINUTE_REGEX,
            name='minute',
            type_=int,
            formatter=lambda d: persian(d.minute)
        ),
        Directive(
            'r',
            consts.PERSIAN_MINUTE_ZERO_PADDED_REGEX,
            name='minute',
            type_=int,
            formatter=lambda d: persian('%.2d' % d.minute)
        ),

        # SECOND
        Directive(
            'S',
            consts.SECOND_REGEX,
            name='second',
            type_=int,
            formatter=lambda d: '%.2d' % d.second
        ),
        Directive(
            'L',
            consts.PERSIAN_SECOND_REGEX,
            name='second',
            type_=int,
            formatter=lambda d: persian(d.second)
        ),
        Directive(
            's',
            consts.PERSIAN_SECOND_ZERO_PADDED_REGEX,
            name='second',
            type_=int,
            formatter=lambda d: persian('%.2d' % d.second)
        ),

        # MICROSECOND
        Directive(
            'f',
            consts.MICROSECOND_REGEX,
            name='microsecond',
            type_=int,
            formatter=lambda d: '%.6d' % d.microsecond
        ),
        Directive(
            'F',
            consts.PERSIAN_MICROSECOND_REGEX,
            name='microsecond',
            type_=int,
            formatter=lambda d: persian('%.6d' % d.microsecond),
            pre_parser=latin_digit,
        ),

        # TIMEZONE
        UTCOffsetDirective('z'),
        PersianUTCOffsetDirective('o'),
        TimezoneNameDirective('Z'),

        # COMPOSITE
        CompositeDirective(
            'c',
            '%s %s %s %s %s:%s' % (
                consts.PERSIAN_WEEKDAY_ABBRS_REGEX,
                consts.PERSIAN_DAY_REGEX,
                consts.PERSIAN_MONTH_ABBRS_REGEX,
                consts.PERSIAN_SHORT_YEAR_REGEX,
                consts.PERSIAN_HOUR24_REGEX,
                consts.PERSIAN_MINUTE_REGEX),
            "%a %D %b %n %k:%v"
        ),
        CompositeDirective(
            'C',
            '%s %s %s %s %s:%s:%s %s' % (
                consts.PERSIAN_WEEKDAY_NAMES_REGEX,
                consts.PERSIAN_DAY_REGEX,
                consts.PERSIAN_MONTH_NAMES_REGEX,
                consts.PERSIAN_YEAR_REGEX,
                consts.PERSIAN_HOUR12_ZERO_PADDED_REGEX,
                consts.PERSIAN_MINUTE_ZERO_PADDED_REGEX,
                consts.PERSIAN_SECOND_ZERO_PADDED_REGEX,
                consts.AM_PM_REGEX),
            "%A %D %B %N %i:%r:%s %p"
        ),
        CompositeDirective(
            'q',
            '%s %s %s %s %s:%s' % (
                consts.PERSIAN_WEEKDAY_ABBRS_ASCII_REGEX,
                consts.DAY_REGEX,
                consts.PERSIAN_MONTH_ABBRS_ASCII_REGEX,
                consts.SHORT_YEAR_REGEX,
                consts.HOUR24_REGEX,
                consts.MINUTE_REGEX),
            "%e %d %g %y %H:%M"
        ),
        CompositeDirective(
            'Q',
            '%s %s %s %s %s:%s:%s %s' % (
                consts.PERSIAN_WEEKDAY_NAMES_ASCII_REGEX,
                consts.DAY_REGEX,
                consts.PERSIAN_MONTH_NAMES_ASCII_REGEX,
                consts.YEAR_REGEX,
                consts.HOUR12_REGEX,
                consts.MINUTE_REGEX,
                consts.SECOND_REGEX,
                consts.AM_PM_ASCII_REGEX),
            "%E %d %G %Y %I:%M:%S %t"
        ),
        CompositeDirective(
            'X',
            '%s:%s:%s %s' % (
                consts.PERSIAN_HOUR12_ZERO_PADDED_REGEX,
                consts.PERSIAN_MINUTE_ZERO_PADDED_REGEX,
                consts.PERSIAN_SECOND_ZERO_PADDED_REGEX,
                consts.AM_PM_REGEX),
            "%i:%r:%s %p"
        ),
    ]

    """

    """

    # _post_parsers = [
    #     'persianday',
    #     'persiandayzeropadded',
    #     'persiandayofyear',
    #     'persiandayofyearzeropadded',
    #     'persianmonth',
    #     'persianmonthzeropadded',
    #     'persianyear',
    #     'persianyearzeropadded',
    #     'persianshortyear',
    #     'persianshortyearzeropadded',
    #     'persianmicrosecond',
    #     'persianhour12',
    #     'persianhour12zeropadded',
    #     'persianhour24',
    #     'persianhour24zeropadded',
    #     'persianminute',
    #     'persianminutezeropadded',
    #     'persiansecond',
    #     'persiansecondzeropadded',
    #     'persianutcoffset',
    #     'localdateformat',
    #     'localshortdatetimeformat',
    #     'localshortdatetimeformatascii',
    #     'localdatetimeformat',
    #     'localdatetimeformatascii',
    #     'localtimeformat',
    #     'monthabbr',
    #     'monthabbr_ascii',
    #     'monthname',
    #     'monthnameascii',
    #     'ampm',
    #     'ampmascii',
    #     'shortyear',
    #     'dayofyear',
    #     'utcoffset'
    # ]


class JalaliTimedeltaFormatter(JalaliDateFormatter):
    """
    Responsible to parse and formatting of a :py:class:`khayyam.JalaliTimedelta` instance.

    """
    _directives = [

        # Total hours
        Directive(
            'H',
            consts.UNLIMITED_INT_REGEX,
            type_=int,
            formatter=lambda d: '%d' % d.total_hours,
            post_parser=lambda ctx, f: ctx.update(hours=ctx['H'])
        ),
        Directive(
            'k',
            consts.PERSIAN_UNLIMITED_INT_REGEX,
            type_=int,
            formatter=lambda d: persian('%d' % d.total_hours),
            pre_parser=latin_digit,
            post_parser=lambda ctx, f: ctx.update(hours=ctx['k'])
        ),

        # Hours
        Directive(
            'I',
            consts.HOUR24_REGEX,
            name='hours',
            type_=int,
            formatter=lambda d: '%.2d' % d.hours,
        ),
        Directive(
            'h',
            consts.PERSIAN_HOUR24_ZERO_PADDED_REGEX,
            name='hours',
            type_=int,
            formatter=lambda d: persian('%.2d' % d.hours),
            pre_parser=latin_digit,
        ),

        # Minutes
        Directive(
            'M',
            consts.UNLIMITED_INT_REGEX,
            type_=int,
            formatter=lambda t: '%d' % t.total_minutes,
            post_parser=lambda ctx, f: ctx.update(minutes=ctx['M'])
        ),
        Directive(
            'm',
            consts.MINUTE_REGEX,
            name='minutes',
            type_=int,
            formatter=lambda t: '%.2d' % t.minutes
        ),

    ]

    # _post_parsers = [
    #
    #     'totalhours',
    #     'persiantotalhours',
    #     'totalminutes',
    #
    # ]

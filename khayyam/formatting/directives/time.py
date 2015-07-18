# -*- coding: utf-8 -*-
import re
from .directive import Directive
import khayyam.constants as consts
from khayyam.compat import get_unicode
__author__ = 'vahid'


class AmPmDirective(Directive):
    def __init__(self):
        super(AmPmDirective, self).__init__(
            'p',
            'ampm',
            consts.AM_PM_REGEX,
            get_unicode)

    def format(self, d):
        return '%s' % d.ampm()

    def post_parser(self, ctx, formatter):
        hour12 = ctx['hour12']
        if hour12 < 12:
            ctx['hour'] = hour12 + (12 if ctx['ampm'] == consts.AM_PM[1] else 0)
        else:
            ctx['hour'] = hour12


class AmPmASCIIDirective(Directive):
    def __init__(self):
        super(AmPmASCIIDirective, self).__init__(
            't',
            'ampm_ascii',
            consts.AM_PM_ASCII_REGEX,
            get_unicode)

    def format(self, d):
        return '%s' % d.ampmascii()

    def post_parser(self, ctx, formatter):
        hour12 = ctx['hour12']
        if hour12 < 12:
            ctx['hour'] = hour12 + (12 if ctx['ampm_ascii'] == consts.AM_PM_ASCII[1] else 0)
        else:
            ctx['hour'] = hour12


class LocalShortDatetimeFormatDirective(Directive):
    def __init__(self):
        super(LocalShortDatetimeFormatDirective, self).__init__(
            'c', 'localshortdatetimeformat', consts.LOCAL_SHORT_DATE_TIME_FORMAT_REGEX, get_unicode)

    def format(self, d):
        return d.localshortformat()

    def post_parser(self, ctx, formatter):
        # TODO: Add this behavior to the documents
        regex = ' '.join([
            '(?P<weekdayabbr>%s)' % consts.PERSIAN_WEEKDAY_ABBRS_REGEX,
            '(?P<day>%s)' % consts.DAY_REGEX,
            '(?P<monthabbr>%s)' % consts.PERSIAN_MONTH_ABBRS_REGEX,
            '(?P<shortyear>%s)' % consts.SHORT_YEAR_REGEX,
            '(?P<hour>%s):(?P<minute>%s)' % (consts.HOUR24_REGEX, consts.MINUTE_REGEX),
        ])

        match = re.match(regex, ctx[self.name])
        d = match.groupdict()
        ctx.update(dict(
            weekdayabbr = formatter.directives_by_key['a'].type_(d['weekdayabbr']),
            day = formatter.directives_by_key['d'].type_(d['day']),
            monthabbr = formatter.directives_by_key['b'].type_(d['monthabbr']),
            shortyear = formatter.directives_by_key['y'].type_(d['shortyear']),
            hour = formatter.directives_by_key['H'].type_(d['hour']),
            minute = formatter.directives_by_key['M'].type_(d['minute'])
        ))


class LocalASCIIShortDatetimeFormatDirective(Directive):
    def __init__(self):
        super(LocalASCIIShortDatetimeFormatDirective, self).__init__(
            'q', 'localshortdatetimeformatascii', consts.LOCAL_SHORT_DATE_TIME_FORMAT_ASCII_REGEX, get_unicode)

    def format(self, d):
        return d.localshortformatascii()

    def post_parser(self, ctx, formatter):
        """
        %e %d %g %y %H:%M
        """
        # TODO: Add this behavior to the documents
        regex = ' '.join([
            '(?P<weekdayabbr>%s)' % consts.PERSIAN_WEEKDAY_ABBRS_ASCII_REGEX,
            '(?P<day>%s)' % consts.DAY_REGEX,
            '(?P<monthabbr>%s)' % consts.PERSIAN_MONTH_ABBRS_ASCII_REGEX,
            '(?P<shortyear>%s)' % consts.SHORT_YEAR_REGEX,
            '(?P<hour>%s):(?P<minute>%s)' % (consts.HOUR24_REGEX, consts.MINUTE_REGEX),
        ])

        match = re.match(regex, ctx[self.name])
        d = match.groupdict()
        ctx.update(dict(
            weekdayabbr_ascii = formatter.directives_by_key['e'].type_(d['weekdayabbr']),
            day = formatter.directives_by_key['d'].type_(d['day']),
            monthabbr_ascii = formatter.directives_by_key['g'].type_(d['monthabbr']),
            shortyear = formatter.directives_by_key['y'].type_(d['shortyear']),
            hour = formatter.directives_by_key['H'].type_(d['hour']),
            minute = formatter.directives_by_key['M'].type_(d['minute'])
        ))




class LocalDatetimeFormatDirective(Directive):
    def __init__(self):
        super(LocalDatetimeFormatDirective, self).__init__(
            'C', 'localdatetimeformat', consts.LOCAL_DATE_TIME_FORMAT_REGEX, get_unicode)

    def format(self, d):
        return d.localdatetimeformat()

    def post_parser(self, ctx, formatter):
        # TODO: Add this behavior to the documents
        """
        %A %d %B %Y %I:%M:%S %p
        """
        regex = ' '.join([
            '(?P<weekdayname>%s)' % consts.PERSIAN_WEEKDAY_NAMES_REGEX,
            '(?P<day>%s)' % consts.DAY_REGEX,
            '(?P<monthname>%s)' % consts.PERSIAN_MONTH_NAMES_REGEX,
            '(?P<year>%s)' % consts.YEAR_REGEX,
            '(?P<hour12>%s):(?P<minute>%s):(?P<second>%s)' % (
                consts.HOUR12_REGEX, consts.MINUTE_REGEX, consts.SECOND_REGEX),
            '(?P<ampm>%s)' % consts.AM_PM_REGEX
        ])

        match = re.match(regex, ctx[self.name])
        d = match.groupdict()
        ctx.update(dict(
            weekdayname = formatter.directives_by_key['A'].type_(d['weekdayname']),
            day = formatter.directives_by_key['d'].type_(d['day']),
            monthname = formatter.directives_by_key['B'].type_(d['monthname']),
            year = formatter.directives_by_key['Y'].type_(d['year']),
            hour12 = formatter.directives_by_key['I'].type_(d['hour12']),
            minute = formatter.directives_by_key['M'].type_(d['minute']),
            second = formatter.directives_by_key['S'].type_(d['second']),
            ampm = formatter.directives_by_key['p'].type_(d['ampm']),
        ))


class LocalASCIIDatetimeFormatDirective(Directive):
    def __init__(self):
        super(LocalASCIIDatetimeFormatDirective, self).__init__(
            'Q', 'localdatetimeformatascii', consts.LOCAL_DATE_TIME_FORMAT_ASCII_REGEX, get_unicode)

    def format(self, d):
        return d.localdatetimeformatascii()

    def post_parser(self, ctx, formatter):
        # TODO: Add this behavior to the documents
        """
        %E %d %G %Y %I:%M:%S %t
        """
        regex = ' '.join([
            '(?P<weekdayname>%s)' % consts.PERSIAN_WEEKDAY_NAMES_ASCII_REGEX,
            '(?P<day>%s)' % consts.DAY_REGEX,
            '(?P<monthname>%s)' % consts.PERSIAN_MONTH_NAMES_ASCII_REGEX,
            '(?P<year>%s)' % consts.YEAR_REGEX,
            '(?P<hour12>%s):(?P<minute>%s):(?P<second>%s)' % (
                consts.HOUR12_REGEX, consts.MINUTE_REGEX, consts.SECOND_REGEX),
            '(?P<ampm>%s)' % consts.AM_PM_ASCII_REGEX
        ])

        match = re.match(regex, ctx[self.name])
        d = match.groupdict()

        ctx.update(dict(
            weekdayname_ascii = formatter.directives_by_key['E'].type_(d['weekdayname']),
            day = formatter.directives_by_key['d'].type_(d['day']),
            monthname_ascii = formatter.directives_by_key['G'].type_(d['monthname']),
            year = formatter.directives_by_key['Y'].type_(d['year']),
            hour12 = formatter.directives_by_key['I'].type_(d['hour12']),
            minute = formatter.directives_by_key['M'].type_(d['minute']),
            second = formatter.directives_by_key['S'].type_(d['second']),
            ampm_ascii = formatter.directives_by_key['t'].type_(d['ampm']),
        ))


"""
%X            Locale’s appropriate time representation.
%z            UTC offset in the form +HHMM or -HHMM (empty string if the the object is naive).    (5)
%Z            Time zone name (empty string if the object is naive).
"""

# TODO: AM PM ASCII

TIME_FORMAT_DIRECTIVES = [
    AmPmDirective(),
    AmPmASCIIDirective(),
    LocalShortDatetimeFormatDirective(),
    LocalDatetimeFormatDirective(),
    LocalASCIIShortDatetimeFormatDirective(),
    LocalASCIIDatetimeFormatDirective(),
    Directive(
        'H',
        'hour',
        consts.HOUR24_REGEX,
        int,
        lambda d: '%.2d' % d.hour,
    ),
    Directive(
        'I',
        'hour12',
        consts.HOUR12_REGEX,
        int,
        lambda d: '%.2d' % d.hour12()
    ),
    Directive(
        'M',
        'minute',
        consts.MINUTE_REGEX,
        int,
        lambda d: '%.2d' % d.minute,
    ),
    Directive(
        'S',
        'second',
        consts.SECOND_REGEX,
        int,
        lambda d: '%.2d' % d.second,
    ),
    Directive(
        'f',
        'microsecond',
        consts.MICROSECOND_REGEX,
        int,
        lambda d: '%.6d' % d.microsecond
    ),
    # --------SUPPORTED--------
]

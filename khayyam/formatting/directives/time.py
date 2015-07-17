# -*- coding: utf-8 -*-
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


"""

=========    =======
Directive    Meaning
=========    =======
%H            Hour (24-hour clock) as a decimal number [00,23].
%M            Minute as a decimal number [00,59].
%S            Second as a decimal number [00,61].    (3)
%f            Microsecond as a decimal number [0,999999], zero-padded on the left    (1)
%I            Hour (12-hour clock) as a decimal number [01,12].
%p            Locale’s equivalent of either AM or PM.    (2)
-----------------
%c            Locale’s appropriate short date and time representation.
%C            Locale’s appropriate date and time representation.
%q            ASCII Locale’s appropriate short date and time representation.
%Q            ASCII Locale’s appropriate date and time representation.
%X            Locale’s appropriate time representation.
%z            UTC offset in the form +HHMM or -HHMM (empty string if the the object is naive).    (5)
%Z            Time zone name (empty string if the object is naive).
=========    =======
"""

# TODO: AM PM ASCII

TIME_FORMAT_DIRECTIVES = [
    AmPmDirective(),
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
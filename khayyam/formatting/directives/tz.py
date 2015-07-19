# -*- coding: utf-8 -*-
import re
from .directive import Directive
import khayyam.constants as consts
from khayyam.compat import get_unicode
from datetime import timedelta
from khayyam.timezones import Timezone
__author__ = 'vahid'


class UTCOffsetDirective(Directive):
    def __init__(self):
        super(UTCOffsetDirective, self).__init__(
            'z', 'utcoffset', consts.UTC_OFFSET_FORMAT_REGEX, get_unicode)

    def format(self, d):
        if not d.tzinfo:
            return ''
        seconds = d.utcoffset().total_seconds()
        return '%s%.2d:%.2d' % (
            '+' if seconds >= 0 else '-',
            int(seconds / 3600),
            int((seconds % 3600) / 60),
        )

    def post_parser(self, ctx, formatter):
        exp = ctx[self.name]
        if exp.strip() == '':
            return
        regex = '(?P<posneg>[-+]?)(?P<hour>\d{2}):(?P<minute>\d{2})'
        match = re.match(regex, exp)
        d = match.groupdict()
        posneg = lambda i: 0 - i if d['posneg'] == '-' else i
        hours = int(d['hour'])
        minutes = int(d['minute'])
        if not hours and not minutes:
            return
        ctx.update(dict(tzinfo=Timezone(timedelta(
            hours = posneg(hours),
            minutes = posneg(minutes)
        ))))


class TimezoneNameDirective(Directive):
    def __init__(self):
        super(TimezoneNameDirective, self).__init__(
            'Z', 'tzname', consts.TZ_NAME_FORMAT_REGEX, get_unicode)

    def format(self, d):
        if d.tzinfo:
            return d.tzname()
        return ''

# -*- coding: utf-8 -*-
import re
from .directive import Directive
import khayyam.constants as consts
from khayyam.compat import get_unicode
from datetime import timedelta
from khayyam.timezones import FixedOffsetTimezone
__author__ = 'vahid'




class UTCOffsetDirective(Directive):
    def __init__(self):
        super(UTCOffsetDirective, self).__init__(
            'z', 'utcoffset', consts.UTC_OFFSET_FORMAT_REGEX, get_unicode)

    def format(self, d):
        seconds = d.utcoffset().total_seconds()
        return '%s%s:%s' % (
            '+' if seconds >= 0 else '',
            int(seconds / 3600),
            int((seconds % 3600) / 60))

    def post_parser(self, ctx, formatter):
        # TODO: Add this behavior to the documents
        regex = '(?P<posneg>[-+]?)(?P<hour>\d{2})(?P<minute>\d{2})'
        match = re.match(regex, ctx[self.name])
        d = match.groupdict()
        posneg = lambda i: 0 - i if d['posneg'] == '-' else i
        ctx.update(dict(tzinfo=FixedOffsetTimezone(timedelta(
            hours = posneg(int(d['hour'])),
            minutes = posneg(int(d['minute']))
        ))))


class TimezoneNameDirective(Directive):
    def __init__(self):
        super(TimezoneNameDirective, self).__init__(
            'Z', 'tzname', consts.TZ_NAME_FORMAT_REGEX, get_unicode)

    def format(self, d):
        if d.tzinfo:
            return d.tzname()
        return ''

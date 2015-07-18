# -*- coding: utf-8 -*-
import re
from .directive import Directive
import khayyam.constants as consts
from khayyam.compat import get_unicode
from datetime import tzinfo, timedelta
__author__ = 'vahid'

class TzInfo(tzinfo):

    def __init__(self, offset, *args, **kw):
        assert(isinstance(offset, timedelta))
        self.offset = offset
        super(TzInfo, self).__init__(*args, **kw)


    def utcoffset(self, dt):
        return self.offset

    def dst(self, dt):
        return consts.ZERO_DELTA

    def tzname(self, dt):
        return self.format_offset(dt)

    def format_offset(self, dt):
        offset = self.utcoffset(dt)
        return '+%s:%s' % (int(offset.seconds / 3600), int((offset.seconds % 3600) / 60))


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
        ctx.update(dict(tzinfo=TzInfo(timedelta(
            hours = posneg(int(d['hour'])),
            minutes = posneg(int(d['minute']))
        ))))

# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import tzinfo, timedelta
from khayyam.helpers import force_encoded_string_output
__author__ = 'vahid'

ZERO_DELTA = timedelta(0)
STDOFFSET = timedelta(minutes=210)  # Minutes
DSTOFFSET = timedelta(minutes=270)  # Minutes
DSTDIFF = DSTOFFSET - STDOFFSET


class Timezone(tzinfo):

    def __init__(self, offset, dst_offset=None, dst_checker=None, name=None):
        assert (isinstance(offset, timedelta))
        self._offset = offset
        self._dst_offset = dst_offset
        self._dst_checker = dst_checker
        self._name = name

    def fromutc(self, dt):
        if dt.tzinfo != self:
            raise ValueError('Datetime timezone mismatch: %s != %s' % (dt.tzinfo, self))

        utc_offset = dt.utcoffset()
        dst_offset = dt.dst()
        if utc_offset is None:
            raise ValueError('The object: %s is naive.' % dt)
        if dst_offset is None:
            raise ValueError('Invalid DST timedelta: %s' % dst_offset)
        delta = utc_offset - dst_offset  # this is self's standard offset
        if delta:
            dt += delta  # convert to standard local time
            dst_offset = dt.dst()
            if dst_offset is None:
                raise ValueError('Invalid DST timedelta: %s' % dst_offset)
        if dst_offset:
            return dt + dst_offset
        else:
            return dt

    def utcoffset(self, dt):
        if self._is_dst(dt):
            return self._offset + self._dst_offset
        else:
            return self._offset

    def dst(self, dt):
        if self._dst_offset and self._is_dst(dt):
            return self._dst_offset
        else:
            return ZERO_DELTA

    def __unicode__(self):
        off = self._offset
        return '%s%.2d:%.2d%s' % (
            '+' if off.total_seconds() >= 0 else '-',
            int(off.total_seconds() / 3600),
            int((off.total_seconds() % 3600) / 60),
            (' dst:%d' % (self._dst_offset.total_seconds() / 60)) if self._dst_offset else ''
        )

    __repr__ = force_encoded_string_output(__unicode__)

    def tzname(self, dt):
        if self._name:
            return self._name
        else:
            return repr(self)

    def _is_dst(self, dt):
        if self._dst_checker:
            return self._dst_checker(dt)
        return False

    def __hash__(self):
        return hash(self._offset) ^ hash(self._dst_offset)


class TehranTimezone(Timezone):
    dst_start = (1, 1)
    dst_end = (7, 1)

    def __init__(self):
        super(TehranTimezone, self).__init__(
            timedelta(minutes=210),
            timedelta(minutes=60),
            lambda dt: (self.dst_start[0] < dt.month < self.dst_end[0]) or \
                       (self.dst_start[0] == dt.month and self.dst_start[1] <= dt.day) or \
                       (self.dst_end[0] == dt.month and self.dst_end[1] > dt.day),
            'Iran/Tehran'
        )

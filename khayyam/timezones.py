
from datetime import tzinfo, timedelta
from khayyam import JalaliDatetime
from khayyam.constants import ZERO_DELTA

STDOFFSET = timedelta(minutes=210) # Minutes
DSTOFFSET = timedelta(minutes=270) # Minutes
DSTDIFF = DSTOFFSET - STDOFFSET


class TehranTimezone(tzinfo):
    
    def utcoffset(self, dt):
        if self._is_dst(dt):
            return DSTOFFSET
        else:
            return STDOFFSET
    
    def _is_dst(self, dt):
        # TODO: reimplement, just test year and month
        dt = dt.replace(tzinfo=None)
        if isinstance(dt, JalaliDatetime):
            jdt = dt
        else:
            jdt = JalaliDatetime.from_datetime(dt)
        start_jdt = jdt.replace(month=1, day=1)
        end_jdt = jdt.replace(month=7, day=1)
        if start_jdt < jdt < end_jdt:
            return True
        else:
            return False
    
    def dst(self, dt):
        if self._is_dst(dt):
            return DSTDIFF
        else:
            return ZERO_DELTA
                     
    def tzname(self, dt):
        return 'Iran/Tehran'
        # return self.format_offset(dt)
    

class FixedOffsetTimezone(tzinfo):

    def __init__(self, offset, name=None):
        assert(isinstance(offset, timedelta))
        self._offset = offset
        self._name = name

    def utcoffset(self, dt):
        return self._offset

    def dst(self, dt):
        return ZERO_DELTA

    def tzname(self, dt):
        if self._name:
            return self._name
        else:
            return '%s:%s' % (int(self._offset.seconds / 3600), int((self._offset.seconds % 3600) / 60))

# -*- coding: utf-8 -*-
from .constants import MINYEAR, MAXYEAR, \
    SATURDAY, SUNDAY, MONDAY, THURSDAY, WEDNESDAY, TUESDAY, FRIDAY
from .jalali_date import JalaliDate
from .jalali_datetime import JalaliDatetime
from .timezones import TehranTimezone, Timezone
teh_tz = TehranTimezone()
__author__ = 'vahid'
__version__ = '2.2.0-alpha'

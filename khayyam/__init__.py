# -*- coding: utf-8 -*-

__version__ = '2.9.8a'

#: Minimum year supported by the library.
MINYEAR = 1

#: Maximum year supported by the library.
MAXYEAR = 3178

#: Representing the Saturday weekday.
SATURDAY = 0

#: Representing the Sunday weekday.
SUNDAY = 1

#: Representing the Monday weekday.
MONDAY = 2

#: Representing the Tuesday weekday.
TUESDAY = 3


#: Representing the Wednesday weekday.
WEDNESDAY = 4


#: Representing the Thursday weekday.
THURSDAY = 5


#: Representing the Friday weekday.
FRIDAY = 6


from .jalali_date import JalaliDate
from .jalali_datetime import JalaliDatetime
from .timezones import TehranTimezone, Timezone
teh_tz = TehranTimezone()
__author__ = 'vahid'

__all__ = [
    'MINYEAR',
    'MAXYEAR',
    'SATURDAY',
    'SUNDAY',
    'MONDAY',
    'THURSDAY',
    'WEDNESDAY',
    'TUESDAY',
    'FRIDAY',
    'JalaliDate',
    'JalaliDatetime',
    'TehranTimezone',
    'Timezone',
    'teh_tz'
]

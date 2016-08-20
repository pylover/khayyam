# -*- coding: utf-8 -*-
from .constants import *
from .jalali_date import JalaliDate
from .jalali_datetime import JalaliDatetime
from .timezones import TehranTimezone, Timezone

__version__ = '3.0.0-dev0'


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

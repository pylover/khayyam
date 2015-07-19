# -*- coding: utf-8 -*-
__version__ = '2.0.0-alpha'
from .constants import MINYEAR, MAXYEAR, \
    SATURDAY, SUNDAY, MONDAY, THURSDAY, WEDNESDAY, TUESDAY, FRIDAY
from .jalali_date import JalaliDate
from .jalali_datetime import JalaliDatetime
from .timezones import TehranTimezone
teh_tz = TehranTimezone()
__author__ = 'vahid'
# TODO: add persian numbers(digits)
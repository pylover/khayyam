# -*- coding: utf-8 -*-
from math import floor, ceil
__author__ = 'vahid'


def get_julian_day_from_gregorian(year, month, day):
    if year / 4.0 == round(year / 4.0):
        if year / 100.0 == round(year / 100.0):
            if year / 400.0 == round(year / 400.0):
                # Leap year checking #
                if month == 2:
                    assert day <= 29, 'Invalid date'
        else:
            # Leap year #
            if month == 2:
                assert day <= 29, 'Invalid date'

    year = float(year)
    month = float(month)
    day = float(day)

    # Determine JD
    if month <= 2:
        year -= 1
        month += 12

    century = floor(year / 100)
    return floor(365.25 * (year + 4716)) + floor(30.6001 * (month + 1)) + day + (2 - century + floor(century / 4)) - 1524.5


def is_leap_year(year):
    return ((((((year - [473, 474][year > 0]) % 2820) + 474) + 38) * 682) % 2816) < 682 


def days_in_year(year):
    return 366 if is_leap_year(year) else 365


def days_in_month(year, month):
    if 1 <= month <= 6:
        return 31
    elif 7 <= month < 12:
        return 30

    assert month == 12, 'Month must be between 1 and 12'
    
    # Esfand(اسفند)
    if is_leap_year(year):
        return 30
    else:
        return 29


def julian_day_from_jalali_date(year, month, day):
    base = year - ([473, 474][year >= 0])
    julian_year = 474 + (base % 2820)
    return day + ([((month - 1) * 30) + 6, (month - 1) * 31][month <= 7]) + floor(((julian_year * 682) - 110) / 2816) + (julian_year - 1) * 365 + floor(base / 2820) * 1029983 + (1948320.5 - 1)


def jalali_date_from_julian_day(julian_day):
    julian_day = floor(julian_day) + 0.5
    offset = julian_day - 2121445.5 # julian_day_from_jalali(475, 1, 1) replaced by its static value
    cycle = floor(offset / 1029983)
    remaining = offset % 1029983
    if remaining == 1029982:
        year_cycle = 2820
    else:
        a1 = floor(remaining / 366)
        a2 = remaining % 366
        year_cycle = floor(((2134 * a1) + (2816 * a2) + 2815) / 1028522) + a1 + 1
    y = year_cycle + (2820 * cycle) + 474
    if y <= 0:
        y -= 1
    days_in_years = (julian_day - julian_day_from_jalali_date(y, 1, 1)) + 1
    m = ceil([(days_in_years - 6) / 30, days_in_years / 31][days_in_years <= 186])
    day = (julian_day - julian_day_from_jalali_date(y, m, 1)) + 1
    return y, m, day


def gregorian_date_from_julian_day(jd):
    y = 0
    m = 0

    if jd <= 0.0:
        raise ValueError('Invalid Date')

    jdm = jd + 0.5
    z = floor(jdm)
    f = jdm - z

    alpha = floor((z - 1867216.25) / 36524.25)
    b = (z + 1 + alpha - floor(alpha / 4)) + 1524
    c = floor((b - 122.1) / 365.25)
    d = floor(365.25 * c)
    e = floor((b - d) / 30.6001)
    day = b - d - floor(30.6001 * e) + f

    if e < 14:
        m = e - 1
    elif e == 14 or e == 15:
        m = e - 13

    if m > 2:
        y = c - 4716
    elif m == 1 or m == 2:
        y = c - 4715

    return int(y), int(m), int(day)


def jalali_date_from_gregorian_date(year, month, day):
    return jalali_date_from_julian_day(get_julian_day_from_gregorian(year, month, day))

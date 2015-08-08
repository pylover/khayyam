from libc.math cimport floor, ceil
from cpython cimport bool

cpdef double get_julian_day_from_gregorian(int year, int month, int day):
    cdef:
        double _year = year
        double _month = month
        double _day = day
        double _century = 0
        double result = 0

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


    if _month <= 2:
        _year -= 1
        _month += 12

    _century = floor(_year / 100)
    result += floor(365.25 * (_year + 4716))
    result += floor(30.6001 * (_month + 1))
    result += _day
    result += 2 - _century + floor(_century / 4)
    result -= 1524.5

    return result


cpdef bool is_leap_year(int year):
    return ((((((year - [473, 474][year > 0]) % 2820) + 474) + 38) * 682) % 2816) < 682


cpdef int days_in_year(int year):
    return 366 if is_leap_year(year) else 365


cpdef int days_in_month(int year, int month):
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

cpdef double julian_day_from_jalali_date(int year, int month, int day):
    cdef:
        int base = year - (474 if year >= 0 else 473)
        int julian_year = 474 + (base % 2820)
        double result = day

    result += [((month - 1) * 30) + 6, (month - 1) * 31][month <= 7]
    result += floor(((julian_year * 682) - 110) / 2816)
    result += (julian_year - 1) * 365
    result += floor(base / 2820) * 1029983
    result += 1948320.5 - 1
    return result


cpdef tuple jalali_date_from_julian_day(double jd):
    cdef:
        double julian_day = floor(jd) + 0.5
        double offset = julian_day - 2121445.5 # julian_day_from_jalali(475, 1, 1) replaced by its static value
        double cycle = floor(offset / 1029983)
        double remaining = offset % 1029983
        double a1, a2, year_cycle, days_in_year
        int year, month, day

    if remaining == 1029982:
        year_cycle = 2820
    else:
        a1 = floor(remaining / 366)
        a2 = remaining % 366
        year_cycle = floor(((2134 * a1) + (2816 * a2) + 2815) / 1028522) + a1 + 1
    year = <int>(year_cycle + (2820 * cycle) + 474)
    if year <= 0:
        year -= 1
    days_in_year = (julian_day - julian_day_from_jalali_date(year, 1, 1)) + 1
    month = <int>ceil([(days_in_year - 6) / 30, days_in_year / 31][days_in_year <= 186])
    day = <int>(julian_day - julian_day_from_jalali_date(year, month, 1)) + 1
    return year, month, day


cpdef tuple gregorian_date_from_julian_day(double jd):
    cdef:
        double year, month, day
        double julian_day, actual_days, remains, alpha, b, c, d, e

    if jd <= 0:
        raise ValueError('Invalid Date')

    julian_day = jd + 0.5
    actual_days = floor(julian_day)
    remains = julian_day - actual_days

    alpha = floor((actual_days - 1867216.25) / 36524.25)
    b = (actual_days + 1 + alpha - floor(alpha / 4)) + 1524
    c = floor((b - 122.1) / 365.25)
    d = floor(365.25 * c)
    e = floor((b - d) / 30.6001)
    day = b - d - floor(30.6001 * e) + remains

    if e < 14:
        month = e - 1
    elif e == 14 or e == 15:
        month = e - 13
    else:
        raise ValueError('Cannot calculate month')


    if month > 2:
        year = c - 4716
    elif month == 1 or month == 2:
        year = c - 4715
    else:
        raise ValueError('Invalid month: %s' % month)

    return <int>year, <int>month, <int>day

cpdef tuple jalali_date_from_gregorian_date(int year, int month, int day):
    return jalali_date_from_julian_day(get_julian_day_from_gregorian(year, month, day))

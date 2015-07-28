from libc.math cimport floor, round
from cpython cimport bool

cpdef double get_julian_day_from_gregorian(int year, int month, int day):
    cdef double _year = year
    cdef double _month = month
    cdef double _day = day
    cdef double _century = 0
    cdef double result = 0

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
    cdef int base = year - ([473, 474][year >= 0])
    cdef int julian_year = 474 + (base % 2820)
    cdef double result = day
    result += [((month - 1) * 30) + 6, (month - 1) * 31][month <= 7]
    result += floor(((julian_year * 682) - 110) / 2816)
    result += (julian_year - 1) * 365
    result += floor(base / 2820) * 1029983
    result += 1948320.5 - 1
    return result

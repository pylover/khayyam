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

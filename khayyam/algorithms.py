# -*- coding: utf-8 -*-
import warnings

__author__ = 'vahid'

try:
    from .algorithms_c import \
        is_leap_year, \
        days_in_year, \
        days_in_month, \
        get_julian_day_from_gregorian, \
        julian_day_from_jalali_date, \
        jalali_date_from_julian_day, \
        gregorian_date_from_julian_day, \
        jalali_date_from_gregorian_date

except ImportError:
    warnings.warn(
        "The Cython extension is not available. Switching to fallback python pure algorithms, "
        "so it's may be slower than C implementation of the algorithms.")
    from .algorithms_pure import \
        is_leap_year, \
        days_in_year, \
        days_in_month, \
        get_julian_day_from_gregorian, \
        julian_day_from_jalali_date, \
        jalali_date_from_julian_day, \
        gregorian_date_from_julian_day, \
        jalali_date_from_gregorian_date




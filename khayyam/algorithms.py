# -*- coding: utf-8 -*-
import warnings

__author__ = 'vahid'

try:
    from .algorithms_c import \
        is_jalali_leap_year, \
        get_julian_day_from_gregorian_date, \
        get_days_in_jalali_year, \
        get_days_in_jalali_month, \
        get_julian_day_from_jalali_date, \
        get_jalali_date_from_julian_day, \
        get_gregorian_date_from_julian_day, \
        get_jalali_date_from_gregorian_date

except ImportError:  # pragma: no cover
    warnings.warn(
        "The C extension is not available. Switching to fallback python pure algorithms,"
        "so it's about 1000X slower than C implementation of the algorithms."
    )
    from .algorithms_pure import \
        is_jalali_leap_year, \
        get_julian_day_from_gregorian_date, \
        get_days_in_jalali_year, \
        get_days_in_jalali_month, \
        get_julian_day_from_jalali_date, \
        get_jalali_date_from_julian_day, \
        get_gregorian_date_from_julian_day, \
        get_jalali_date_from_gregorian_date

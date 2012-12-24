# coding: utf-8

from math import floor, ceil

def get_julian_day_from_gregorian(year, month, day):
    # Checking #
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
            
    y = year + 0.0
    m = month + 0.0
    d = day + 0.0
    
    # Determine JD
    if m <= 2:
        y = y - 1
        m = m + 12

    a = floor(y / 100)
    return floor(365.25 * (y + 4716)) + floor(30.6001 * (m + 1)) + d + (2 - a + floor(a / 4)) - 1524.5

def is_leap_year(year):
    return ((((((year - [473, 474][year > 0]) % 2820) + 474) + 38) * 682) % 2816) < 682 


def days_in_month(year, month):
    if month >= 1 and month <= 6:
        return 31
    elif month >= 7 and month < 12:
        return 30

    assert month == 12, 'Month must  be between 1 and 12'
    
    ### Esfand(اسفند) ###
    if is_leap_year(year):
        return 30 #Leap Year
    else:
        return 29

def julian_day_from_jalali(year, month, day):
    epbase = year - ([473, 474][year >= 0])
    epyear = 474 + (epbase % 2820)
    return day + ([((month - 1) * 30) + 6, (month - 1) * 31][month <= 7]) + floor(((epyear * 682) - 110) / 2816) + (epyear - 1) * 365 + floor(epbase / 2820) * 1029983 + (1948320.5 - 1);

def jalali_date_from_julian_days(jd):
    jdmp = floor(jd) + 0.5
    depoch = jdmp - 2121445.5 # julian_day_from_jalali(475, 1, 1) replaced by its static value
    cycle = floor(depoch / 1029983)
    cyear = depoch % 1029983
    if cyear == 1029982:
        ycycle = 2820
    else:
        a1 = floor(cyear / 366)
        a2 = cyear % 366
        ycycle = floor(((2134 * a1) + (2816 * a2) + 2815) / 1028522) + a1 + 1
    y = ycycle + (2820 * cycle) + 474
    if y <= 0:
        y -= 1
    yday = (jdmp - julian_day_from_jalali(y, 1, 1)) + 1
    m = ceil([(yday - 6) / 30, yday / 31][yday <= 186])
    day = (jdmp - julian_day_from_jalali(y, m, 1)) + 1
    return [y, m, day]
    
def gregorian_date_from_julian_day(jd):
    y = 0
    m = 0
    day = 0.0
    
    if jd > 0.0:
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
    else:
        raise ValueError(), 'Invalid Date'
    return (y, m, day)

def jalali_from_gregorian(year, month, day):
    return jalali_date_from_julian_days(get_julian_day_from_gregorian(year, month, day))


def parse(cls, date_string, format, valid_codes):
    available_codes = {}
    for code in valid_codes:
        try:
            i = format.index(code)
            available_codes[i] = code
        except ValueError:
            continue
    
    parts = []
    for code_index in sorted(available_codes):
        code = available_codes[code_index]
        try:
            i = format.index(code)
            if i > 0:
                parts.append(('gap', format[:i]))
            parts.append(('field', code))
            format = format[i + len(code):]
        except ValueError:
            continue
    
    fields = {}
    field_start = None
    for part in parts:
        if part[0] == 'gap': # Gap
            if field_start:
                gap_index = date_string.index(part[1]) 
                fields[field_start] = date_string[:gap_index]
                field_start = None
                date_string = date_string[gap_index + len(part[1]):]
            else:
                date_string = date_string[len(part[1]):]
        else: # Field
            if field_start:
                fields[field_start] = date_string[:valid_codes[part[1]][0]]
            else:
                field_start = part[1]
    
    if field_start:
        fields[field_start] = date_string
        
    values = {}
    for field, value in fields.iteritems():
        values[valid_codes[field][1]] = int(value) 
    
    result = cls(**values)
    
    return result    

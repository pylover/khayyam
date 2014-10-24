# coding=UTF-8

from datetime import date, timedelta
import re
from algorithms import  days_in_month, \
                        is_leap_year, \
                        get_julian_day_from_gregorian, \
                        jalali_date_from_julian_days, \
                        julian_day_from_jalali, \
                        gregorian_date_from_julian_day, \
                        parse

MINYEAR = 1
MAXYEAR = 3178

PERSIAN_WEEKDAY_NAMES = {
            0: u'دوشنبه',
            1: u'سه شنبه',
            2: u'چهارشنبه',
            3: u'پنجشنبه',
            4: u'جمعه',
            5: u'شنبه',
            6: u'یکشنبه'}

PERSIAN_WEEKDAY_ABBRS = {
            0: u'د',
            1: u'س',
            2: u'چ',
            3: u'پ',
            4: u'ج',
            5: u'ش',
            6: u'ی'}

PERSIAN_MONTH_NAMES = {
            1:  u'فروردین',
            2:  u'اردیبهشت',
            3:  u'خرداد',
            4:  u'تیر',
            5:  u'مرداد',
            6:  u'شهریور',
            7:  u'مهر',
            8:  u'آبان',
            9:  u'آذر',
            10: u'دی',
            11: u'بهمن',
            12: u'اسفند'}
PERSIAN_MONTH_ABBRS = {
            1:  u'فر',
            2:  u'ار',
            3:  u'خر',
            4:  u'تی',
            5:  u'مر',
            6:  u'شه',
            7:  u'مه',
            8:  u'آب',
            9:  u'آذ',
            10: u'دی',
            11: u'به',
            12: u'اس'}

def _replace_if_match(data, pattern, new):
    if re.search(pattern, data):
        if callable(new):
            new = new()
        if not isinstance(new, basestring):
            new = unicode(new)
        return data.replace(pattern, new)
    return data

class JalaliDate(object):
    """
    Representing the Jalali Date, without the time data.
    """
    def __init__(self, year=1, month=1, day=1):
        if year < MINYEAR or year > MAXYEAR:
            raise ValueError, 'Year must be between %s and %s' % (MINYEAR, MAXYEAR)
        self.year = int(year)
        
        if month < 1 or month > 12:
            raise ValueError, 'Month must be between 1 and 12' 
        self.month = int(month)
        
        daysinmonth = days_in_month(year, month)
        if day < 1 or day > daysinmonth:
            raise ValueError, 'Day must be between 1 and %s' % daysinmonth
        self.day = int(day)

    ##################
    ### Properties ###
    ##################

    @property
    def is_leap(self):
        """
        Determines the year is leap or not.
        """
        return is_leap_year(self.year)
            
    @property
    def days_in_month(self):
        """
        Get number of days in month. 
        """
        return days_in_month(self.year, self.month)
    
    #####################
    ### Class Methods ###
    #####################
    
    @classmethod
    def from_julian_days(cls, jd):
        """
        Create JalaliDate from julian day
        """
        arr = jalali_date_from_julian_days(jd)
        return cls(arr[0], arr[1], arr[2])
    
    @classmethod
    def from_date(cls, d):
        """
        Create JalaliDate from python's datetime.date
        """
        julian_days = get_julian_day_from_gregorian(d.year, d.month, d.day)
        return cls.from_julian_days(julian_days)

    @classmethod
    def today(cls):
        """
        Return the current local date. 
        """
        return cls.from_date(date.today())

        
    @classmethod
    def fromtimestamp(cls, timestamp, tz=None):
        """
        Return the local date and time corresponding to the POSIX timestamp, such as is returned by time.time(). If optional argument tz is None or not specified, the timestamp is converted to the platform's local date and time, and the returned datetime object is naive.
        
        Else tz must be an instance of a class tzinfo subclass, and the timestamp is converted to tz's time zone. In this case the result is equivalent to tz.fromutc(datetime.utcfromtimestamp(timestamp).replace(tzinfo=tz)).
        
        fromtimestamp() may raise ValueError, if the timestamp is out of the range of values supported by the platform C localtime() or gmtime() functions. It's common for this to be restricted to years in 1970 through 2038. Note that on non-POSIX systems that include leap seconds in their notion of a timestamp, leap seconds are ignored by fromtimestamp(), and then it's possible to have two timestamps differing by a second that yield identical datetime objects. See also utcfromtimestamp().
        """
        return cls.from_date(date.fromtimestamp(timestamp, tz=tz))
    
    @classmethod    
    def fromordinal(cls, ordinal):
        """
        Return the datetime corresponding to the proleptic Gregorian ordinal, where January 1 of year 1 has ordinal 1. ValueError is raised unless 1 <= ordinal <= datetime.max.toordinal(). The hour, minute, second and microsecond of the result are all 0, and tzinfo is None.
        """
        #return cls.from_date(date.fromordinal(ordinal))
        raise NotImplementedError()
    
    
    @classmethod
    def strptime(cls, date_string, frmt):
        """
        Return a datetime corresponding to date_string, parsed according to format. This is equivalent to datetime(*(time.strptime(date_string, format)[0:6])). ValueError is raised if the date_string and format can't be parsed by time.strptime() or if it returns a value which isn't a time tuple. See section strftime() and strptime() Behavior.
        '1387/4/12'
        '%Y/%m/%d'
        """
        valid_codes = {'%Y':(4, 'year'),
                       '%m':(2, 'month'),
                       '%d':(2, 'day')}
        
        return parse(cls, date_string, frmt, valid_codes)

        
    
    ########################
    ### Instance Methods ###
    ########################
    
    def to_julianday(self):
        return julian_day_from_jalali(self.year, self.month, self.day)
    
    def copy(self):
        return JalaliDate(self.year, self.month, self.day)
            
    def replace(self, year=None, month=None, day=None):
        result = self.copy()
        if year:
            result.year = year
        if month:
            result.month = month
        if day:
            result.day = day
        
        return result
    
    def to_date(self):
        arr = gregorian_date_from_julian_day(self.to_julianday())
        return date(int(arr[0]), int(arr[1]), int(arr[2]))
    
    def toordinal(self):
        raise NotImplementedError()
        
    def timetuple(self):
        raise NotImplementedError()
    
    def weekday(self):
        return self.to_date().weekday()

    
    def isoweekday(self):
        return self.weekday() + 1
    
    def isocalendar(self):
        return (self.year, self.month, self.day)
    
    def isoformat(self):
        return '%s-%s-%s' % (self.year, self.month, self.day)
    
    def __str__(self):
        return self.isoformat()
            
    def __repr__(self):
        return 'khayyam3.JalaliDate(%s, %s, %s)' % \
            (self.year, self.month, self.day)
    
    def strftime(self, frmt):
        """
=========    =======
Directive    Meaning
=========    =======
%a           Locale’s abbreviated weekday name.     
%A           Locale’s full weekday name.     
%b           Locale’s abbreviated month name.     
%B           Locale’s full month name.     
%d           Day of the month as a decimal number [01,31].     
%j           Day of the year as a decimal number [001,366].     
%m           Month as a decimal number [01,12].     
%U           Week number of the year (Sunday as the first day of the week) as a decimal number [00,53]. All days in a new year preceding the first Sunday are considered to be in week 0.    (4)
%w           Weekday as a decimal number [0(Sunday),6].     
%W           Week number of the year (Monday as the first day of the week) as a decimal number [00,53]. All days in a new year preceding the first Monday are considered to be in week 0.    (4)
%x           Locale’s appropriate date representation.     
%y           Year without century as a decimal number [00,99].     
%Y           Year with century as a decimal number.     
%%           A literal '%' character.
=========    =======
        """
        
        result = _replace_if_match(frmt, '%Y', self.year)
        result = _replace_if_match(result, '%y', lambda: str(self.year)[-2:])
        
        result = _replace_if_match(result, '%m', self.month)
        result = _replace_if_match(result, '%d', self.day)
        
        result = _replace_if_match(result, '%a', self.weekdayabbr)
        result = _replace_if_match(result, '%A', self.weekdayname)

        result = _replace_if_match(result, '%b', self.monthabbr)
        result = _replace_if_match(result, '%B', self.monthname)

        
        result = _replace_if_match(result, '%x', self.localformat)
        
        result = _replace_if_match(result, '%j', self.dayofyear)
        
        result = _replace_if_match(result, '%U', lambda: self.weekofyear(6))
        result = _replace_if_match(result, '%W', lambda: self.weekofyear(0))
        
        result = _replace_if_match(result, '%w', self.weekday)
        
        result = _replace_if_match(result, '%%', '%')
        
        return result
    
    def weekdayname(self):
        return PERSIAN_WEEKDAY_NAMES[self.weekday()]         

    def weekdayabbr(self):
        return PERSIAN_WEEKDAY_ABBRS[self.weekday()]
    
    def monthname(self):
        return PERSIAN_MONTH_NAMES[self.month]

    def monthabbr(self):
        return PERSIAN_MONTH_ABBRS[self.month]

    def localformat(self):
        return '%s %s %s %s' % (self.weekdayname(), self.day, self.monthname(), self.year)

    def dayofyear(self):
        return (self -JalaliDate(self.year, 1, 1)).days + 1
    
    def weekofyear(self, first_day_of_week):
        raise NotImplementedError()
        #return (self - JalaliDate(self.year,1,1)).days / 7
    
    #################
    ### Operators ###
    #################
        
    def __add__(self, x):
        if isinstance(x, timedelta):
            days = self.to_julianday() + x.days
            return JalaliDate.from_julian_days(days)
        
        raise ValueError('JalaliDate object can added by timedelta or JalaliDate object')
        
    def __sub__(self, x):
        if isinstance(x, timedelta):
            days = self.to_julianday() - x.days
            return JalaliDate.from_julian_days(days)
        elif isinstance(x, JalaliDate):
            days = self.to_julianday() - x.to_julianday()
            return timedelta(days=days)
        
        raise ValueError('JalaliDate object can added by timedelta or JalaliDate object')
    
    def __lt__(self, x):
        assert isinstance(x, JalaliDate), 'Comparison just allow with JalaliDate'
        return self.to_julianday() < x.to_julianday()
        
    def __le__(self, x):
        assert isinstance(x, JalaliDate), 'Comparison just allow with JalaliDate'
        return self.to_julianday() <= x.to_julianday()

    def __eq__(self, x):
        if not x:
            return False
        assert isinstance(x, JalaliDate), 'Comparison just allow with JalaliDate'
        return self.to_julianday() == x.to_julianday()
    
    def __ne__(self, x):
        assert isinstance(x, JalaliDate), 'Comparison just allow with JalaliDate'
        return self.to_julianday() <> x.to_julianday()
        
    def __gt__(self, x):
        assert isinstance(x, JalaliDate), 'Comparison just allow with JalaliDate'
        return self.to_julianday() > x.to_julianday()
    
    def __ge__(self, x):
        assert isinstance(x, JalaliDate), 'Comparison just allow with JalaliDate'
        return self.to_julianday() >= x.to_julianday()
    
    

## Class attributes
JalaliDate.min = JalaliDate(MINYEAR, 1, 1)
JalaliDate.max = JalaliDate(MAXYEAR, 12, 29)
JalaliDate.resolution = timedelta(days=1)

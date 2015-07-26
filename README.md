khayyam
=======

Jalali Date and Time types and algorithms for Python2 and Python3.

### Jump To:

 * [Documentation](http://khayyam.dobisel.com)
 * [Python package index](https://pypi.python.org/pypi/khayyam)
 * [Source on github](https://github.com/pylover/khayyam)


### Basic Usage

    >>> from khayyam import *
    >>> JalaliDate(1346, 12, 30)
    khayyam.JalaliDate(1346, 12, 30, Chaharshanbeh)
    
    >>> JalaliDatetime(989, 3, 25, 10, 43, 23, 345453)
    khayyam.JalaliDatetime(989, 3, 25, 10, 43, 23, 345453, Seshanbeh)

#### Current date and time

    >>> print(JalaliDatetime.now(TehranTimezone()) - timedelta(days=6*30))
    1393-11-02 20:01:11.663719+03:30
  
    >>> print(JalaliDate.today())
    1394-4-30
  

#### Parsing & Formatting
  
    >>> print(JalaliDatetime.now().strftime('%C'))
    شنبه ۳ مرداد ۱۳۹۴ ۰۲:۳۷:۵۲ ب.ظ
    
    >>> JalaliDatetime.strptime(u'چهارشنبه ۳۱ تیر ۱۳۹۴ ۰۵:۴۵:۴۰ ب.ظ', '%C')
    khayyam.JalaliDatetime(1394, 4, 31, 17, 45, 40, 0, Chaharshanbeh)

#### Converting

    >>> from datetime import date, datetime
    >>> JalaliDate(1394, 4, 31).todate()
    datetime.date(2015, 7, 22)
  
    >>> now = JalaliDatetime(1394, 4, 31, 15, 38, 6, 37269)
    >>> now.todate()
    datetime.date(2015, 7, 22)
  
    >>> now.todatetime()
    datetime.datetime(2015, 7, 22, 15, 38, 6, 37269)
  
    >>> JalaliDatetime.fromdatetime(datetime(2015, 7, 22, 14, 47, 9, 821830))
    khayyam.JalaliDatetime(1394, 4, 31, 14, 47, 9, 821830, Chaharshanbeh)
  
    >>> JalaliDatetime.fromdatetime(datetime(2015, 7, 22, 14, 47, 9, 821830, TehranTimezone()))
    khayyam.JalaliDatetime(1394, 4, 31, 14, 47, 9, 821830, tzinfo=+03:30±60, Chaharshanbeh)
  
    >>> JalaliDate.fromdate(date(2015, 7, 22))
    khayyam.JalaliDate(1394, 4, 31, Chaharshanbeh)

#### Arithmetics & Operators

    >>> from datetime import timedelta
    >>> from khayyam import JalaliDate, JalaliDatetime
    >>> now = JalaliDatetime(1394, 4, 31, 16, 17, 31, 374398)
    >>> now + timedelta(days=1)
    khayyam.JalaliDatetime(1394, 5, 1, 16, 17, 31, 374398, Panjshanbeh)
  
    >>> now + timedelta(seconds=3600)
    khayyam.JalaliDatetime(1394, 4, 31, 17, 17, 31, 374398, Chaharshanbeh)
  
    >>> now - timedelta(seconds=3600)
    khayyam.JalaliDatetime(1394, 4, 31, 15, 17, 31, 374398, Chaharshanbeh)
  
    >>> yesterday = now - timedelta(1)
    >>> yesterday
    khayyam.JalaliDatetime(1394, 4, 30, 16, 17, 31, 374398, Seshanbeh)
  
    >>> now - yesterday
    datetime.timedelta(1)
  
    >>> JalaliDatetime.now() - now
    datetime.timedelta(0, 478, 328833) # 478 seconds taken to writing this section


#### Comparison

    >>> now > yesterday
    True
  
    >>> now != yesterday
    True
  
    >>> now.todate() == yesterday.todate()
    False



### Change Log

  * 2.7.0-beta (2015-07-25)
    * some bug fixes.
    * method `Jalalidate.fromdate` removed. use constructor instead: `JalaliDate(date)`
    * method `Jalalidate.fromjulianday` removed. use constructor instead: `JalaliDate(julian_days=..)`
    * method `Jalalidate.fromdatetime` removed. use constructor instead: `JalaliDatetime(datetime)`

                                 
  * 2.6.0-beta (2015-07-25)
    * All possible formatting directives(a-z, A-Z) are supported, except: T
    * All format directives are tested.
    * Formatting and parsing test cases moved to `khayyam.formatting.tests` package.
    * In project: docs/html
    * `JalaliDate.from_julian_days` renamed to `JalaliDate.fromjuliandays`
    * `JalaliDate.from_julian_days` renamed to `JalaliDate.fromjuliandays`
    * `JalaliDate.days_in_month` renamed to `JalaliDate.daysinmonth`
    * `JalaliDate.is_leap` renamed to `JalaliDate.isleap`
    * `JalaliDatetime` Modern properties.
    * README.md updated
    
    

  * 2.5.0-beta (2015-07-23)
    * Doc: doctest
    * Doc: formatting and parsing directives table.
    * Doc: adding examples of new formatting directives in introduction: %D, %J, %R, %N, %n, %F, %h, %i, %r, %s, %o.
    * local date & time formats are changed: digits -> persian
    * Formatting and parsing test cases has been separated

  * 2.4.0-beta (2015-07-22)
    * Persian Numbers
    * %D, %J, %R, %N, %n, %F, %h, %i, %r, %s, %o directives has been added.

  * 2.3.0-alpha (2015-07-22)
    * Constants are moved to formatting packages except MINYEAR, MAXYEAR ans weekdays.
    * Doc: Introduction -> Formatting & parsing
    * Doc: Introduction -> Converting
    * New methods `jalaliDate.todate`, `jalaliDate.fromdate`, `jalaliDatetime.todatetime` and `jalaliDatetimefromdatetime`
    * Removed methods `jalaliDate.to_date`, `jalaliDate.from_date`, `jalaliDatetime.to_datetime` and `jalaliDatetime.fromdate_time`
    

  * 2.2.1-alpha (2015-07-21)
    * Doc: Reading package's version automatically from khayyam/__init__.py in `sphinx/conf.py`
    * Doc: Installation: (PYPI, Development version)
    * Doc: Testing
    * Doc: Contribution

  * 2.2.0-alpha (2015-07-21)
    * Generating API Documentation  

  * 2.1.0-alpha (2015-07-20)
    * Adding ascii weekdayname in `JalaliDatetime` and `JalaliDate` representation(__repr__). 

  * 2.0.0-alpha (2015-07-19) Incompatible with < 2.0.0
    * JalaliDate: method `localformat` renamed to `localdateformat`.
    * JalaliDatetime: method `localformat` renamed to `localdatetimeformat`.
    * JalaliDatetime: method `localshortformat_ascii` renamed to `localshortformatascii`.
    * JalaliDatetime: method `localdatetimeformat_ascii` renamed to `localdatetimeformatascii`.
    * JalaliDatetime: method `ampm_ascii` renamed to `ampmascii`.
    * JalaliDatetime: Migrating to New Formatter/Parser Engine
    * TehTz: renamed to TehranTimezone
    * Comparison and Timezones
    * Comparison with `datetime.date` & `datetime.datetime`
    * Fixing timezone bug
    
  * 1.1.0 (2015-07-17)
    * JalaliDate: New Formatter/Parser & full unittests.
    
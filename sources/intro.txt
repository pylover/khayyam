Introduction
============

Basic Usage
-----------

Importing
^^^^^^^^^
::

  from khayyam import *

This will imports
:py:class:`khayyam.JalaliDate`,
:py:class:`khayyam.JalaliDatetime`,
:py:class:`khayyam.Timezone`,
:py:class:`khayyam.TehranTimezone`,
:py:obj:`khayyam.MINYEAR`,
:py:obj:`khayyam.MAXYEAR`,
:py:obj:`khayyam.SATURDAY`,
:py:obj:`khayyam.SUNDAY`,
:py:obj:`khayyam.MONDAY`,
:py:obj:`khayyam.THURSDAY`,
:py:obj:`khayyam.WEDNESDAY`,
:py:obj:`khayyam.TUESDAY`,
:py:obj:`khayyam.FRIDAY`


Current date and time
^^^^^^^^^^^^^^^^^^^^^

::

  >>> JalaliDatetime.now()
  khayyam.JalaliDatetime(1394, 4, 30, 20, 49, 55, 205834, Seshanbeh)

  >>> print(JalaliDatetime.now())
  1394-04-30 20:56:20.991585

DST aware::

  >>> print(JalaliDatetime.now(TehranTimezone()))
  1394-04-30 19:59:12.935506+04:30

  >>> print(JalaliDatetime.now(TehranTimezone()) - timedelta(days=6*30))
  1393-11-02 20:01:11.663719+03:30

As you see, the DST offset in the second statement is `+3:30`. so
the :py:class:`khayyam.TehranTimezone` is supporting `daylight saving time` properly.

Today::

  >>> JalaliDate.today()
  khayyam.JalaliDate(1394, 4, 30, Seshanbeh)

  >>> print(JalaliDate.today())
  1394-4-30

  >>> print JalaliDate.today().strftime('%A %d %B %Y')
  چهارشنبه 31 تیر 1394


Right-to-left
^^^^^^^^^^^^^

Additionally, if right to left text rendering is not supported by your terminal
emulator, you can install the rtl package::


  $ pip install rtl

And then use it to reshape and change direction of the text::

  >>> from rtl import rtl
  >>> print(rtl(JalaliDatetime.now().strftime('%C')))
  'چهارشنبه 31 تیر 1394 02:10:30 ب.ظ'

rprint() function
^^^^^^^^^^^^^^^^^

If you are using python2 its good to import new print function::

  >>>from __future__ import print_function


Extending your practice environment by defining a handy print function for RTL::

  >>> def rprint(s):
  ...     print(rtl(s))

  >>> rprint(JalaliDatetime.now().strftime('%C'))
  چهارشنبه 31 تیر 1394 02:10:30 ب.ظ

Formatting & Parsing
--------------------

All format directives supported by python's native :ref:`strftime-strptime-behavior` are covered by this library, plus:

=========     =======
Directive     Meaning
=========     =======
%e	          ASCII Locale’s abbreviated weekday name.
%E	          ASCII Locale’s full weekday name.
%g	          ASCII Locale’s abbreviated month name.
%G	          ASCII Locale’s full month name.
%C	          Locale’s appropriate date and time representation.
%q	          ASCII Locale’s appropriate short date and time representation.
%Q	          ASCII Locale’s appropriate date and time representation.
=========     =======

All format directives are documented in :py:meth:`khayyam.JalaliDate.strftime`

To format locale's date & time::

  >>> from khayyam import JalaliDatetime
  >>> time_string = JalaliDatetime.now().strftime('%C')
  >>> print(time_string)
  'چهارشنبه 31 تیر 1394 02:10:30 ب.ظ'

And parsing it again to a :py:class:`khayyam.JalaliDatetime` instance::

  >>> JalaliDatetime.strptime(time_string, '%C')
  khayyam.JalaliDatetime(1394, 4, 31, 14, 10, 30, 0, Chaharshanbeh)


You may use `%f` and or `%z` formatting directives to represent
microseconds and timezone info in your formatting or parsing pattern.

So, to reach accurate serialization, you could include those two
directive alongside time and date directives in your pattern. for example::

  >>> from datetime import timedelta
  >>> from khayyam import Timezone
  >>> tz = Timezone(timedelta(seconds=60*210)) # +3:30 Tehran
  >>> now_string = JalaliDatetime.now(tz).strftime('%Y-%m-%d %H:%M:%S.%f %z')
  >>> print(now_string)
  1394-04-31 14:10:21.452958 +03:30

Parse it back to the :py:class:`khayyam.JalaliDatetime` instance::

  >>> now = JalaliDatetime.strptime(now_string, '%Y-%m-%d %H:%M:%S.%f %z')
  >>> repr(now)
  khayyam.JalaliDatetime(1394, 4, 31, 14, 10, 21, 452958, tzinfo=+03:30, Chaharshanbeh)


Try some formatting and parsing directives::

  >>> now = JalaliDatetime.now()
  >>> rprint(now.strftime('%a %d %B %y'))
  چ 31 تیر 94

  >>> rprint(now.strftime('%A %d %b %Y'))
  چهارشنبه 31 تی 1394

  >>> from khayyam import TehranTimezone
  >>> rprint(now.astimezone(TehranTimezone()).strftime('%A %d %B %Y %Z'))
  چهارشنبه 31 تیر 1394 Iran/Tehran

Converting
----------

Converting to gregorian calendar, python's native
:py:class:`datetime.date` and :py:class:`datetime.datetime`::

  >>> from datetime import date, datetime
  >>> from khayyam import JalaliDate, JalaliDatetime, TehranTimezone

  >>> JalaliDate.today().todate()
  datetime.date(2015, 7, 22)

  >>> now = JalaliDatetime.now()
  >>> now.todate()
  datetime.date(2015, 7, 22)

  >>> now.todatetime()
  datetime.datetime(2015, 7, 22, 15, 38, 6, 37269)

And vise-versa::

  >>> JalaliDatetime.fromdatetime(datetime.now())
  khayyam.JalaliDatetime(1394, 4, 31, 15, 44, 11, 934253, Chaharshanbeh)

  >>> JalaliDatetime.from_datetime(datetime.now(TehranTimezone()))
  khayyam.JalaliDatetime(1394, 4, 31, 14, 47, 9, 821830, tzinfo=+03:30±60, Chaharshanbeh)

  >>> JalaliDate.from_date(date.today())
  khayyam.JalaliDate(1394, 4, 31, Chaharshanbeh)


..
  Overview
  ========


  To convert a jalali datetime to python's standard datetime::

     In [1]: import khayyam

     In [2]: khayyam.JalaliDatetime.now().to_datetime()
     Out[2]: datetime.datetime(2012, 4, 14, 1, 21, 8, 842241)

     In [3]: khayyam.JalaliDate.today().to_date()
     Out[3]: datetime.date(2012, 4, 14)

  To create jalali datetime from python's standard datetime::

     In [1]: import khayyam,datetime

     In [2]: now = datetime.datetime.now()

     In [3]: jalali_now = khayyam.JalaliDatetime.from_datetime(now)

     In [4]: print jalali_now
     1391-1-26T1:31:10.34972

  To format you can use the native python's `datetime.strftime`_ function::

     In [1]: import khayyam

     In [2]: now = khayyam.JalaliDatetime.now()

     In [3]: print now.strftime("%Y-%m-%d %H:%M:%S")
     1391-1-26 1:26:28

     In [4]: print now.strftime("%C")
     شنبه 26 فروردین 1391 1:26:28 ق.ظ

     In [5]: print now.strftime("%c")
     ش 26 فر 91 1:26

  Using timezone::

     In [1]: import khayyam

     In [2]: now = khayyam.JalaliDatetime.now(khayyam.teh_tz)

     In [3]: now
     Out[3]: khayyam.JalaliDatetime(1391, 1, 26, 1, 32, 49, 108209, tzinfo=<khayyam.tehran_timezone.TehTz object at 0x8a6812c>)

     In [4]: now.dst()
     Out[4]: datetime.timedelta(0, 3600)

     In [5]: now.tzinfo
     Out[5]: <khayyam.tehran_timezone.TehTz object at 0x8a6812c>


  .. _datetime.strftime: http://docs.python.org/library/datetime.html#strftime-and-strptime-behavior
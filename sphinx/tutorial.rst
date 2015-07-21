Tutorial
========

To find current date and time you use following statements::
   
   In [1]: import khayyam

   In [2]: print khayyam.JalaliDatetime.now()
   1391-1-26T1:16:36.397590
   
   In [3]: khayyam.JalaliDatetime.now()
   Out[3]: khayyam.JalaliDatetime(1391, 1, 26, 1, 16, 43, 991857)
   
   In [4]: khayyam.JalaliDate.today()
   Out[4]: khayyam.JalaliDate(1391, 1, 26)
   
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
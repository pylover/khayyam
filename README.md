khayyam
=======

Jalali Date and Time types and algorithms for Python2 and Python3.



### To Do

  * Naming conventions
  * Constructors act as converter: `JalaliDate(date)`
  * Create TehranDatetime object
  * Add two methods: d.next(SATURDAY) & d.previous(WEDNESDAY)
  * Use compiled regex if matters in performance
  * Readme:
    * Installation: (PYPI, Development version)
    * Testing
    * Parsing, post processors priority
    * Formatting
    * Conversions
    * Operators
    * Compatibility
    * Contribution
  * API-Doc
    * Fetch version automatically from khayyam/__init__.py
    * Add custom page into doc-site 
  * Cython
    * setup.py pure python fallback switch
    * Distribute pre compiled binaries from some platforms
  * Alphabetical number format

### Change Log

  * 2.2.0-alpha (2015-07-21)
    * Generating Document, ShowSource 

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
    
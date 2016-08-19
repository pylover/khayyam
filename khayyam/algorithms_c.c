
#include <Python.h>
#include <stdio.h>
#include <math.h>


typedef int Error;


typedef int Boolean;
#define TRUE 1
#define FALSE 0


/*
Internal function, simulating pythons mod operator.
*/
#define mod(a,b) ((((a)%(b))+(b))%(b))


/*
The round function is not available on microsoft C++ prior to MSVC++ 12.0.
*/
#if defined _MSC_VER && _MSC_VER < 1800
double round(double d)
{
  return floor(d + 0.5);
}
#endif


/*
Internal function, pythons integer division.
*/
static int pythonLikeIntegerDivision(int a, int b){
    if ( a < 0 ){
        return (int)floor((float)a / b);
    }
    return a / b;
}


static Error getJulianDayFromGregorianDate(int year, int month, int day, double *julianDay){
    Boolean y4Cond, y100Cond, y400Cond, isLeap;
    double century, y4, y100, y400, yearDouble;
    char *exceptionMessage;

    /*
    Determining leap year
    */
    y4 = (double)year / 4.0;
    y100 = (double)year / 100.0;
    y400 = (double)year / 400.0;
    y4Cond = y4 == round(y4);
    y100Cond = y100 == round(y100);
    y400Cond = y400 == round(y400);
    isLeap = y4Cond && ( (y100Cond && y400Cond) || (! y100Cond) );

    /*
    Validating the day
    */
    if ( (month == 2) && ( day > (isLeap ? 29 : 28) ) ) {
        exceptionMessage = (char*) PyMem_Malloc(33 * sizeof(char));
        sprintf(exceptionMessage, "Invalid day: %02d, it must be <= %02d", day, (isLeap ? 29 : 28));
        PyErr_SetString(PyExc_ValueError, exceptionMessage);
        PyMem_Free(exceptionMessage);
        return -1;
    }

    /*
    Correcting year and month based on month
    */
    if (month <= 2){
        year -= 1;
        month += 12;
    }
    yearDouble = (double)year;

    /*
    Finding the century
    */
    century = floor(yearDouble / 100.0);

    /*
    Calculating the result
    */
    *julianDay =
        floor(365.25 * ( yearDouble + 4716.0)) +
        floor(30.6001 * ( (double)month + 1.0)) +
        (double)day +
        (2 - century + floor(century / 4.0)) - 1524.5;

    return 0;

}


static Boolean isJalaliLeapYear(int year){
    int a = mod(year - (year > 0 ? 474 : 473), 2820) + 474 + 38;
    return mod(a * 682, 2816) < 682;
}


static int getDaysInJalaliYear(int year){

    return isJalaliLeapYear(year) ? 366 : 365;
}


static Error getDaysInJalaliMonth(int year, int month, int *days){
    if ( (1 <= month) && (month <= 6) ){
        *days = 31;
    }
    else if ( (7 <= month) && (month < 12) ){
        *days = 30;
    }
    else if ( month == 12 ){ // Esfand
        *days = isJalaliLeapYear(year) ? 30 : 29;
    }
    else{
        PyErr_SetString(PyExc_ValueError, "Month must be between 1 and 12");
        return -1;
    }
    return 0;
}


static double getJulianDayFromJalaliDate(int year, int month, int day){
    int base = year - (year >= 0 ? 474 : 473);
    int julianYear = 474 + mod(base, 2820);
    return
        day +
        ( (month <= 7) ? (month - 1) * 31 : ((month - 1) * 30) + 6) +
        ((julianYear * 682) - 110) / 2816 +
        (julianYear - 1) * 365 +
        pythonLikeIntegerDivision(base, 2820) * 1029983 +
        (1948320.5 - 1);
}


static void getJalaliDateFromJulianDay(double julianDay, int *year, int *month, int *day){
    double offset, cycle, daysInYears;
    int remaining, yearCycle, a1, a2;

    julianDay = floor(julianDay) + 0.5;

    // get_julianDay_from_jalali_date(475, 1, 1) replaced by its static value
    offset = julianDay - 2121445.5;

    cycle = floor(offset / 1029983);
    remaining = mod((int)offset, 1029983);

    if ( remaining == 1029982){
        yearCycle = 2820;
    }
    else{
        a1 = (int) floor(remaining / 366);
        a2 = (int) mod(remaining, 366);
        yearCycle = (int)floor(( 2134*a1 + 2816*a2 + 2815) / 1028522) + a1 + 1;
    }

    *year = (int)(yearCycle + 2820*cycle + 474);

    if ( *year <= 0 ){
        *year -= 1;
    }

    daysInYears = (julianDay - getJulianDayFromJalaliDate(*year, 1, 1)) + 1;
    *month = (int) ceil(daysInYears <= 186 ? daysInYears / 31 : (daysInYears - 6) / 30);
    *day = (int) (julianDay - getJulianDayFromJalaliDate(*year, *month, 1)) + 1;

}


static Error getGregorianDateFromJulianDay(double julianDay, int *year, int *month, int *day){
    double jdm, z, f, alpha, b, c, a, e, d,
        y = 0,
        m = 0;

    if ( julianDay <= 0 ){
        PyErr_SetString(PyExc_ValueError, "Invalid Date");
        return -1;
    }

    jdm = julianDay + 0.5;
    z = floor(jdm);
    f = jdm - z;
    alpha = floor((z - 1867216.25) / 36524.25);
    b = (z + 1 + alpha - floor(alpha / 4)) + 1524;
    c = floor((b - 122.1) / 365.25);
    a = floor(365.25 * c);
    e = floor((b - a) / 30.6001);
    d = b - a - floor(30.6001 * e) + f;

    if (e < 14)
        m = e - 1;
    else if (e == 14 || e == 15)
        m = e - 13;


    if (m > 2)
        y = c - 4716;
    else if (m == 1 || m == 2)
        y = c - 4715;


    *year = (int) y;
    *month = (int) m;
    *day = (int) d;

    return 0;
}


/* ################################## Python ################################################### */


static PyObject * createPythonDateTuple(int year, int month, int day){
    PyObject *t = PyTuple_New(3);

    #if PY_MAJOR_VERSION >= 3
        PyTuple_SetItem(t, 0, PyLong_FromLong(year));
        PyTuple_SetItem(t, 1, PyLong_FromLong(month));
        PyTuple_SetItem(t, 2, PyLong_FromLong(day));
    #else
        PyTuple_SetItem(t, 0, PyInt_FromLong(year));
        PyTuple_SetItem(t, 1, PyInt_FromLong(month));
        PyTuple_SetItem(t, 2, PyInt_FromLong(day));
    #endif

    return t;
}


static PyObject * get_julian_day_from_gregorian_date(PyObject *self, PyObject *args){
    double julianDay;
    int year, month, day;
    Error err;

    if (!PyArg_ParseTuple(args, "iii", &year, &month, &day)){
        return NULL;
    }

    err = getJulianDayFromGregorianDate(year, month, day, &julianDay);

    /*
    Catch exception if any
    */
    if (err != 0){
        return NULL;
    }

    return PyFloat_FromDouble(julianDay);
}


static PyObject * is_jalali_leap_year(PyObject *self, PyObject *args){
    int year;

    if (!PyArg_ParseTuple(args, "i", &year)){
        return NULL;
    }

    return PyBool_FromLong(isJalaliLeapYear(year));
}


static PyObject * get_days_in_jalali_year(PyObject *self, PyObject *args){
    int year;

    if (!PyArg_ParseTuple(args, "i", &year)){
        return NULL;
    }

    return PyLong_FromLong(getDaysInJalaliYear(year));
}


static PyObject * get_days_in_jalali_month(PyObject *self, PyObject *args){
    int year, month, result;
    Error err;

    if (!PyArg_ParseTuple(args, "ii", &year, &month)){
        return NULL;
    }

    err = getDaysInJalaliMonth(year, month, &result);

    /*
    Catch exception if any
    */
    if (err != 0){
        return NULL;
    }

    return PyLong_FromLong(result);
}


static PyObject * get_julian_day_from_jalali_date(PyObject *self, PyObject *args){
    double julianDay;
    int year, month, day;

    if (!PyArg_ParseTuple(args, "iii", &year, &month, &day)){
        return NULL;
    }

    julianDay = getJulianDayFromJalaliDate(year, month, day);

    return PyFloat_FromDouble(julianDay);
}


static PyObject * get_jalali_date_from_julian_day(PyObject *self, PyObject *args){
    float julianDay;
    int year, month, day;

    if (!PyArg_ParseTuple(args, "f", &julianDay)){
        return NULL;
    }

    getJalaliDateFromJulianDay(julianDay, &year, &month, &day);

    return createPythonDateTuple(year, month, day);
}


static PyObject * get_gregorian_date_from_julian_day(PyObject *self, PyObject *args){
    float julianDay;
    int year, month, day;
    Error err;

    if (!PyArg_ParseTuple(args, "f", &julianDay)){
        return NULL;
    }

    err = getGregorianDateFromJulianDay(julianDay, &year, &month, &day);
    /*
    Catch exception if any
    */
    if (err != 0){
        return NULL;
    }

    return createPythonDateTuple(year, month, day);
}


static PyObject *  get_jalali_date_from_gregorian_date(PyObject *self, PyObject *args){
    int gYear, gMonth, gDay, jYear, jMonth, jDay;
    double julianDay;
    Error err;

    if (!PyArg_ParseTuple(args, "iii", &gYear, &gMonth, &gDay)){
        return NULL;
    }

    err = getJulianDayFromGregorianDate(gYear, gMonth, gDay, &julianDay);

    if ( err != 0){
        return NULL;
    }

    getJalaliDateFromJulianDay(julianDay, &jYear, &jMonth, &jDay);

    return createPythonDateTuple(jYear, jMonth, jDay);
}


static PyMethodDef moduleFunctions[] = {

    {
        "get_julian_day_from_gregorian_date",
        get_julian_day_from_gregorian_date,
        METH_VARARGS,
        "Gets julian day from gregorian date."
    },

    {
        "is_jalali_leap_year",
        is_jalali_leap_year,
        METH_VARARGS,
        "Determines the jalali year is leap or not."
    },

    {
        "get_days_in_jalali_year",
        get_days_in_jalali_year,
        METH_VARARGS,
        "Determines the number of days in jalali year."
    },

    {
        "get_days_in_jalali_month",
        get_days_in_jalali_month,
        METH_VARARGS,
        "Determines the number of days in jalali month."
    },

    {
        "get_julian_day_from_jalali_date",
        get_julian_day_from_jalali_date,
        METH_VARARGS,
        "Gets julian day from jalali date."
    },

    {
        "get_jalali_date_from_julian_day",
        get_jalali_date_from_julian_day,
        METH_VARARGS,
        "Gets jalali date from julian day."
    },

    {
        "get_gregorian_date_from_julian_day",
        get_gregorian_date_from_julian_day,
        METH_VARARGS,
        "Gets gregorian date from julian day."
    },

    {
        "get_jalali_date_from_gregorian_date",
        get_jalali_date_from_gregorian_date,
        METH_VARARGS,
        "Gets jalali date from gregorian date."
    },

    {NULL, NULL, 0, NULL}        /* Sentinel */
};


#if PY_MAJOR_VERSION >= 3
  #define MOD_ERROR_VAL NULL
  #define MOD_SUCCESS_VAL(val) val
  #define MOD_INIT(name) PyMODINIT_FUNC PyInit_##name(void)
  #define MOD_DEF(ob, name, doc, methods) \
          static struct PyModuleDef moduledef = { \
            PyModuleDef_HEAD_INIT, name, doc, -1, methods, }; \
          ob = PyModule_Create(&moduledef);
#else
  #define MOD_ERROR_VAL
  #define MOD_SUCCESS_VAL(val)
  #define MOD_INIT(name) PyMODINIT_FUNC init##name(void)
  #define MOD_DEF(ob, name, doc, methods) \
          ob = Py_InitModule3(name, methods, doc);
#endif


MOD_INIT(algorithms_c)
{
    PyObject *m;

    MOD_DEF(m, "algorithms_c", "Khayyam algorithms C implementation.", moduleFunctions);

    if (m == NULL)
        return MOD_ERROR_VAL;

    return MOD_SUCCESS_VAL(m);

}

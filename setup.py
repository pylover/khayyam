# -*- coding: utf-8 -*-
import os
import re
import warnings
from setuptools import setup, find_packages, Extension
import traceback
__author__ = 'vahid'

# reading package version (same way sqlalchemy does)
with open(os.path.join(os.path.dirname(__file__), 'khayyam', '__init__.py')) as v_file:
    package_version = re.compile(r".*__version__ = '(.*?)'", re.S).match(v_file.read()).group(1)

setup_args = dict(
    name="Khayyam",
    version=package_version,
    author="Vahid Mardani",
    author_email="vahid.mardani@gmail.com",
    url="http://khayyam.dobisel.com",
    description="A cythonic and fast Persian Date & Time library (aka: Jalali Calendar) with timezone, DST"
                "(daylight-saving), full formatting & parsing support for python 2 & 3.",
    zip_safe=True,
    keywords="Khayyam persian jalali date time datetime conversion",
    long_description=open(os.path.join(os.path.dirname(__file__), 'README.rst')).read(),
    license="GPLv3",
    packages=find_packages(),
    test_suite="khayyam.tests",
    tests_require=[
        'rtl'
    ],
    classifiers=[
        "Programming Language :: Python",
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        "Intended Audience :: Developers",
        "Natural Language :: Persian",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Software Development :: Localization"],
)


def run_setup(with_extensions=True):
    if with_extensions:
        try:
            from Cython.Build import cythonize
            print('Using Cython to build the extensions.')
            USE_CYTHON = True
        except ImportError:
            USE_CYTHON = False
            warnings.warn('Not using Cython to build the extensions.')

        extensions = [
            Extension("khayyam.algorithms_c",
                      sources=["khayyam/algorithms_c%s" % ('.pyx' if USE_CYTHON else '.c')],
                      libraries=["m"]  # Unix-like specific
                      )
        ]

        if USE_CYTHON:
            extensions = cythonize(extensions)

        setup_args['ext_modules'] = extensions

    if not with_extensions:

        del setup_args['ext_modules']

    setup(**setup_args)


try:
    run_setup()
except Exception as ex:
    traceback.print_exc()
    BUILD_EXT_WARNING = ("WARNING: The C extension could not be compiled, "
                         "speedups are not enabled.")
    print('*' * 75)
    print(BUILD_EXT_WARNING)
    print("Failure information, if any, is above.")
    print("I'm retrying the build without the C extension now.")
    print('*' * 75)

    run_setup(False)

    print('*' * 75)
    print(BUILD_EXT_WARNING)
    print("Plain-Python installation succeeded.")
    print('*' * 75)


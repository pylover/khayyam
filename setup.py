# -*- coding: utf-8 -*-
import os
import re
import sys
import warnings
from setuptools import setup, find_packages, Extension
import traceback

__author__ = 'vahid'

# reading package version (same way sqlalchemy does)
with open(os.path.join(os.path.dirname(__file__), 'khayyam', '__init__.py')) as v_file:
    package_version = re.compile(r".*__version__ = '(.*?)'", re.S).match(v_file.read()).group(1)

if sys.version_info >= (3, ):
    def readme(fn):
        with open(fn, encoding='UTF-8') as f:
            return f.read()
else:
    def readme(fn):
        with open(fn) as f:
            return f.read()


setup_args = dict(
    name="Khayyam",
    version=package_version,
    author="Vahid Mardani",
    author_email="vahid.mardani@gmail.com",
    url="http://khayyam.dobisel.com",
    description="Persian Date & Time library (aka: Jalali Calendar) with timezone, DST"
                "(daylight-saving), full formatting & parsing support for python 2 & 3 including c extention",
    zip_safe=True,
    keywords="Khayyam persian jalali date time datetime conversion",
    long_description=readme(os.path.join(os.path.dirname(__file__), 'README.rst')),
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
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        "Intended Audience :: Developers",
        "Natural Language :: Persian",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Software Development :: Localization"
    ],
)


def run_setup(with_extensions=True):
    if with_extensions:

        setup_args['ext_modules'] = [
            Extension(
                "khayyam.algorithms_c",
                sources=["khayyam/algorithms_c.c"]
            )
        ]

    elif 'ext_modules' in setup_args:
        del setup_args['ext_modules']

    setup(**setup_args)


def warning_c_extention():
    warnings.warn(
        '\n%s\n%s\n%s' % (
            '#' * 40,
            "WARNING: The C extension could not be compiled.\n"
            "WARNING: Speedups are not enabled.",
            '#' * 40
        ))


try:
    run_setup()

# noinspection PyBroadException
except:
    traceback.print_exc()
    warning_c_extention()
    run_setup(with_extensions=False)
    warning_c_extention()

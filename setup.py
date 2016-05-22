# -*- coding: utf-8 -*-
import os
import re
import sys
import warnings
import platform
from setuptools import setup, find_packages, Extension
import traceback
__author__ = 'vahid'


# reading package version (same way sqlalchemy does)
with open(os.path.join(os.path.dirname(__file__), 'khayyam', '__init__.py')) as v_file:
    package_version = re.compile(r".*__version__ = '(.*?)'", re.S).match(v_file.read()).group(1)


if sys.version_info.major == 3:
    def readme(fn):
        with open(fn, encoding='UTF-8') as f:
            return f.read()
else:
    def readme(fn):
        with open(fn) as f:
            return f.read()


WARNING_HEADER = '#' * 40


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
            # noinspection PyPackageRequirements
            from Cython.Build import cythonize
            print('Using Cython to build the extensions.')
            use_cython = True
        except ImportError:
            use_cython = False

            # noinspection PyUnusedLocal
            def cythonize(*a, **kw):
                raise ImportError('Cython is not installed.')

            warnings.warn(
                '\n%s\nNot using Cython to build the extensions.\nUsing available C compiler instead.\n%s' % (
                    WARNING_HEADER, WARNING_HEADER
                ))

        libraries = []

        if platform.system() != 'Windows':
            libraries.append('m')  # Unix-like specific

        extensions = [
            Extension("khayyam.algorithms_c",
                      sources=["khayyam/algorithms_c%s" % ('.pyx' if use_cython else '.c')],
                      libraries=libraries
                      )
        ]

        if use_cython:
            extensions = cythonize(extensions)

        setup_args['ext_modules'] = extensions

    if not with_extensions and 'ext_modules' in setup_args:
        del setup_args['ext_modules']

    setup(**setup_args)


def warning_c_extention():
    warnings.warn(
        '\n%s\n%s\n%s' % (
            WARNING_HEADER,
            "WARNING: The C extension could not be compiled.\n"
            "WARNING: Speedups are not enabled.",
            WARNING_HEADER
        ))


try:
    run_setup()

# noinspection PyBroadException
except:
    traceback.print_exc()
    warning_c_extention()
    run_setup(False)
    warning_c_extention()

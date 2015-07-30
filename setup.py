# -*- coding: utf-8 -*-
import os
import re
from setuptools import setup, find_packages, Extension
from Cython.Build import cythonize

__author__ = 'vahid'

# reading package version (same way sqlalchemy does)
with open(os.path.join(os.path.dirname(__file__), 'khayyam', '__init__.py')) as v_file:
    package_version = re.compile(r".*__version__ = '(.*?)'", re.S).match(v_file.read()).group(1)


ext_modules = [
    Extension("khayyam.algorithms_c",
              sources=["khayyam/algorithms_c.pyx"],
              libraries=["m"]  # Unix-like specific
              )
]

setup(
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
    ext_modules=cythonize(ext_modules),
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

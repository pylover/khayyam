'''
Created on Jan 15, 2011

@author: vahid
'''
import os
from setuptools import setup, find_packages
 

import re

# reading package version (same way sqlalchemy does)
with open(os.path.join(os.path.dirname(__file__),'khayyam', '__init__.py')) as v_file:
    package_version = re.compile(r".*__version__ = '(.*?)'",re.S).match(v_file.read()).group(1)


setup(
    name="Khayyam",
    version=package_version,
    packages=find_packages(),
    author="Vahid Mardani",
    author_email="vahid.mardani@gmail.com",
    url="https://github.com/pylover/khayyam",
    description="Khayyam(Jalali Persian Datetime) library",
    zip_safe=True,
    keywords="Khayyam persian jalali date time datetime conversion",
    long_description=open(os.path.join(os.path.dirname(__file__), 'README.txt')).read(),
    classifiers=[
        "Programming Language :: Python",
        "Development Status :: 5 - Production/Stable",                 
        "License :: Freeware",
        "Operating System :: OS Independent",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Software Development :: Localization"],
    use_2to3 = True
)

# -*- coding: utf-8 -*-
import sys
from os import mkdir
from os.path import join, dirname, exists, basename
from sphinx.ext.intersphinx import fetch_inventory
import warnings
__author__ = 'vahid'

this_dir = dirname(__file__)
cache_dir = join(this_dir, '_inv-cache')

if not exists(cache_dir):
    mkdir(cache_dir)


def make_cache(name, uri):
    dest_dir = join(cache_dir, name)
    if not exists(dest_dir):
        mkdir(dest_dir)
    inv = fetch_inventory(warnings, uri, join(uri, 'objects.inv'))
    for k, v in inv.items():
        filename = join(dest_dir, k.replace(':', '-'))
        line_counter = 0
        with open(filename, 'w+') as f:
            for sk, sv in v.items():
                line_counter +=1
                if line_counter % 100 == 0:
                    print('File: %s, Line: %s' % (basename(filename), line_counter))
                f.write('%s\t%s\n' % (sk, sv))


if __name__ == '__main__':
    make_cache('python3', 'https://docs.python.org/3')
    make_cache('python2', 'https://docs.python.org/2')
    print('done')
    sys.exit(0)




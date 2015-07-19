# -*- coding: utf-8 -*-
import re
__author__ = 'vahid'


for i in range(0, 61):
    p = '^([0]?\d|[1-5]\d)$'

    try:
        if int(re.match(p, '%d' % i).group()) != i: print(i)
    except AttributeError:
        print('Error: %d' % i)

    try:
        if int(re.match(p, '%.2d' % i).group()) != i: print(i)
    except AttributeError:
        print('Error: %.2d' % i)

    # try:
    #     if int(re.match(p, '%.3d' % i).group()) != i: print('%.3d' % i)
    # except AttributeError:
    #     print('Error: %.3d' % i)

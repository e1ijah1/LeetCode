# -*- coding: utf-8 -*-
# Created by f1renze on 2019-02-14 00:35
__author__ = 'f1renze'
__time__ = '2019-02-14 00:35'

import os


def disk_usage(path):
    total = os.path.getsize(path)
    if os.path.isdir(path):
        for filename in os.listdir(path):
            childpath = os.path.join(path, filename)
            total += disk_usage(childpath)
    print('{0: <7}'.format(total), path)
    return total


if __name__ == '__main__':
    pass

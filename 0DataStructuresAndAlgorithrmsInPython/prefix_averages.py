# -*- coding: utf-8 -*-
# Created by f1renze on 2019-02-12 23:31
__author__ = 'f1renze'
__time__ = '2019-02-12 23:31'

"""
前缀平均值
"""


def prefix_average1(s):
    n = len(s)
    a = [0] * n
    for j in range(n):
        # 前 1 ~ n 个数的平均值
        total = 0
        for i in range(j + 1):
            total += s[i]
        a[j] = total // (j + 1)
    return a


def prefix_average2(s):
    """
    1 的简写形式
    :param s:
    :return:
    """
    n = len(s)
    a = [0] * n
    for j in range(n):
        a[j] = sum(s[0: j+1]) // (j + 1)
    return a


def prefix_average3(s):
    n = len(s)
    a = [0] * n
    total = 0
    for j in range(n):
        total += s[j]
        a[j] = total // (j+1)
    return a


if __name__ == '__main__':
    l = [12, 14, 13, 15, 19, 17, 16, 11, 18, 20]
    print(
        # [12, 13, 13, 13, 14, 15, 15, 14, 15, 15]
        prefix_average3(l)
    )

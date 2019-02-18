# -*- coding: utf-8 -*-
# Created by f1renze on 2019-02-18 23:01
__author__ = 'f1renze'
__time__ = '2019-02-18 23:01'


def reverse(S, start, stop):
    """
    start == stop 隐含范围为空
    start == stop -1 隐含范围仅有一个元素
    :param S:
    :param start:
    :param stop:
    :return:
    """
    if start < stop -1:
        S[start], S[stop-1] = S[stop-1], S[start]
        reverse(S, start+1, stop-1)


if __name__ == '__main__':
    pass

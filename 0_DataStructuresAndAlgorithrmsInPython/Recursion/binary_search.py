# -*- coding: utf-8 -*-
# Created by f1renze on 2019-02-14 00:30
__author__ = 'f1renze'
__time__ = '2019-02-14 00:30'


def binary_search(data, target, low, high):
    """

    :param data:
    :param target:
    :param low:
    :param high:
    :return:
    """
    if low > high:
        return False
    mid = (low + high // 2)
    if target == data[mid]:
        return True
    elif target < data[mid]:
        return binary_search(data, target, low, mid - 1)
    else:
        return binary_search(data, target, mid + 1, high)


if __name__ == '__main__':
    pass

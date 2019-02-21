# -*- coding: utf-8 -*-
# Created by f1renze on 2019-02-20 23:52
__author__ = 'f1renze'
__time__ = '2019-02-20 23:52'

import sys
import ctypes

"""
python dynamic list 策略类似于寄居蟹, 随着数据量增加底层数组更换为更大的容量
"""


data = list()

for k in range(5):
    print(f'Length: {len(data)}; Size in bytes: {sys.getsizeof(data)}')
    data.append(None)


"""
使用 ctypes 模块提供的原始数组实现 Dynamic Array
"""


class DynamicArray:

    def __init__(self):
        self._n = 0
        self._capacity = 1
        self._A = self._make_array(self._capacity)
        print(f'len: {len(self._A)}; size: {sys.getsizeof(self._A)}')

    def __len__(self):
        return self._n

    def __getitem__(self, item):
        if not 0 <= k < self._n:
            raise IndexError('Invalid Index')
        return self._A[k]

    def append(self, obj):
        if self._n == self._capacity:
            self._resize(2 * self._capacity)
        self._A[self._n] = obj
        self._n += 1

    def _resize(self, c):
        na = self._make_array(c)
        for k in range(self._n):
            na[k] = self._A[k]
        self._A = na
        self._capacity = c

    def _make_array(self, c):
        """
        :param c:
        :return: a new array with capacity c
        """
        return (c * ctypes.py_object)()


if __name__ == '__main__':
    d = DynamicArray()
    print(f'len: {len(d)}; size: {sys.getsizeof(d)}')
    d.append(1)
    print(f'len: {len(d)}; size: {sys.getsizeof(d)}')
    d.append(2)
    print(f'len: {len(d)}; size: {sys.getsizeof(d)}')

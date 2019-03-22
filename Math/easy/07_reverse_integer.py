# -*- coding: utf-8 -*-
# Created by f1renze on 2019-02-12 23:05
__author__ = "f1renze"
__time__ = "2019-02-12 23:05"

"""
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21
Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: 
[−231,  231 − 1]. 
For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
"""


def reverse(x):
    rev = 0
    tmp = 1
    if x < 0:
        tmp = -1
        x = abs(x)
    while x != 0:
        pop = x % 10
        x //= 10
        rev = rev * 10 + pop
    rev *= tmp
    if not is_int32(rev):
        return 0
    return rev


def is_int32(n):
    # check if a num is a 32 bit integer
    return abs(n) <= 2 ** 32 - 1


if __name__ == "__main__":
    print(reverse(1563847412))

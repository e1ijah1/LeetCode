# -*- coding: utf-8 -*-
# Created by f1renze on 2019-02-17 12:02
__author__ = 'f1renze'
__time__ = '2019-02-17 12:02'

"""
The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,

F(0) = 0,   F(1) = 1
F(N) = F(N - 1) + F(N - 2), for N > 1.
Given N, calculate F(N).

 

Example 1:

Input: 2
Output: 1
Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.
Example 2:

Input: 3
Output: 2
Explanation: F(3) = F(2) + F(1) = 1 + 1 = 2.
Example 3:

Input: 4
Output: 3
Explanation: F(4) = F(3) + F(2) = 2 + 1 = 3.

"""


def fibonacci_num_dp(n):
    if n < 1:
        return 0
    a, b = 0, 1
    for i in range(1, n):
        a, b = b, a+b
    return b


if __name__ == '__main__':
    print(
        fibonacci_num_dp(10)
    )

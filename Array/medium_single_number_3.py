# -*- coding: utf-8 -*-
# Created by f1renze on 18-5-23 下午3:05
__author__ = 'f1renze'
__time__ = '18-5-23 下午3:05'

# Single Number III medium
'''
Example:
Input:  [1,2,1,3,2,5]
Output: [3,5]
'''


def single_number(nums):
    s1, s2 = set([]), set([])
    for num in nums:
        if num in s1:
            s2.add(num)
        else:
            s1.add(num)
    return list(s1 - s2)


if __name__ == '__main__':
    list_ = [1, 2, 1, 3, 2, 5]
    single_number(list_)

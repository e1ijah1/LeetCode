# -*- coding: utf-8 -*-
# Created by f1renze on 2019-02-20 23:19
__author__ = 'f1renze'
__time__ = '2019-02-20 23:19'


def single_num_sort(nums):
    """
    排序后判断左右
    :param nums:
    :return:
    """
    if len(nums) < 2:
        return nums[0]
    nums = sorted(nums)
    for i in range(len(nums)):
        if nums[i] != nums[i - 1] and (i + 1 == len(nums) or nums[i] != nums[i + 1]):
            return nums[i]


def single_num(nums):
    r = 0
    for i in nums:
        r ^= i
    return r


if __name__ == '__main__':
    pass

# -*- coding: utf-8 -*-
# Created by f1renze on 2019-02-21 01:42
__author__ = "f1renze"
__time__ = "2019-02-21 01:42"


def plus_one(nums):
    plus_one_r(nums, len(nums) - 1)
    return nums


def plus_one_r(nums, i):
    if i == 0 and nums[i] > 8:
        nums[i] = 0
        nums.insert(0, 0)
    if nums[i] == 9:
        nums[i] = 0
        plus_one_r(nums, i - 1)
    else:
        nums[i] += 1


if __name__ == "__main__":
    print(plus_one([9]), plus_one([9, 9, 2]))

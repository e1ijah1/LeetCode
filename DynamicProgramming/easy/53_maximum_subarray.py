# -*- coding: utf-8 -*-
# Created by f1renze on 2019-02-16 18:00
__author__ = "f1renze"
__time__ = "2019-02-16 18:00"

"""
Given an integer array nums, find the contiguous subarray 
(containing at least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Follow up:

If you have figured out the O(n) solution, try coding another
 solution using the divide and conquer approach, which is more subtle.
"""


def max_sub_sequence_sum(arr):
    """
    迭代穷举取最大连续子序列和, 复杂度 n^2
    :param arr:
    :return:
    """
    max_sum = 0
    # 子序列左边界
    for i in range(len(arr)):
        tmp = 0
        # 子序列右边界
        for j in range(i, len(arr)):
            tmp += arr[j]
            if tmp > max_sum:
                max_sum = tmp
    return max_sum


def dp_max_sub_sequence_sum(arr):
    """
    缺点: 当最大值为负时无效
    如果a[i]是负数，那么它不可能代表最优序列的起点，
    因为任何包含a[i]的作为起点的子序列都可以通过使用a[i+1]作为起点得到改进。
    类似的，任何负的子序列也不可能是最优子序列的前缀（原理相同）。
    :param arr:
    :return:
    """
    max_sum, tmp = 0, 0
    for i in range(len(arr)):
        tmp += arr[i]
        if tmp > max_sum:
            max_sum = tmp
        elif tmp < 0:
            tmp = 0
    return max_sum


def best_dp_max_sub_sequence_sum(nums):
    """
    将 sum 存储于已遍历的 val 中以节约空间， 且当最大值为负时依然可得正确结果
    将以下语句简写
    if nums[i-1] > 0:
            nums[i] += nums[i-1]
    :param nums:
    :return:
    """
    for i in range(1, len(nums)):
        nums[i] = max(nums[i], nums[i] + nums[i - 1])
    return max(nums)


if __name__ == "__main__":
    t1 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    t2 = [-1]
    t3 = [-2, -1]
    r = max_sub_sequence_sum(t1)
    r2 = max_sub_sequence_sum(t1)
    r3 = best_dp_max_sub_sequence_sum(t2)

    print(r, r2, r3, best_dp_max_sub_sequence_sum(t3))

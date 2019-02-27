# -*- coding: utf-8 -*-
# Created by f1renze on 2019-02-17 12:29
__author__ = 'f1renze'
__time__ = '2019-02-17 12:29'

from functools import lru_cache

"""
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.

Example 1:

Input: [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
             Total amount you can rob = 1 + 3 = 4.
Example 2:

Input: [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
             Total amount you can rob = 2 + 9 + 1 = 12.
             
逆推分析:
1. 最后一个房子有2种选择.
    1.1 若最后一个房子 + 上上个房子 + 之前的部分最大, 则偷
    1.2 若上个房子 + 之前的部分最大, 则不偷
2. 故状态转移表达式: f(x) = max(f(x-2) + x.val, f(x-1))
"""


def rob(nums):
    """
    false: [2, 1, 1, 2]
    :param nums:
    :return:
    """
    odd_sum, even_sum = 0, 0
    for i in range(len(nums)):
        if i % 2 == 0:
            even_sum += nums[i]
        else:
            odd_sum += nums[i]
    return max(odd_sum, even_sum)


def rob_r(nums):
    # Recursive (top-down)
    return rob_recursion(nums, len(nums) - 1)


# @lru_cache(1024)
def rob_recursion(nums, i):
    """
    每一间房子都有两种选择:
    rob(i) = Math.max( rob(i - 2) + currentHouseValue, rob(i - 1) )
    逆推, 由最后一个开始, 取当前+前第2个与前第1个的最大值, 每次选择都递归, 分割为子问题(更小的数组), 直至边界条件,
    时间复杂度: O(2^N)
    :param nums:
    :param i:
    :return:
    """
    if i < 0:
        return 0
    return max(rob_recursion(nums, i-2) + nums[i], rob_recursion(nums, i-1))


memo = None


def rob_rm(nums):
    # Recursive + memo (top-down).
    global memo
    memo = [-1 for _ in range(len(nums))]
    return rob_memo(nums, len(nums)-1)


def rob_memo(nums, i):
    if i < 0:
        return 0
    if memo[i] >= 0:
        return memo[i]
    memo[i] = max(rob_recursion(nums, i-2) + nums[i], rob_recursion(nums, i-1))
    return memo[i]


def rob_memo_dp(nums):
    """
    边界条件: 设 nums[0] 为 v0, 设 nums[1] 为 v1
    sub = [v0, v1] 时, 设 max(sub) 为 m2 = max(v0, v1)
    sub = [v0, v1, v2], m3 = max(v0 + v2, v1)
    sub = [v0, v1, v2, v3], m4 = max(m2 + v4, m3)
    :param nums:
    :return:
    """
    if len(nums) < 2:
        return nums[0]
    tmp = [0 for _ in range(len(nums))]
    tmp[0] = nums[0]
    tmp[1] = max(nums[0], nums[1])
    for i in range(2, len(nums)):
        tmp[i] = max(nums[i] + tmp[i-2], tmp[i-1])
    return tmp[-1]


def rob_dp(nums):
    """
    不借助备忘录的 dp 思想, 只需保存前2个状态即可
    :param nums:
    :return:
    """
    prev1, prev2 = 0, 0
    for i in range(len(nums)):
        prev1, prev2 = max(nums[i] + prev2, prev1), prev1
    return prev1


if __name__ == '__main__':
    t1 = [2, 7, 9, 3, 1]
    t2 = [2, 1, 1, 2]
    print(
        rob_r(t1), rob_r(t2), rob_rm(t2), rob_memo_dp(t2), rob_dp(t2)
    )

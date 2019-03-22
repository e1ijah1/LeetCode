# -*- coding: utf-8 -*-
# Created by f1renze on 2019-02-17 16:27
__author__ = "f1renze"
__time__ = "2019-02-17 16:27"

import sys

"""
On a staircase, the i-th step has some non-negative cost cost[i] assigned (0 indexed).

Once you pay the cost, you can either climb one or two steps. 
You need to find minimum cost to reach the top of the floor, 
and you can either start from the step with index 0, or the step with index 1.

Example 1:
Input: cost = [10, 15, 20]
Output: 15
Explanation: Cheapest is start on cost[1], pay that cost and go to the top.
Example 2:
Input: cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
Output: 6
Explanation: Cheapest is start on cost[0], and only step on 1s, skipping cost[3].
Note:
cost will have a length in the range [2, 1000].
Every cost[i] will be an integer in the range [0, 999].


动态规划原则:
将问题分解为子问题, 将 cost 逆序后, 每格的最小开销 = 当前格开销 + min(前1步的开销, 前2步的开销)
f(n) = cost[n] + min(f(n-1), f(n-2))
"""


def mccs_iter_memo(cost):
    """
    带备忘录的 iter, mccs 为题目缩写
    :param cost:
    :return:
    """
    memo = [0, 0]
    for x in reversed(cost):
        memo.append(x + min(memo[-1], memo[-2]))
    return min(memo[-2:])


def mccs_dp(cost):
    prev1 = prev2 = 0
    for x in reversed(cost):
        prev1, prev2 = x + min(prev1, prev2), prev1
    return min(prev1, prev2)


def solution_dp(cost):
    """ 官方题解
    将 cost 逆序后可得:
    状态转移方程: f(x) = cost[x] + min(f(x+1), f(x+2))
    :param cost:
    :return:
    """
    f1 = f2 = 0
    for x in reversed(cost):
        f1, f2 = x + min(f1, f2), f1
    return min(f1, f2)


if __name__ == "__main__":
    t1 = [10, 15, 20]
    t2 = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
    t3 = [0, 2, 2, 1]

    print(mccs_iter_memo(t1), mccs_iter_memo(t2), mccs_iter_memo(t3))

    print(mccs_dp(t1), mccs_dp(t2), mccs_dp(t3))

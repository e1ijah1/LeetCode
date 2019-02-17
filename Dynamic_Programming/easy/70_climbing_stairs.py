# -*- coding: utf-8 -*-
# Created by f1renze on 2019-02-17 11:02
__author__ = 'f1renze'
__time__ = '2019-02-17 11:02'

from functools import lru_cache


"""
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Note: Given n will be a positive integer.

Example 1:

Input: 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step


以总数为10的台阶分析:
1. 若只差最后一步登上台阶最高点, 有两种情况，爬1级或2级
2. 设 0 ~ 8 级台阶有 x 种走法, 0 ~ 9 级台阶有 y 种走法, 10 级台阶走法可根据最后1步的不同走法分为2种, 
最后一步爬1级时, 前面的部分的走法等同于 0 ~ 9 级台阶的 x 种走法, 最后一步爬2级时, 前面部分的走法等同于
0 ~ 8 级台阶的 y 种走法, 故 10 级台阶的走法共有 x + y 种, 故此问题属于 fibonacci 问题的变种:
f(n) = f(n-1) + f(n-2) 
"""


@lru_cache(1024)
def climb_stairs_recursion(n):
    """
    仅使用递归逆推时会有许多重复操作, 使用 lru_cache 缓存结果(即实现备忘录算法),
    展开来为一颗二叉树, 故时间复杂度: O(2 ^ n)
    :param n:
    :return:
    """
    if n < 1:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 2
    return climb_stairs_recursion(n - 1) + climb_stairs_recursion(n - 2)


def climb_stairs_dp(n):
    """
    动态规划思想: 求 f(n) 只需要知道 f(n-1) + f(n-2), 故只保留前面2个状态即可
    时间复杂度: O(n), 空间复杂度: O(1)
    :param n:
    :return:
    """
    if n < 1:
        return 0
    if n == 1:
        return 1
    a, b = 1, 2
    for i in range(2, n):
        a, b = b, b + a
    return b


if __name__ == '__main__':
    print(
        climb_stairs_recursion(10),
        climb_stairs_recursion(9),
        climb_stairs_recursion(8),
        climb_stairs_dp(10)
    )

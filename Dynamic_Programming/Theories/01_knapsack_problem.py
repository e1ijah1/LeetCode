# -*- coding: utf-8 -*-
# Created by f1renze on 2019-01-24 23:33
__author__ = 'f1renze'
__time__ = '2019-01-24 23:33'

from pprint import pprint
from collections import namedtuple


"""
01 背包问题
"""

# class Store:
#     """
#     ($, pounds)
#     """
#     stereo = (3000, 4),
#     laptop = (2000, 3),
#     guitar = (1500, 1)


MAX_WEIGHT = 4
Good = namedtuple('Good', ['price', 'weight'])
# 吉他, 音响, 笔记本电脑
Store = [Good(1500, 1), Good(3000, 4), Good(2000, 3)]


def bag_01_implementation():
    """
    cell is a 2d array
    :return:
    """
    cell = [[0 for __ in range(MAX_WEIGHT)] for _ in range(len(Store))]
    pprint(cell)

    # 从小背包到大背包
    for j in range(MAX_WEIGHT):
        # 遍历所有物品
        for i, good in enumerate(Store):
            price = good[0]
            weight = good[1]
            bag_weight = j + 1
            # 第一行只有一种选择
            if i == 0:
                cell[i][j] = price
            # 背包容量 > 当前物品重量
            elif bag_weight >= weight:
                # 剩余重量
                sur_wei = bag_weight-weight
                surplus_value = 0 if not (i-1) or not (sur_wei) else cell[i-1][sur_wei]
                cell[i][j] = max(cell[i - 1][j], price + surplus_value)
            # 装不下
            else:
                cell[i][j] = cell[i - 1][j]
                # cell[i][j] = max(cell[i-1][j], price + cell[i-1][j if not (j-weight) else (j-weight)])

    pprint(cell)


if __name__ == '__main__':
    bag_01_implementation()

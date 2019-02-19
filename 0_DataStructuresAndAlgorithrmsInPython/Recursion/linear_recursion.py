# -*- coding: utf-8 -*-
# Created by f1renze on 2019-02-18 23:01
__author__ = 'f1renze'
__time__ = '2019-02-18 23:01'


def reverse(S, start, stop):
    """ 使用线性递归逆置序列的元素
    start == stop 隐含范围为空
    start == stop -1 隐含范围仅有一个元素, 此算法保证在进行 1 + n/2 次递归后终止,
    时间复杂度 O(n)
    :param S:
    :param start:
    :param stop:
    :return:
    """
    if start < stop -1:
        S[start], S[stop-1] = S[stop-1], S[start]
        reverse(S, start+1, stop-1)


def power(x, n):
    """
    2^13 = 2 * 2^6 * 2^6,
    时间复杂度 O(log n), 操作次数 log2n + 1, 空间复杂度同样 O(log n)
    :param x:
    :param n:
    :return:
    """
    if n == 0:
        return 1
    else:
        partial = power(x, n // 2)
        result = partial * partial
        if n % 2 == 1:
            result *= x
    return result


if __name__ == '__main__':
    print(
        reverse([4, 3, 6, 2, 8, 9, 5])
    )

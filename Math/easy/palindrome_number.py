# -*- coding: utf-8 -*-
# Created by f1renze on 18-5-29 上午10:22
__author__ = "f1renze"
__time__ = "18-5-29 上午10:22"

"""
Palindrome Number / easy

判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。

示例 1:
输入: 121
输出: true

示例 2:
输入: -121
输出: false
解释: 从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。

示例 3:
输入: 10
输出: false
解释: 从右向左读, 为 01 。因此它不是一个回文数。

进阶:
你能不将整数转为字符串来解决这个问题吗？
"""


def is_palindrome_str(x):
    """
    :type x: int
    :rtype: bool
    """
    return str(x)[::-1] == str(x)


"""
>>> n = 123456
>>> n % 10 # 得到最后一位数字
6
>>> n // 10 # 移除最后一位数字
12345
>>> n % 10 # 得到倒数第二位数字
5

>>> n1 = 123456
>>> rn = 0
>>> while n1 > rn:
...     rn = rn*10 + n1%10
...     n1 //= 10
... 
>>> print(n1, rn, sep=' ') # 得到后半部分的反转
123 654
>>> n1 = 12345
>>> rn = 0
>>> while n1 > rn:
...     rn = rn*10 + n1%10
...     n1 //= 10
... 
# 因为n1有5个数字, 反转判断条件为n1 > rn, 所以最后得到 (n // 2)+1 个数字的反转
# 中间的数字不影响两边是否对称, 将其移除即可
>>> print(n1, rn, rn//10, sep=' ') 
12 543 54
# 若前面的数字大, 后面的数字小, 得到的反转数位数占原来的大部分, 但不影响判断结果
>>> n1 = 65432
>>> rn = 0
>>> while n1 > rn:
...     rn = rn*10 + n1%10
...     n1 //= 10
... 
>>> print(n1, rn, rn//10, sep=' ')
65 234 23
>>> n1 = 654321
>>> rn = 0
>>> while n1 > rn:
...     rn = rn*10 + n1%10
...     n1 //= 10
... 
>>> print(n1, rn, rn//10, sep=' ')
65 1234 123
"""


def is_palindrome(x):
    """
    反转数字的一半并与前半部分进行比较(为了避免反转后的数字溢出)
    :param x:
    :return:
    """
    if (x < 0) or (x != 0 and x % 10 == 0):
        # 负数不是回文数, 最后一位为0也不是回文数
        return False
    reversed_half_num = 0
    while x > reversed_half_num:
        reversed_half_num = reversed_half_num * 10 + x % 10
        x //= 10
    return (x == reversed_half_num) or (x == reversed_half_num // 10)


if __name__ == "__main__":
    pass

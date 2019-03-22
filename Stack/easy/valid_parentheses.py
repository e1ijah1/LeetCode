# -*- coding: utf-8 -*-
# Created by f1renze on 18-6-2 下午11:40
__author__ = "f1renze"
__time__ = "18-6-2 下午11:40"

"""
Valid Parentheses / Easy

给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。

有效字符串需满足：

左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
注意空字符串可被认为是有效字符串。

示例 1:
输入: "()"
输出: true

示例 2:
输入: "()[]{}"
输出: true

示例 3:
输入: "(]"
输出: false

示例 4:
输入: "([)]"
输出: false

示例 5:
输入: "{[]}"
输出: true
"""


def is_valid(s):
    """
    44 ms
    :param s: str
    :return: bool
    """
    stack = []
    d = {")": "(", "]": "[", "}": "{"}
    for c in s:
        if c in d.values():
            stack.append(c)
        elif c in d.keys():
            if stack == [] or d[c] != stack.pop():
                return False
        else:
            return False
    return stack == []


if __name__ == "__main__":
    pass

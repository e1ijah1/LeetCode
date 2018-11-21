# -*- coding: utf-8 -*-
# Created by f1renze on 2018/11/20 下午9:20

import unittest
from functools import reduce

'''
给定 S 和 T 两个字符串，当它们分别被输入到空白的文本编辑器后，
判断二者是否相等，并返回结果。# 代表退格字符。
输入：S = "ab#c", T = "ad#c"
输出：true
解释：S 和 T 都会变成 “ac”。
'''


class Solution:

    @staticmethod
    def list2str(l):
        return reduce(lambda x, y: f'{x}{y}', l)

    def backspace_compare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if s == t:
            return True

        stack1 = []
        stack2 = []

        for c in s:
            if c != '#':
                stack1.append(c)
            elif stack1:
                stack1.pop()

        for c in t:
            if c != '#':
                stack2.append(c)
            elif stack2:
                stack2.pop()
        return stack1 == stack2
        # return self.list2str(stack1) == self.list2str(stack2)


class Tester(unittest.TestCase):

    def setUp(self):
        self.testcase = [
            ['ab#c', 'ad#c'],  # true  ac
            ['ab##', 'c#d#'],  # true  ''
            ['a##c', '#a#c'],  # true  c
            ['a#c', 'b']       # false  c != b
        ]
        self.solution = Solution()

    def test_logic(self):
        self.assertEqual(
            self.solution.backspace_compare(*self.testcase[0]), True
        )
        self.assertEqual(
            self.solution.backspace_compare(*self.testcase[1]), True
        )
        self.assertEqual(
            self.solution.backspace_compare(*self.testcase[2]), True
        )
        self.assertEqual(
            self.solution.backspace_compare(*self.testcase[3]), False
        )


if __name__ == '__main__':
    unittest.main()

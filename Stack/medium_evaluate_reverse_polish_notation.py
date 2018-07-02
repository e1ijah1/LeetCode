# -*- coding: utf-8 -*-
# Created by f1renze on 18-7-2 下午11:47
__author__ = 'f1renze'
__time__ = '18-7-2 下午11:47'


class Solution:
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        if len(tokens) < 1:
            return None
        operators = {
            '+': lambda x, y: x + y,
            '-': lambda x, y: x - y,
            '*': lambda x, y: x * y,
            '/': lambda x, y: int(x / y)
        }
        stack = []
        for x in tokens:
            if x not in operators:
                stack.append(int(x))
                continue
            a = stack.pop()
            b = stack.pop()
            c = operators[x](b, a)
            stack.append(c)
        return stack[0]


if __name__ == '__main__':
    s = Solution()
    test_case = ["0", "3", "/"]
    test_case2 = ["2", "1", "+", "3", "*"]
    test_case3 = ["4", "13", "5", "/", "+"]
    t4 = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
    print(s.evalRPN(test_case3), s.evalRPN(t4), sep='\n')

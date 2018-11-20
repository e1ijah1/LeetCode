# -*- coding: utf-8 -*-
# Created by f1renze on 18-6-3 上午10:28
__author__ = 'f1renze'
__time__ = '18-6-3 上午10:28'

'''
Min Stack / Easy

设计一个支持 push，pop，top 操作，并能在常数时间内检索到最小元素的栈。

push(x) -- 将元素 x 推入栈中。
pop() -- 删除栈顶的元素。
top() -- 获取栈顶元素。
getMin() -- 检索栈中的最小元素。

示例:
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> 返回 -3.
minStack.pop();
minStack.top();      --> 返回 0.
minStack.getMin();   --> 返回 -2.
'''


class MinStack:
    """
    64 ms / 76 ms
    """

    def __init__(self):
        """
        initialize your data structure here.
        """
        self._elem = []
        self._min = []

    def push(self, x):
        """
        将最小元素单独存为一个栈
        :type x: int
        :rtype: void
        """
        if self._elem == [] or x < self._min[-1]:
            self._min.append(x)
        self._elem.append(x)

    def pop(self):
        """
        :rtype: void
        """
        if not self._elem:
            raise ValueError
        n = self._elem.pop()
        # 如果栈顶元素在栈中重复, 即使为最新的最小元素也不能删除
        if (n not in self._elem) and (n == self._min[-1]):
            self._min.pop()

    def top(self):
        """
        :rtype: int
        """
        if not self._elem:
            raise ValueError
        return self._elem[-1]

    def get_min(self):
        """
        :rtype: int
        """
        if not self._elem:
            raise ValueError
        '''
        在栈顶元素为最小时删除 _min 的栈顶元素而不考虑栈中有重复元素时
        使用下面的代码
        '''
        # if not self._min:
        #     sorted_l = sorted(self._elem)
        #     self._min.append(sorted_l[0])
        return self._min[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()


if __name__ == '__main__':
    pass

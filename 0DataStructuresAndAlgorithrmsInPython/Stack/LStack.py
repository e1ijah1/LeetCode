# -*- coding: utf-8 -*-
# Created by f1renze on 18-5-31 下午8:06
__author__ = "f1renze"
__time__ = "18-5-31 下午8:06"

"""
栈的链表(Linked List)实现
"""


class StackUnderflow(ValueError):
    pass


class LNode:
    def __init__(self, elem, next_=None):
        self.elem = elem
        self.next = next_


class LStack:
    def __init__(self):
        self._top = None

    def is_empty(self):
        return self._top is None

    def top(self):
        if self._top is None:
            raise StackUnderflow("in LStack.top()")
        return self._top.elem

    def push(self, elem):
        self._top = LNode(elem, self._top)

    def pop(self):
        if self._top is None:
            raise StackUnderflow("in LStack.pop()")
        p = self._top
        self._top = p.next
        return p.elem


if __name__ == "__main__":
    pass

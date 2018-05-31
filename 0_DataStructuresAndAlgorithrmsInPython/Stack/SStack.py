# -*- coding: utf-8 -*-
# Created by f1renze on 18-5-31 下午4:23
__author__ = 'f1renze'
__time__ = '18-5-31 下午4:23'

'''
栈的顺序表(Sequence table)实现
'''


class StackUnderflow(ValueError):
    """
    栈下溢(空栈访问)时抛出此异常, 由于操作时栈不满足需要
    (如空栈弹出)可以看作参数值错误, 故继承 ValueError
    """
    pass


class SStack:
    """
    基于顺序表技术实现的栈类,
    用 list 对象 _elem 存储栈中元素,
    所有栈操作都映射到 list 操作
    """
    def __init__(self):
        self._elem = []

    def is_empty(self):
        return self._elem == []

    def top(self):
        if not self._elem:
            raise StackUnderflow('in SStack.top()')
        return self._elem[-1]

    def push(self, elem):
        self._elem.append(elem)

    def pop(self):
        if not self._elem:
            raise StackUnderflow('in SStack.pop()')
        return self._elem.pop()


if __name__ == '__main__':
    st1 = SStack()
    st1.push(3)
    st1.push(5)
    while not st1.is_empty():
        print(st1.pop())

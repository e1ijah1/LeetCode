# -*- coding: utf-8 -*-
# Created by f1renze on 2018-12-24 01:01
__author__ = 'f1renze'
__time__ = '2018-12-24 01:01'


'''
ADT BinTree:                            # 一个二叉树抽象数据类型
        BinTree(self, data, left, right)    # 构造
        is_empty(self)
        num_nodes(self)                     # 节点个数
        data(self)                          # 取得根
        left(self)
        right(self)
        set_left(self, btree)
        set_right(self, btree)
        traversal(self)                     # 遍历各个节点
        forall(self, op)                    # 对每个节点执行 op 
'''


class ListBinTree:
    """
    基于 list 实现的二叉树
    eg:
        ['a', ['b', None, None],
              ['c', ['d', ['f', None, None],
                          ['g', None, None]],
                    ['e', ['h', None, None],
                          ['i', None, None]]]]
    """

    def __init__(self, data, left=None, right=None):
        self.__list = [data, left, right]

    def is_empty(self):
        return bool(self)

    @property
    def nodes_count(self):
        return len(list(filter(lambda x: bool(x), self.__list)))

    @property
    def root(self):
        return self.__list[0]

    @root.setter
    def root(self, data):
        if data:
            self.__list[0] = data

    @property
    def left(self):
        return self.__list[1]

    @left.setter
    def left(self, left):
        if left:
            self.__list[1] = left

    @property
    def right(self):
        return self.__list[2]

    @right.setter
    def right(self, right):
        if right:
            self.__list[2] = right


'''
'''


class BinTreeNode:
    """
    基于链接(引用)实现的二叉树
    """
    def __init__(self, _data, _left=None, _right=None):
        self.data = _data
        self.left = _left
        self.right = _right
        
# TODO print tree shape


if __name__ == '__main__':
    pass

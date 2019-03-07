
from abc import abstractmethod

from .abstract_tree import Tree

'''
完全二叉树 / 满二叉树: 每个节点都有0或2个节点
反之为不完全二叉树
决策树是完全二叉树

设 T 为非空二叉树, n 为节点数, nE 为外部节点数, nI 为内部节点数, h 为高度, 有:

h + 1 <= n <= 2^(h+1) - 1
1 <= nE <= 2^h
h <= nI <= 2^h-1
log(n+1) - 1 <= h <= n - 1

在非空完全二叉树中, nE = nI + 1  
'''


class BinaryTree(Tree):

    @abstractmethod
    def left(self, p):
        """
        返回 p 的左子的位置
        :param p:
        :return:
        """

    @abstractmethod
    def right(self, p):
        """
        返回 p 的右子的位置
        :param p:
        :return:
        """

    def sibling(self, p):
        """
        返回 p 的兄弟节点的位置, 无则返回 None
        :param p:
        :return:
        """
        parent = self.parent(p)
        if not parent:
            return None
        elif p == self.left(parent):
            return self.right(parent)
        else:
            return self.left(parent)

    def children(self, p):
        if self.left(p):
            yield self.left(p)
        elif self.right(p):
            yield self.right(p)

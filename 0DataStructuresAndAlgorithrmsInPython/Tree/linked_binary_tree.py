

class Node:
    """
    链表二叉树的一种实现:
    分别使用4个引用
    """

    __slots__ = 'ele', 'parent', 'left', 'right'

    def __init__(self, ele, parent, left, right):
        self.ele = ele
        self.parent = parent
        self.left = left
        self.right =right


class TreeNode:
    """
    一种更优雅的实现, 引用父节点与自身的子节点
    """

    __slots__ = 'parent', 'children', 'ele'

    def __init__(self, ele, parent, children):
        self.ele = ele
        self.parent = parent
        self.children = children


class LinkedTree:

    def __init__(self):
        self.size = 0
        self._root = None

    def len(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def root(self):
        return self._root

    def parent(self, p):
        return p.parent

    def children(self, p):
        pass

    def is_root(self, p):
        return self._root is p

    def is_leaf(self, p):
        return p.children is None

    def depth(self, p):
        """
        返回 p 到 root 的距离, p 的深度即为 p 祖先的个数
        :param p:
        :return:
        """
        if self.is_root(p):
            return 0
        else:
            return 1 + self.depth(self.parent(p))

    def _height(self, p):
        """
        计算以 p 节点为根的子树的高度, O(n), 若使用 depth 对每个子节点从下往上计算深度, 含有大量重复计算, 最坏情况 O(n^2)
        :param p:
        :return:
        """
        if self.is_leaf(p):
            return 0
        else:
            return 1 + max(self.height(c) for c in self.children(p))

    def height(self, p=None):
        if not p:
            p = self.root()
        return self._height(p)

    """
    实现树遍历的前提
    """
    def positions(self, p=None):
        """
        🌲的所有位置的迭代器
        :param p:
        :return:
        """
        if not p:
            p = self._root
        while p:
            yield p
            p = p.children

    def __iter__(self):
        for p in self.positions():
            yield p.ele

    """
    树的先序遍历
    """
    def preorder(self):
        if not self.is_empty():
            for p in self._sub_tree_preorder(self.root()):
                yield p

    def _subtree_preorder(self, p):
        yield p
        for c in self.children(p):
            for other in self._subtree_preorder(c):
                yield other

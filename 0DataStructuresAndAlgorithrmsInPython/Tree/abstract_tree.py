

from abc import ABC, abstractmethod


class Position(ABC):

    @abstractmethod
    def element(self):
        pass

    @abstractmethod
    def __eq__(self, other):
        pass

    @abstractmethod
    def __ne__(self, other):
        pass


class Tree(ABC):

    @abstractmethod
    def __len__(self):
        pass

    @abstractmethod
    def root(self):
        """
        返回根节点的位置
        :return:
        """
        pass

    @abstractmethod
    def parent(self, p):
        """
        返回 p 的父节点的位置
        :param p:
        :return:
        """
        pass

    @abstractmethod
    def num_children(self, p):
        """
        返回位置 p 的子节点位置
        :param p:
        :return:
        """
        pass

    @abstractmethod
    def children(self, p):
        """
        产生 p 之后的子节点的迭代
        :param p:
        :return:
        """
        pass

    def is_root(self, p):
        return self.root() == p

    def is_leaf(self, p):
        return self.num_children(p) == 0

    def is_empty(self):
        return len(self) == 0

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


if __name__ == '__main__':
    Position().element()

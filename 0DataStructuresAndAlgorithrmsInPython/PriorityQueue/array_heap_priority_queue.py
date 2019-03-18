

class ArrayHeapPriorityQueue:
    """
    用基于数组表示的堆来实现优先级队列,
    若 p 是 T 的根节点, f(p) = 0
    若 x 是 p 的左子, f(x) = 2f(p) + 1
    若 y 是 p 的右子, f(y) = 2f(p) + 2
    最坏情况下堆向上/向下排序复杂度为堆高度即 O(log n)
    为了使堆高度尽量小, 它必须是完全二叉
    数组实现相比链式结构实现更容易定位底层的元素
    堆实现相比排序 list 实现极大提升了性能
    """

    def __init__(self):
        self.data = list()

    def __len__(self):
        return len(self.data)

    def is_empty(self):
        return len(self.data) == 0

    @staticmethod
    def parent(j):
        return (j-1) // 2

    @staticmethod
    def left(j):
        return 2 * j + 1

    @staticmethod
    def right(j):
        return 2 * j + 2

    def has_left(self, j):
        return self.left(j) < len(self.data)

    def has_right(self, j):
        return self.right(j) < len(self.data)

    def swap(self, i, j):
        self.data[i], self.data[j] = self.data[j], self.data[i]

    def up_heap(self, j):
        """
        堆向上冒泡
        :param j:
        :return:
        """
        par = self.parent(j)
        if j > 0 and self.data[j] < self.data[par]:
            self.swap(j, par)
            self.up_heap(par)

    def down_heap(self, j):
        """
        堆向下冒泡
        :param j:
        :return:
        """
        if self.has_left(j):
            small_child = left = self.left(j)
            if self.has_right(j):
                right = self.right(j)
                if self.data[right] < self.data[left]:
                    small_child = right

            if self.data[small_child] < self.data[j]:
                self.swap(j, small_child)
                self.down_heap(small_child)

    def add(self, key, val):
        self.data.append((key, val))
        # 插入后向上冒泡
        self.up_heap(len(self.data) - 1)

    def min(self):
        if self.is_empty():
            raise RuntimeError('Priority Queue is empty')
        # 返回栈顶的 tuple
        return self.data[0]

    def remove_min(self):
        if self.is_empty():
            raise RuntimeError('Priority Queue is empty')
        # 将栈顶元素与最底层的最右交换后删除
        self.swap(0, len(self.data) - 1)
        result = self.data.pop()
        # 删除后向下冒泡4
        self.down_heap(0)
        return result

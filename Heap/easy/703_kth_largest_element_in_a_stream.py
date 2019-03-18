
class KthLargest:

    def __init__(self, k, nums):
        """
        维护一个节点为 k 的小顶堆, 第 k 个最大值置于堆顶
        :param k:
        :param nums:
        """
        self.k = k
        self.data = list()
        for i in sorted(nums):
            self.add(i)

    def add(self, val: int) -> int:
        if len(self.data) < self.k:
            self.data.append(val)
        elif val > self.data[0]:
            self.remove_min()
            self.data.append(val)

        self.up_heap(len(self.data) - 1)
        return self.data[0]

    def remove_min(self):
        if not self.data:
            raise RuntimeError('Priority Queue is empty')
        # 将栈顶元素与最底层的最右交换后删除
        self.swap(0, len(self.data) - 1)
        result = self.data.pop()
        # 删除后向下冒泡4
        self.down_heap(0)
        return result

    @staticmethod
    def parent(i):
        return (i-1) // 2

    @staticmethod
    def left(i):
        return 2 * i + 1

    @staticmethod
    def right(i):
        return 2 * i + 2

    def has_left(self, i):
        return self.left(i) < len(self.data)

    def has_right(self, i):
        return self.right(i) < len(self.data)

    def swap(self, i, j):
        self.data[i], self.data[j] = self.data[j], self.data[i]

    def up_heap(self, i):
        par = self.parent(i)
        if i > 0 and self.data[par] > self.data[i]:
            self.swap(i, par)
            self.up_heap(par)

    def down_heap(self, i):
        if self.has_left(i):
            smallest = left = self.left(i)
            if self.has_right(i):
                right = self.right(i)
                smallest = min(left, right, key=lambda x: self.data[x])
            if self.data[i] > self.data[smallest]:
                self.swap(i, smallest)
                self.down_heap(smallest)


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)


def t(k, arr, tc):
    kth_largest = KthLargest(k, arr)
    for i in tc:
        print(kth_largest.add(i))


def t1():
    t(3, [4, 5, 8, 2], [3, 5, 10, 9, 4])


def t2():
    t(1, [], [-3, -2, -4, 0, 4])


if __name__ == '__main__':
    t1()

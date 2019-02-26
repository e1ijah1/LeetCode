

class ArrayQueue:
    """ 使用首位相连的循环数组模拟队列
    使用 list 实现的 Queue, 实现 FIFO 可以使用 append + pop(0),
    但 pop(0) 实现的 Queue, 出队操作时间复杂度总为 O(n),
    故可以使用 ptr 指示长度为 N 的 Queue, 设 ptr 在底层 list 中间,
    若 ptr 位置元素出队, 使用 ptr + 1 % N 可获得下一个队首元素
    """

    DEFAULT_CAPACITY = 10

    def __init__(self):
        self._data = [None] * self.DEFAULT_CAPACITY
        self._size = 0
        self._front = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def first(self):
        if self.is_empty():
            raise RuntimeError('Queue is empty!')
        return self._data[self._front]

    def dequeue(self):
        """
        均摊 O(1)
        :return:
        """
        if self.is_empty():
            raise RuntimeError('Queue is empty!')
        result = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1
        # 收缩底层数组
        if 0 < self._size < len(self._data) // 4:
            self._resize(len(self._data) // 2)
        return result

    def enqueue(self, e):
        """
        均摊 O(1)
        :param e:
        :return:
        """
        if self._size == len(self._data):
            self._resize(2 * len(self._data))
        avail = (self._front + self._size) % len(self._data)
        self._data[avail] = e
        self._size += 1

    def _resize(self, cap):
        """

        :param cap:
        :return:
        """
        old = self._data
        self._data = [None] * cap
        walk = self._front
        for k in range(self._size):
            self._data[k] = old[walk]
            walk = (1 + walk) % len(old)
        self._front = 0


class ArrayDeque(ArrayQueue):

    def __init__(self):
        super().__init__()

    def add_first(self, e):
        self._front = (self._front - 1) % (len(self._data))
        if self._data[self._front]:
            self._resize(2 * len(self._data))
            self._front = (self._front - 1) % (len(self._data))
        self._data[self._front] = e
        self._size += 1

    def add_last(self, e):
        self.enqueue(e)

    def delete_first(self):
        self.dequeue()

    def delete_last(self):
        if self.is_empty():
            raise RuntimeError('Queue is empty!')
        back = (self._front + self._size - 1) % len(self._data)
        if back > self._size:
            result = self._data[self._front]
            back = self._front
        else:
            result = self._data[back]
        self._data[back] = None
        self._size -= 1
        # 收缩底层数组
        if 0 < self._size < len(self._data) // 4:
            self._resize(len(self._data) // 2)
        return result

    def last(self):
        if self.is_empty():
            raise RuntimeError('Queue is empty!')
        back = (self._front + self._size - 1) % len(self._data)
        if back > self._size:
            return self._data[self._front]
        return self._data[back]

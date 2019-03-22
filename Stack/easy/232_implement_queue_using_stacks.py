class StackQueue:

    DEFAULT_CAPACITY = 10

    def __init__(self):
        self.data = [None] * self.DEFAULT_CAPACITY
        self.size = 0
        self.head = 0

    def resize(self, n):
        old = self.data
        self.data = [None] * n
        walk = self.head
        for k in range(self.size):
            self.data[k] = old[walk]
            walk = walk + 1 % len(old)
        self.head = 0

    def push(self, x: int) -> None:
        """

        :param x:
        :return:
        """
        location = (self.head + self.size) % len(self.data)
        self.data[location] = x
        self.size += 1
        if self.size >= len(self.data):
            self.resize(len(self.data) * 2)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        :return:
        """
        if self.empty():
            raise RuntimeError("Queue is empty!")
        result = self.data[self.head]
        self.data[self.head] = None
        self.head = (self.head + 1) % len(self.data)
        self.size -= 1
        if 0 < self.size < len(self.data) // 4 and len(self.data) > 10:
            self.resize(len(self.data) // 2)
        return result

    def peek(self) -> int:
        """
        Get the front element.
        :return:
        """
        return self.data[self.head]

    def empty(self) -> bool:
        """

        :return:
        """
        return self.size == 0


class MyQueue:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.a = []

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: void
        """
        self.a.append(x)
        print(self.a)
        # 将末尾元素移至 first
        self.a[0], self.a[1:] = self.a[-1], self.a[:-1]
        print(self.a)

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        print(self.a)
        return self.a.pop()

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        return self.a[-1]

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return len(self.a) == 0


if __name__ == "__main__":
    q = MyQueue()
    q.push(1)
    q.push(2)
    q.push(3)
    q.push(4)
    print(q.pop(), q.pop(), q.pop())

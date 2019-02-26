

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


    def push(self, x: int) -> None:
        """

        :param x:
        :return:
        """
        if self.empty():
            raise RuntimeError('Queue is empty!')
        location = (self.head + self.size) % len(self.data)
        self.data[location] = x
        self.size += 1
        if self.size >= len(self.data):
            self.resize(len(self.data) * 2)

    def pop(self) -> int:
        """

        :return:
        """

    def peek(self) -> int:
        """

        :return:
        """

    def empty(self) -> bool:
        """

        :return:
        """

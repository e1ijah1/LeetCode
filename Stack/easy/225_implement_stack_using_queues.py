from queue import Queue


class QueueStack:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = Queue()

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.data.put(x)
        for i in range(self.data.qsize() - 1):
            self.data.put(self.data.get())

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        return self.data.get()

    def top(self) -> int:
        """
        Get the top element.
        """
        r = self.data.get()
        self.push(r)
        return r

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return self.data.empty()


class MyStack:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.a = []

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: void
        """
        self.a.append(x)

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        b = self.a[-1]
        del self.a[-1]
        return b

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        return self.a[-1]

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return len(self.a) == 0


if __name__ == "__main__":
    q = MyStack()
    q.push(1)
    q.push(2)
    q.push(3)
    print(q.top(), q.pop(), q.top(), q.pop())

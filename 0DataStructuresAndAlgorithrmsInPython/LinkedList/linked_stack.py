

class Node:
    __slots__ = 'element', 'next', 'prev'

    def __init__(self, element, _next, prev=None):
        self.element = element
        self.next = _next
        self.prev = prev


class LinkedStack:
    """
    LIFO Stack implementation using a singly linked list for storage
    所有操作均为 O(1)
    """

    def __init__(self):
        self.head = None
        self.size = 0

    def __len__(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def push(self, e):
        self.head = Node(e, self.head)
        self.size += 1

    def top(self):
        if self.is_empty():
            raise RuntimeError('Stack is empty!')
        return self.head.element

    def pop(self):
        if self.is_empty():
            raise RuntimeError('Stack is empty!')
        r = self.head.element
        self.head = self.head.next
        self.size -= 1
        return r


class LinkedQueue:
    """
    FIFO
    """

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __len__(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def first(self):
        if self.is_empty():
            raise RuntimeError('Queue is empty!')
        return self.head.element

    def dequeue(self):
        if self.is_empty():
            raise RuntimeError('Queue is empty!')
        r = self.head.element
        self.head = self.head.next
        self.size -= 1
        if self.is_empty():
            self.tail = None
        return r

    def enqueue(self, x):
        tail = Node(x, None)
        if self.is_empty():
            self.head = tail
        else:
            self.tail.next = tail
        self.tail = tail
        self.size += 1


class CircularQueue:

    def __init__(self):
        self.tail = None
        self.size = 0

    def __len__(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def first(self):
        if self.is_empty():
            raise RuntimeError('Queue is empty!')
        return self.tail.next

    def dequeue(self):
        if self.is_empty():
            raise RuntimeError('Queue is empty!')
        old = self.tail.next
        if self.size == 1:
            self.tail = None
        else:
            self.tail.next = old.next
        self.size -= 1
        return old

    def enqueue(self, x):
        new = Node(x, self.tail.next)
        if self.is_empty():
            new.next = new
        else:
            self.tail.next = new
        self.tail = new
        self.size += 1

    def rotate(self):
        """
        指针前移, 相当于将元素出队再入队
        :return:
        """
        if self.size > 0:
            self.tail = self.tail.next


class DoublyLinkedBase:
    """
    带哨兵的双向链表的基本实现, 使用哨兵简化操作逻辑, 无需处理链表为空时的头尾处理
    """

    def __init__(self):
        self.header = Node(None, None, None)
        self.trailer = Node(None, None, None)
        self.header.next = self.trailer
        self.trailer.prev = self.header
        self.size = 0

    def __len__(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def insert_between(self, e, predecessor, successor):
        new = Node(e, successor, predecessor)
        predecessor.next = new
        successor.prev = new
        self.size += 1
        return new

    def delete_node(self, node):
        prev = node.prev
        _next = node.next
        prev.next = _next
        _next.prev = prev
        self.size -= 1
        ele = node.element
        # 清除引用
        node.prev = node.next = node.element = None
        return ele


class LinkedDeque(DoublyLinkedBase):
    """
    基于双向链表的双头队列
    """

    def first(self):
        if self.is_empty():
            raise RuntimeError('Deque is empty')
        return self.header.next.element

    def last(self):
        if self.is_empty():
            raise RuntimeError('Deque is empty')
        return self.trailer.prev.element

    def insert_first(self, e):
        self.insert_between(e, self.header.next, self.header)

    def insert_last(self, e):
        self.insert_between(e, self.trailer, self.trailer.prev)

    def delete_first(self):
        if self.is_empty():
            raise RuntimeError('Deque is empty')
        return self.delete_node(self.header.next)

    def delete_last(self):
        if self.is_empty():
            raise RuntimeError('Deque is empty')
        return self.delete_node(self.trailer.prev)


class Position:
    """
    序列中位置的抽象
    """

    def __init__(self, container, node: Node):
        self.container = container
        self.node = node

    def element(self):
        return self.node.element

    def __eq__(self, other):
        return isinstance(other, Position) and other.node == self.node

    def __ne__(self, other):
        return not (self == other)


class PositionList(DoublyLinkedBase):
    """

    """
    def __iter__(self):
        cursor = self.first()
        while cursor is not None:
            yield cursor.element()
            cursor = self.after(cursor)

    def _validate(self, p):
        if not isinstance(p, Position):
            raise TypeError('p must be proper Position type')
        if p.container is not self:
            raise ValueError('p does not belong to this container')
        if p.node.next is None:
            raise ValueError('p is no longer valid')
        return p.node

    def _make_position(self, node):
        if node is self.header or node is self.trailer:
            return None
        else:
            return Position(self, node)

    def first(self):
        return self._make_position(self.header.next)

    def last(self):
        return self._make_position(self.trailer.prev)

    def before(self, p):
        node = self._validate(p)
        return self._make_position(node.prev)

    def after(self, p):
        node = self._validate(p)
        return self._make_position(node.next)

    def insert_between(self, e, prev, _next):
        """
        重载, 加一层封装, 封装为位置抽象
        :param e:
        :param prev:
        :param _next:
        :return:
        """
        node = super().insert_between(e, prev, _next)
        return self._make_position(node)

    def add_first(self, e):
        return self.insert_between(e, self.header, self.header.next)

    def add_last(self, e):
        return self.insert_between(e, self.trailer.prev, self.trailer)

    def add_before(self, p, e):
        original = self._validate(p)
        return self.insert_between(e, original.prev, original)

    def add_after(self, p, e):
        original = self._validate(p)
        return self.insert_between(e, original, original.next)

    def delete(self, p):
        original = self._validate(p)
        return self.delete_node(original)

    def replace(self, p, e):
        original = self._validate(p)
        old_value = original.element
        original.element = e
        return old_value


def insertion_sort(l: PositionList):
    """
    按从大到小排序, maker 之前的序列会排好序, pivot 在 maker 之后且 walk 会为其找到合适的位置
    :param l:
    :return:
    """
    if not l:
        return None
    elif len(l) < 1:
        return l.first()

    maker = l.first()
    while maker != l.last():
        pivot = l.after(maker)
        value = pivot.element()
        if value > maker.element():
            maker = pivot
        else:
            walk = maker
            while walk != l.first() and l.before(walk).element() > value:
                walk = l.before(walk)
            l.delete(pivot)
            l.add_before(walk, value)


if __name__ == '__name__':
    pass

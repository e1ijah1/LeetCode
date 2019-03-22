# -*- coding: utf-8 -*-
# Created by f1renze on 18-5-31 上午10:23
__author__ = "f1renze"
__time__ = "18-5-31 上午10:23"

"""
假设有 n 个人围坐一圈, 现在要求从第 k 个人开始报数,
报到第 m 个人退出, 从下一个人开始继续报数并按照同样规则退出,
直至所有人退出, 按顺序输出各列人的编号 
"""


def josephus_array(n, k, m):
    """
    使用数组实现的解法, 梗概如下.
    初始:
        建立一个包含 n 个人(编号)的表.
        找到第 k 个人, 从那里开始.
    处理过程中采用把相应元素修改为 0 的方式表示已出列, 反复做:
        数 m 个人, 遇到表的末端就转回下标 0 继续.
        把表示第 m 个人的表元素修改为 0.
    n 个人出列即结束.
    :param n: 数组长度, 最后需要全部出列(即数组元素全部为0)
    :param k: 从第k个人开始, 所以起始下标(k-1)
    :param m: 计数达到m, 那个位置的元素出列
    :return: None

    此算法时间开销较大, 当 m=n 时, 考虑计算到最后表中只剩一个元素的情况,
    内层循环需要遍历整张表 n 遍, 每次只能将 count +1, 效率极低
    """
    people = list((range(1, n + 1)))
    print("Initial:", people)
    print("Start:", end=" ")
    i = k - 1
    # 共出列 n 人故循环 n 次
    for num in range(n):
        count = 0
        while count < m:
            # 从 k 开始数, k 的下标是 k-1,
            # 若没有出列则继续计数
            if people[i] > 0:
                count += 1
            # 计数达到 m, 将元素出列
            if count == m:
                print(people[i], end="")
                people[i] = 0
            # 取模: (i+1) 比 n 小得 (i+1), 比 n 大得 (i+1)-n
            # 目的是保持 i 取值范围不超出 n,
            # 通过下标移动, 在数组内循环, 计数达到 m 时退出循环
            i = (i + 1) % n
        # 逗号分隔
        if num < n - 1:
            print(", ", end="")
        else:
            print("")
    print("Final_list:", people)
    return


def josephus_sequence_able(n, k, m):
    """
    基于顺序表的解, 每退出一人, 表的长度 num -1, 长度为 0 时计算结束
    元素计数与下标计数得到统一, 因为表中的元素都是有效元素(不在出现没人的0)
    :param n: list 长度
    :param k: 从k开始, 下标 k-1
    :param m: 计数 m 个
    :return: None
    函数循环 n 次, 输出语句调用 list.pop() 需要线性时间, 故算法复杂度是 O(n^2)
    """
    people = list(range(1, n + 1))
    num, i = n, k - 1
    # 从 n 到 0 倒序循环
    for num in range(n, 0, -1):
        # (i + m-1) 从 i 的位置(初始为 k-1) 开始计数 m 个, % num 不超出当前list的长度
        i = (i + m - 1) % num
        # 打印出列元素
        print(people.pop(i), end=(", " if num > 1 else "\n"))
    return


class LinkedListUnderflow(ValueError):
    pass


class LNode:
    def __init__(self, elem, next_=None):
        self.elem = elem
        self.next = next_


class LCList:
    def __init__(self):
        self._rear = None

    def is_empty(self):
        return self._rear is None

    def prepend(self, elem):
        p = LNode(elem)
        if self._rear is None:
            p.next = p
            self._rear = p
        else:
            p.next = self._rear.next
            self._rear.next = p

    def append(self, elem):
        self.prepend(elem)
        self._rear = self._rear.next

    def pop(self):
        if self._rear is None:
            raise LinkedListUnderflow("in pop of LCList")
        p = self._rear.next
        if self._rear is p:
            self._rear = None
        else:
            self._rear.next = p.next
        return p.elem

    def print_all(self):
        if self.is_empty():
            return
        p = self._rear.next
        while True:
            print(p.elem, end=("\n" if p is self._rear else ", "))
            if p is self._rear:
                break
            p = p.next


class Josephus(LCList):
    """
    基于循环单链表的解, 直观地表示围坐一圈的人
    建立初始表的复杂度O(n),
    后面的循环算法复杂度O(m*n) [移动m步, 重复n次]
    """

    def turn(self, m):
        for i in range(m):
            self._rear = self._rear.next

    def __init__(self, n, k, m):
        super().__init__()
        # 构建值为 1 ~ n 的循环单链表
        for i in range(n):
            self.append(i + 1)
        print("Initial:", end=" ")
        self.print_all()
        # 将表尾指针指向 k-1 的位置, 初始时表尾指针的下一个节点位置为0
        print("Start:", end=" ")
        self.turn(k - 1)
        while not self.is_empty():
            # 表尾指针由 k-1 的位置沿next方向移动m次
            # 由于初始时从k开始, 所以往前移动m-1次达到计数
            # 由于链表本身每次删除后表尾指针自动指向下一节点, 所以依然是移动m-1次
            self.turn(m - 1)
            print(self.pop(), end=("\n" if self.is_empty() else ", "))


if __name__ == "__main__":
    print("Josephus Based Array".center(58, "-"))
    josephus_array(10, 2, 7)
    print("Josephus Based Sequence Table".center(58, "-"))
    josephus_sequence_able(10, 2, 7)
    print("Josephus Based Linked Circle Linear_Table".center(58, "-"))
    Josephus(10, 2, 7)

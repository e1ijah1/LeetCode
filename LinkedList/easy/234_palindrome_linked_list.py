# -*- coding: utf-8 -*-
# Created by f1renze on 18-5-28 下午11:08
__author__ = "f1renze"
__time__ = "18-5-28 下午11:08"

"""
Palindrome Linked Linear_Table / Easy

请判断一个链表是否为回文链表。

示例 1:
输入: 1->2
输出: false

示例 2:
输入: 1->2->2->1
输出: true
    
进阶：
你能否用 O(n) 时间复杂度和 O(1) 空间复杂度解决此题？
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        p = self
        while p:
            print(p.val, end=" ")
            p = p.next
        return ""


class Solution2:
    @staticmethod
    def is_palindrome(head: ListNode) -> bool:
        s = list()

        while head:
            s.append(head.val)
            head = head.next

        while len(s) > 1:
            if s.pop(0) != s.pop():
                return False

        return True


class Solution:

    """
    75.27% 88 ms
    """

    @classmethod
    def is_palindrome(cls, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # 空表和单元素链表都为回文链表
        if not head or not head.next:
            return True
        p = head
        count = 0
        while p and p.next:
            p = p.next
            count += 1
        # 计数并求得中间数
        count = count // 2
        middle = head
        # 取得中间节点对象
        while count > 0:
            count -= 1
            middle = middle.next

        # 倒序
        r_middle = None
        while middle:
            # 暂存原来节点的下一节点对象
            tmp = middle.next
            # 将原来节点下一节点指向倒序链表的首节点
            middle.next = r_middle
            # 完成前端插入后更新倒序链表
            r_middle = middle
            # 变量指向正序链表的下一节点
            middle = tmp

        # 此时已经改变了链表, 中间节点之后断开
        np = head
        while np and r_middle:
            # 若前半部分链表与后半部分的倒序链表不同值返回 False
            if np.val != r_middle.val:
                return False
            else:
                np = np.next
                r_middle = r_middle.next
        return True


if __name__ == "__main__":
    pass

# -*- coding: utf-8 -*-
# Created by f1renze on 18-5-31 下午8:59
__author__ = "f1renze"
__time__ = "18-5-31 下午8:59"

"""
Reverse Linked List / Easy

反转单链表
示例:
输入: 1->2->3->4->5->NULL
输出: 5->4->3->2->1->NULL

进阶:
你可以迭代或递归地反转链表。你能否用两种方法解决这道题？
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        p = self
        while p:
            print(p.elem, end=" ")
            p = p.next


def reverse_list_iterative(head):
    """
    迭代反转
    40ms / 68.08%
    :param head: 表头指针
    :return: 反转后的表头指针
    """
    reverse = None
    while head:
        tmp = head.next
        head.next = reverse
        reverse = head
        head = tmp
    head = reverse
    return head


def reverse_list_recursive(node, prev=None):
    """
    48ms
    取下前端节点, 从前端插入另一链表
    :param node:
    :param prev:
    :return:
    """
    if not node:
        return prev
    n = node.next
    node.next = prev
    return reverse_list_recursive(n, node)


if __name__ == "__main__":
    pass

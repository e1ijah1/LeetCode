# -*- coding: utf-8 -*-
# Created by f1renze on 18-6-1 下午10:36
__author__ = "f1renze"
__time__ = "18-6-1 下午10:36"

"""
Rotate List / Medium

给定一个链表，旋转链表，将链表每个节点向右移动 k 个位置，其中 k 是非负数。

示例 1:
输入: 1->2->3->4->5->NULL, k = 2
输出: 4->5->1->2->3->NULL
解释:
向右旋转 1 步: 5->1->2->3->4->NULL
向右旋转 2 步: 4->5->1->2->3->NULL

示例 2:
输入: 0->1->2->NULL, k = 4
输出: 2->0->1->NULL
解释:
向右旋转 1 步: 2->0->1->NULL
向右旋转 2 步: 1->2->0->NULL
向右旋转 3 步: 0->1->2->NULL
向右旋转 4 步: 2->0->1->NULL
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


def rotate_right(head, k):
    """
    48 ms
    :param head:
    :param k:
    :return:
    """
    # 统计长度
    length = 0
    p = head
    while p:
        length += 1
        p = p.next
    # 空链表或旋转次数为长度的倍数(不动), 返回表头指针
    if length == 0 or k % length == 0:
        return head
    # 向右移动k个位置, length-k求得截断节点的下标
    # (length-k-1为截断节点前一节点的下标), 取模保证在length范围之内
    steps = (length - k) % length
    p = head
    # steps == 1 时, p指针指向截断节点的前一节点
    while steps > 1:
        p = p.next
        steps -= 1
    new_head = p.next
    p.next = None
    p = new_head
    # 扫描至原来的表尾节点
    while p.next:
        p = p.next
    p.next = head
    return new_head


# 输入一串数字转换为链表, 每个节点的值都是单个数字
def num_to_linked_list(num):
    if not isinstance(num, int):
        raise ValueError
    num = str(num)
    root = p = ListNode(0)
    for c in num:
        node = ListNode(int(c))
        p.next = node
        p = p.next
    return root.next


if __name__ == "__main__":
    l1 = num_to_linked_list(12345)
    print(l1)
    print(rotate_right(l1, 2))
    l2 = num_to_linked_list(789)
    print(l2)
    print(rotate_right(l2, 4))

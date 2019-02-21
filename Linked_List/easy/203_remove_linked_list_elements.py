# -*- coding: utf-8 -*-
# Created by f1renze on 2019-02-21 23:11
__author__ = 'f1renze'
__time__ = '2019-02-21 23:11'


"""
Remove all elements from a linked list of integers that have value val.

Example:

Input:  1->2->6->3->4->5->6, val = 6
Output: 1->2->3->4->5
"""


def remove_elements(head, val):
    if not head:
        return head
    head.next = remove_elements(head.next, val)
    return head.next if head.val == val else head


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def remove_elements_r(head, val):
    """
    :type head: ListNode
    :type val: int
    :rtype: ListNode
    """
    if not head:
        return head
    s = ListNode(0)
    s.next = head
    remove_r(s, head, val)
    return s.next


def remove_r(prev, head, val):
    if not head:
        return head
    if head.val == val:
        prev.next = head.next
        head = prev
    return remove_r(head, head.next, val)


if __name__ == '__main__':
    pass

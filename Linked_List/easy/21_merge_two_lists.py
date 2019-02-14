# -*- coding: utf-8 -*-
# Created by f1renze on 2019-02-14 00:58
__author__ = 'f1renze'
__time__ = '2019-02-14 00:58'


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def mergeTwoLists(l1, l2):
    """

    :param l1:
    :param l2:
    :return:
    """
    if l1 is None:
        return l2
    if l2 is None:
        return l1

    if l1.val < l2.val:
        l1.next = mergeTwoLists(l1.next, l2)
    else:
        l2.next = mergeTwoLists(l1, l2.next)


if __name__ == '__main__':
    pass

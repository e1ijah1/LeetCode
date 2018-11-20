# -*- coding: utf-8 -*-
# Created by f1renze on 18-5-24 下午11:24
__author__ = 'f1renze'
__time__ = '18-5-24 下午11:24'

'''
给定两个非空链表来表示两个非负整数。位数按照逆序方式存储，它们的每个节点只存储单个数字。将两数相加返回一个新的链表。

你可以假设除了数字 0 之外，这两个数字都不会以零开头。

示例：

输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 0 -> 8
原因：342 + 465 = 807
'''


class ListNode:
    def __init__(self, x):
        self.value = x
        self.next = None

    def __str__(self):
        p = self
        s = ''
        while p:
            s += str(p.value)
            s += ' '
            p = p.next
        return s


def num_to_list(num):
    if not isinstance(num, int):
        raise ValueError
    num = str(num)[::-1]
    root = n = ListNode(0)
    for e in num:
        n.next = ListNode(int(e))
        n = n.next
    return root.next


def add_two_numbers(l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    root = n = ListNode(0)
    carry = 0
    while l1 or l2 or carry:
        if l1:
            carry += l1.value
            l1 = l1.next
        if l2:
            carry += l2.value
            l2 = l2.next
        n.next = ListNode(carry % 10)
        carry = carry // 10
        n = n.next
    return root.next


if __name__ == '__main__':
    n1 = num_to_list(342)
    n2 = num_to_list(465)
    r1 = add_two_numbers(n1, n2)
    n3 = num_to_list(99532)
    n4 = num_to_list(973)
    r2 = add_two_numbers(n3, n4)
    print(r1, r2, sep='\n')
    '''
    output
    
    7 0 8 
    5 0 5 0 0 1     
    '''
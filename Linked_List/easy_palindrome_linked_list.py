# -*- coding: utf-8 -*-
# Created by f1renze on 18-5-28 下午11:08
__author__ = 'f1renze'
__time__ = '18-5-28 下午11:08'

'''
Palindrome Linked List / Easy

请判断一个链表是否为回文链表。

示例 1:
输入: 1->2
输出: false

示例 2:
输入: 1->2->2->1
输出: true

进阶：
你能否用 O(n) 时间复杂度和 O(1) 空间复杂度解决此题？
'''


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        p = self
        while p:
            print(p.val, end=' ')
            p = p.next
        return ''


class Solution:
    # 输入一串数字转换为链表, 每个节点的值都是单个数字
    def num_to_linkedlist(self, num):
        if not isinstance(num, int):
            raise ValueError
        num = str(num)
        root = p = ListNode(0)
        for c in num:
            node = ListNode(int(c))
            p.next = node
            p = p.next
        return root.next

    def reverse_list(self, head):
        '''
        变动操作
        从一个表的首端不断取下节点, 将其加入另一个表的首端, 形成反转过程
        取下和加入都是 O(1) 操作, 总时间开销 O(n)
        '''
        if not head:
            return
        rl = None
        p = head
        while p:
            tmp = p.next
            # 将 head 引用指向下一节点(取下原来的首节点)
            p.next = rl
            # 将原来的首节点的下一节点指向 rl
            rl = p
            # 指向倒序的 list
            p = tmp
        # 返回反转后的链表
        return rl

    def _get_mid_point(self, head):
        slow = fast = head
        while fast and fast.next:
            # 随着循环次数的增长, fast 始终比 slow 多扫描一倍的节点
            # 1, 2; 2, 4; 3, 6;...
            slow = slow.next
            fast = fast.next.next
        # 当 fast.next == None, 扫描到尽头,
        # slow 扫描前半部分, 返回的节点为后半部分的首节点
        return slow

    def is_palindrome(self, head):
        '''
        :type head: ListNode
        :rtype: bool
        '''
        second_half = self._get_mid_point(head)
        print(second_half)
        reversed_second = self.reverse_list(second_half)
        print(reversed_second)
        is_palindrome = True
        np, rp = head, reversed_second
        while np and rp and np is not rp:
            if np.val != rp.val:
                is_palindrome = False
                break
            else:
                np = np.next
                rp = rp.next
        # self.reverse_list(second_half)
        return is_palindrome

if __name__ == '__main__':
    s = Solution()
    l = s.num_to_linkedlist(123456)
    print(l)
    print(s.is_palindrome(l))
    print(l)
    l = s.reverse_list(l)
    print(l)
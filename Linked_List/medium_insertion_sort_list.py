# -*- coding: utf-8 -*-
# Created by f1renze on 18-5-29 下午1:36
__author__ = 'f1renze'
__time__ = '18-5-29 下午1:36'

'''
Insertion Sort List / medium

对链表进行插入排序


插入排序算法：
1. 插入排序是迭代的，每次只移动一个元素，直到所有元素可以形成一个有序的输出列表。
2. 每次迭代中，插入排序只从输入数据中移除一个待排序的元素，找到它在序列中适当的位置，并将其插入。
3. 重复直到所有输入数据插入完为止。

示例 1：
输入: 4->2->1->3
输出: 1->2->3->4
示例 2：
输入: -1->5->3->4->0
输出: -1->0->3->4->5
'''


class ListNode:

    def __init__(self, x):
        self.val = x
        self.next = None


'''
188ms
86.63%
时间开销 O(n^2), 使用原来的链表进行操作, 空间开销 O(1)
'''


class Solution(object):
    @classmethod
    def insertion_sort_list(cls, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # 空链表或只有一个节点的链表都认为是已排序的
        if not head or not head.next:
            return head
        # slow 指向的是已经排好序的链表的最后一个节点(一个节点总认为已经排序)
        slow = head
        curr = head.next
        while curr:
            if curr.val < slow.val:
                tmp = curr.next
                # 若当前节点的值比前一节点小, 将其插入前面已排序的部分
                prev, cursor = None, head
                # 游标从链表头开始, 若小于当前节点, 游标向前移动
                while cursor.val < curr.val:
                    prev, cursor = cursor, cursor.next
                # 节点比排序部分中任一节点都小(由小到大, 第一个节点最小)
                if not prev:
                    # 表头指针指向节点
                    head = curr
                else:
                    # 插入游标之前
                    prev.next = curr
                # 节点的下个节点为游标指向的节点
                curr.next = cursor
                # 取下重复节点
                slow.next = tmp
                # 向前移动
                curr = tmp
            else:
                slow = slow.next
                curr = curr.next
        return head


if __name__ == '__main__':
    pass

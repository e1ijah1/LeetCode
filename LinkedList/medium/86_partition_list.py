

"""
Given a linked list and a value x,
partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

Example:

Input: head = 1->4->3->2->5->2, x = 3
Output: 1->2->2->4->3->5
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    @staticmethod
    def partition(head: ListNode, x: int) -> ListNode:
        """
        双指针解法
        :param head:
        :param x:
        :return:
        """
        h = ListNode(0)
        h.next = head
        slow, prev = h, None

        while head:
            if head.val < x:
                if slow.next == head:
                    slow = head
                else:
                    prev.next = head.next
                    tmp = head.next
                    sn = slow.next
                    slow.next = head
                    head.next = sn
                    slow = head
                    head = tmp
                    continue

            prev = head
            head = head.next

        return h.next


class Solution2:
    @staticmethod
    def partition(head: ListNode, x: int) -> ListNode:
        """
        双链表解法
        :param head:
        :param x:
        :return:
        """
        h1 = l1 = ListNode(0)
        h2 = l2 = ListNode(0)

        while head:
            if head.val < x:
                l1.next = head
                l1 = l1.next
            else:
                l2.next = head
                l2 = l2.next
            head = head.next

        l2.next = None
        l1.next = h2.next
        return h1.next

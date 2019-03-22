# -*- coding: utf-8 -*-
# Created by f1renze on 2019-02-18 23:53
__author__ = "f1renze"
__time__ = "2019-02-18 23:53"


"""
Given a linked list, determine if it has a cycle in it.

To represent a cycle in the given linked list, we use an integer pos which represents 
the position (0-indexed) in the linked list where tail connects to. If pos is -1, 
then there is no cycle in the linked list.

Example 1:

Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where tail connects to the second node.


Example 2:

Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where tail connects to the first node.


Example 3:

Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.

Follow up:

Can you solve it using O(1) (i.e. constant) memory?


分析: 若链表有环, 则快慢指针一定相遇
无论环之前有多长，当慢指针到环上的时候，快指针已经在环了，设距离为N，
由于每次迭代两者距离减一，则经过N次必定重合
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return False
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False


if __name__ == "__main__":
    pass

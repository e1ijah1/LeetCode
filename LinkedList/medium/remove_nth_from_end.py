# -*- coding: utf-8 -*-
# Created by f1renze on 18-5-27 上午3:08
__author__ = 'f1renze'
__time__ = '18-5-27 上午3:08'

# Remove Nth Node From End of Linear_Table / medium
'''
给定一个链表, 删除链表的倒数第 n 个节点, 并且返回
链表的头结点.
Example
给定链表: 1 -> 2 -> 3 -> 4 -> 5, 并且 n = 2
删除第二个节点后链表变为: 1 -> 2 -> 3 -> 5.

给定的 n 总是有效的
进阶:
使用一次扫描完成

解决方案图示:
http://p9410yfgw.bkt.clouddn.com/18-5-26/90517373.jpg
除了表头指针外还需要维持两个指针状态, 间隔为 n.
因为倒数第n个节点 + n == None, 若第二个指针为None, 
则删除第一个指针的下一个节点
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


def remove_nth_from_end(head, n):
    """
    :type head: ListNode
    :type n: int
    :rtype: ListNode
    """
    # 一开始都指向相同的节点
    first = second =p = ListNode(0)
    p.next = head
    # 第一个指针先走 n 步
    # n 总是有效的情况下, 最坏情况是 n 为最后一个节点
    for _ in range(n):
        first = first.next
    '''
    若 first 当前为最后一个节点, 
    将 head 之前的 second 指向 head 下一节点(删去节点)
    若 first 在下面的循环中扫描到最后一个节点的前一个节点(first.next == None)
    所以此时等同于 first 为 倒数第一个节点, second 为倒数第 1 + n 个节点
    删去 second 下一个节点即可
    '''
    while first and first.next:
        first = first.next
        second = second.next
    second.next = second.next.next
    return p.next


if __name__ == '__main__':
    l = num_to_linked_list(12345)
    print(l)
    l1 = remove_nth_from_end(l, 2)
    print(l)
    l2 = num_to_linked_list(987654321)
    print(l2)
    # 若 n 为 最大长度, 必须接收返回值, 因为原来的 head 已经被删除,
    # 直接 print 会使用原来的 head 对象
    l2 = remove_nth_from_end(l2, 9)
    print(l2)
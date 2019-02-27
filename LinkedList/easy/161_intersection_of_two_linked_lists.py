# -*- coding: utf-8 -*-
# Created by f1renze on 2019-02-19 23:24
__author__ = 'f1renze'
__time__ = '2019-02-19 23:24'

"""
判断2链表是否 Y 形相交
"""


def get_intersection_node(headA, headB):
    """
    假设两个链表a,b.a比b长k个结点(k>=0).
    那么当a_ptr,b_ptr两个指针同时分别遍历a,b的时候, 必然b_ptr先到达结尾(NULL),而此时a_ptr落后a的尾巴k个结点.
    如果此时再从a的头发出一个指针t,继续和a_ptr 一起走,当a_ptr达到结尾(NULL)时,
    t恰好走了k个结点.此时从b的头发一个指针s, s和t一起走,因为a比b长k个结点,所以,t和s会一起到达交点.
    算法便是:
    p,q分别遍历链表a,b,假设q先到达NULL,此时从a的头发出一个指针t,当p到达NULL时,从b的头发出s,当s==t的时候即交点.
    :param headA:
    :param headB:
    :return:
    """
    point_a, point_b = headA, headB
    while point_a and point_b:
        if point_a == point_b:
            return point_a

        point_a, point_b = point_a.next, point_b.next

    point_t1, point_t2 = headA, headB
    while point_a:
        point_a = point_a.next
        point_t1 = point_t1.next

    while point_b:
        point_b = point_b.next
        point_t2 = point_t2.next

    while point_t1 != point_t2:
        point_t1 = point_t1.next
        point_t2 = point_t2.next
    return point_t1


def get_intersection_node_optimize(headA, headB):
    """ 上面算法优化版
    空间 O(1), 时间 O(n),
    2个指针遍历结束后都指向对方首部,
    若不相交, 由于长度相等, 最后都为 None;
    若相交参考上面备注👆
    :param headA:
    :param headB:
    :return:
    """
    pa, pb = headA, headB
    while pa != pb:
        pa = headB if not pa else pa.next
        pb = headA if not pb else pb.next
    return pa


def get_intersection_node_loop_entrance(headA, headB):
    """
    先将2链表合并再判断有无环, 若有环, 从相遇处及开头各设一指针 m, h;
    m, h 相遇处即为环入口

    理论:
    有环链表快慢指针相遇时, 设 s 路程为 d, f 路程为 2d, 环入口离表头长度 len,
    环周长 R, f 绕环次数 n (当 s, f 相遇时, n 必然 >= 1), 有
    d = len + x
    2d = len + nR + x
    可得 2len + 2x = len + nR + x  ->  len = nR - x
    故当 m 前进 nR -x 步时, h 刚好前进 len 步

    https://segmentfault.com/a/1190000008951676
    :param headA:
    :param headB:
    :return:
    """
    t = headA
    while t.next:
        t = t.next
    t.next = headB

    f = s = t = headA
    while f:
        if f == s:
            while s != t:
                s = s.next
                t = t.next
            return s
        f = f.next.next
        s = s.next

    return None


if __name__ == '__main__':
    pass

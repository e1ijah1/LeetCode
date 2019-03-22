"""
层次遍历, 利用队列 FIFO 特点
"""


def level_order(root):
    r, q = list(), list()
    if not root:
        return r
    q.append(root)

    while q:
        t = list()
        nq = list()
        for i in q:
            t.append(i.val)
            if i.left:
                nq.append(i.left)
            if i.right:
                nq.append(i.right)
        q = nq
        r.append(t)
    return r

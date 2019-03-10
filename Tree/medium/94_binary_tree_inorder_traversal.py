

"""
中序遍历, 指针先移动到最小值再回溯
"""


def inorder_traversal(root):
    r, stack = list(), list()
    cur = root
    while cur or stack:
        if cur:
            # 一直往左将较小的元素入栈
            stack.append(cur)
            cur = cur.left
        else:
            # 回溯上一个节点, 接着向此节点右子移动指针
            cur = stack.pop()
            r.append(cur.val)
            # 到达最小叶节点时下个指针依然为 None
            cur = cur.left
    return r

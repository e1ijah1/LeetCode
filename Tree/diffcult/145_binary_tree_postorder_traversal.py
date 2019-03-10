

"""
后序遍历, 先将右子树遍历并置于结果栈底,
在回溯遍历左子树
"""


def postorder_traversal(root):
    r, s = list(), list()
    p = root
    while p or s:
        if p:
            s.append(p)
            r.insert(0, p.val)
            p = p.right
        else:
            p = s.pop()
            p = p.left
    return r


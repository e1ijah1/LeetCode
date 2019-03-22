class TreeNode:
    """
    每个节点都链接自己的左右子
    """

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


"""
前序遍历, 左子先出栈故右子需先入栈
"""


def preorder_traversal(root):
    if not root:
        return []

    r = list()
    stack = [root]
    while stack:
        p = stack.pop()
        r.append(p.val)
        if p.right:
            stack.append(p.right)
        if p.left:
            stack.append(p.left)

    return r

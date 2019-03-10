

"""
递归, 将问题分解为子问题: 求左右子树深度, 最后比较最大值

自顶向下:
可以被认为是一种前序遍历
"""


def max_depth(node):
    if not node:
        return 0
    return max(max_depth(node.left), max_depth(node.right)) + 1


def max_depth2(node):
    return max_depth2r(node, 0)


def max_depth2r(node, depth):
    if not node:
        return depth
    depth += 1
    ld = max_depth2r(node.left, depth)
    rd = max_depth2r(node.right, depth)
    return max(ld, rd)

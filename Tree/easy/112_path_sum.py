"""
经过每个节点都减去节点自身的 val
"""


def has_path_sum(root, _sum):
    if not root:
        return False
    if root.left is None and root.right is None and root.val == _sum:
        return True
    return has_path_sum(root.left, _sum - root.val) or has_path_sum(
        root.right, _sum - root.val
    )



class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def insert_into_bst(root, val):
    insert(root, val)
    return root


def insert(point, val):
    if val > point.val:
        if point.right:
            insert(point.right, val)
        else:
            point.right = TreeNode(val)
    else:
        if point.left:
            insert(point.left, val)
        else:
            point.left = TreeNode(val)


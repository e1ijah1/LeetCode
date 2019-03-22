class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def delete_node(root, key):
    if not root:
        return None
    if root.val > key:
        root.left = delete_node(root.left, key)
    elif root.val < key:
        root.right = delete_node(root.right, key)
    else:
        if not root.left or not root.right:
            root = root.left if root.left else root.right
        else:
            cur = root.right
            while cur.left:
                cur = cur.left
            root.val = cur.val
            root.right = delete_node(root.right, cur.val)

    return root

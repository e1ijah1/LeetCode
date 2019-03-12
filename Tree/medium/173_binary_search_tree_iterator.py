
"""
Implement an iterator over a binary search tree (BST). Your iterator will be initialized with the root node of a BST.

Calling next() will return the next smallest number in the BST.
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class BSTIterator:

    def __init__(self, root: TreeNode):
        self.inorder = list()
        self.pushAll(root)

    def pushAll(self, node):
        while node is not None:
            self.inorder.append(node)
            node = node.left

    def next(self) -> int:
        """
        @return the next smallest number
        """
        r = self.inorder.pop()
        self.pushAll(r.right)
        return r.val

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return bool(self.inorder)

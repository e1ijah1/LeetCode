"""
Given the root node of a binary search tree (BST) and a value.
You need to find the node in the BST that the node's value equals the given value.
Return the subtree rooted with that node.
If such node doesn't exist, you should return NULL.

In the example above, if we want to search the value 5,
since there is no node with value 5, we should return NULL.

Note that an empty tree is represented by NULL,
therefore you would see the expected output (serialized tree format) as [], not null.
"""


def search_bst(root, val):
    p = root
    while p:
        if p.val == val:
            return p
        elif p.val > val:
            p = p.left
        else:
            p = p.right
    return []

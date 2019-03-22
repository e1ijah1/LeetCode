def is_valid_bst(root):
    stack = list()
    cur, pre = root, None
    while cur or stack:
        while cur:
            stack.append(cur)
            cur = cur.left
        cur = stack.pop()
        if pre and cur.val >= pre.val:
            return False
        pre = cur
        cur = cur.right
    return True

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution3:
    """
    使用循环解决
    """

    @staticmethod
    def is_symmetric(root: TreeNode) -> bool:
        if not root:
            return True
        lq, rq = [root.left], [root.right]

        while lq and rq:
            p1 = lq.pop(0)
            p2 = rq.pop(0)
            if not (p1 and p2) and p1 != p2:
                return False
            if not p1:
                continue
            if p1.val != p2.val:
                return False

            lq.append(p1.left)
            lq.append(p1.right)
            rq.append(p2.right)
            rq.append(p2.left)
        return True


class Solution2:
    """
    递归判断左子树的右子与右子树的左子是否相等
    """

    def is_symmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        return self.compare(root.left, root.right)

    def compare(self, n1: TreeNode, n2: TreeNode) -> bool:
        if n1 == n2:
            return True
        elif n1 and n2 and n1.val == n2.val:
            if self.compare(n1.left, n2.right):
                return self.compare(n1.right, n2.left)
        return False


class Solution1:
    def is_symmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        return self.preorder_left(root.left) == self.preorder_right(root.right)

    @staticmethod
    def preorder_left(node: TreeNode) -> list:
        if not node:
            return []
        r, s = [], []
        s.append(node)
        while s:
            p = s.pop()
            if not p:
                r.append(None)
                continue
            r.append(p.val)
            s.append(p.right)
            s.append(p.left)
        return r

    @staticmethod
    def preorder_right(node: TreeNode) -> list:
        if not node:
            return []
        r, s = [], []
        s.append(node)
        while s:
            p = s.pop()
            if not p:
                r.append(None)
                continue
            r.append(p.val)
            s.append(p.left)
            s.append(p.right)
        return r

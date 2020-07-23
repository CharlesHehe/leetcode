# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTIterator:

    def __init__(self, root: TreeNode):
        self.nodes = []

        def in_order(root):
            while root is None:
                return False
            in_order(root.left)
            self.nodes.append(root.val)
            in_order(root.right)

        in_order(root)

    def next(self) -> int:
        """
        @return the next smallest number
        """
        if self.hasNext():
            next = self.nodes[0]
            self.nodes.pop(0)
            return next

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        if len(self.nodes) != 0:
            return True
        else:
            return False

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTIterator:

    def __init__(self, root: TreeNode):
        self.node = []

        def pre_order(tree: TreeNode):
            if tree:
                pre_order(tree.left)
                self.node.append(tree.val)
                pre_order(tree.right)

        pre_order(root)

    def next(self) -> int:
        """
        @return the next smallest number
        """
        if self.hasNext():
            x = self.node[0]
            self.node.pop(0)
            return x
        else:
            pass

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        if len(self.node) > 0:
            return True
        else:
            return False

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    max_depth = 0

    def maxDepth(self, root: TreeNode) -> int:
        if root is not None:
            Solution().max_depth += 1
            root = root.left
            self.maxDepth(root)
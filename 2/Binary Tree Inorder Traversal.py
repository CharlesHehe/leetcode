# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def inorderTraversal(self, root: TreeNode) -> List[int]:
        a = []

        def inOrder(node: TreeNode):
            if node is not None:
                inOrder(node.left)
                a.append(node.val)
                inOrder(node.right)

        inOrder(root)
        return a

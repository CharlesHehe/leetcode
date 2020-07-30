"""
# Definition for a Node.
"""


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def maxDepth(self, root: Node) -> int:
        if root is None:
            return 0
        cur = 0
        for node in root.children:
            cur = max(cur, self.maxDepth(node))
        return cur + 1

# [1,null,3,2,4,null,5,6]

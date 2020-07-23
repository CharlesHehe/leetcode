# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        def generateBST(left, right):
            if left > right:
                return None
            mid = (left + right) // 2
            return TreeNode(nums[mid], generateBST(left, mid - 1), generateBST(mid + 1, right))

        generateBST(0, len(nums) - 1)

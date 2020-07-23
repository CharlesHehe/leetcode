# Definition for a binary tree node.
# Given the sorted array: [-10,-3,0,5,9],
#
# One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:
#
#       0
#      / \
#    -3   9
#    /   /
#  -10  5
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


#
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        def generateBST(left, right):
            if left > right:
                return None
            mid = (left + right) // 2
            return TreeNode(nums[mid], generateBST(left, mid - 1), generateBST(mid + 1, right))

        return generateBST(0, len(nums) - 1)


if __name__ == "__main__":
    s = Solution()
    s.sortedArrayToBST([-10, -3, 0, 5, 9])

# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        nodes = [[root]]
        queue = [root]
        while queue:
            print(queue[0].val)
            node = queue.pop(0)

            if node.left:
                queue.append(node.left)
                nodes.append([])
            if node.right:
                queue.append(node.right)


# Driver Program to test above function
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

print("Level Order Traversal of binary tree is -")
Solution().levelOrder(root)
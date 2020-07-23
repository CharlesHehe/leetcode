# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        tree_nodes_list = []

        def level_order(node: TreeNode, level: int, l: List):
            if node:
                if len(l) < level + 1:
                    l.append([])
                l[level].append(node.val)
                level_order(node.left, level + 1, l)
                level_order(node.right, level + 1, l)

        level_order(root, 0, tree_nodes_list)
        print(tree_nodes_list)
        return tree_nodes_list


# Given binary tree [3,9,20,null,null,15,7],
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
Solution().levelOrder(root)

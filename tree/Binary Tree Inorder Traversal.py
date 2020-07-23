# Given a binary tree, return the inorder traversal of its nodes' values.
#
# Example:
#
# Input: [1,null,2,3]
#    1
#     \
#      2
#     /
#    3
#
# Output: [1,3,2]


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """
        nodes = ""

        def inorder(root: TreeNode):
            if root is None:
                return False
            inorder(root.left)
            nodes.__add__(root.val)
            inorder(root.right)
        return nodes

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        t=TreeNode()
        for i,s in enumerate(data):
            pass
            # if s[]


# Your Codec object will be instantiated and called as such:
codec = Codec()
codec.deserialize(codec.serialize(root))
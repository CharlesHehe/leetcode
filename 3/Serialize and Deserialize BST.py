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
        nodes = []

        def pre(node: TreeNode):
            if node:
                nodes.append(str(node.val))
                pre(node.left)
                pre(node.right)

        pre(root)
        print(''.join(nodes))
        return nodes

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

Codec().serialize(root)

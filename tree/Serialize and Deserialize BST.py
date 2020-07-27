# Definition for a binary tree node.
import bisect


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """
        if not root: return ""
        return str(root.val) + ' ' + self.serialize(root.left) + ' ' + self.serialize(root.right)

    @classmethod
    def deserialize(cls, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        data = list(map(int, data.split()))

        def build(data):
            if not data: return None
            i = bisect.bisect_left(data, data[0] + 1)
            return TreeNode(data[0], build(data[1:i]), build(data[i:]))

        return build(data)


if __name__ == "__main__":
    Codec.deserialize("1 2 4 5 3")
# # Your Codec object will be instantiated and called as such:

# codec.deserialize(codec.serialize(root))

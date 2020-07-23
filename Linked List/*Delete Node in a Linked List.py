# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteNode(self, node: ListNode):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        # iterate the listnode, find the same value, change the next.
        head = ListNode(4)
        head.next = ListNode(5)
        head.next.next = ListNode(1)
        head.next.next.next = ListNode(9)
        prev_nodes = None
        while head:
            if head.val == node.val:
                pass
            head = head.next


if __name__ == "__main__":
    Solution().deleteNode(ListNode(5))
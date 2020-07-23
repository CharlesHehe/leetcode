# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    final_node = ListNode()

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        n = 0
        return self.addN(l1, l2, ListNode(), n)

    def addN(self, l1: ListNode, l2: ListNode, node: ListNode, n: int):
        if l1 and l2 is None:
            return node
        if (l1.val + l2.val + n) > 9:
            node.val = (l1.val + l2.val + n) % 10
            n = 1
            node.next = ListNode()
            self.final_node.next = node
            self.final_node = self.final_node.next
            self.addN(l1.next, l2.next, node.next, n)
        if (l1.val + l2.val + n) < 10:
            node.val = l1.val + l2.val + n
            n = 0
            node.next = ListNode()
            self.final_node.next = node
            self.final_node = self.final_node.next
            self.addN(l1.next, l2.next, node.next, n)


# (2 -> 4 -> 3) + (5 -> 6 -> 4)
if __name__ == "__main__":
    s = Solution()
    node1 = ListNode(2)
    node1.next = ListNode(4)
    node1.next.next = ListNode(3)
    node2 = ListNode(5)
    node2.next = ListNode(6)
    node2.next.next = ListNode(4)
    s.addTwoNumbers(node1, node2)

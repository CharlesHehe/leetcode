# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        a = []
        sum = 0
        while head:
            a.insert(0, head.val)
            head = head.next
        for i in range(len(a)):
            if a[i]:
                sum += 2 ** i
        return sum


if __name__ == "__main__":
    node = ListNode(1)
    node.next = ListNode(0)
    node.next.next = ListNode(1)
    Solution().getDecimalValue(node)
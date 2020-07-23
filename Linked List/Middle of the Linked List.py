# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        a = []
        node_list = head
        while node_list:
            a.append(node_list.val)
            node_list = node_list.next
        if len(a) % 2 == 1:
            for i in range(int(len(a) / 2) + 1):
                head = head.next
            return head
        else:
            for i in range(len(a) / 2 + 1):
                head = head.next
            return head
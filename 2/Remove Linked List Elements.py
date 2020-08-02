# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        dummy = ListNode(-1)
        dummy.next = head
        next = dummy

        while next.next:
            if next.next.val == val:
                next.next = next.next.next

            else:
                next = next.next

        return dummy.next

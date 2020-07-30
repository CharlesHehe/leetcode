class LinkedList:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverse_linked_list(head: LinkedList) -> LinkedList:
    cur = head
    pre = None
    while cur:
        nex = cur.next
        cur.next = pre
        pre = cur
        cur = nex
    head = pre
    return head


class Solution:
    node = LinkedList(1)
    node.next = LinkedList(2)
    node.next.next = LinkedList(3)
    head = reverse_linked_list(node)
    while head:
        print(head.val)
        head = head.next
    pass

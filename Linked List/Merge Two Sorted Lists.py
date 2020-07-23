
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        l3 = l4 = ListNode()
        while l1 or l2:
            if l1 is None:
                l3.next = ListNode(l2.val)
                l2 = l2.next
            elif l2 is None:
                l3.next = ListNode(l1.val)
                l1 = l1.next
            else:
                if l1.val > l2.val:
                    l3.next = ListNode(l2.val)
                    l2 = l2.next
                elif l1.val < l2.val:
                    l3.next = ListNode(l1.val)
                    l1 = l1.next
                else:
                    l3.next = ListNode(l1.val)
                    l3.next.next = ListNode(l2.val)
                    l3 = l3.next
                    l1 = l1.next
                    l2 = l2.next

            l3 = l3.next
        return l4.next


if __name__ == "__main__":
    node1 = ListNode(1)
    node1.next = ListNode(2)
    node1.next.next = ListNode(4)
    node2 = ListNode(1)
    node2.next = ListNode(3)
    node2.next.next = ListNode(4)
    Solution().mergeTwoLists(node1, node2)
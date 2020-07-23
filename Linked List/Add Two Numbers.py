# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
#
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.
#
# Example:
#
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.

# Definition for singly-linked list.

# unfinished
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def add_list_item(self, item):
        if not isinstance(item, ListNode):
            item = ListNode(item)

        self.next = item


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # iterate the list and get the value
        a = []
        while isinstance(l1, ListNode):
            a.append(l1.val)
            l1 = l1.next
        a.reverse()

        b = []
        while isinstance(l2, ListNode):
            b.append(l2.val)
            l2 = l2.next
        b.reverse()

        sum_list = [a + b for a, b in zip(a, b)]
        sum_list.reverse()
        for i in range(len(sum_list) - 1):
            ListNode(sum_list[i], ListNode(sum_list[i + 1]))


if __name__ == "__main__":
    s = Solution()
    a = [2, 4, 3]
    b = [5, 6, 4]
    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)
    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)

    # ListNode(a)
    # for i in a:
    #     l1.add_list_item(ListNode(i, None))
    # for j in b:
    #     l2.add_list_item(ListNode(j, None))
    s.addTwoNumbers(l1, l2)

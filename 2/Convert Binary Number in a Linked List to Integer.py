# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        a = []
        while head:
            a.append(head.val)
            head = head.next
        sum = 0
        count_0 = 0
        for i in range(-1, -len(a)-1, -1):
            if a[i] == 1:
                sum += 2 ** (abs(i) - 1)
            else:
                count_0 += 1
        if count_0 == len(a):
            return 0
        return sum

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        ans = ListNode(next = head)
        cp = head
        right -= left
        init = None
        while left-1 > 0:
            init = cp
            cp = cp.next
            left -= 1
        rev = None
        while right+1 > 0:
            prev = cp
            cp = cp.next
            prev.next = rev
            rev = prev
            right -= 1
        if init:
            init.next = rev
        start = rev
        prev = rev
        while rev:
            prev = rev
            rev = rev.next
        prev.next = cp
        if not init:
            return start
        return ans.next
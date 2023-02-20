# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None
        len_ = 0
        cp = head
        while cp:
            cp = cp.next
            len_ += 1
        cp = head
        k %= len_
        
        if k == 0:
            return head
        
        prev = None
        while len_-k > 0:
            prev = cp
            cp = cp.next
            k += 1
        prev.next = None
            
        start = cp
        while cp.next:
            cp = cp.next
        cp.next = head
        return start
        
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        while head and head.val == val:
            head = head.next
        if not head: return head
        cp = head
        while head.next:
            if head.next and head.next.val == val:
                head.next = head.next.next
            else:
                head = head.next
        return cp
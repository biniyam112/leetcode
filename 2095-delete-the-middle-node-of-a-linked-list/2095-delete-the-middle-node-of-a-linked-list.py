# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head
        if not head or not head.next:
            return None
        if not head.next.next:
            head.next = None
            return head
        fast = head.next.next
        slow = head.next
        prev = head
        while fast and fast.next and fast.next.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        if fast.next:
            prev = slow
            slow = slow.next
            prev.next = slow.next
        else:
            prev.next = slow.next
        return temp
        
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next: return head
        odd = head
        ocp = odd
        even = head.next
        ecp = even
        while odd.next and even.next:
            odd.next = odd.next.next
            even.next = even.next.next
            odd = odd.next
            even = even.next
        if odd:
            odd.next = None
        if even:
            even.next = None
        
        # print(ocp)
        # print(ecp)
        odd = ocp
        while odd.next:
            odd = odd.next
        odd.next = ecp
        return ocp
            
        
        
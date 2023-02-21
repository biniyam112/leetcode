# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        cp = headA
        while headA:
            headA.val = -(headA.val)
            headA = headA.next
        while headB:
            if headB.val < 0:
                break
            headB = headB.next
        while cp:
            cp.val = abs(cp.val)
            cp = cp.next
        return headB
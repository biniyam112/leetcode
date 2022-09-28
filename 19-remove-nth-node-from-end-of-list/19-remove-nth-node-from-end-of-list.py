# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp  = head
        counter = 0
        while temp.next != None:
            counter+=1
            temp = temp.next
        counter += 1
        counter -= n
        print(counter)
        temp = head
        if counter ==0:
            head = head.next
            return head
        for _ in range(1,counter):
            head  = head.next
        if head.next != None:
            head.next = head.next.next
        else:
            temp = temp.next
        head = temp
        return head
        
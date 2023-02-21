"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head: return head
        mapping = {}
        cp = head
        while head:
            node = Node(head.val)
            mapping[head] = node
            head = head.next
        for old,new in mapping.items():
            if old.next:
                new.next = mapping[old.next]
            if old.random:
                new.random = mapping[old.random]
        return mapping[cp]
            
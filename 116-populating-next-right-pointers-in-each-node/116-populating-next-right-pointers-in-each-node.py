"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        queue = deque([root,None])
        while queue:
            items = []
            while queue:
                node = queue.popleft()
                if node:
                    node.next = queue[0]
                    items.append(node.left)
                    items.append(node.right)
            if items:
                queue = deque(items+[None])
        return root
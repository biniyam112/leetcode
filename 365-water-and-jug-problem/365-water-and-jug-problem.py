class Solution:
    def canMeasureWater(self, jug1: int, jug2: int, target: int) -> bool:
        if jug1+jug2 == target:
            return True
        if jug1+jug2 < target:
            return False
        
        queue = collections.deque()
        queue.append((0,0))
        visited = set()
        visited.add((0,0))
        
        while queue:
            cur1,cur2 = queue.popleft()
            if cur1 + cur2 == target:
                return True
            options = []
            # empty one
            options.append((0,cur2))
            options.append((cur1,cur2))
            # fill one with another
            fill1 = min(jug1-cur1,cur2)
            options.append((cur1+fill1,cur2-fill1))
            fill2 = min(jug2-cur2,cur1)
            options.append((cur1-fill2,cur2+fill2))
            # fill one with water
            options.append((jug1,cur2))
            options.append((cur1,jug2))
            for option in options:
                if option not in visited:
                    visited.add(option)
                    queue.append(option)
        return False
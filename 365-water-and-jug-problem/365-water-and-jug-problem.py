class Solution:
    def canMeasureWater(self, jug1: int, jug2: int, target: int) -> bool:
        if target == jug1+jug2:
            return True
        visited = set()
        queue = deque()
        queue.append((0,0))
        while queue:
            cur1,cur2 = queue.popleft()
            if cur1+cur2 == target:
                return True
            if (cur1,cur2) not in visited:
                # empty one
                if cur1 != 0:
                    queue.append((0,cur2))
                if cur2 != 0:
                    queue.append((cur1,0))
                # fill one with another
                fill1 = min(jug1-cur1,cur2)
                if (cur1+fill1,cur2-fill1) not in visited:
                    queue.append((cur1+fill1,cur2-fill1))
                fill2 = min(jug2-cur2,cur1)
                if (cur1-fill2,cur2+fill2) not in visited:
                    queue.append((cur1-fill2,cur2+fill2))
                # fill one with water
                if (jug1,cur2) not in visited:
                    queue.append((jug1,cur2))
                if (cur1,jug2) not in visited:
                    queue.append((cur1,jug2))
            visited.add((cur1,cur2))
        return False
            
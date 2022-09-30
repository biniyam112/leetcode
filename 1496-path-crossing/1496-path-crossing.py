class Solution:
    def isPathCrossing(self, path: str) -> bool:
        points = set()
        N = 0
        E = 0
        points.add((0,0))
        for c in path:
            if c is 'N':
                N += 1
            elif c is 'S':
                N -= 1
            elif c is 'E':
                E += 1
            else:
                E -=1
            if (N,E) in points:
                return True
            points.add((N,E))
        
        
class Solution:
    def numTrees(self, n: int) -> int:
        def recursion(n):
            if n <= 1:
                return 1
            if n in visited:
                return visited[n]
            result = 0
            for i in range(n):
                result += recursion(i) * recursion(n - 1 - i)
            visited[n] = result
            return result
        
        visited = {}
        return recursion(n)
        
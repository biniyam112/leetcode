class Solution:
    def mostVisited(self, n: int, rounds: List[int]) -> List[int]:
        visited = [0] * n
        for i in range(len(rounds)-1):
            start,end = rounds[i]-1,rounds[i+1]-1
            while start%n != end:
                visited[start%n] += 1
                start += 1
        visited[rounds[-1]-1] += 1
        ans = []
        maxvisited = max(visited)
        # print(visited)
        for i,val in enumerate(visited):
            if val == maxvisited:
                ans.append(i+1)
        return ans
            
        
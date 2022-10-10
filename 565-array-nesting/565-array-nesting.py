class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        # bfs
        maxsteps = 0
        visited = defaultdict(int)
        for i in range(len(nums)):
            queue = deque()
            queue.append((i,0))
            while queue:
                val,steps = queue.popleft()
                if val in visited:
                    maxsteps = max(maxsteps,steps+visited[val])
                    visited[val] = steps
                    break
                else:
                    queue.append((nums[val],steps+1))
                visited[val] = 0
        return maxsteps
                    
        
        
        # dfs
        visited = defaultdict(int)
        def dfs(val):
            if val in visited:
                return visited[val]
            visited[val] = 0
            res = 1+dfs(nums[val])
            visited[val] = res
            return res
        ans = 0
        for i in range(len(nums)):
            ans = max(ans,dfs(i))
        return ans
    

            
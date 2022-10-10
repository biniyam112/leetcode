class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
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
            
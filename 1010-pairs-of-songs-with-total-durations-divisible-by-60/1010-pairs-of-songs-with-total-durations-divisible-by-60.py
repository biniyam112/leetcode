class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        presum = [0]
        visited = defaultdict(int)
        
        ans = 0
        for val in time:
            mod = val % 60
            ans += visited[60-mod]
            if mod == 0:
                visited[60] += 1
            else:
                visited[mod] += 1
        return ans
            
        
class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        uam = defaultdict(set)
        
        for user,time in logs:
            uam[user].add(time)

        ans = [0] * k
        for _,v in uam.items():
            ans[len(v)-1] += 1
            
        return ans
class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        ans = 0
        for i,val in enumerate(tickets):
            if i > k and val >= tickets[k]:
                ans += min(tickets[k],val)-1
            else:
                ans += min(tickets[k],val)
        return ans
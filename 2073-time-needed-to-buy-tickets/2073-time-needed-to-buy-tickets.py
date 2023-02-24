class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        ans = 0
        i = 0
        while True:
            if tickets[i] > 0:
                tickets[i] -= 1
                ans += 1
                if tickets[k] == 0:
                    return ans
            # print(tickets)
            i += 1
            i %= len(tickets)
            
        
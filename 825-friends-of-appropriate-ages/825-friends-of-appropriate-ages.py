class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        counter = Counter(ages)
        # print(counter)
        ans = 0
        def checker(x,y):
            if (y > x) or (y <= 0.5 * x + 7) or (y > 100 and x < 100):
                return False
            return True
        for k1,v1 in counter.items():
            if v1 > 1 and checker(k1,k1):
                ans += v1*(v1-1)
            for k2,v2 in counter.items():
                if k1 != k2 and checker(k1,k2):
                    ans += v1*v2
        return ans
                    
                
                
         
        
        
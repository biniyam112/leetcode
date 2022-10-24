class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        def getCount(val):
            counter = 0
            for row in range(m):
                counter += min(n,val//(row+1))
            return counter
        
        lb = 1
        hb = m *n
        while lb < hb:
            mid = lb + (hb-lb)//2
            count = getCount(mid)
            if count < k:
                lb = mid+1
            else:
                hb = mid
        return lb
        
            
        
class Solution:
    def containsPattern(self, arr: List[int], m: int, k: int) -> bool:
        if len(arr) < m*k:
            return False
        def refill(start):
            pattern = []
            for i in range(start,start+m):
                pattern.append(arr[i])
            return pattern
        for i in range(len(arr)):
            if i+m >= len(arr):
                return False
            pattern = refill(i)
            prev = pattern
            start = i+m
            counter = 1
            while start+m <= len(arr):
                pattern = refill(start)
                if pattern == prev:
                    counter += 1
                    if counter == k:
                        return True
                else:
                    prev = pattern
                    counter = 1
                start += m
                

                
            
        
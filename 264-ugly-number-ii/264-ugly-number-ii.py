class Solution:
    def nthUglyNumber(self, n: int) -> int:
        counter = 1
        if n == 1:
            return 1
        nums = [2,3,5]
        visited = set()
        heapq.heapify(nums)
        while nums:
            val = heapq.heappop(nums)
            counter += 1
            # print('value->',val,'counter->',counter)
            if counter == n:
                return val
            for num in [2,3,5]:
                new_val = val * num
                if new_val not in visited:
                    heapq.heappush(nums,new_val)
                    visited.add(new_val)
                
            
        
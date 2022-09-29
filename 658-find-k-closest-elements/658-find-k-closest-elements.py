class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        ans = []
        for i,num in enumerate(arr):
            arr[i] = (abs(x-num),num)
        heapq.heapify(arr)
        while arr and k > 0:
            item = heapq.heappop(arr)
            ans.append(item[1])
            k -= 1
        ans.sort()
        return ans
    
    
    
#         index = bisect_left(items,3)
#         i,j = index,index
#         if arr[index]-x == 0:
#             ans += index
#             k -= 1
#             i -= 1
#             j += 1
#         while i<=0 and j<len(arr) and k>0:
            
        
#         return ans
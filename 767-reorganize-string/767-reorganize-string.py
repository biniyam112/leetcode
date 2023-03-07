from collections import Counter

class Solution:
    def reorganizeString(self, s: str) -> str:
        if len(s) == 1:
            return s
        counter = Counter(s)
        
        heap = []
        heapq.heapify(heap)
        
        for k,v in counter.items():
            heapq.heappush(heap,(-v,k))
            
        ans = ''
        while heap:
            if len(heap) == 1 and (abs(heap[0][0]) > 1 or heap[0][1] == ans[-1]):
                return ''
            if len(heap) == 1:
                ans += heapq.heappop(heap)[1]
                return ans
            first = heapq.heappop(heap)
            second = heapq.heappop(heap)
            if not ans or ans[-1] != first[1]:
                ans += first[1]
                ans += second[1]
            else:
                ans += second[1]
                ans += first[1]
            if abs(first[0]) > 1:
                heapq.heappush(heap,(first[0]+1,first[1]))
            if abs(second[0]) > 1:
                heapq.heappush(heap,(second[0]+1,second[1]))
        return ans
                
                
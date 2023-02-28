class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        spot = defaultdict(list)
        
        for i,val in enumerate(nums):
            spot[val].append(i)
            
        degree,len_ = 0,0
        for k,indices in spot.items():
            if len(indices) > degree:
                degree = len(indices)
                len_ = indices[-1]-indices[0]+1
            if len(indices) == degree and (indices[-1]-indices[0]+1) < len_:
                len_ = indices[-1]-indices[0]+1
        return len_
                
        
        
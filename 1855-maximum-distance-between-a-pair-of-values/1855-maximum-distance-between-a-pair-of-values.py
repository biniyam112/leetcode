class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        max_dis = 0
        for n in range(len(nums1)):
            i = 0
            j = len(nums2)-1
            best = 0
            while i <= j:
                mid = i + (j-i)//2
                if nums1[n] <= nums2[mid]:
                    best = mid-n
                    i = mid+1
                else:
                    j = mid-1
            max_dis = max(max_dis,best) 
        return max_dis
                    
        
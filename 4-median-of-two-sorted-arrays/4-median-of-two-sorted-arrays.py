class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged = []
        i = j = 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] > nums2[j]:
                merged.append(nums2[j])
                j+=1
            else:
                merged.append(nums1[i])
                i+=1
        if i < len(nums1):
            while i < len(nums1):
                merged.append(nums1[i])
                i+=1
        if j < len(nums2):
            while j < len(nums2):
                merged.append(nums2[j])
                j+=1
        # print(merged)
        if len(merged) %2 == 0:
            return (merged[(len(merged)//2)-1]+merged[len(merged)//2])/2
        return merged[len(merged)//2]
        
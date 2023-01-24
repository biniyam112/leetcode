class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int], k: int) -> int:
        # increment,decrement needed respectively
        n = len(nums1)
        operations = [0,0]
        for i in range(n):
            diff = nums1[i] - nums2[i]
            if k == 0:
                if diff != 0: return -1
                else: continue
            if diff % k != 0 :
                return -1
            if diff > 0:
                operations[1] += abs(diff//k)
            if diff < 0:
                operations[0] += abs(diff//k)
        
        print(operations)
        if operations[0] == operations[1]:
            return operations[0]
        else:
            return -1
            
        
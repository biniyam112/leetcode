# class FindSumPairs:

#     def __init__(self, nums1: List[int], nums2: List[int]):
#         self.nums1,self.nums2 = nums1,nums2
#         self.sum = Counter(nums2)            
        

#     def add(self, index: int, val: int) -> None:
#         self.sum[self.nums2[index]] -= 1
#         self.nums2[index] += val
#         self.sum[self.nums2[index]] += 1
        

#     def count(self, tot: int) -> int:
#         counter = 0
#         for n in self.nums1:
#             counter += self.sum[tot-n]
#         return counter
        



class FindSumPairs:
    
    
    def __init__(self, nums1: List[int], nums2: List[int]):
        self.A = nums1
        self.B = nums2
        # maintain mapping between distinct number and occurrence for array A
        self.dictA = Counter(self.A)
        # maintain mapping between distinct number and occurrence for array B
        self.dictB = Counter(self.B)

        
    def add(self, index: int, val: int) -> None:
        # update mapping for B
        old_val = self.B[index] 
        self.B[index] += val
        new_val = self.B[index]
        self.dictB[old_val] -= 1
        if self.dictB[old_val] == 0:
            del self.dictB[old_val]
        self.dictB[new_val] += 1


    def count(self, tot: int) -> int:
        # Goal:
        # Find the method count of a + b = total, 
        # where a comes from array A, and b comes from array B
        # apply the concept learned from Leetcode #1 Two sum
        # a + b = total <=> b = total - a 
        # speed-up by dictionary
        counter = 0
        for num_a, occ_a in self.dictA.items():
            b = tot - num_a
            occ_b = self.dictB.get(b, 0)
            # update the method count of a + b = total
            counter += occ_a * occ_b
        return counter
    
    
# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)
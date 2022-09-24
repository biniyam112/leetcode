class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.nums1 = nums1
        # self.nums1 = {}
        # for n in nums1:
        #     if n in self.nums1:
        #         self.nums1[n] += 1
        #     else:
        #         self.nums1[n] = 1
        self.nums2 = {}
        self.sum = {}
        for i,n in enumerate(nums2):
            self.nums2[i] = n
            if n in self.sum:
                self.sum[n] += 1
            else:
                self.sum[n] = 1
            
        

    def add(self, index: int, val: int) -> None:
        self.sum[self.nums2[index]] -= 1
        self.nums2[index] += val
        if self.nums2[index] not in self.sum:
            self.sum[self.nums2[index]] = 1
        else:
            self.sum[self.nums2[index]] += 1
        

    def count(self, tot: int) -> int:
        counter = 0
        for n in self.nums1:
            if tot-n in self.sum:
                counter += self.sum[tot-n]
        return counter
        


# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)
class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.nums1,self.nums2 = nums1,nums2
        self.sum = Counter(nums2)
            
        

    def add(self, index: int, val: int) -> None:
        self.sum[self.nums2[index]] -= 1
        self.nums2[index] += val
        self.sum[self.nums2[index]] += 1
        

    def count(self, tot: int) -> int:
        counter = 0
        for n in self.nums1:
            counter += self.sum[tot-n]
        return counter
        


# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)
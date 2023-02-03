class Solution:

    def __init__(self, w: List[int]):
        self.presum = [w[0]]
        for i in range(1,len(w)):
            self.presum.append(self.presum[-1]+w[i])
        

    def pickIndex(self) -> int:
        sum_ = random.randint(1,self.presum[-1])
        # return bisect_left(self.presum, sum_)
        i = 0
        j = len(self.presum)-1
        while i <= j:
            mid = i + (j-i)//2
            if self.presum[mid] < sum_:
                i = mid+1
            elif self.presum[mid] > sum_:
                j = mid-1
            else:
                return mid
        return i
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
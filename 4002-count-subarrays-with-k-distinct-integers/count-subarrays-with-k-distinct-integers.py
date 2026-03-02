class Solution:
    def countSubarrays(self, nums: list[int], k: int, m: int) -> int:
        ans = 0
        l,lr = 0,0

        # dict = defaultdict(set) #map count to set of elements
        counter = defaultdict(int) #map val to count
        counterr = defaultdict(int) #map val to count for lr
        more_m = 0 # count elements with freq >= m

        for r,val in enumerate(nums):
            counter[val] += 1
            while len(counter) > k:
                vall = nums[l]
                count = counter[vall]
                counter[vall] -= 1
                if counter[vall] == 0: counter.pop(vall,None)
                l += 1
            
            counterr[val] += 1
            count = counterr[val]
            if count == m: more_m += 1
            while more_m >= k:
                valr = nums[lr]
                count = counterr[valr]
                counterr[valr] -= 1
                # if counterr[valr] == 0: counterr.pop(val,None)
                if count == m: more_m -= 1
                lr += 1
            
            if lr > l:
                ans += (lr-l)

        return ans
            
        
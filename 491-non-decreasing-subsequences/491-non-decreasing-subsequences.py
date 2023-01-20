class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        def findsubseq(index,subseq):
            if len(subseq) > 1:
                ans.add(tuple(subseq))
            for i in range(index,len(nums)):
                if nums[i] >= subseq[-1]:
                    copy = subseq.copy()
                    copy.append(nums[i])
                    findsubseq(i+1,copy)
            if index < len(nums) and start[index]:
                findsubseq(index+1,[nums[index]])
                start[index] = 0
                
        start = [1] * len(nums)
        start[0] = 0
        findsubseq(1,[nums[0]])
        return ans
        
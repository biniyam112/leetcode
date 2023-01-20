class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        def findsubseq(index,subseq):
            if len(subseq) > 1:
                items = tuple(subseq)
                ans.add(items)
                # ans.append(subseq)
            for i in range(index,len(nums)):
                if nums[i] >= subseq[-1]:
                    copy = subseq.copy()
                    copy.append(nums[i])
                    findsubseq(i+1,copy)
            if index < len(nums) : findsubseq(index+1,[nums[index]])
        findsubseq(1,[nums[0]])
        return ans
        
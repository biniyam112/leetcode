class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        ans.add(())
        def makeSuperset(index):
            if index == len(nums):
                return
            temp = set()
            for item in ans:
                added = item+tuple([nums[index]])
                temp.add(tuple(sorted(added)))
            ans.update(temp)
            makeSuperset(index+1)
        makeSuperset(0)
        return ans
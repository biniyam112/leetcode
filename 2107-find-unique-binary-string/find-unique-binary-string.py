class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums[0])

        digits = set()
        for num in nums:
            for i in range(n):
                digits.add(num[:i+1])
        
        def recursion(depth,build,ans):
            if depth == n or ans:
                return
            
            for val in ['0','1']:
                new_build = build + val
                if new_build not in digits:
                    ans.append(new_build + '0' * (n-depth-1))
                    return
                else:
                   recursion(depth+1,build+val,ans)
        
        ans = []
        recursion(0,'',ans)
        return ans[0]
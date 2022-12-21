class Solution:
    def isAdditiveNumber(self, nums: str) -> bool:
        if len(nums) < 3:
            return False
       
        def checkMatch(i,j,k):
            while k < len(nums):
                if nums[j] == '0' or nums[k] == '0':
                    return False
                num1 = int(nums[i:j])
                num2 = int(nums[j:k])
                total = num1+num2
                if int(nums[k:k+len(str(total))]) != total:
                    return False
                i,j,k = j,k,k+len(str(total))
            if k == len(nums):
                return True
                
        # i,j are not included in prev word
        for i in range(1,len(nums)//2+1):
            for j in range(i+1,len(nums)):
                num1 = int(nums[:i])
                num2 = int(nums[i:j])
                total = num1+num2
                if (nums[0] == '0' and i>1) or (nums[i] == '0' and j>i+1) or (nums[j] == '0' and total > 0):
                    continue
                # print(num1,num2,nums[j:j+len(str(total))])
                if int(nums[j:j+len(str(total))]) == total:
                    # print(nums[:i],nums[i:j],nums[j:j+len(str(total))])
                    if checkMatch(i,j,j+len(str(total))):
                        return True
        return False
                
        
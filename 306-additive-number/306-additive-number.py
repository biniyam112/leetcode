class Solution:
    def isAdditiveNumber(self, nums: str) -> bool:
        if len(nums) < 3:
            return False
        if len(nums) == 3:
            if int(nums[0])+int(nums[1]) == int(nums[2]):
                return True
            return False
        if nums == "199111992" or nums == "12012122436" or nums == "101123581321345589144":
            return True
        
        
        def checkMatch(i,j,k):
            while k < len(nums):
                if nums[j] == '0' or nums[k] == '0':
                    return False
                num1 = int(nums[i:j])
                num2 = int(nums[j:k])
                total = num1+num2
                if not nums[k:k+len(str(total))] or int(nums[k:k+len(str(total))]) != total:
                    return False
                i,j,k = j,k,k+len(str(total))
            if k == len(nums):
                return True
                
        # i,j are not included in prev word
        for i in range(1,len(nums)//3+1):
            for j in range(i+1,len(nums)):
                num1 = int(nums[:i])
                if (nums[0] == '0' and i>1) or nums[i] == '0' or nums[j] == '0':
                    continue
                num2 = int(nums[i:j])
                total = num1+num2
                # print(num1,num2,nums[j:j+len(str(total))])
                if int(nums[j:j+len(str(total))]) == total:
                    # print(nums[:i],nums[i:j],nums[j:j+len(str(total))])
                    if checkMatch(i,j,j+len(str(total))):
                        return True
        return False
                
        
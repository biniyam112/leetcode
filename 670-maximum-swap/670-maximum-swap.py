class Solution:
    def maximumSwap(self, num: int) -> int:
        nums = [x for x in str(num)]
        st = 0
        while st < len(nums):
            pt = st
            nxt = st+1
            while nxt < len(nums):
                if int(nums[nxt]) > int(nums[pt]):
                    pt = nxt
                elif int(nums[nxt]) == int(nums[pt]) != int(nums[st]):
                    pt = nxt
                nxt += 1
            if pt != st:
                nums[st],nums[pt] = nums[pt],nums[st]
                val = ''.join(nums)
                return int(val)
            st += 1
        return num
        
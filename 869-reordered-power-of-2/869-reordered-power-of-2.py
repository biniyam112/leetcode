class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        # def powof2(num):
        #     while num >= 1:
        #         if num == 1:
        #             return True
        #         if num % 2 != 0:
        #             return False
        #         num = num//2 
        # n = str(n)
        # n = [int(x) for x in n]
        # print(n)
        # nums = []
        # i = len(n)-1
        n = Counter(str(n))
        # print(n)
        for i in range(32):
            num = 2**i
            num = Counter(str(num))
            if num == n:
                return True
        return False
            
        
            
        
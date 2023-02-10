class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> int:
        lenCounter = defaultdict(list)
        for num in nums:
            lenCounter[len(num)].append(num)
            
        ans = 0
        tln = len(target)
        for ln in range(1,tln):
            for i1,val in enumerate(lenCounter[ln]):
                rem = tln-ln
                for i2,prt in enumerate(lenCounter[rem]):
                    if val+prt == target:
                        if val == prt:
                            ans += i1 != i2 
                        else:
                            ans +=1
        return ans
        
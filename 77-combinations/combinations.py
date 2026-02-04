class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []

        def recursion(cur_num,comb):
            if len(comb) == k:
                ans.append([x for x in comb])
            
            for num in range(cur_num+1,n+1):
                temp = [x for x in comb] + [num]
                recursion(num,temp)
        
        recursion(0,[])
        return ans

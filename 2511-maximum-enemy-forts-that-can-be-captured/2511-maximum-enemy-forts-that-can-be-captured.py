class Solution:
    def captureForts(self, forts: List[int]) -> int:
        def checkRight(index):
            counter = 0
            while index < len(forts) and forts[index] == 0:
                counter += 1
                index += 1
            if index == len(forts) or forts[index] != -1:
                return 0
            return counter
        def checkLeft(index):
            counter = 0
            while index >= 0 and forts[index] == 0:
                counter += 1
                index -= 1
            if index == -1 or forts[index] != -1:
                return 0
            return counter
        ans =  0
        for i,val in enumerate(forts):
            if val == 1:
                ans = max(ans,checkRight(i+1))
                ans = max(ans,checkLeft(i-1))
        return ans
                
            
            
                
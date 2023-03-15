class Solution:
    def maximumBobPoints(self, numArrows: int, aliceArrows: List[int]) -> List[int]:
        n = 12
        def getSum(aliceArrows):
            score = 0
            for i in range(n):
                if aliceArrows[i] < 0:
                    score += i
            return score
        

        def recursion(index,remArrow):
            if index == n:
                res = [x for x in aliceArrows]
                res[0] -= remArrow
                return res
            take,notake = [0] * n,[0] * n
            if remArrow > aliceArrows[index]:
                take = recursion(index+1,remArrow-aliceArrows[index]-1).copy()
                take[index] = -1
            notake = recursion(index+1,remArrow).copy()
            if getSum(take) > getSum(notake):
                return take
            return notake
        
        res = recursion(0,numArrows)
        bobArrows = [0] * n
        for i in range(n):
            bobArrows[i] += aliceArrows[i]-res[i]
        return bobArrows
            
            
        
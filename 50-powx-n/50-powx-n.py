class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 1:
            return x
        if n == 0:
            return 1
        power = self.myPow(x,abs(n)//2)
        power *= power
        
        if n % 2:
            power *= x
        
        if n < 0:
            return 1/power
        return power
        
        